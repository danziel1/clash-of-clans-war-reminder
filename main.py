import requests

# Get your token from developer.clashofclans.com Make sure that you keep "Bearer" before your token
token = 'Bearer API_KEY'
tag = 'CLAN_TAG' # clan tag without the "#", example: "2LYR9RYVP"
webhook = 'WEBHOOK_URL'


headers = {'Authorization': token}
r = requests.get(f'https://api.clashofclans.com/v1/clans/%23{tag}/currentwar', headers=headers).json()
needToAttack = []

if r['state'] == 'inWar':
    for num in range(len(r['clan']['members'])):
        try:
            if len(r['clan']['members'][num]['attacks']) != 2:
                print(len(r['clan']['members'][num]['attacks']))
                needToAttack.append(r['clan']['members'][num]['name']+":"+"1")
        except:
            needToAttack.append(r['clan']['members'][num]['name']+":"+"2")

message = ''

for i in needToAttack:
    member, attacksLeft = i.split(':')
    message += "> " + member + " has " + attacksLeft + " attacks left\n"

data = {
    "username": "War Log",
    # "content": "War Log",
    "embeds": [ 
    {
        "description" : message,
        "title" : ">> Unused Attacks <<"
    }
    ]
}

r = requests.post(webhook, json = data)

import requests
import json

with open('./src/config.json') as file:
    data = json.load(file)

with open('./src/message.json') as file:
    webhook_message = json.load(file)

webhook = data["webhook"]
apiaddr = data["apiaddr"]

print(webhook)
print(apiaddr)

embeds = webhook_message["embeds"]
# webhook_header = webhook_message.pop(embeds)

print(embeds)



# response = requests.get('http://'+apiaddr+'/api/tunnels')
# response_json = response.json()
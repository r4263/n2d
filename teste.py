import requests
import json
import socket
import getpass

with open('./src/config.json') as file:
    data = json.load(file)

with open('./src/message.json') as file:
    webhook_message = json.load(file)

computer_name = socket.gethostname()
username = getpass.getuser()
webhook = data["webhook"]
apiaddr = data["apiaddr"]
embeds = webhook_message["embeds"]
del webhook_message["embeds"]

# print(embeds)
# print(webhook_message + embeds)






# response = requests.get('http://'+apiaddr+'/api/tunnels')
# response_json = response.json()
import requests
import json
import datetime

webhook = "https://discord.com/api/webhooks/1120595006353313902/s-C9CxiNMyGJ8GcuhlnoBXVv2KEVL_k_kd6CulbqGd01JhbB8LsTdB94p9t0w0xH7cv1"

webhookcontent = {
    'content': 'New tunnel(s) detected!',
    'embeds': [],
    'username': 'ngrok2disc notifier'
}

response = requests.get('http://localhost:4040/api/tunnels')
response_json = response.json()

tunnelcount = 1

for tunnel in response_json["tunnels"]:

    tunnelname = tunnel["name"] if tunnel["name"] != "command_line" else "No name(ngrok is being executed by command line)"
    publicurl = tunnel["public_url"]
    publicurl_f = (publicurl.split("://",1))[1]
    ct = str(datetime.datetime.now())

    webhookcontent["embeds"] += [
        {
       'title': 'Tunnel #'+str(tunnelcount),
       'url': publicurl,
       'color': '1679001',
       'fields': [
         {
           'name': 'Tunnel name',
           'value': tunnelname
         },
         {
           'name': 'Tunnel URL',
           'value': publicurl_f
         }
       ],
       'author': {
         'name': 'Python Agent',
         'icon_url': 'https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png'
       },
       'footer': {
         'text': 'Timestamp'
       },
       'timestamp': ct
        }
      ]

    tunnelcount += 1

result = requests.post(webhook, data=json.dumps(webhookcontent), headers={'Content-type':'application-json'})

try:
  result.raise_for_status()
except requests.exceptions.HTTPError as err:
  print(err)
else:
  print("Payload delivered successfully, code {}.".format(result.status_code))
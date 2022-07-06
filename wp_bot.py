import time
import requests
from requests import get
import json
import pystyle
from pystyle import *


System.Size(150, 47)

banner1 = """


▄▀▀▄    ▄▀▀▄  ▄▀▀▄▀▀▀▄      ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀█▀▀▄ 
█   █    ▐  █ █   █   █     ▐ ▄▀   █ █      █ █    █  ▐ 
 ▐  █        █ ▐  █▀▀▀▀        █▄▄▄▀  █      █ ▐   █     
    █   ▄    █     █            █   █  ▀▄    ▄▀    █      
    ▀▄▀ ▀▄ ▄▀   ▄▀            ▄▀▄▄▄▀    ▀▀▀▀    ▄▀       
          ▀    █             █    ▐            █         
                ▐             ▐                 ▐         


"""

print(Colorate.Horizontal(Colors.blue_to_white, Center.XCenter(banner1)))

webhook_url = Write.Input("[?] enter the webhook URL ->",  Colors.blue_to_white, interval=0.005)
print()
name = Write.Input("[?] enter the name of the bot ->",  Colors.blue_to_white, interval=0.005)
print()
#webhook_url = "https://discord.com/api/webhooks/985856019840237618/opDyjvsd025DgAd6TLWek_cID1zYjqAU85C7kMEXIjMO8LV0hB80skjCBcUej7B9NwUe"

content_message = Write.Input("[?] what you wanna say ->",  Colors.blue_to_white, interval=0.005)
print()
start = int(Write.Input("[?] how often do you want to send the message [in second]->", Colors.blue_to_white, interval=0.005))
print()

for i in range(10000):
    message = content_message
    r = requests.post(webhook_url, json={'username': name, 'content': message})
    number = Write.Print("[!] Message sent to the webhook \n", Colors.blue_to_white, interval=0.005)
    time.sleep(start)

print()
Write.Input("The message succesfully sent to the webhook", Colors.blue_to_white, interval=0.005)
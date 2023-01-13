import requests as rq
import json
import numpy as np
from bs4 import BeautifulSoup
import logging
from datetime import datetime
import base64
from re import search
from src.gununmaclari import *
from src.birlestirfoto import *

import config
config = config.Config('./config/config.py')
headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 123.0.0.21.115 (iPhone11,8; iOS 14_0; en_US; en-US; scale=2.00; 828x1792; 165586599)",
    "content-type": "application/json",
    "cache-control": "private, no-cache, no-store, must-revalidate",
    "access-control-allow-origin": "https://www.instagram.com",
    "access-control-expose-headers": "X-IG-Set-WWW-Claim",
    "alt-svc": '''h3=":443"; ma=86400'''
}

def footballpredictionsnet(dailymatches):
    def skorgetir(match):   
        html = rq.get(url="https://footballpredictions.net/super-lig-predictions-turkey-tips",headers=headers)
        content = html.content
        soup = BeautifulSoup(content, 'html.parser')
        for maciara in soup.find_all("div",{"class","blue-card-outer-outer mb-5"}):
            if search(match.split(' ')[0],maciara.find_all("div",{"class","team-label"})[0].text):
                matchurl = maciara.find('a')['href']
                html = rq.get(url=matchurl,headers=headers)
                content = html.content
                soup = BeautifulSoup(content, 'html.parser')
                macadi = str(soup.find("h1",{"class","text-center text-white px-2 mb-3"}).text.split(" Live")[0])
                mactahmini = 'FootballPredictions'+':'+str(soup.find_all("div",{"class","prediction d-inline-flex align-items-center"})[-1].text.strip())
                takim1foto = str(soup.find_all("div",{"class","img-holder"})[0].find("img")).split('v-lazy=')[1].split('"')[1].split("'")[1]
                cizgi = "https://imgrosetta.mynet.com.tr/file/14722372/14722372-728xauto.jpg"
                takim2foto = str(soup.find_all("div",{"class","img-holder"})[1].find("img")).split('v-lazy=')[1].split('"')[1].split("'")[1]
                print(takim1foto.replace("small","big"))
                fotograf = fotobirlestir(takim1foto.replace("small","big"),cizgi,takim2foto.replace("small","big"))
                print(fotograf)
                discord_webhook(macadi,mactahmini,fotograf)
    for match in dailymatches:
        if match.split('Match League:')[1] == "Turkish Super Lig":         
            skorgetir(match)
        elif match.split('Match League:')[1] == "Turkish Super Lig":
            skorgetir(match)
        elif match.split('Match League:')[1] == "Turkish Super Lig":
            skorgetir(match)
        elif match.split('Match League:')[1] == "Turkish Super Lig":
            skorgetir(match)
        



def __main__():
    dailymatches = dailymatch()
    footballpredictionsnet(dailymatches)

















def discord_webhook(macadi,mactahmini,fotograf):
    '''
    Sends a test Discord webhook notification
    '''
    with open('./uploads/final.png', mode='rb') as file:
        img = file.read()
    data = {
            "username": config.USERNAME,
            "avatar_url": config.AVATAR_URL,
            "embeds": [{
                "title": macadi,
                "thumbnail": {"url": "attachment://final.png"},
                "color": int(config.COLOUR),
                "footer": {'text': 'made by izzy'},
                "timestamp": str(datetime.utcnow()),      
                "fields": [{"name": mactahmini.split(':')[0],"value": '***'+mactahmini.split(':')[1]+'***'}]    
            }]
    }
    result = rq.post(config.WEBHOOK, json=data, headers={'Content-Type': 'application/json'}, files={'final.png': ('final.png', img, 'image/png')})
    
    try:
        result.raise_for_status()
    except rq.exceptions.HTTPError as err:
        logging.error(msg=err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
        logging.info(msg="Payload delivered successfully, code {}.".format(result.status_code))



__all__ = ["__main__"]
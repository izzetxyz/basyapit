from bs4 import BeautifulSoup
import requests as rq
import json
import numpy as np
from bs4 import BeautifulSoup
import logging
from datetime import datetime
from src.discord_messages.discordtahmin import *
from src.birlestirfoto import *
from re import search
from requests.auth import HTTPProxyAuth

headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 123.0.0.21.115 (iPhone11,8; iOS 14_0; en_US; en-US; scale=2.00; 828x1792; 165586599)",
    "content-type": "application/json",
    "cache-control": "private, no-cache, no-store, must-revalidate",
    "access-control-allow-origin": "https://www.instagram.com",
    "access-control-expose-headers": "X-IG-Set-WWW-Claim",
    "alt-svc": '''h3=":443"; ma=86400'''
}

def footballpredictionscom(match,mac):   
    try:
        link = datetime.now().strftime("%d-%m-%Y")
        html = rq.get(url=f"https://footballpredictions.com/footballpredictions/?date={(link)}",headers=headers)
        print(f"https://footballpredictions.com/footballpredictions/?date={(link)}")
        content = html.content
        i = 0
        soup = BeautifulSoup(content, 'html.parser')
        for maciara in soup.find_all("div",{"class","predtitle"}):
            if search(match.split(' ')[0],maciara.text.strip()):
                mactahmini = 'FootballPredictions.com'+':'+str(soup.find_all("div",{"class","divTableCell2 pred-box-info-result"})[i].find('strong').text.strip())
                toplu = mac.split('?')
                aradeger = toplu[1]+','+mactahmini
                toplu = toplu[0]+'?'+aradeger+'?'+toplu[2]
                print(toplu)
                return toplu
            i += 1
    except Exception as hata:
        print(hata)
__all__ = ["footballpredictionscom"]
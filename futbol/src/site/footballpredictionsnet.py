from bs4 import BeautifulSoup
import requests as rq
import json
import numpy as np
from bs4 import BeautifulSoup
import logging
from datetime import datetime
from src.discord_messages.discordtahmin import *
from src.birlestirfoto import *
from site.footballPredictionscom import *
from re import search


headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 123.0.0.21.115 (iPhone11,8; iOS 14_0; en_US; en-US; scale=2.00; 828x1792; 165586599)",
    "content-type": "application/json",
    "cache-control": "private, no-cache, no-store, must-revalidate",
    "access-control-allow-origin": "https://www.instagram.com",
    "access-control-expose-headers": "X-IG-Set-WWW-Claim",
    "alt-svc": '''h3=":443"; ma=86400'''
}
def footballpredictionsnet(dailymatches):
    def skorgetir(match,link):   
        html = rq.get(url=f"https://footballpredictions.net/{link}",headers=headers)
        content = html.content
        soup = BeautifulSoup(content, 'html.parser')
        for maciara in soup.find_all("div",{"class","blue-card-outer-outer mb-5"}):
            if search(match.split(' ')[0],maciara.find_all("div",{"class","team-label"})[0].text):
                matchurl = maciara.find('a')['href']
                html = rq.get(url=matchurl,headers=headers)
                content = html.content
                soup = BeautifulSoup(content, 'html.parser')
                macadi = str(soup.find("h1",{"class","text-center text-white px-2 mb-3"}).text.split(" Live")[0])
                mactahmini = 'FootballPredictions.net'+':'+str(soup.find_all("div",{"class","prediction d-inline-flex align-items-center"})[-1].text.strip())
                takim1foto = str(soup.find_all("div",{"class","img-holder"})[0].find("img")).split('v-lazy=')[1].split('"')[1].split("'")[1]
                takim2foto = str(soup.find_all("div",{"class","img-holder"})[1].find("img")).split('v-lazy=')[1].split('"')[1].split("'")[1]
                fotograf = fotobirlestir(takim1foto.replace("small","big"),takim2foto.replace("small","big"))
                toplu = macadi+'?'+mactahmini+'?'+fotograf
                return toplu
    for match in dailymatches:
        try:
            if match.split('Match League:')[1] == "Turkish Super Lig":    
                link = "super-lig-predictions-turkey-tips"     
                mac = skorgetir(match,link)
                link = "/Regions/225/Tournaments/17/Turkey-Super-Lig"
                mac = footballpredictionscom(match,mac)
                discord_webhook(mac.split('?')[0],mac.split('?')[1],mac.split('?')[2])
            elif match.split('Match League:')[1] == "English Premier League":
                link = "premier-league-predictions-england-tips" 
                mac = skorgetir(match,link)
                mac = footballpredictionscom(match,mac)
                discord_webhook(mac.split('?')[0],mac.split('?')[1],mac.split('?')[2])
            elif match.split('Match League:')[1] == "Spanish LaLiga":
                link = "la-liga-predictions-spain-tips" 
                mac = skorgetir(match,link)
                mac = footballpredictionscom(match,mac)
                discord_webhook(mac.split('?')[0],mac.split('?')[1],mac.split('?')[2])
            elif match.split('Match League:')[1] == "French Division 1 Féminine":
                link = "ligue-1-predictions-france-tips" 
                mac = skorgetir(match,link)
                mac = footballpredictionscom(match,mac)
                discord_webhook(mac.split('?')[0],mac.split('?')[1],mac.split('?')[2])
            elif match.split('Match League:')[1] == "Italian Serie A":
                link = "serie-a-predictions-italy-tips" 
                mac = skorgetir(match,link)
                mac = footballpredictionscom(match,mac)
                discord_webhook(mac.split('?')[0],mac.split('?')[1],mac.split('?')[2])
        except Exception as hata:
            print(hata)
__all__ = ["footballpredictionsnet"]
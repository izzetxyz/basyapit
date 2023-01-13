import requests as rq
from bs4 import BeautifulSoup
from datetime import datetime

def dailymatch():
    date_string = datetime.now().strftime("%Y%m%d")
    url= f"https://www.espn.com/soccer/fixtures/_/date/{date_string}"
    html = rq.get(url=url)
    content = html.content
    soup = BeautifulSoup(content, 'html.parser') 
    matches = []
    lignames = soup.find_all("h2",{"class","table-caption date-header-caption"})
    i = 0
    for leaguename in lignames:
        if leaguename.text.strip() == "English Premier League" or leaguename.text.strip() == "Spanish LaLiga" or leaguename.text.strip() == "Italian Serie A" or leaguename.text.strip() == "French Division 1 Féminine" or leaguename.text.strip() == "Turkish Super Lig":
            findedmatch = soup.find_all("div",{"class","responsive-table-wrap scoreboard-table-header"})[i]
            maclar = []
            for teams in findedmatch.find_all("a",{"class","team-name"}):
                teams = teams.text[:-3]
                maclar.append(teams)
            j = 0
            for mac in maclar:
                if j % 2 == 0:
                    matches.append(maclar[j].strip()+' vs '+maclar[j+1].strip()+' Match League:'+leaguename.text.strip())
                j += 1
            
        i += 1
    return matches

__all__ = ["dailymatch"]
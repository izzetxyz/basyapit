import config
from datetime import datetime
import requests as rq
import logging
import ast
import json
config = config.Config('./config/config.py')
def discord_webhook(macadi,mactahmini,fotograf):
    '''
    Sends a test Discord webhook notification
    '''
    data = {
            "username": config.USERNAME,
            "avatar_url": config.AVATAR_URL,
            "embeds": [{
                "title": macadi,
                "thumbnail": {"url": fotograf},
                "color": int(config.COLOUR),
                "footer": {'text': 'made by izzy'},
                "timestamp": str(datetime.utcnow()),      
                "fields": []    
            }]
    }
    try:
        for item in mactahmini.split(','):
            stocklar = {
                'name': item.split(":")[0], 'value': item.split(":")[1],"inline": True
            }
            data["embeds"][0]["fields"].append(stocklar)
    except Exception as hata:
        print(hata)
    result = rq.post(config.WEBHOOK, data=json.dumps(data), headers={"Content-Type": "application/json"})
    
    try:
        result.raise_for_status()
    except rq.exceptions.HTTPError as err:
        logging.error(msg=err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
        logging.info(msg="Payload delivered successfully, code {}.".format(result.status_code))

__all__ = ["discord_webhook"]
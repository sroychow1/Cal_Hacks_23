import os
import asyncio
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import Hume_sentiment_analysis as hume
import math

import requests

async def start():
    load_dotenv()
    url = os.getenv("GET_REQUEST_URL")
    # print('url: ' + url)
    result = requests.get(url)
    
    if result == None:
        print('An error has occured.')
        return
    
    data = result.json()
    # print(data[0]["text"])

    for i in range(3):
        tweet = data[i]
        text = tweet["text"]
        score = await hume.run_hume(text)
        print("score: " + str(score) + " text: \"" + text + "\"")
    
    await asyncio.sleep(10)
    await start()
    

asyncio.run(start())


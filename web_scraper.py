import os
import asyncio
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import Hume_sentiment_analysis as hume
import math
import firebase_helper as fb

import requests

run_ids = []
left_url = ""
right_url = ""
token=""
async def start():
    run_id = 'last'
    url = left_url + str(run_id) + right_url
    # print(url)

    result = requests.get(str(url))
    
    if not result:
        print('An error has occured.')
        return
    
    data = result.json()
    # print(data[0]["text"])

    negative_tweets_indices = []
    # data = data[:3]
    for i in range(len(data)):
        tweet = data[i]
        text = tweet["text"]
        score = await hume.run_hume(text)
        if (is_negative(score)):
            negative_tweets_indices.append(i)
        print("tweet id: " + str(tweet["id"]) + " score: " + str(score))
    
    # TODO: for every score above the threshold, upload that tweet to firebase
    for i in range(len(negative_tweets_indices)):
        await fb.upload_tweet(data[negative_tweets_indices[i]])

    # await asyncio.sleep(10)
    # await start()
    
# async def search_runs():
#     url = "https://api.apify.com/v2/acts/actorId/runs?" +
# token=soSkq9ekdmfOslopH&offset=0&limit=20&desc=true&status=SUCCEEDED

def is_negative(score):
    return score > 0

def initialize_and_start():
    load_dotenv()
    global left_url
    global right_url
    global token
    # url = os.getenv("GET_REQUEST_URL")
    left_url = os.getenv("LEFT_GET_REQUEST_URL")
    right_url = os.getenv("RIGHT_GET_REQUEST_URL")
    token = os.getenv("TOKEN")

    asyncio.run(start())

initialize_and_start()


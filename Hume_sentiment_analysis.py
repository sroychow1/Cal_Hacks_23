import asyncio
import os
from dotenv import load_dotenv

from hume import HumeStreamClient, StreamSocket
from hume.models.config import LanguageConfig
import random as Random


negative_emotions = ["anger", "disgust", "fear", "sadness", "envy", "horror", "pain", "surprise (negative)"]
load_dotenv()
HUME_API_KEY = os.getenv("HUME_API_KEY")

async def query_hume(text):
    client = HumeStreamClient(HUME_API_KEY)
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        # result = await socket.send_file("./test.text")
        result = await socket.send_text(text)

        emotions = result['language']['predictions'][0]['emotions']
        sorted_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)
        top_10_emotions = [item for item in sorted_emotions[:10]]
        # top_10_emotions = sorted_emotions[:10]
        # print(top_10_emotions)
        dict = convert_to_dict(top_10_emotions)
        # print(dict)
        # return 1;
        return negativity_score(dict)


async def run_hume(text):
    return await query_hume(text)
    
def negativity_score(emotions) -> float:
    return Random.randrange(0, 100, 1) / 100

def convert_to_dict(emotions):
    dict = {}
    for item in emotions:
        dict[item["name"]] = item["score"]
    return dict

def mean_score(emotions):
    total_scores = 0
    num_negative_emotions = 1
    for item in emotions.keys():
        if (item.lower() in negative_emotions):
            total_scores += emotions[item]
            num_negative_emotions += 1
    return total_scores / num_negative_emotions

# score = asyncio.run(run_hume("programmers should get their heads chopped off"))
# print("score: " + str(score))
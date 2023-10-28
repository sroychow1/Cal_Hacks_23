import asyncio

from hume import HumeStreamClient, StreamSocket
from hume.models.config import LanguageConfig


negative_emotions = ["anger", "disgust", "fear", "sadness", "envy", "horror", "pain", "surprise (negative)"]

async def query_hume(text):
    client = HumeStreamClient("1cJ51ZOtKPkG4GXbPjZoHESZOo2ou2IMTUS1lLBFgHa4pASm")
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        # result = await socket.send_file("./test.text")
        result = await socket.send_text(text)

        emotions = result['language']['predictions'][0]['emotions']
        sorted_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)
        top_10_emotions = [item['name'] for item in sorted_emotions[:10]]
        # print(emotions)
        return negativity_score(emotions)

async def run_hume(text):
    return await query_hume(text)
    
def negativity_score(emotions) -> float:
    return mean_score(emotions);

def mean_score(emotions):
    total_scores = 0
    num_negative_emotions = 1
    for item in emotions:
        if (item["name"].lower() in negative_emotions):
            total_scores += item["score"]
            num_negative_emotions += 1
    return total_scores / num_negative_emotions

# def print_emotion_keys(emotions):
#     for item in emotions:
#         print(item["name"])
    
# score = asyncio.run(run_hume("I hate programmers, they deserve to go to jail"))
# print("score: " + str(score))
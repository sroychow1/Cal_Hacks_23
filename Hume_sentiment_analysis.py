import asyncio

from hume import HumeStreamClient, StreamSocket
from hume.models.config import LanguageConfig

async def main():
    client = HumeStreamClient("1cJ51ZOtKPkG4GXbPjZoHESZOo2ou2IMTUS1lLBFgHa4pASm")
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        result = await socket.send_file("./test.text")
        emotions = result['language']['predictions'][0]['emotions']
        sorted_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)
        top_10_emotions = [item['name'] for item in sorted_emotions[:10]]
        print(emotions)


asyncio.run(main())


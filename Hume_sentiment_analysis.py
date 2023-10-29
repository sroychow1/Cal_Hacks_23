import asyncio
import numpy as np

from hume import HumeStreamClient, StreamSocket
from hume.models.config import LanguageConfig

async def main():
    client = HumeStreamClient("6zhPTYAeccmYjFwgfCMIwXbdtszFAuKn6sT5HdSSAbIWmQyu")
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        result = await socket.send_file("test.txt")
        emotions = result['language']['predictions'][0]['emotions']
        sorted_emotions = sorted(emotions, key=lambda x: x['name'])
        vector_vals = [item['score'] for item in sorted_emotions]
        vector = np.array(vector_vals)
        return np.transpose(vector)


asyncio.run(main())
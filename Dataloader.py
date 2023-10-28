import pandas as pd
import torch 
from torch.utils.data import Dataset, DataLoader
import asyncio
from hume import HumeStreamClient, StreamSocket
from hume.models.config import LanguageConfig
import numpy as np
from Embeddings import Embedding
import intel_extension_for_pytorch as ipex

class ToxicCommentDataset(Dataset):
    client = HumeStreamClient("1cJ51ZOtKPkG4GXbPjZoHESZOo2ou2IMTUS1lLBFgHa4pASm")
    config = LanguageConfig()

    def __init__(self, path_to_csv) -> None:
        self.data = pd.read_csv(path_to_csv)
        self.len = len(self.data)

    def __len__(self):
        return self.len

    def __getitem__(self, idx):
        text = self.data.loc[idx, 'comment_text']
        selected_columns = self.data[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].iloc[idx]
        toxic_tensor = torch.tensor(selected_columns.values, dtype=torch.float32)  # Now a 1D tensor

        # Run the async method synchronously and block on the result
        loop = asyncio.new_event_loop()
        #print("text", len(text))
        hume_tensor = loop.run_until_complete(self.hume_analysis(text[0:999]))
        #print("tensor", len(hume_tensor))
        loop.close()

        embedding_tensor = self.embedding_of_text(text)
        concatenated_tensor = torch.cat((toxic_tensor.unsqueeze(0), hume_tensor.unsqueeze(0), embedding_tensor.unsqueeze(0)), dim=1)  # Ensure compatible dimensions
        flattened_tensor = torch.flatten(concatenated_tensor)
        label = self.get_label(toxic_tensor)

        return flattened_tensor, label
       

    async def hume_analysis(self,text):
        async with self.client.connect([self.config]) as socket:
            result = await socket.send_text(text)
            emotions = result['language']['predictions'][0]['emotions']
            scores = [item['score'] for item in emotions if 'score' in item]
            scores_array = np.array(scores).astype(np.float32) 
            return torch.tensor(scores_array, dtype=torch.float32)

    def embedding_of_text(self, text):
        return torch.tensor(Embedding(text).embeddings,dtype=torch.float32)


    def get_label(self,tensor):
        return np.linalg.norm(tensor) == 0
            
        


if __name__=="__main__":
    data = ToxicCommentDataset(path_to_csv='/home/ubuntu/Cal_Hacks_23/train.csv')
    inputs, label = data.__getitem__(4)

    print(inputs.shape)
    print(label)
    
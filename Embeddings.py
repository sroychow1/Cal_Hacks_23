import umap
from transformers import AutoModel
from numpy.linalg import norm
import matplotlib.pyplot as plt
import intel_extension_for_pytorch as ipex
import numpy as np

class Embedding():
    model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-en', trust_remote_code=True)
    model = ipex.optimize(model)

    def __init__(self, text):
        self.text = text
        self.embeddings = self.generate_embeddings(self.text)  # adjusted to unpack the returned tuple
    
    def generate_embeddings(self, text):
        embeddings = self.model.encode(text)
        return embeddings
    



    

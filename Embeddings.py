from transformers import AutoModel
from numpy.linalg import norm
import intel_extension_for_pytorch as ipex

cos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))
model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-en', trust_remote_code=True) # trust_remote_code is needed to use the encode method

model = ipex.optimize(model)

embeddings = model.encode(['How is the weather today?', 'What is the current weather like today?'])
print(embeddings[0], embeddings[1])

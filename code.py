!pip install transformers torchvision pillow
from transformers import ViTForImageClassification,ViTImageProcessor
from PIL import Image
import requests
import torch
import time

url="https://i0.wp.com/segredosdomundo.r7.com/wp-content/uploads/2024/10/Tamandua-Bandeira-curiosidades-1.jpg?w=1500&ssl=1"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

model=ViTForImageClassification.from_pretrained ("google/vit-large-patch16-224")
feature_extractor = ViTImageProcessor.from_pretrained ("google/vit-large-patch16-224")

# Pré-processar imagem 
inputs = feature_extractor(images=image, return_tensors="pt") 

ti=time.time()
# Inferência 
model.eval() 

with torch.no_grad(): 
  outputs = model(**inputs) 
  probs = torch.nn.functional.softmax(outputs.logits, dim=1) 
  pred = torch.argmax(probs) 
tf=time.time()
tt=tf-ti

# Obter o nome da classe 
label = model.config.id2label[pred.item()] 
print(f"Classe predita: {label} Tempo: {tt}") 

# Get the top 5 classes and their probabilities
top_probs, top_preds = torch.topk(probs, k=10)

# Print the top 5 predictions
for prob, pred in zip(top_probs[0], top_preds[0]):
    label = model.config.id2label[pred.item()]
    print(f"Classe: {label} | Probabilidade: {prob.item():.4f}")

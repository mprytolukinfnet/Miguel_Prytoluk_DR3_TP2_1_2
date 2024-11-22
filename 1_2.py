from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import torch

# Inicialização do FastAPI
app = FastAPI()

# Modelo de entrada
class TextInput(BaseModel):
    text: str

# Verifica se uma GPU está disponível
device = 0 if torch.cuda.is_available() else -1

# Carregar o pipeline de tradução
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr", device=device)

@app.post("/translate/")
async def translate_text(input: TextInput):
    translated = translator(input.text)
    return {"input": input.text, "translation": translated[0]['translation_text']}

"""
Necessário Instalar Pytorch: https://pytorch.org/get-started/locally/

Executar com
curl -X POST "http://127.0.0.1:8000/translate/" \
-H "Content-Type: application/json" \
-d '{"text": "I am a Data Scientist and work with machine learning models on a daily basis."}'
"""
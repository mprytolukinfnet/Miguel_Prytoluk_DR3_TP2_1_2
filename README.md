# TP2 Exercício 1_2: Tradução do Inglês para o Francês
Este aplicativo utiliza o modelo Helsinki-NLP/opus-mt-en-fr da HuggingFace para traduzir textos do inglês para o francês.

**Passos para Configuração**:

1. Certifique-se de que o ambiente Python está configurado.
2. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```
3. Instalar Pytorch: https://pytorch.org/get-started/locally/

**Como Executar**: Inicie o servidor FastAPI com o comando:
```bash
uvicorn 1_2:app --reload
```

**Uso da API**: Realize uma tradução com:

```bash
curl -X POST "http://127.0.0.1:8000/translate/" \
-H "Content-Type: application/json" \
-d '{"text": "I am a Data Scientist."}'
```
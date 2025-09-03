import requests  


OLLAMA_URL = "http://localhost:11434"


def chat_simples(pergunta):
    
    payload = {
        "model": "gemma3:1b",  # Modelo a usar
        "messages": [{"role": "user", "content": pergunta}],  # Mensagem do usuário
        "stream": False  # Não usar stream para simplicidade
    }
    
    # Envia a requisição POST
    response = requests.post(f"{OLLAMA_URL}/api/chat", json=payload)
    
    # Verifica se deu certo e retorna a resposta
    if response.status_code == 200:
        return response.json()["message"]["content"]
    else:
        return "Erro na API!"

# Exemplo de uso
pergunta = "O que é Ollama?"
print(pergunta)
resposta = chat_simples(pergunta)
print(resposta)  # Mostra a resposta do LLM sem contexto (pode alucinar)
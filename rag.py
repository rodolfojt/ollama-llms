import requests
import numpy as np 

OLLAMA_URL = "http://localhost:11434"


def gerar_embedding(texto):
    """
    Função para gerar embedding de um texto
    """
    payload = {
        "model": "qwen3:4b",  # Modelo de embeddings
        "input": texto  # Texto para embeddar
    }
    response = requests.post(f"{OLLAMA_URL}/api/embed", json=payload)
    if response.status_code == 200:
        return np.array(response.json()["embeddings"][0])  # Retorna o vetor como array
    else:
        return None

def preparar_rag():
    """
    Carrega o FAQ e gera embeddings (divida em chunks simples).
    """
    chunks = [
        "Pergunta: O que é Ollama? Resposta: Ollama é uma ferramenta para rodar LLMs localmente.",
        "Pergunta: Como instalar Ollama? Resposta: Baixe do site oficial e execute o instalador.",
        "Pergunta: Qual modelo usar para embeddings? Resposta: Modelos como all-minilm são bons para embeddings."
    ]
    
    embeddings = []  # Lista para armazenar vetores
    for chunk in chunks:
        emb = gerar_embedding(chunk)
        if emb is not None:
            embeddings.append((chunk, emb))  # Armazena texto e embedding
    
    return embeddings  # Retorna o "vetor store" simples

def buscar_top_k(pergunta, embeddings, k=2):
    """
    Função para buscar top-k similares (usa similaridade cosseno)
    """
    emb_pergunta = gerar_embedding(pergunta)
    if emb_pergunta is None:
        return []
    
    similaridades = []  # Calcula similaridade
    for chunk, emb_chunk in embeddings:
        # Similaridade cosseno: dot product / (normas)
        sim = np.dot(emb_pergunta, emb_chunk) / (np.linalg.norm(emb_pergunta) * np.linalg.norm(emb_chunk))
        similaridades.append((sim, chunk))
    
    # Ordena e pega top-k
    similaridades.sort(reverse=True)
    return [chunk for sim, chunk in similaridades[:k]]


def chat_com_rag(pergunta, embeddings):
    """
    Função de chat com RAG.
    """
    # Busca contexto relevante
    contexto = buscar_top_k(pergunta, embeddings)
    contexto_texto = "\n".join(contexto)  # Junta os chunks
    
    # Prepara prompt com contexto
    prompt = f"Contexto: {contexto_texto}\nPergunta: {pergunta}\nResponda baseado no contexto."
    
    payload = {
        "model": "meu-llm",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    
    response = requests.post(f"{OLLAMA_URL}/api/chat", json=payload)
    if response.status_code == 200:
        return response.json()["message"]["content"]
    else:
        return "Erro na API!"

# Exemplo de uso
print("Iniciando RAG...")
embeddings = preparar_rag()  # Prepara o RAG uma vez
#print("embeddings:", embeddings)
embeddings = []
print("RAG preparado! ")
pergunta = "Como instalar Ollama?"
print(f"---- Pergunta: {pergunta}")
resposta = chat_com_rag(pergunta, embeddings)
print(f"---- Resposta: {resposta}")  # Agora responde baseado no FAQ!

#contexto = buscar_top_k(pergunta, embeddings)
#print("Mostrando contexto...")
#print(f"---- Contexto: {contexto}")
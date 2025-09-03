# Workshop RAG com Ollama

## Objetivo
Este repositório contém scripts Python simples para demonstrar o uso prático de **Large Language Models (LLMs)** locais com **Retrieval-Augmented Generation (RAG)**.  
O foco é mostrar como resolver problemas reais, como buscar respostas em documentos locais (ex: um FAQ), evitando "alucinações" do modelo.  
Usamos o **Ollama** como ferramenta principal para rodar LLMs localmente, promovendo **privacidade** e **controle sobre os dados**.

---

## O que é Ollama?
O **Ollama** é uma ferramenta **open-source gratuita** que permite rodar LLMs diretamente no seu computador, sem depender de serviços na nuvem.  
Ele suporta modelos como **Llama**, **Mistral** e outros, via uma API simples (HTTP).  

Isso é ideal para desenvolvedores que querem integrar IA em aplicações locais, com foco em **privacidade** e **custo zero**.  

Exemplo de uso:  

```bash
ollama pull gemma3:1b
````

## O que é RAG?
O **RAG (Retrieval-Augmented Generation)** é uma técnica que melhora as respostas de LLMs.  

Em vez de o modelo responder só com o que "sabe" (o que pode levar a erros), o RAG primeiro **busca informações relevantes em documentos locais** (usando **embeddings**, representações numéricas de texto). Depois, passa esse contexto ao LLM para gerar uma resposta **precisa e baseada em fatos**.  

É como dar "dicas" ao modelo antes de ele falar!

---

## Instruções de Instalação

### 1. Instale o Ollama
- Acesse [ollama.com](https://ollama.com) e baixe o instalador para o seu SO (Windows, macOS ou Linux).  
- Rode o instalador e verifique:  
  ```bash
    ollama --version
  ```

### 2. Baixe os modelos necessários

```bash
ollama pull gemma3:1b   # Para chat
ollama pull qwen3:4b # Para embeddings
```

### 3. Instale Python e Bibliotecas
- Tenha Python 3.8+ instalado (python.org).
- Crie um ambiente virtual (opcional, recomendado):

```
python3 -m venv .venv
```

Ative o ambiente virtual (Linux/macOS):
``` bash
source env/bin/activate
```

Ative o ambiente virtual (Windows):
``` bash
.\env\Scripts\activate
```

Instale as dependências:
``` bash
pip3 install requests numpy
```

### 4. Customização com Modelfile

Não é um script Python, mas uma configuração. Crie um arquivo Modelfile definindo um modelo baseado em gemma3 com um prompt de sistema fixo para respostas em PT-BR concisas. Use o comando ollama create meu-llm -f Modelfile no terminal.
Atualize os scripts anteriores mudando o modelo para meu-llm. Isso personaliza o comportamento do LLM.

Licença: MIT.
# Projeto RAG Simples com Ollama

Este projeto demonstra uma implementação básica de Retrieval-Augmented Generation (RAG) utilizando o Ollama para embeddings e um modelo de linguagem, juntamente com a biblioteca Langchain para orquestração.

## Arquivos do Projeto

O projeto é composto por quatro arquivos principais em Python:

1.  **`carrega_e_separa.py`**: Responsável por carregar os documentos (atualmente suporta arquivos PDF e TXT) de um diretório especificado e dividi-los em partes menores (chunks) para facilitar o processamento dos embeddings. Futuramente (acompanhe os proximos commits) pretendo usar o docling para gerenciar essa parte de carregar os documentos ja que a lib suporta varios formatos.

2.  **`embbegings.py`**: Contém a classe `OllamaCustomEmbeddings`, responsável por gerar embeddings de texto utilizando a API local do Ollama. Este trecho, pretendo consumir um modelo local rodando em um servidor proprio, ainda preciso aprender Nginx para deixar essa comunicação segura.
  
4.  **`rag.py`**: Este script utiliza as funções de `carrega_e_separa.py` para carregar e dividir os documentos, usa a classe `OllamaCustomEmbeddings` para gerar os embeddings desses chunks e, finalmente, cria um índice FAISS (Facebook AI Similarity Search) para armazenar e pesquisar esses embeddings. O índice é então salvo localmente.

5.  **`testando o rag.py`**: Este script carrega o índice FAISS salvo, inicializa um modelo de linguagem do Ollama e cria uma cadeia `RetrievalQA` para responder a perguntas com base nos documentos indexados. Ele também retorna os documentos de origem que foram usados para gerar a resposta.

## Pré-requisitos

* **Python:** Certifique-se de ter o Python instalado (versão 3.7 ou superior é recomendada).
* **Ollama:** Você precisa ter o Ollama instalado e rodando localmente. Além disso, o modelo de embedding (`nomic-embed-text`) e o modelo de linguagem (`gemma3:1b` ou outro de sua escolha) devem estar baixados no Ollama. Você pode baixá-los executando comandos como `ollama pull nomic-embed-text` e `ollama pull gemma3:1b` no seu terminal. É bem tranquilo executar localmente ate para computadores menos potentes, caso ocorra um consumo muito grande de memoria ram considera um modelo menor como o Qwen2.5:0.5b.
  
* **Dependências Python:** As bibliotecas listadas no arquivo `requirements.txt` precisam ser instaladas. Você pode instalá-las executando `pip install -r requirements.txt` no diretório do projeto (preferencialmente dentro de um ambiente virtual). 

## Como Usar

1.  **Clone o repositório (se aplicável) ou crie os arquivos conforme mostrado acima.**
2.  **Crie um diretório chamado `arquivos`** no mesmo local dos seus scripts Python e coloque seus arquivos PDF e TXT dentro dele. Se você quiser usar um diretório diferente, atualize a variável `diretorio_dos_arquivos` no arquivo `rag.py`.
3.  **Execute o script `rag.py`:**
    ```bash
    python rag.py
    ```
    Este script carregará seus documentos, criará os embeddings usando o Ollama e salvará o índice FAISS na pasta `meu_indice_rag_ollama`.
4.  **Execute o script `testando o rag.py`:**
    ```bash
    python testando_o_rag.py
    ```
    **Lembre-se de substituir `"caminho dos seus arquivos_"` no `testando o rag.py` e `rag.py` pelo caminho correto para onde o índice foi salvo.** Este script carregará o índice, fará uma pergunta de teste e imprimirá a resposta gerada pelo modelo de linguagem, juntamente com os documentos de origem.

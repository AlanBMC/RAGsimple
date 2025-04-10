from langchain.vectorstores import FAISS
from embbegins import OllamaCustomEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

# Carregue o índice FAISS salvo
nome_indice = "caminho dos seus arquivos_/meu_indice_rag_ollama"
embeddings = OllamaCustomEmbeddings(model_name="nomic-embed-text")
vectorstore = FAISS.load_local(nome_indice, embeddings, allow_dangerous_deserialization=True)

retri = vectorstore.as_retriever(search_kwargs={'k': 1})
llm = Ollama(model='gemma3:1b', temperature=0.2)
qa_com_source =  RetrievalQA.from_llm(llm=llm, retriever=retri, return_source_documents= True)
pergunta = 'pergunta'
#reposta =  qa(pergunta)
resultado = qa_com_source({"query": pergunta})

print(f"Pergunta: {pergunta}")
print(f"Resposta: {resultado['result']}")
print("\nDocumentos de Origem:")
print('documento de origin: ',  resultado['source_documents'])
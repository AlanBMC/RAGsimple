import os
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def carregar_documentos(diretorio):
    """Carrega documentos PDF e TXT de um diretório."""
    documentos = []
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if arquivo.endswith(".pdf"):
            loader = PyPDFLoader(caminho_arquivo)
            documentos.extend(loader.load())
        elif arquivo.endswith(".txt"):
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                texto = f.read()
            documentos.append(Document(page_content=texto, metadata={"source": caminho_arquivo}))
    return documentos
            
def dividir_documentos(documentos, tamanho_chunk=1000, sobreposicao_chunk=200):
    """
    Divide os documentos em partes menores para processamento
    fazemos um chunking dos documentos
    
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=tamanho_chunk, chunk_overlap=sobreposicao_chunk
    )
    chunks = text_splitter.split_documents(documentos)
    #chunk_size = 1000 é basicamente quanto de careacteres queremos que cada parte tenha
    #chunk_overlap = 200 é a quantidade de caracteres que se sobrepoem entre os chunks
    #length_function = len é a função que vai contar os caracteres
    return chunks


from langchain.vectorstores import FAISS
from embbegins import OllamaCustomEmbeddings
from carrega_e_separa import carregar_documentos, dividir_documentos
custom_embeddings = OllamaCustomEmbeddings(model_name="nomic-embed-text")

diretorio_dos_arquivos = "caminho do arquivo"  # Substitua pelo caminho do seu diretório
documentos_carregados = carregar_documentos(diretorio_dos_arquivos)
chunks_de_texto = dividir_documentos(documentos_carregados)
# Assumindo que você já tem seus 'chunks_de_texto' do passo anterior
# Crie o índice FAISS usando os embeddings customizados do Ollama
vectorstore = FAISS.from_documents(chunks_de_texto, custom_embeddings)

# Salve o índice para uso posterior
nome_indice = "meu_indice_rag_ollama"
vectorstore.save_local(nome_indice)

print(f"Embeddings criados com Ollama e índice FAISS salvo em '{nome_indice}'.")

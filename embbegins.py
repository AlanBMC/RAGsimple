from langchain_core.embeddings import Embeddings
from typing import List
import requests
import json

class OllamaCustomEmbeddings(Embeddings):
    """Embeddings usando a API do Ollama."""

    def __init__(self, model_name="nomic-embed-text", ollama_base_url="http://localhost:11434"):
        self.model_name = model_name
        self.ollama_base_url = ollama_base_url

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        embeddings = [self._get_embedding(text) for text in texts]
        return embeddings

    def embed_query(self, text: str) -> List[float]:
        return self._get_embedding(text)

    def _get_embedding(self, text: str) -> List[float]:
        url = f"{self.ollama_base_url}/api/embeddings"
        headers = {"Content-Type": "application/json"}
        data = {"prompt": text, "model": self.model_name}
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            response.raise_for_status()
            return response.json()["embedding"]
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Erro ao comunicar com a API do Ollama: {e}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Erro ao processar a resposta da API do Ollama: {e}")
 
"""
Multimodal processing pipeline using Voyage AI.
"""
import os
from typing import List, Union, Tuple
from PIL import Image
import numpy as np
from voyageai import Client

class MultimodalPipeline:
    def __init__(self, api_key: str = None, model_name: str = "voyage-multimodal-3"):
        """
        Initialize the multimodal pipeline.
        
        Args:
            api_key: Voyage AI API key. If None, will try to get from environment variable.
            model_name: Name of the Voyage AI model to use.
        """
        if api_key is None:
            api_key = os.getenv('VOYAGE_API_KEY')
            if api_key is None:
                raise ValueError("No API key provided and VOYAGE_API_KEY not found in environment")
        
        self.client = Client(api_key=api_key)
        self.model_name = model_name
    
    def embed_documents(self, 
                       documents: List[List[Union[str, Image.Image]]],
                       normalize: bool = True) -> np.ndarray:
        """
        Generate embeddings for a list of documents.
        Each document can contain interleaved text and images.
        
        Args:
            documents: List of documents, where each document is a list of strings and/or PIL Images
            normalize: Whether to L2-normalize the embeddings
            
        Returns:
            Document embeddings as a numpy array
        """
        result = self.client.multimodal_embed(
            documents=documents,
            model=self.model_name,
            normalize=normalize
        )
        return result.embeddings
    
    def compute_similarity(self, query_embedding: np.ndarray, document_embeddings: np.ndarray) -> np.ndarray:
        """
        Compute cosine similarity between a query embedding and document embeddings.
        
        Args:
            query_embedding: Query embedding vector
            document_embeddings: Matrix of document embeddings
            
        Returns:
            Array of similarity scores
        """
        return np.dot(document_embeddings, query_embedding)
    
    def search_documents(self, 
                        query: List[Union[str, Image.Image]], 
                        documents: List[List[Union[str, Image.Image]]],
                        top_k: int = 5) -> List[Tuple[int, float]]:
        """
        Search documents using a query.
        
        Args:
            query: Query as a list of strings and/or images
            documents: List of documents to search through
            top_k: Number of top results to return
            
        Returns:
            List of (document_index, similarity_score) tuples
        """
        # Embed query and documents
        query_embedding = self.embed_documents([query])[0]
        doc_embeddings = self.embed_documents(documents)
        
        # Compute similarities
        similarities = self.compute_similarity(query_embedding, doc_embeddings)
        
        # Get top-k results
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        return [(idx, similarities[idx]) for idx in top_indices]
    
    def batch_embed_documents(self, 
                            documents: List[List[Union[str, Image.Image]]], 
                            batch_size: int = 32) -> np.ndarray:
        """
        Embed documents in batches to handle large document collections.
        
        Args:
            documents: List of documents to embed
            batch_size: Size of each batch
            
        Returns:
            Matrix of document embeddings
        """
        embeddings = []
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i + batch_size]
            batch_embeddings = self.embed_documents(batch)
            embeddings.append(batch_embeddings)
        return np.vstack(embeddings)

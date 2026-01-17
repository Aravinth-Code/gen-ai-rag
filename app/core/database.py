import os
from langchain_community.vectorstores.pgvector import PGVector
from langchain_community.embeddings import OpenAIEmbeddings
from app.core.config import config


COLLECTION_NAME = "documents"

def get_pgvector_store(embeddings=None):
    if embeddings is None:
        embeddings = OpenAIEmbeddings()

    return PGVector(
        collection_name=COLLECTION_NAME,
        connection_string=config.DATABASE_URL,
        embedding_function=embeddings,
    )
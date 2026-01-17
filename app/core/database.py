import os
from langchain_community.vectorstores.pgvector import PGVector
from langchain_community.embeddings import OpenAIEmbeddings

POSTGRES_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/ragdb"
)

COLLECTION_NAME = "documents"

def get_pgvector_store(embeddings=None):
    if embeddings is None:
        embeddings = OpenAIEmbeddings()

    return PGVector(
        collection_name=COLLECTION_NAME,
        connection_string=POSTGRES_URL,
        embedding_function=embeddings,
    )

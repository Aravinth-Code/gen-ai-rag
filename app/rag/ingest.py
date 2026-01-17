from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.core.database import get_pgvector_store

def ingest_documents(docs: list[str], source: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=60
    )

    chunks = splitter.create_documents(
        docs,
        metadata = [{"source": source}] * len(docs)
    )

    vectorstore = get_pgvector_store()
    vectorstore.add_documents(chunks)
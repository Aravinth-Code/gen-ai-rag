from app.core.database import get_pgvector_store

def retrieve_context(query: str, k: int = 4):
    vectorstore = get_pgvector_store()
    results = vectorstore.similarity_search(query, k=k)

    return "\n\n".join([r.page_content for r in results])
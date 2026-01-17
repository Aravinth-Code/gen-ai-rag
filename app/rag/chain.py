from app.rag.prompts import SYSTEM_PROMPT
from app.rag.retriever import retrieve_context
from openai import OpenAI

client = OpenAI()

def run_rag(query: str):
    context = retrieve_context(query)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{query}"
            }
        ]
    )
    return response.choices[0].message.content

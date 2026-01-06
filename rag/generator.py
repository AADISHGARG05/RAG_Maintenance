from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(contexts, query):
    if not contexts:
        return "Answer not found in provided documents."

    prompt = f"""
Answer strictly from the context below.
If the answer is not present, say "Answer not found in provided documents."

Context:
{chr(10).join(contexts)}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()
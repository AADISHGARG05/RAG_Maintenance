from groq import Groq
import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL_NAME = "llama-3.1-8b-instant"
def generate_answer(contexts, query):
    if not contexts:
        return "Answer not found in provided documents.", []

    prompt = f"""
You are a document-grounded assistant.

Answer ONLY using the context below.
If the answer is not in the context, say:
"Answer not found in provided documents."

Context:
{chr(10).join(contexts)}

Question:
{query}

Answer:
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=512
        )

        return response.choices[0].message.content.strip(), []

    except Exception as e:
        return f"Groq API error: {str(e)}", []
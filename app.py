from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

from rag.retriever import retrieve_relevant_chunks
from rag.generator import generate_answer

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ui")
def ui():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat_endpoint():
    data = request.get_json()
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"answer": "Empty query received.", "sources": []})

    contexts, sources = retrieve_relevant_chunks(query)
    answer = generate_answer(contexts, query)

    return jsonify({
        "answer": answer,
        "sources": sources
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
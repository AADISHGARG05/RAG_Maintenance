from flask_cors import CORS
from flask import Flask, request, jsonify, render_template
import os
from rag.retriever import retrieve_relevant_chunks
from rag.generator import generate_answer
app = Flask(__name__)
CORS(app)  
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
@app.route("/", methods=["GET"])
def health_check():
    return {"status": "RAG backend running"}
@app.route("/ui", methods=["GET"])
def chat_ui():
    return render_template("chat.html")
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "query" not in data:
        return jsonify({"error": "Query not provided"}), 400
    query = data["query"].strip()
    if not query:
        return jsonify({"error": "Empty query"}), 400
    contexts, sources = retrieve_relevant_chunks(query)
    answer, _ = generate_answer(contexts, query)
    return jsonify({
        "query": query,
        "answer": answer,
        "sources": sources
    })
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
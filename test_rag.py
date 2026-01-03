from rag.retriever import retrieve_relevant_chunks
from rag.generator import generate_answer
query = "What is machine learning? "
contexts, sources = retrieve_relevant_chunks(query)
answer, _ = generate_answer(contexts, query)
print("\nANSWER:\n", answer)
print("\nSOURCES:\n", sources)

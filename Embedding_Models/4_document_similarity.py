from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",  # Google's embedding model
    dimensions=300  # Specify the dimensions if needed
)
docs = [
    "India is a country in South Asia.",
    "The capital of India is New Delhi.",
    "The capital of Japan is Tokyo.",
    "The capital of France is Paris."
]

query = "Tell me about India"

doc_embeddings = embedding.embed_documents(docs)
query_embedding = embedding.embed_query(query)


scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# print(list(enumerate(scores))) # this will print the index and similarity score of each document

# print(sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)) # sorted list of documents based on similarity score
sorted_scores = sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)
index, score = sorted_scores[0]

print("query:", query)
print(docs[index])
print("Similarity Score:", score)
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
# a small 90M model

text = "Delhi is the capital of India."

docs = [
    "India is a country in South Asia. It is the seventh-largest country by land area, the second-most populous country, and the most populous democracy in the world. The capital of India is New Delhi.",
    "The capital of Japan is Tokyo. It is the largest city in Japan and one of the most populous metropolitan areas in the world.",
    "The capital of France is Paris. It is known for its art, fashion, gastronomy, and culture."
]

vector = embedding.embed_query(text)

doc_vectors = embedding.embed_documents(docs)
# print(str(vector))
print(str(doc_vectors))
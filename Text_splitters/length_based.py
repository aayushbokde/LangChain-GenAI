from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
text = """

Clownfishes are saltwater fishes found in the warm and tropical waters of the Indo-Pacific. They mainly inhabit coral reefs and have a distinctive colouration typically consisting of white vertical bars on a red, orange, yellow, brown or black background. Clownfishes developed a symbiotic and mutually beneficial relationship with sea anemones, which they rely on for shelter and protection, while they in turn, clean, fan and protect them. Clownfishes live in groups consisting of a breeding female and male, along with some non-breeding individuals. The female ranks at the top of the hierarchy, followed by the breeding male. The recognisable colour patterns and social nature of clownfishes have contributed to their popularity, having appeared in the film Finding Nemo. They are highly sought after in the aquarium trade and are often taken from the wild, which has led to their decline.

"""
loader = PyPDFLoader(r'C:\Users\aayus\Downloads\Langchain+GenAI\Document_Loaders\cricket.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator = ''
)
result = splitter.split_documents(docs)

print(result[0].page_content)

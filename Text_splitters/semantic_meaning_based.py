from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    GoogleGenerativeAIEmbeddings(
        model = "gemini-embedding-001"
    ), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=0.5 
)

sample = """

Agriculture is the practice of cultivating the soil, planting, raising, and harvesting both food and non-food crops, as well as livestock production.A gun is a device that propels a projectile using pressure or explosive force.[1][2] The projectiles are typically solid, but can also be pressurized liquid (e.g. in water guns or cannons), or gas (e.g. light-gas gun).

Terrorism, in its broadest sense, is the use of violence against non-combatants to achieve political or ideological aims.[1] The term is used in this regard primarily to refer to intentional violence during peacetime or in the context of war against non-combatants.[2] There are various different definitions of terrorism, with no universal agreement about it.[3][4][5] Different definitions of terrorism emphasize its randomness, its aim to instill fear, and its broader impact beyond its immediate victims.[1]


"""

docs = text_splitter.create_documents([sample])
print(len(docs))
print(docs)
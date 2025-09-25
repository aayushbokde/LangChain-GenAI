# from langchain_anthropic import ChatAnthropic (this will nor work, as it strictly accepsts anthropic API key)
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()
import os


API_KEY = os.getenv("OPENROUTER_API_KEY")
# we can use anthropic models with openrouter API key 

llm = ChatOpenAI(
    model="anthropic/claude-sonnet-4",
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1",
    max_completion_tokens=1024,
)
#max_completion_tokens is the maximum number of tokens that the model can generate in its response when accessing any Anthropic model.
#max_tokens is not a valid parameter for Anthropic models, it is specific to OpenAI models.
#basically each provider has its own set of parameters and we need to use the correct ones for each provider.

result = llm.invoke("what is the capital of America?")

print(result.content) 

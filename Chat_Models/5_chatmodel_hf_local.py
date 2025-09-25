from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"temperature":0.7, "max_new_tokens":256}
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is the capital of Japan?, be a bit more specific and give answer in a sentence")
print(result.content)

# loacally running the model
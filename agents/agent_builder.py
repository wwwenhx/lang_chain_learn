import os
from openai import AzureOpenAI
from ..configs import API_VERSION, AZURE_ENDPOINT, DEPLOYMENT_NAME, AZURE_API_KEY
from langchain import chat_models

model = chat_models.init_chat_model(model=DEPLOYMENT_NAME, model_provider="azure")
question = "你好 你是谁"
res = model.invoke(question)
print(res.content)

def build_agent():
    client = AzureOpenAI(
        api_key=AZURE_API_KEY,
        api_version=API_VERSION,
        azure_endpoint=AZURE_ENDPOINT
    )
    return client
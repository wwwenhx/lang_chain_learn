from config import API_VERSION, AZURE_ENDPOINT, DEPLOYMENT_NAME, AZURE_API_KEY
from langchain import chat_models

model = chat_models.init_chat_model(model=DEPLOYMENT_NAME, model_provider="azure_openai")
question = "你好 你是谁"
res = model.invoke(question)
print(res.content)
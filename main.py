# 导入langchain包
from langchain import chat_models
from langchain_core.output_parsers import StrOutputParser
from config import DEPLOYMENT_NAME

model = chat_models.init_chat_model(model=DEPLOYMENT_NAME, model_provider="azure_openai")
question = "为什么我部署的服务器版本code-server的vscode 第三方库没有代码提示 以及补全 我使用的是python"
res = model.invoke(question)
print(res.content)
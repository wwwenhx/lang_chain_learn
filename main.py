# 导入langchain包
from langchain import chat_models
from langchain_core.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
from config import DEPLOYMENT_NAME

model = chat_models.init_chat_model(model=DEPLOYMENT_NAME, model_provider="azure_openai")
parser = StructuredOutputParser.from_response_schemas
prompt_template = ChatPromptTemplate([
    ("system", "你是主要学习langchain的高级agent工程师, 请根据你的学生提出的问题 做出解答"),
    ("user","这是你的学生的问题: {topic}, 请详细解答学生的问题")
])
basic_qa_chain  = prompt_template | model | parser
question = "我要从零开始学习agent 并且使用langchain 你会怎么教我 我应该去学习什么技术栈"
res = basic_qa_chain.invoke(question)
print(res)
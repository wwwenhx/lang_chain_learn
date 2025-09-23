# 导入langchain包
from langchain import chat_models
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from config import DEPLOYMENT_NAME

model = chat_models.init_chat_model(model=DEPLOYMENT_NAME, model_provider="azure_openai")
parser = StrOutputParser()
prompt_template = ChatPromptTemplate([
    ("system", "帮我根据用户的语句 推断出他的年龄以及姓名"),
    ("user","这是说的话 : {topic}")
])
basic_qa_chain  = prompt_template | model | parser
question = "我叫王力宏,我今年39岁了"

res = basic_qa_chain.invoke(question)
print(res)
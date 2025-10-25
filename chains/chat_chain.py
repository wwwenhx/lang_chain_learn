from core import llm_load, load_prompt, load_memory, load_parser
import os
from langchain.prompts import MessagesPlaceholder
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

def create_chat_chain():
    model = llm_load()
    prompt = load_prompt("chat")
    parser = load_parser()
    chain = prompt | model | parser
    return chain

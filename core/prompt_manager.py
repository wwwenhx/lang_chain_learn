import os
from langchain.prompts import ChatPromptTemplate
import yaml

def load_prompt(name: str):
    with open("configs/prompts.yaml") as f:
        data = yaml.safe_load(f)
    section = data[name]
    return ChatPromptTemplate.from_messages([
        ("system", section["system"]),
        ("human", section["user"]),
    ])
from langchain.schema import BaseOutputParser
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

class ChatOutput(BaseModel):
    output: str

def load_parser():
    return PydanticOutputParser(pydantic_object=ChatOutput)
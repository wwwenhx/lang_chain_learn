from langchain.schema import BaseOutputParser

class AnswerOutputParser(BaseOutputParser):
    def parse(self, text: str):
        """
        text: LLM 返回的原始文本
        返回字典，包含 answer 字段
        """
        print("Raw LLM output:", text)  # 调试输出
        return text.strip()
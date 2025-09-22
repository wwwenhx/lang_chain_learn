from setuptools import setup, find_packages

setup(
    name="lang_chain_learn",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "langchain",
        "openai",
        "dotenv",
    ],
)
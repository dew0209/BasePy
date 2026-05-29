import os

# 环境变量

# 使用环境变量的方式，在jupyter中执行不合适，需要在.py中执行
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI


# 调用非对话模型
# llms = OpenAI()

# 调用对话模型
chat_model = ChatOpenAI(
    model_name="GLM-5.1",# 默认使用的是gpt3.5
    base_url=os.getenv('Z-AI-URL-ENV'),
    api_key=os.environ['Z-AI-KEY-ENV'],
)

# 调用模型
resp = chat_model.invoke("您好，1 + 1 等于几？")

# 查看响应文本
print(resp.content)
# 安装依赖（如果没有）
# pip install openai python-dotenv

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # 从.env文件加载API Key

# 豆包/DeepSeek/通义千问都支持OpenAI兼容格式
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://api.deepseek.com"  # deepseek API base url
    # 通义千问：base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    # DeepSeek：base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-v4-flash",  # deepseek模型名
    # model="qwen-turbo"     # 通义千问
    messages=[
        {"role": "system", "content": "你是一个友好的AI助手"},
        {"role": "user", "content": "用三句话解释什么是RAG技术"}
    ]
)

print(response.choices[0].message.content)
# 🎉 恭喜！你完成了第一次AI API调用！

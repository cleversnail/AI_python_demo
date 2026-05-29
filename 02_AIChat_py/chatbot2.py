# pip install streamlit openai python-dotenv
# 文件名：chatbot.py

import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://api.deepseek.com"  # deepseek API base url
)

st.title("🤖 我的第一个AI助手")
st.caption("基于deepseek-v4-flash大模型")

# 初始化对话历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史消息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 用户输入
if prompt := st.chat_input("输入你的问题..."):
    # 显示用户消息
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # 获取AI回复（流式输出）
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=[
                {"role": "system", "content": "你是一个专业的AI助手，回答简洁准确"},
                *st.session_state.messages
            ],
            stream=True
        )
        full_response = st.write_stream(
            chunk.choices[0].delta.content or ""
            for chunk in response
            if chunk.choices[0].delta.content
        )
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})

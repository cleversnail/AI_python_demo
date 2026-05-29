# 安装依赖命令：如果没有安装过这些包，需要在终端运行 pip install streamlit openai python-dotenv
# pip install streamlit openai python-dotenv

# 文件名：chatbot.py（基于 Streamlit 和 DeepSeek API 的 AI 聊天机器人）

# ========== 导入依赖库 ==========

# 导入 Streamlit 库，这是一个用于创建数据应用的 Python 框架
import streamlit as st

# 从 openai 库导入 OpenAI 客户端类，用于调用 AI 接口
from openai import OpenAI

# 导入 os 模块，用于访问环境变量
import os

# 导入 load_dotenv 函数，用于从 .env 文件加载环境变量
# （在本地开发时使用，部署到 Streamlit Cloud 后不需要）
from dotenv import load_dotenv

# ========== 初始化 OpenAI 客户端 ==========

# 创建 OpenAI 客户端实例，配置 DeepSeek API 的访问凭证
# api_key: 从环境变量中读取 API 密钥（优先使用 OPENAI_API_KEY，回退到 API_KEY）
# base_url: DeepSeek API 的接口地址
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY") or os.getenv("API_KEY"),
    base_url="https://api.deepseek.com"
)

# ========== 设置页面标题和副标题 ==========

# 设置 Streamlit 页面的标题，显示在浏览器标签页和页面顶部
st.title("🤖 我的第一个AI助手")

# 设置页面的副标题，显示在标题下方，用于说明基于的模型
st.caption("基于deepseek-v4-flash大模型")

# ========== 初始化对话历史 ==========

# 检查 session_state 中是否存在 messages 键
# session_state 是 Streamlit 提供的会话状态管理，用于在用户交互过程中保存数据
# 如果不存在（首次访问），则初始化为空列表
if "messages" not in st.session_state:
    st.session_state.messages = []

# ========== 显示历史消息 ==========

# 遍历对话历史记录，逐条显示之前的消息
# 每条消息包含 role（角色：user/assistant）和 content（内容）
for msg in st.session_state.messages:
    # 使用 st.chat_message 在界面上创建一个消息容器
    # 参数为消息发送者的角色：user（用户）或 assistant（AI助手）
    with st.chat_message(msg["role"]):
        # 使用 st.write 在容器中显示消息内容
        st.write(msg["content"])

# ========== 处理用户输入 ==========

# 使用 st.chat_input 创建一个聊天输入框
# := 是海象运算符，用于在 if 条件语句中同时赋值和判断
# 如果用户输入了内容，prompt 变量会被赋值；如果用户未输入，条件为 False
if prompt := st.chat_input("输入你的问题..."):

    # ========== 显示用户消息 ==========

    # 将用户的消息添加到会话状态中，保存对话历史
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 在界面上创建用户消息的容器
    with st.chat_message("user"):
        # 显示用户输入的内容
        st.write(prompt)

    # ========== 获取 AI 回复 ==========

    # 创建一个 AI 助手的响应容器
    with st.chat_message("assistant"):

        # 调用 DeepSeek API 获取 AI 回复
        # model: 指定的模型名称，这里使用 deepseek-v4-flash（轻量快速版本）
        # messages: 对话消息列表，包含系统提示和历史对话
        # stream=True: 开启流式输出模式，AI 会逐段返回响应内容
        response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=[
                # system 消息：定义 AI 助手的角色和回答风格
                {"role": "system", "content": "你是一个专业的AI助手，回答简洁准确"},
                # 使用解包运算符 * 将历史消息列表展开并添加到消息列表中
                *st.session_state.messages
            ],
            stream=True
        )

        # 使用 st.write_stream 实现流式显示 AI 的响应内容
        # 遍历 response 中的每个 chunk（数据块），提取其中的文本内容
        # chunk.choices[0].delta.content 包含 AI 回复的增量内容
        # 如果内容存在则返回，否则返回空字符串
        full_response = st.write_stream(
            chunk.choices[0].delta.content or ""
            for chunk in response
            if chunk.choices[0].delta.content
        )

    # 将 AI 的完整回复添加到对话历史中，以便在页面刷新后仍能显示
    st.session_state.messages.append({"role": "assistant", "content": full_response})

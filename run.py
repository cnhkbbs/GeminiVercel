# import requests
# import json
#
# url = "https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=AIzaSyBBWi-RvNvNqX3w3K5DnUfFR3ZGmMu69M0"
# headers = {"Content-Type": "application/json"}
#
# data = {
#     "prompt": {
#         "text": "What's the meaning of life"
#     }
# }
#
# # 将数据转换为JSON格式
# json_data = json.dumps(data)
#
# # 发送POST请求
# response = requests.post(url, headers=headers, data=json_data)
#
# # 检查响应
# if response.status_code == 200:
#     # 打印生成的文本
#     print(response.json())
# else:
#     print(f"请求失败，状态码: {response.status_code}")
#     print(response.text)

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# api key
genai.configure(api_key='AIzaSyBBWi-RvNvNqX3w3K5DnUfFR3ZGmMu69M0')

# 列出模型
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")

print(response.text)
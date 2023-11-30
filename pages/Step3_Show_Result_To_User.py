

# 有一个prompt做中间数值处理,SystemMessage, HumanMessage
# 然后把结果数值直接呈现出来，是直接呈现效果，而不一定再是对话框格式

#前面可以加上图像的说明


#这里需要有一个内部处理的方式，

#所以这里其实就是模拟，来进行对话的展示

import streamlit as st

st.title('Your Asset Report')
st.header('🤠 Welcome to FinGPT-Columbia')

import sys
sys.path.append('..')

import b_forStep3_text_put_json_to_langchain

Asset_Result = b_forStep3_text_put_json_to_langchain.Asset_Result

st.expander("Full Text").markdown(Asset_Result)

import streamlit as st


# 图片文件路径
img1_path = './picture/TestVision1.jpg'
img2_path = './picture/TestVision2.jpg'

# 显示第一张图片
st.image(img1_path)

# 空行
st.write('')

# 显示第二张图片
st.image(img2_path)

# 文本
txt = """
Hi Text Explain for Graph
"""
st.write(txt)

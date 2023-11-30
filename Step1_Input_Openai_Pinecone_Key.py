
import streamlit as st
import pages.Step2_Chat_With_User_Info as next_page

#1. 用户【一进入】我们的网址，就会看到这个输入两种Key的界面
#1.1 这里应该与部署的问题有关系(尚未部署测试）



#1.2 基本页面和数据传输的测试
print("Initializing session state")
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ""

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ""
print("Session state initialized")

#st.set_page_config(page_title="Step 1: Basic Settings", layout="wide")

st.title("Step 1: Basic Settings (Pinecone & OpenAI)")

openai_api_key = st.text_input("OpenAI API Key", value=st.session_state["OPENAI_API_KEY"], max_chars=None, key=None,
                               type='password')

pinecone_api_key = st.text_input("Pinecone API Key", value=st.session_state["PINECONE_API_KEY"], max_chars=None,
                                 key=None, type='default')
environment = st.text_input("Environment", value=st.session_state["PINECONE_ENVIRONMENT"], max_chars=None, key=None,
                            type='default')

# 2. save的话【保留一次】就可以，然后两种就都可以保存进入系统内部

saved = st.button("Save")

if saved:
    st.session_state["PINECONE_API_KEY"] = pinecone_api_key
    st.session_state["PINECONE_ENVIRONMENT"] = environment
    st.session_state["OPENAI_API_KEY"] = openai_api_key

    # Inject JavaScript for notification
    #st.success("Settings saved successfully!")
# 3. 点击save完成之后，【最好有个提示，表明保存成功】，然后自动跳转到下一个对话的界面
    with st.form(key='success_form'):
        st.success("Settings saved successfully!")
        success_sent = st.form_submit_button(label='Go to next page?')
        if success_sent:
            st.write(f"Going to next page")
            # Code to go to next page
            st.experimental_redirect("/pages/Step2_Chat_With_User_Info.py")
            next_page.run()





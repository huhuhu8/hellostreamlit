# import streamlit as st

# # 打印所有的 secrets 内容
# st.write(st.secrets)

# # 读取和显示 'message' 键
# #下面一行代码必须要有
# message = st.secrets.get('message', 'Key "message" not found in secrets')
# st.write("Message:", message)
import streamlit as st
def display():
    st.title('st.secrets')

    #(st.secrets['message'])真存储在secrets.toml里面
    st.write(st.secrets['message'])
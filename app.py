import streamlit as st
import homepage,streamlit_app3, streamlit_app5, streamlit_app8  # 导入其他页面的模块

# 设置侧边栏的单选按钮来选择页面
option = st.sidebar.radio(
    "Choose a page:",
    (
        "Homepage",
        "App 3",
        "App 5",
        "App 8",
        # 继续添加其他页面
    )
)

# 基于选择执行不同页面的代码
if option == "Homepage":
    homepage.display()  # 需要在homepage.py中定义display函数
elif option == "App 3":
    streamlit_app3.display()  # 需要在streamlit_app3.py中定义display函数
elif option == "App 5":
    streamlit_app5.display()  # 需要在streamlit_app5.py中定义display函数
elif option == "App 8":
    streamlit_app8.display()  # 需要在streamlit_app8.py中定义display函数
# 继续添加其他页面的条件分支

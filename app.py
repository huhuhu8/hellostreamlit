import streamlit as st
import homepage, streamlit_app3, streamlit_app5, streamlit_app8, \
    streamlit_app9, streamlit_app10, streamlit_app11, streamlit_app12, \
    streamlit_app13, streamlit_app15, streamlit_app16, \
    streamlit_app17, streamlit_app18, streamlit_app19, \
    streamlit_app21, streamlit_app22, streamlit_app23, streamlit_app24, \
    streamlit_app25, streamlit_app26, streamlit_app27, streamlit_app28, \
    streamlit_app29, streamlit_app30
 # 导入其他页面的模块

# 设置侧边栏的单选按钮来选择页面
option = st.sidebar.radio(
    "Choose a page:",
    (
        "Homepage",
        "App 3",
        "App 5",
        "App 8",
        "App 9",
        "App 10",
        "App 11",
        "App 12",
        "App 13",
        # "App 14",
        "App 15",
        "App 16",
        "App 17",
        "App 18",
        "App 19",
        "App 21",
        "App 22",
        "App 23",
        "App 24",
        "App 25",
        "App 26",
        "App 27",
        "App 28",
        "App 29",
        "App 30"
    )
)

# 基于选择执行不同页面的代码
if option == "Homepage":
    homepage.display()
elif option == "App 3":
    streamlit_app3.display()
elif option == "App 5":
    streamlit_app5.display()
elif option == "App 8":
    streamlit_app8.display()
elif option == "App 9":
    streamlit_app9.display()
elif option == "App 10":
    streamlit_app10.display()
elif option == "App 11":
    streamlit_app11.display()
elif option == "App 12":
    streamlit_app12.display()
elif option == "App 13":
    streamlit_app13.display()
#子页面崩溃导致全部崩溃
# elif option == "App 14":
#     streamlit_app14.display()
elif option == "App 15":
    streamlit_app15.display()
elif option == "App 16":
    streamlit_app16.display()
elif option == "App 17":
    streamlit_app17.display()
elif option == "App 18":
    streamlit_app18.display()
elif option == "App 19":
    streamlit_app19.display()
elif option == "App 21":
    streamlit_app21.display()
elif option == "App 22":
    streamlit_app22.display()
elif option == "App 23":
    streamlit_app23.display()
elif option == "App 24":
    streamlit_app24.display()
elif option == "App 25":
    streamlit_app25.display()
elif option == "App 26":
    streamlit_app26.display()
elif option == "App 27":
    streamlit_app27.display()
elif option == "App 28":
    streamlit_app28.display()
elif option == "App 29":
    streamlit_app29.display()
elif option == "App 30":
    streamlit_app30.display()

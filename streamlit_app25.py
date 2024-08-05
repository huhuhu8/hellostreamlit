import streamlit as st
# #工作原理
# 每次用户在输入框中输入或更改数值时，Streamlit会重新运行脚本。
# 使用st.session_state来保存和共享变量，以便在脚本的多次运行之间保持状态。
# st.number_input的on_change回调机制在用户输入改变时调用指定的转换函数，实现自动单位转换。
def display():
    st.title('st.session_state')

    def lbs_to_kg():
        st.session_state.kg = st.session_state.lbs/2.2046
    def kg_to_lbs():
        st.session_state.lbs = st.session_state.kg*2.2046

    st.header('Input')
    col1, spacer, col2 = st.columns([2,1,2])
    with col1:
        pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
    with col2:
        kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

    st.header('Output')
    st.write("st.session_state object:", st.session_state)
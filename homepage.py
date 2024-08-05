import streamlit as st

def display():
    st.title("🌟 Welcome to SEIKU_streamlit 🌟")

    # 在特定动作后显示气球
    if st.button('Celebrate!'):
        st.balloons()

    st.markdown("""
    ### Welcome everyone to my project "SEIKU_streamlit"! 
    This project aims to showcase a variety of Streamlit applications demonstrating different functionalities and use-cases.
    """)

    st.image("pictures/5bd61cc55dcb871f14f8ebd610bd284a.jpg", use_column_width=True)
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ## Explore the Apps
        Use the sidebar to navigate through different Streamlit apps in this project. Each app focuses on specific features or datasets.
        """)

    with col2:
        st.markdown("""
        ## About This Project
        Created to explore and demonstrate the capabilities of Streamlit, an awesome tool for building interactive and beautiful data-driven applications.
        """)

    st.markdown("""
    ### Enjoy exploring!
    If you find the applications interesting, don't hesitate to reach out or contribute to the project.
    """)

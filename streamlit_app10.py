import streamlit as st
def display():
     st.header('st.selectbox')

     option = st.selectbox(
          'What is your favorite color?',
          ('Blue', 'Red', 'Green'))

     st.write('Your favorite color is ', option)
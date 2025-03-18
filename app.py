import streamlit as st

st.title("Welcome Bug Hunters Group1!!!")

domain = st.text_input("Enter the domain name")

if (st.button("Submit")):
  result = domain.title()
  st.success(result)

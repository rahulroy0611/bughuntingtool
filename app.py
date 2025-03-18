import streamlit as st
import re

st.title("Welcome Bug Hunters Group1!!!")


def is_valid_domain(domain):
  pattern = r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
  if re.match(pattern, domain):
    return True
  else:
    return False


def subdomain(domain):
  st.success(domain)


domain = st.text_input("Enter the domain name")

if (st.button("Check")):
  if is_valid_domain(domain):
    # st.success("The domain name is valid.")
    subdomain(domain)
  else:
    st.error("The domain name is invalid.")

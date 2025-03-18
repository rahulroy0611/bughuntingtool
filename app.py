import streamlit as st
import re, requests

st.title("Welcome Bug Hunters Group!!!")
bot_token = "7970524018:AAHYtReX0EtEU1Wjg7rWU8s5Y5z6BkJ9h18"
channel_id = "-1002580630440"
url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage'


def send_message(message):
  params = {
      'chat_id':
      channel_id,  # For username use '@channel_name', for ID use channel ID
      'text': message
  }
  response = requests.get(url, params=params)
  print(response.json())
  if response.status_code == 200:
    st.success("Message sent successfully!")
  else:
    st.error("Failed to send message.")


def is_valid_domain(domain):
  pattern = r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
  if re.match(pattern, domain):
    return True
  else:
    return False


def subdomain(domain):
  send_message(f"Subdomain {domain} submitted for testing")


domain = st.text_input("Enter the domain name")
action = st.multiselect("Action: ",
                        ["Subdomain Enumeration", "Subdomain Takeover"])

if (st.button("Check")):
  if is_valid_domain(domain):
    subdomain(domain)
  else:
    st.error("The domain name is invalid.")

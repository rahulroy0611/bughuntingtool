
import streamlit as st
import re, requests
import os

if __name__ == "__main__":
    st.set_page_config(page_title="Bug Hunters Group")

st.title("Welcome Bug Hunters Group!!!")
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
channel_id = "2580630440"

def send_message(message):
    if not bot_token:
        st.error("Telegram bot token not found. Please set it in Secrets.")
        return
        
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': channel_id,
        'text': message
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        st.success("Message sent successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to send message: {str(e)}")

def is_valid_domain(domain):
    pattern = r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    if re.match(pattern, domain):
        return True
    else:
        return False

def subdomain(domain):
    message = f"New domain submitted for checking: {domain}"
    send_message(message)

domain = st.text_input("Enter the domain name")
action = st.multiselect("Action: ",
                       ["Subdomain Enumeration", "Subdomain Takeover"])

if (st.button("Check")):
    if is_valid_domain(domain):
        subdomain(domain)
    else:
        st.error("The domain name is invalid.")

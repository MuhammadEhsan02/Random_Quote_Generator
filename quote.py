import streamlit as st
import requests

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return data["content"]
    else:
        return "Failed to fetch a random quote."

def main():
    st.title("Random Quote Generator")
    st.subheader("Click the button to get a random quote")
    
    if st.button("Generate Quote"):
        quote = get_random_quote()
        st.write(quote)

if __name__ == '__main__':
    main()

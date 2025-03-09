import streamlit as st
import random
import string
import pyperclip

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = string.ascii_letters
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits   # Adds Numbers (0-9) if selected
    if use_special:
        characters += string.punctuation  # Adds Special Characters if selected

    if not characters:
        return "Please select at least one character type"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

st.title("Password Generator")

length = st.slider("Select the length of the password", min_value=6, max_value=33, value=8)
use_uppercase = st.checkbox("Include Uppercase Letters")
use_lowercase = st.checkbox("Include Lowercase Letters")
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    st.write(f"Generated Password: {password}")

if st.button("Copy to Clipboard"):
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    pyperclip.copy(password)
    st.success("Password copied to clipboard")

st.write("Made with ❤️ by [M Yusuf khan](https://github.com/Myusufkhann)")

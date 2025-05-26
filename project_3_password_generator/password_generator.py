import streamlit as st
import random
import string 

#  creating logic

def Password_generator (length, use_num, use_special):
    character = string.ascii_letters

    if use_num:
       character += string.digits

    if use_special:
       character += string.punctuation

    return "".join(random.choice(character) for _ in range(length))

# creating UI

st.title("PASSWORD GENERATOR")
st.write("Can generate a random password.")


length = st.slider("Select the Password's Length" , min_value=1 , max_value=20, value=10)
use_num = st.checkbox("Select Digits")
use_special = st.checkbox("Select Special Characters")

password =" "
if st.button("Generate Password"):
    password = Password_generator(length, use_num, use_special)

st.write(f"Password Generated: '{password}'")    

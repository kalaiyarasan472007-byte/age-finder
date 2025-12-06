import streamlit as st
import datetime

st.title("How Old are you?")

min_value = datetime.date(1900, 1, 1)
dob = st.date_input("Enter your Date of birth", min_value=min_value)

if dob:
    # calculate the current age
    age = (datetime.datetime.now().date() - dob).days // 365
    st.write(f"You are {age} years old.")
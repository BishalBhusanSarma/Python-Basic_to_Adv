import streamlit as st
import main
from fastapi import HTTPException
from jose import jwt



st.title("Register/Login")
uname = st.text_input("Enter your username")
pw = st.text_input("Entrer your password")

user = main.User(
    username=uname,
    password=pw
)

col1, col2 = st.columns(2)

with col1:
    try:
        if st.button("Register"):
            result =  main.register(user)
            st.success(result["message"])
    except HTTPException as e:
        st.error(e.detail)
with col2:
    try:
        if st.button("Login"):
            result =  main.login(user)
            if result:

                st.success(result["message"])
                tk = result['token']
                st.session_state.token = tk
                st.session_state.logged_in = True

                st.code(tk)
                st.write(main.decode_token(tk))
                
                

            else:
                st.text("Wrong password")

    except HTTPException as e:
        st.error(e.detail)


if st.session_state.logged_in:

    st.title("Dashboard")

    payload = main.decode_token(
    st.session_state.token)

    st.write(payload)

else:

    st.title("Login")
import streamlit as st 

def app():
    st.title("welcome to the App")
    
    choice = st.selectbox('login/Signup',['login','Sign Up'])
    
    if choice == 'login':
        email = st.text_input("Email address")
        password = st.text_input("Password",type="password")
        
        st.button('login')
        
    else:
        email = st.text_input("Email address")
        password = st.text_input("Password",type="password")
        username = st.text_input("enter your unique username")
        
        st.button("create my account")

        
        
    
    
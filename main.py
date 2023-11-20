import streamlit as st 
from streamlit_option_menu import option_menu
import home, about, account, trending,your_posts
st.set_page_config(
    page_title=("multi page")
)

class MultiApp:
    def __init__(self):
        self.apps=[]
    def add_app(self,title,func):
        self.apps.append({
            "title":title,
            "function":func
        })
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="pondering",
                options=['Account','Home','Trending','Your Posts','About'],
                default_index=1)
        if app == 'Account':
            account.app()
        if app == 'home':
            home.app()
        if app == 'Trending':
            trending.app()
        if app == 'Your Posts':
            your_posts.app()
        if app == 'About':
            about.app()
    run()

import streamlit as st
from streamlit_option_menu import option_menu


import home, test, about, chat

st.set_page_config(
    page_title="ThinkingBridge",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title="ThinkingBridge ",
                options=["홈", "계정", "채팅", "개발자"],
                icons=[
                    "house-fill",
                    "person-circle",
                    "chat-fill",
                    "info-circle-fill",
                ],
                menu_icon="chat-text-fill",
                default_index=1,
                styles={
                    "container": {
                        "padding": "5!important",
                        "background-color": "black",
                    },
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {
                        "color": "white",
                        "font-size": "20px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "blue",
                    },
                    "nav-link-selected": {"background-color": "#02ab21"},
                },
            )

        if app == "홈":
            home.app()
        if app == "계정":
            test.app()
        if app == "채팅":
            chat.app()
        if app == "개발자":
            about.app()

    run()

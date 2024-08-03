import streamlit as st
import json

@st.cache_data
def load_corpus():
    # Setup corpus etc.
    with open('Files/eng_to_spa.json') as json_file:
        corpus = json.load(json_file)
    return corpus


def reset_states():
    st.session_state.page = "start"
    st.session_state.settings = None
    st.session_state.words_eng = None
    st.session_state.ans_user = None
    st.session_state.curr_word = None


if 'corpus' not in st.session_state:
    corpus = load_corpus()
    st.session_state['corpus'] = corpus

if "page" not in st.session_state:
    st.session_state.page = "start"

if "settings" not in st.session_state:
    st.session_state.settings = None

if "words_eng" not in st.session_state:
    st.session_state.words_eng = None

if "ans_user" not in st.session_state:
    st.session_state.ans_user = None

if "curr_word" not in st.session_state:
    st.session_state.curr_word = None

st.title("Welcome")
st.button("Reset states", on_click=reset_states)

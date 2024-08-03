import streamlit as st
import random as r


def get_random_word():
    return r.sample(st.session_state.words_eng, 1)[0]


def start(freq_range, n_words):
    settings = {
        "word_range": freq_range,
        "n_words": n_words,
        "score": [],
        "failed": []
    }
    # Get words for current game
    words_eng = list(st.session_state.corpus.keys())  # All English words in corpus
    words_eng = r.sample(words_eng[freq_range[0]: freq_range[1]], n_words)

    # Set session states
    st.session_state.words_eng = words_eng
    st.session_state.curr_word = get_random_word()
    st.session_state.settings = settings
    st.session_state.page = "play"


def restart():
    for key in ["words_eng", "ans_user", "curr_word", "settings"]:
        st.session_state[key] = None
    st.session_state.page = "start"


# Function to save user input and then clear upon pressing enter
def submit():
    st.session_state.ans_user = st.session_state.widget  # Save user input to session state
    st.session_state.widget = ""

    ans_user = st.session_state.ans_user
    ans_spa = st.session_state.corpus[st.session_state.curr_word]

    # Check if answer is correct and present correct translation
    if ans_user.lower() == ans_spa.lower():
        # Update word list
        st.session_state.settings["score"].append(1)
        words_eng = st.session_state.words_eng
        words_eng.pop(words_eng.index(st.session_state.curr_word))
        st.session_state.words_eng = words_eng
        if len(words_eng) == 0:
            st.session_state.page = "finished"
            return

        # New word
        st.session_state.curr_word = get_random_word()
        curr_word.header(st.session_state.curr_word)
        correction.success("Correct!")
        return
    else:
        # New word
        st.session_state.settings["score"].append(0)
        st.session_state.settings["failed"].append(ans_spa)
        st.session_state.curr_word = get_random_word()
        curr_word.header(st.session_state.curr_word)
        correction.error(f"Incorrect. The correct answer is: {ans_spa}")
        return


if st.session_state.page == "start":

    # Layout
    cont_start = st.container()
    cont_start.subheader("Select frequency range")
    freq_range = cont_start.slider("", min_value=0, max_value=5000, value=(0, 1000), step=10)
    cont_start.write("\n")  # Create some space
    cont_start.subheader("Select number of words to train on")
    n_words = cont_start.number_input("Select number of words", value=10, min_value=1, step=1)
    cont_start.write("\n")

    button_start = cont_start.button("Start", on_click=start, args=[freq_range, n_words], use_container_width=True)

if st.session_state.page == "play":

    # Layout
    cont_main = st.container()
    curr_word = cont_main.header(st.session_state.curr_word)
    cont_main.text_input("Answer", value="", key="widget", on_change=submit, label_visibility="hidden", placeholder="Type your answer")
    correction = st.container()
    cont_lookup = st.expander("Lookup")

if st.session_state.page == "finished":
    cont_fin = st.container()

    # Final score
    score_list = st.session_state.settings["score"]
    final_score = int((score_list.count(1) / len(score_list)) * 100)
    cont_fin.title(f"Score: {final_score} %")

    # Balloons
    if final_score > 50:
        for _ in range(7):
            st.balloons()

    # Incorrect answers
    cont_fin.subheader("Words answered incorrectly:")
    for word in set(st.session_state.settings["failed"]):
        cont_fin.write(f"- {word.capitalize()}")

    # Restart button
    button_restart = cont_fin.button("Finish & Restart", on_click=restart)

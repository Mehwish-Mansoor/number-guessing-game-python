import streamlit as st 
import random 
#initalize session statr for storing the rendom number
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1,15)
    
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
    st.set_page_config(page_title="Guees the number", page_icon="🎲", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color:#ffe5e5e5;
    }
    .stApp {
        background-color: #ffe4e4e4;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stTextInput input, .stNumberInput input {
        background-color:rgba(248, 199, 199);
        border-radius: 5px;
        padding: 5px;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #ff9a9e, #fade00);
        color: black;
        font-weight; bold;
        padding: 10px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        transition: background 0.3s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #ff9a9e, #fade00);
        color: black;
    }
    </style>
    """,unsafe_allow_html=True
)

st.markdown("<h1 style='text-align:center; color: #333;'>🎲Guess the Number🎲</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align:center; color:#999;'>I'm thinking of a number between 1 and 15. Can you guess it?</h4>", unsafe_allow_html=True)

#get user's guess

user_guess = st.number_input("Enter your guess:", min_value=1, max_value=15, step=1)

#check button

if st.button("check guess num"):
    st.session_state.attempts +=1
    if user_guess == st.session_state.random_number:
        st.success(f"congratulation! ✨you guessed the correct number in{st.session_state.attempts} attempts.")
        st.session_state.random_number = random.randint(1 , 15)
        st.session_state.attempts = 0
    else:
        st.error("incorrect guess. please try again.")
        
        if st.button("Reset Game"):
            st.session_state.random_number = random.randint(1, 15)
            st.session_attempts = 0
            st.rerurn()
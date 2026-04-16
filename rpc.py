#Rock-paper-scissor game
import streamlit as st
import random

st.markdown("<h1 style='text-align: center; color: red;'>🔥 Rock-paper-scissor 🎮 🔥</h1>", unsafe_allow_html=True)
choices = ['Rock 🪨','Paper 📄','Scissors ✂️']
user_choice = st.radio("Pick one:", choices)
computer_choice = random.choice(choices)

# Strip emojis to get plain names
def normalize(choice):
    if "Rock" in choice: return "Rock"
    if "Paper" in choice: return "Paper"
    if "Scissors" in choice: return "Scissors"

if st.button("Play"):
    u = normalize(user_choice)
    c = normalize(computer_choice)

    st.write(f"You chose: {user_choice}")
    st.write(f"Computer chose: {computer_choice}")

    if u == c:
        st.success("It's a tie!")
    elif (u == "Rock" and c == "Scissors") or \
         (u == "Paper" and c == "Rock") or \
         (u == "Scissors" and c == "Paper"):
        st.success("You win!")
    else:
        st.error("You lose!")

#Rock-paper-scissor game
import streamlit as st
import random

st.markdown("<h1 style='text-align: center; color: red;'>🔥 Rock-paper-scissor 🎮 🔥</h1>", unsafe_allow_html=True)
choices = ['Rock 🪨','Paper 📄','Scissors ✂️']
user_choice=st.radio("Choose your weapon",choices)
computer_choice=random.choice(choices)

if st.button("Play"):
    st.write(f"You chose: {user_choice}")
    st.write(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        st.success("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        st.success("You win!")
    else:
        st.error("You lose!")

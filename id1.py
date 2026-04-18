import streamlit as st

st.title("ID generator")
Template = 'UL04X1X'

name = st.text_input("Enter your name :").strip()

# Only run validation if user typed something
if st.button("Generate ID"):
  if not name:  
    st.error("Name can't be empty.")
  
  else:
    parts = name.split()
    if len(parts) == 1:
        for k in parts:
            if not k.isalpha():
              st.error("Only alphabetic characters with atleast first & last name are allowed in name.")
              break 
            else:
              st.error("Please enter at least first & last name.")

    else:
        valid = True
        for i in parts:
            for j in i:
                if not j.isalpha():
                    st.error("Only alphabetic characters are allowed in name.")
                    valid = False
                    break
            if valid is False:
               break        
        if valid == True:     
              first = parts[0][0].upper()
              last = parts[1][0].upper()
              user_id = Template[:4] + first + Template[5] + last
              st.success(f'USER ID IS: {user_id}')
    

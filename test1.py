#ID pgm
import streamlit as st
ID='UL04S1X'

st.title=('User ID generator')
name=st.text_input('enter your name:')
sub=name.split()
length=len(sub)
if name.strip()=='':
   pass
elif length == 2:
    st.success(f'user id is : {ID}')
elif length >2:
    x = sub[1][0].upper() 
    st.success(f"USER ID IS: UL04S1{x}")    
else:
    st.error(f"Invalid name entered,Enter atleast 2 words.")    


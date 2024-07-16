import streamlit as st
if 'key' not in st.session_state:
    st.session_state.key = "NULL"
    
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.session_state.key = "Hi"
else:
    st.session_state.key = "Bye"
    st.switch_page("Main.py")

st.page_link("pages/1_Layout.py", label="RESULT", icon="🏠")

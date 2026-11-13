import streamlit as st
import random

st.title("🎲 Dice Roller")

if "roll" not in st.session_state:
    st.session_state.roll = 1

if st.button("Roll"):
    st.session_state.roll = random.randint(1, 6)

st.markdown(
    f"""
    <div style="
        width:120px;
        height:120px;
        background:#7B2CBF;
        border-radius:15px;
        display:flex;
        align-items:center;
        justify-content:center;
        color:white;
        font-size:64px;
        margin:auto;
    ">
        {st.session_state.roll}
    </div>
    """,
    unsafe_allow_html=True
)

st.write(f"Result: {st.session_state.roll}")
import streamlit as st
import random
import time

st.set_page_config(page_title="DnD Dice Roller")

st.title("🎲 DnD Dice Roller")

# Theme options
dice_colour = st.color_picker("Dice Colour", "#7B2CBF")

pip_style = st.selectbox(
    "Pip Style",
    [
        "● Classic",
        "◆ Crystal",
        "✦ Arcane",
        "☠ Skull",
        "★ Star"
    ]
)

dice_size = st.slider("Dice Size", 80, 200, 120)

pip_map = {
    "● Classic": "●",
    "◆ Crystal": "◆",
    "✦ Arcane": "✦",
    "☠ Skull": "☠",
    "★ Star": "★"
}

if "roll_result" not in st.session_state:
    st.session_state.roll_result = 1

dice_faces = {
    1: [4],
    2: [0,8],
    3: [0,4,8],
    4: [0,2,6,8],
    5: [0,2,4,6,8],
    6: [0,2,3,5,6,8]
}

placeholder = st.empty()

if st.button("🎲 Roll D6"):
    
    # Animation
    for _ in range(10):
        temp = random.randint(1,6)
        placeholder.markdown(
            render_dice(
                temp,
                dice_colour,
                pip_map[pip_style],
                dice_size
            ),
            unsafe_allow_html=True
        )
        time.sleep(0.08)

    st.session_state.roll_result = random.randint(1,6)

def render_dice(number, colour, pip, size):

    positions = [""] * 9

    for pos in dice_faces[number]:
        positions[pos] = pip

    html = f"""
    <div style="
        width:{size}px;
        height:{size}px;
        background:{colour};
        border-radius:15px;
        display:grid;
        grid-template-columns:repeat(3,1fr);
        grid-template-rows:repeat(3,1fr);
        padding:10px;
        font-size:{size//5}px;
        box-shadow:0 0 25px rgba(0,0,0,0.3);
        color:white;
        margin:auto;
    ">
    """

    for p in positions:
        html += f"""
        <div style="
            display:flex;
            justify-content:center;
            align-items:center;
        ">
            {p}
        </div>
        """

    html += "</div>"

    return html

placeholder.markdown(
    render_dice(
        st.session_state.roll_result,
        dice_colour,
        pip_map[pip_style],
        dice_size
    ),
    unsafe_allow_html=True
)

st.write(f"Result: **{st.session_state.roll_result}**")
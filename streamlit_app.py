import streamlit as st
import random
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="DnD Dice Roller", layout="centered")

st.title("🎲 DnD Dice Roller")


# ------------------------
# Dice Renderer
# ------------------------

DICE_FACES = {
    1: [4],
    2: [0, 8],
    3: [0, 4, 8],
    4: [0, 2, 6, 8],
    5: [0, 2, 4, 6, 8],
    6: [0, 2, 3, 5, 6, 8],
}


def render_dice(number, colour, symbol, size):
    positions = [""] * 9

    for pos in DICE_FACES[number]:
        positions[pos] = symbol

    cells = ""

    for pip in positions:
        cells += f"""
        <div style="
            display:flex;
            justify-content:center;
            align-items:center;
            font-size:{size//4}px;
            color:white;
        ">
            {pip}
        </div>
        """

    return f"""
    <div style="
        width:{size}px;
        height:{size}px;
        background:{colour};
        border-radius:20px;
        display:grid;
        grid-template-columns:repeat(3,1fr);
        grid-template-rows:repeat(3,1fr);
        padding:10px;
        box-sizing:border-box;
        box-shadow:0px 6px 20px rgba(0,0,0,0.4);
        margin:auto;
    ">
        {cells}
    </div>
    """


# ------------------------
# Customisation
# ------------------------

dice_colour = st.color_picker(
    "Dice Colour",
    "#7B2CBF"
)

pip_style = st.selectbox(
    "Pip Style",
    [
        "Classic",
        "Crystal",
        "Arcane",
        "Star",
        "Skull"
    ]
)

size = st.slider(
    "Dice Size",
    80,
    200,
    120
)

symbols = {
    "Classic": "●",
    "Crystal": "◆",
    "Arcane": "✦",
    "Star": "★",
    "Skull": "☠"
}

symbol = symbols[pip_style]

# ------------------------
# Session State
# ------------------------

if "result" not in st.session_state:
    st.session_state.result = 1

dice_placeholder = st.empty()


def show_dice(value):
    components.html(
        render_dice(
            value,
            dice_colour,
            symbol,
            size
        ),
        height=size + 50
    )


# ------------------------
# Roll Button
# ------------------------

if st.button("🎲 Roll D6"):

    for _ in range(15):
        temp_roll = random.randint(1, 6)

        dice_placeholder.components.v1.html(
            render_dice(
                temp_roll,
                dice_colour,
                symbol,
                size
            ),
            height=size + 50
        )

        time.sleep(0.05)

    st.session_state.result = random.randint(1, 6)

# ------------------------
# Final Dice Display
# ------------------------

with dice_placeholder:
    components.html(
        render_dice(
            st.session_state.result,
            dice_colour,
            symbol,
            size
        ),
        height=size + 50
    )

st.markdown(
    f"## Result: **{st.session_state.result}**"
)

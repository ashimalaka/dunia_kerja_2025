import streamlit as st
import pandas as pd

st.write(1234)
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)

import streamlit as st
import streamlit as st

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)
import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
    import streamlit as st

left, middle, right = st.columns(3)
if left.button("Plain button", width="stretch"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", width="stretch"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")
import streamlit as st

with st.container(horizontal=True, horizontal_alignment="distribute"):
    "`A`" if st.button("A", shortcut="A") else "` `"
    "`S`" if st.button("S", shortcut="Ctrl+S") else "` `"
    "`D`" if st.button("D", shortcut="Cmd+Shift+D") else "` `"
    "`F`" if st.button("F", shortcut="Mod+Alt+Shift+F") else "` `"

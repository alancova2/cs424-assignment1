import streamlit as st
import matplotlib.pyplot as plt
from study_common import load_data, dot_panels, good_counts, draw_bars

st.set_page_config(page_title="Good bet for a quiet seat (interactive)", layout="wide")
df = load_data()

st.title("Where is a good bet for a quiet seat?")
st.write("A visit is a good bet if its noise and crowd scores (1 to 5) are both at or under a limit. "
         "Each dot below is one visit to a space (6 visits per space). The bigger the dot, the more people were there.")

noise_limit = st.sidebar.slider("Most noise (1 to 5)", 1, 5, 1)
crowd_limit = st.sidebar.slider("Most crowding (1 to 5)", 1, 5, 1)

st.subheader("Every visit")
st.pyplot(dot_panels(df, noise_limit, crowd_limit))

st.subheader("Good bet visits (out of 6)")
fig, ax = plt.subplots(figsize=(5, 3))
draw_bars(ax, good_counts(df, noise_limit, crowd_limit),
          f"Noise {noise_limit} or less, crowd {crowd_limit} or less", fontsize=9)
fig.tight_layout()
st.pyplot(fig)

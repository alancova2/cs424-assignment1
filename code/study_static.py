import streamlit as st
from study_common import load_data, dot_panels, limits_grid

st.set_page_config(page_title="Good bet for a quiet seat (static)", layout="wide")
df = load_data()

st.title("Where is a good bet for a quiet seat?")
st.write("A visit is a good bet if its noise and crowd scores (1 to 5) are both at or under a limit. "
         "Each dot below is one visit to a space (6 visits per space). The bigger the dot, the more people were there.")

st.subheader("Every visit")
st.pyplot(dot_panels(df))

st.subheader("Good bet visits (out of 6) for different limits")
st.pyplot(limits_grid(df))

import streamlit as st
import pandas as pd
st.markdown("# Racer Page 🎈")
st.sidebar.markdown("# Racer Page 🎈")

st.write(' # Mariokart *Stats Website*')

df_racer = pd.read_csv('data/racer_stats.csv')

#st.write(df_racer)

st.dataframe(df_racer.style.highlight_max(color='red', axis=0, subset=['Speed', 'Acceleration']))

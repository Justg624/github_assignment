import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

dfKart = pd.read_csv('github_assignment/streamlit_template/data/kart_stats.csv')


#st.dataframe(dfKart)

dfKart = dfKart[['Body', 'Acceleration', 'Anti-Gravity Speed','Water Speed', 'Air Speed', 'Ground Speed']]
#Vis1
st.dataframe(dfKart.style
             .highlight_max(color='blue', axis=0, subset=['Anti-Gravity Speed', 'Water Speed', 'Air Speed', 'Ground Speed'])
             .highlight_min(color='green', axis=0, subset=['Anti-Gravity Speed', 'Water Speed', 'Air Speed', 'Ground Speed'])
             )



#Vis2
st.bar_chart(dfKart, x='Body', y=['Anti-Gravity Speed', 'Water Speed', 'Air Speed', 'Ground Speed'])

#Vis3
df_line = dfKart['Body'].drop(columns=['Body', 'Acceleration'])
st.line_chart(df_line, y='Body', )


st.header('Kart speed comparison')
right1, left1 = st.columns(2)
with right1:
    chosen1 = st.selectbox('Pick a kart 1', dfKart['Body'])
    df_single_kart1 = dfKart.loc[dfKart['Body'] == chosen1].drop(columns=['Body', 'Acceleration'])
    df_comp_kart1 = df_single_kart1.unstack().rename_axis(['category', 'row number']).reset_index().drop(columns='row number').rename({0:"Stats"}, axis=1)
    st.write(df_comp_kart1)
    st.header('Acceleration Stats')
    df_bar_kart1= dfKart.loc[dfKart['Body'] == chosen1].drop(columns=['Body', 'Anti-Gravity Speed', 'Water Speed', 'Air Speed', 'Ground Speed'])
    st.dataframe(df_bar_kart1)
    df_single_kart1 = dfKart.loc[dfKart['Body'] == chosen1]
    df_single_kart1 = df_single_kart1.drop(columns=['Body'])
    df_unp_kart1 = df_single_kart1.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)
    st.header('Bar Stats')
    st.bar_chart(df_unp_kart1, x='category', y='strength')


with left1:
    chosen2 = st.selectbox('Pick a kart 2', dfKart['Body'])
    df_single_kart2 = dfKart.loc[dfKart['Body'] == chosen2].drop(columns=['Body', 'Acceleration'])
    df_comp_kart2 = df_single_kart2.unstack().rename_axis(['category', 'row number']).reset_index().drop(columns='row number').rename({0:"Stats"}, axis=1)
    st.write(df_comp_kart2)
    st.header('Acceleration Stats')
    df_bar_kart2= dfKart.loc[dfKart['Body'] == chosen2].drop(columns=['Body', 'Anti-Gravity Speed', 'Water Speed', 'Air Speed', 'Ground Speed'])
    st.dataframe(df_bar_kart2)
    df_single_kart2 = dfKart.loc[dfKart['Body'] == chosen2]
    df_single_kart2 = df_single_kart2.drop(columns=['Body'])
    df_unp_kart2 = df_single_kart2.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)
    st.header('Bar Stats')
    st.bar_chart(df_unp_kart2, x='category', y='strength')














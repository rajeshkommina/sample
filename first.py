import streamlit as st
st.title('my first app')
data=pd.read_csv('salary')
st.dataframe(data)

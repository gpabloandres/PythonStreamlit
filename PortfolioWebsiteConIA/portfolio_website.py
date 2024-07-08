import streamlit as st
 
col1, col2 = st.columns(2)
 
with col1:
    st.subheader("Hi :wave:")
    st.title("I am Murtaza Hassan")
 
with col2:
    st.image("images/murtaza.png")
 
st.title(" ")
 
 
st.title("Murtaza's AI Bot")
st.write("Ask anything about me")
st.text_input("")
st.button("ASK", use_container_width=400)
 
st.title(" ")
 
col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Largest Computer Vision Channel")
    st.write("- 400k+ Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")
 
with col2:
    st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")
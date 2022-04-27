import streamlit as st

st.title("Streamlit tuto !")
st.markdown('''
# Les commandes
Bonjour,
Cette page a été créée pour vous montrer en direct l'effet des commandes de base. 
**Par exemple**, vous verrez ci-dessous le code utilisé pour afficher ces premières lignes.
''')

st.code('''
import streamlit as st

st.title("Streamlit tuto !")
st.markdown(\'\'\'
# Les commandes
Cette page a été créée pour vous montrer en direct l'effet des commandes de base. 
**Par exemple**, vous verrez ci-dessous le code utilisé pour afficher ces premières lignes.
\'\'\')
''')

from PIL import Image
img = Image.open('image_cool.jpeg')

col1, col2 = st.columns([3,1])
with col1:
    st.markdown("## A large column ! I can display so many things")
with col2:
    st.markdown("Wow it's a small one 😢")
    st.image(img, width = 200)

st.code('''
from PIL import Image
img = Image.open('image_cool.jpeg')
col1, col2 = st.columns([3,1])
with col1:
    st.markdown("## A large column ! I can display so many things")
with col2:
    st.markdown("Wow it's a small one 😢")
    st.image(img, width = 200)
''')

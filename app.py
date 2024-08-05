import streamlit as st
from generate import check

st.set_page_config(page_title='Learn with Falcon',page_icon=':computer:')

st.title('Learn From Mistakes!:bulb:')

answer=st.text_area('Enter your text')

submit=st.button('Check your performance')

if submit:
    if answer=='': 
        st.write('No text given:slightly_frowning_face:')
    else:
        result=check(answer)
        st.write(result)
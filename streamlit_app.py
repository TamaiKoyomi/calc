import streamlit as st
import random

li = []

su = st.number_input()
if st.button('計算'):
    for i in range(su):
        li.append(random.randint(1,100))
    print(''.join(li))
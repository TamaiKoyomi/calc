import streamlit as st
import random

st.title('四則演算')

def calc():
    sign=random.randint(1,4)
    if sign==1:
        return '+'
    elif sign==2:
        return '-'
    elif sign==3:
        return '÷'
    elif sign==4:
        return '×'

a=random.randint(1,20)
b=random.randint(1,20)
c=random.randint(1,20)

total=a+b+c

if st.button('計算する'):
    calc
    st.write
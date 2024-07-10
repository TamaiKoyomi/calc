import streamlit as st
import random

def show_name_input():
    st.title('名前と所属チームの入力')

    # 名前と所属チームの入力フォーム
    with st.form(key='input_form'):
        user_name = st.text_input('名前')
        team_name = st.text_input('所属チーム')
        submit_button = st.form_submit_button('ゲーム開始')

        if submit_button:
            if user_name and team_name:
                # セッションステートに保存
                st.session_state.user_name = user_name
                st.session_state.team_name = team_name
                # ページをゲーム画面に切り替える
                st.session_state.page = 'game'
            else:
                st.error('名前と所属チームを入力してください。')

def show_game():
    st.title('ゲーム画面')
    st.write(f"ようこそ、{st.session_state.user_name}さん！")
    st.write(f"あなたの所属チームは{st.session_state.team_name}です。")

    # ここにゲームのロジックを追加
    st.write("ここにゲームの内容が入ります。")

def main():
    # ページの初期設定
    if 'page' not in st.session_state:
        st.session_state.page = 'name_input'

    if st.session_state.page == 'name_input':
        show_name_input()
    elif st.session_state.page == 'game':
        show_game()

if __name__ == "__main__":
    main()

'''st.title('四則演算')

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
    st.write'''
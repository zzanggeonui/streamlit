import streamlit as st
#다른 파일의 함수를 호출하고 싶으면, 함수를 임포트 한다.
from app8_home import run_home_app
from app8_eda import run_eda_app
from app8_ml import run_ml_app

def main() :
    st.title('파일 분리앱')

    # Exploratory Data Analysis(탐색적 데이터분석 판다스로 했던 데이터분석) 'ml'은 머신러닝
    menu = ['Home', 'EDA' , 'ML', 'About' ]

    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == 'Home' :
        run_home_app() #컨트롤 누르면 자동으로 링크이동 가능
    elif choice == 'EDA' :
        run_eda_app()
    elif choice == 'ML' :
        run_ml_app()
    elif choice == 'About' :
        pass




if __name__ == '__main__' :
    main()
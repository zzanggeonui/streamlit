# 웹 대시보드에 이미지파일, 동영상파일 넣는 방법


import streamlit as st

#이미지 처리를 위한 라이브러리
from PIL import Image

def main() :
    img = Image.open('streamlit_data/image_03.jpg')

    st.image(img)

    st.image(img , use_column_width=True)
    
    image_url = 'https://post-phinf.pstatic.net/MjAyMjEyMTBfMTI0/MDAxNjcwNjM3OTc3MjQ5.zzadVR4veJgTv7IJUCLKOJnDqZBfGfGnB16zOfhwVbcg.30iAepH1FKqHPla3Nw4kGP1a3cFa737iq92UqF_N8LYg.JPEG/4.jpg?type=w1200'

    st.image(image_url)

    #동영상
    video_file = open('streamlit_data/secret_of_success.mp4', 'rb')
    st.video( video_file)

if __name__ == '__main__' :
    main()
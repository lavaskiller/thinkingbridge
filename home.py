import streamlit as st


def app():
    st.subheader("ThinkBridge : 친절하지 않은 LLM")
    st.subheader("")
    image = 'logo.png'

    # Streamlit 컬럼을 사용하여 이미지를 중앙에 배치
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(image)
        
    

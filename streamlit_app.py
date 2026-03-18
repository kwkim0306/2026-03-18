import streamlit as st

# 페이지 설정
st.set_page_config(page_title="자기소개", layout="centered")

# 프로필 헤더
st.markdown("---")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/200", width=200)
with col2:
    st.title("👋 안녕하세요!")
    st.subheader("저는 개발자 입니다")
    st.markdown("Streamlit을 사용한 웹 애플리케이션 개발에 관심이 있습니다.")

st.markdown("---")

# 자기소개
st.header("📝 자기소개")
st.markdown("""
저는 웹 개발과 데이터 분석에 열정을 가진 개발자입니다. 
최신 기술을 배우고 실무에 적용하는 것을 즐기며, 
팀과 함께 협력하여 멋진 프로젝트를 만드는 것을 목표로 하고 있습니다.
""")

# 기술 스택
st.header("💻 기술 스택")
col1, col2 = st.columns(2)
with col1:
    st.subheader("언어")
    st.markdown("""
    - 🐍 Python
    - 🌐 JavaScript
    - 🔷 TypeScript
    - 📝 SQL
    """)

with col2:
    st.subheader("프레임워크 & 도구")
    st.markdown("""
    - 📊 Streamlit
    - ⚛️ React
    - 🖥️ Django
    - 📚 Pandas
    """)

# 경험
st.header("🎯 경험")
exp_col1, exp_col2, exp_col3 = st.columns(3)
with exp_col1:
    st.metric("프로젝트", "5+")
with exp_col2:
    st.metric("경력", "3년")
with exp_col3:
    st.metric("기술", "8+")

# 프로젝트
st.header("🚀 주요 프로젝트")
tab1, tab2, tab3 = st.tabs(["프로젝트 1", "프로젝트 2", "프로젝트 3"])

with tab1:
    st.subheader("데이터 분석 대시보드")
    st.markdown("**기술**: Python, Streamlit, Pandas")
    st.write("실시간 데이터를 시각화하는 대시보드를 개발했습니다.")

with tab2:
    st.subheader("웹 애플리케이션")
    st.markdown("**기술**: React, Node.js, MongoDB")
    st.write("사용자 친화적인 웹 애플리케이션을 구축했습니다.")

with tab3:
    st.subheader("머신러닝 프로젝트")
    st.markdown("**기술**: Python, TensorFlow, Jupyter")
    st.write("머신러닝 모델을 학습하고 배포했습니다.")

# 연락처
st.markdown("---")
st.header("📞 연락처")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("📧 **이메일**: dev@example.com")
with col2:
    st.markdown("💼 **링크드인**: linkedin.com/in/profile")
with col3:
    st.markdown("🐙 **깃허브**: github.com/profile")

# 메시지 남기기
st.markdown("---")
st.header("💬 메시지 남기기")
with st.form(key="contact_form"):
    name = st.text_input("이름")
    email = st.text_input("이메일")
    message = st.text_area("메시지", height=100)
    submitted = st.form_submit_button("전송")
    
    if submitted:
        if name and email and message:
            st.success("✅ 메시지가 전송되었습니다. 감사합니다!")
        else:
            st.error("❌ 모든 필드를 입력해주세요.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026. All rights reserved.</p>", unsafe_allow_html=True)

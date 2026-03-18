import streamlit as st

# 페이지 설정
st.set_page_config(page_title="김관우 자기소개", layout="centered")

# 프로필 헤더
st.markdown("---")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/200", width=200)
with col2:
    st.title("👋 안녕하세요!")
    st.subheader("김관우입니다")
    st.markdown("수학과 수학교육학에 관심 있는 학생입니다.")

st.markdown("---")

# 자기소개
st.header("📝 자기소개")
st.markdown("""
저는 수학 기초를 탄탄히 다지고 이를 실생활과 교육에 어떻게 적용할 수 있을지 
깊이 있게 탐구하는 것을 좋아합니다.
수학교육학을 통해 다른 사람들에게 수학의 아름다움을 전달하고 싶은 목표를 가지고 있습니다.
""")

# 주요 관심사
st.header("💡 주요 관심사")
col1, col2 = st.columns(2)
with col1:
    st.subheader("학문 분야")
    st.markdown("""
    - 📐 순수 수학
    - 📊 통계학
    - 🔢 선형대수
    - 📈 미적분학
    """)

with col2:
    st.subheader("교육 관심분야")
    st.markdown("""
    - 👨‍🎓 수학 교수법
    - 💻 디지털 교육
    - 📚 교과과정 개발
    - 🔬 교육 연구
    """)

# 경험 및 통계
st.header("🎯 경험")
exp_col1, exp_col2, exp_col3 = st.columns(3)
with exp_col1:
    st.metric("학습 기간", "3년")
with exp_col2:
    st.metric("주요 과목", "2개")
with exp_col3:
    st.metric("프로젝트", "진행 중")

# 학습 분야
st.header("📚 학습 분야")
tab1, tab2 = st.tabs(["수학", "수학교육학"])

with tab1:
    st.subheader("수학 분야")
    st.markdown("""
    - 정수론과 추상대수
    - 해석학 기초
    - 위상수학 입문
    - 확률론과 통계
    """)

with tab2:
    st.subheader("수학교육학 분야")
    st.markdown("""
    - 수학 개념 형성과정
    - 학습자의 오류 분석
    - 효과적인 교수 전략
    - 평가와 피드백
    """)

# 연락처
st.markdown("---")
st.header("📞 연락처")
col1, col2 = st.columns(2)
with col1:
    st.markdown("📧 **이메일**: kwkim0306@naver.com")
with col2:
    st.markdown("💼 **현재**: 학생")

# 메시지 남기기
st.markdown("---")
st.header("💬 메시지 남기기")
with st.form(key="contact_form"):
    visitor_name = st.text_input("이름")
    visitor_email = st.text_input("이메일")
    message = st.text_area("메시지", height=100)
    submitted = st.form_submit_button("전송")
    
    if submitted:
        if visitor_name and visitor_email and message:
            st.success("✅ 메시지가 전송되었습니다. 감사합니다!")
        else:
            st.error("❌ 모든 필드를 입력해주세요.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026. 김관우. All rights reserved.</p>", unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(page_title="Streamlit 요소 예시", layout="wide")

# 제목 및 소개
st.title("🎈 Streamlit 요소 가이드")
st.markdown("Streamlit의 다양한 요소들을 보여주는 예시 페이지입니다.")

# 1. 텍스트 요소
st.header("1️⃣ 텍스트 요소")
st.subheader("제목, 텍스트, 마크다운")
st.text("일반 텍스트입니다.")
st.markdown("**마크다운** 형식을 지원합니다. [링크](https://streamlit.io)")
st.info("ℹ️ 정보 메시지")
st.success("✅ 성공 메시지")
st.warning("⚠️ 경고 메시지")
st.error("❌ 에러 메시지")

# 2. 입력 요소
st.header("2️⃣ 입력 요소")

col1, col2 = st.columns(2)
with col1:
    st.subheader("텍스트 입력")
    name = st.text_input("이름을 입력하세요:", "기본값")
    st.write(f"입력한 이름: {name}")

with col2:
    st.subheader("슬라이더")
    age = st.slider("나이를 선택하세요:", 0, 100, 25)
    st.write(f"선택한 나이: {age}")

col3, col4 = st.columns(2)
with col3:
    st.subheader("셀렉트박스")
    option = st.selectbox("옵션을 선택하세요:", ["옵션 1", "옵션 2", "옵션 3"])
    st.write(f"선택한 옵션: {option}")

with col4:
    st.subheader("체크박스")
    agree = st.checkbox("동의합니다")
    st.write(f"동의 상태: {agree}")

st.subheader("다중 선택")
options = st.multiselect("여러 항목을 선택하세요:", ["A", "B", "C", "D", "E"])
st.write(f"선택한 항목: {options}")

st.subheader("버튼 및 라디오")
col5, col6 = st.columns(2)
with col5:
    if st.button("클릭 버튼"):
        st.write("버튼을 클릭했습니다! 🎉")

with col6:
    choice = st.radio("선택하세요:", ["선택지 1", "선택지 2", "선택지 3"])
    st.write(f"선택한 항목: {choice}")

# 3. 데이터 표시
st.header("3️⃣ 데이터 표시")

# 샘플 데이터 생성
data = pd.DataFrame({
    "이름": ["Alice", "Bob", "Charlie", "David"],
    "나이": [25, 30, 35, 28],
    "점수": [85, 92, 78, 88]
})

col7, col8 = st.columns(2)
with col7:
    st.subheader("테이블")
    st.table(data)

with col8:
    st.subheader("데이터프레임")
    st.dataframe(data, use_container_width=True)

st.subheader("메트릭")
col9, col10, col11 = st.columns(3)
with col9:
    st.metric("판매액", "1,200,000원", "+10%")
with col10:
    st.metric("방문자", "3,500명", "-5%")
with col11:
    st.metric("평점", "4.8", "+0.2")

# 4. 그래프
st.header("4️⃣ 그래프")

# 선 그래프 데이터
chart_data = pd.DataFrame({
    "월": ["1월", "2월", "3월", "4월", "5월"],
    "매출": [100, 150, 120, 200, 180],
    "비용": [60, 80, 70, 100, 90]
})

col12, col13 = st.columns(2)
with col12:
    st.subheader("선 그래프")
    st.line_chart(chart_data.set_index("월"))

with col13:
    st.subheader("막대 그래프")
    st.bar_chart(chart_data.set_index("월"))

# 산점도
scatter_data = pd.DataFrame({
    "X": np.random.randn(100),
    "Y": np.random.randn(100)
})
st.subheader("산점도")
st.scatter_chart(scatter_data, use_container_width=True)

# 5. 레이아웃
st.header("5️⃣ 레이아웃 및 컨테이너")

with st.expander("확장 가능한 섹션 (클릭하면 펼쳐집니다)"):
    st.write("숨겨진 내용이 여기에 있습니다.")
    st.code("print('Hello, Streamlit!')", language="python")

# Tabs
tab1, tab2, tab3 = st.tabs(["탭 1", "탭 2", "탭 3"])
with tab1:
    st.write("탭 1의 내용입니다.")
    st.image("https://via.placeholder.com/300")

with tab2:
    st.write("탭 2의 내용입니다.")
    st.write("여기에도 다양한 요소를 넣을 수 있습니다.")

with tab3:
    st.write("탭 3의 내용입니다.")

# 6. 폼 (Form)
st.header("6️⃣ 폼 (Form)")
with st.form(key="my_form"):
    st.write("회원가입 폼")
    email = st.text_input("이메일:")
    password = st.text_input("비밀번호:", type="password")
    genre = st.radio("선호 장르:", ["액션", "드라마", "코미디"])
    submitted = st.form_submit_button("제출")
    
    if submitted:
        st.success(f"제출되었습니다! 이메일: {email}, 선호장르: {genre}")

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="나의 소개 페이지",
    page_icon="🙋",
    layout="wide",
)

st.title("🙋 안녕하세요, 저는 김다운입니다.")
st.caption("이 페이지는 제 소개를 담고 있습니다.")

st.markdown("---")

with st.sidebar:
    st.header("프로필 설정")
    st.image("https://via.placeholder.com/150", width=120)
    st.write("이름: 홍길동")
    st.write("직무: 백엔드 / 데이터 / 웹 개발")
    st.write("관심사: Python, Streamlit, 데이터 시각화")

st.subheader("1. 자기소개")

intro_col1, intro_col2 = st.columns([2, 1])

with intro_col1:
    st.markdown(
        """
        저는 과학 교사로 고등학교에서 지구과학을 가르치고 있습니다.  
                
                """
    )

with intro_col2:
    st.info("현재 목표\n- 작동되는 앱 제작\n- 계획한 연수와 출제 완료하기\n- 충전하기")

st.markdown("---")

st.subheader("2. 이번 방학 목표")

skill1, skill2, skill3 = st.columns(3)

with skill1:
    st.success("웹앱 개발")
    st.write("연수 참여, 2학기 수업에 활용, 할 수 있다!")

with skill2:
    st.success("AI활용 서술형 문항 개발")
    st.write("생성형AI, 서술형 문항이란, 교육과정에 대한 고찰")

with skill3:
    st.success("지친 심신 회복")
    st.write("휴식과 충전")

with skill4:
    st.success("2학기 준비")
    st.write("수업 준비", "진학 상담")

st.markdown("---")


st.subheader("3. 관심 분야")

interest = st.multiselect(
    "제가 특히 좋아하는 분야를 선택해 주세요.",
    ["여행", "음악", "운동", "TV 시청", "산책","게임"],
    default=["여행", "음악"],
)

st.write(f"선택한 관심 분야: {', '.join(interest) if interest else '선택된 항목이 없습니다.'}")

st.markdown("---")

st.subheader("4. 간단한 연락 폼")
st.caption("저에게 하고 싶은 이야기가 있다면 아래 폼을 통해 남겨주세요.")


with st.form("contact_form"):
    name = st.text_input("이름", placeholder="아무개")
    message = st.text_area("메시지", height=120, placeholder="간단한 인사나 문의 내용을 남겨주세요.")
    submitted = st.form_submit_button("보내기")

if submitted:
    st.success(f"{name}님, 메시지를 받았습니다. 감사합니다!")
    st.json({"name": name, "message": message})

st.markdown("---")

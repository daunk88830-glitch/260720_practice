import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

st.set_page_config(
    page_title="Streamlit Elements Showcase",
    page_icon="✨",
    layout="wide",
)

st.title("✨ Streamlit 요소 예시 페이지")
st.caption("한 화면에서 다양한 Streamlit 컴포넌트가 어떻게 조합되는지 보여주는 예시입니다.")

st.markdown("---")

with st.sidebar:
    st.header("사이드바 설정")
    st.radio("레이아웃 선택", ["기본", "와이드", "집중형"], horizontal=True)
    st.selectbox("카테고리", ["개발", "데이터", "대시보드", "교육"])
    st.multiselect("관심 주제", ["입력", "시각화", "테이블", "파일 다운로드"])
    st.slider("사이드바 슬라이더", 0, 100, 35)
    st.toggle("실시간 업데이트", value=True)

st.subheader("1. 텍스트와 메시지")
st.markdown("여기에는 **굵은 텍스트**, *기울임 텍스트*, 그리고 [링크](https://docs.streamlit.io/)도 넣을 수 있습니다.")

st.info("정보 메시지입니다. 사용자에게 안내를 줄 때 자주 사용합니다.")
st.warning("경고 메시지입니다. 중요한 내용을 강조할 수 있습니다.")
st.success("성공 메시지입니다. 작업 결과를 보여줄 수 있습니다.")
st.error("오류 메시지입니다. 예외 상황을 표시할 때 쓰면 좋습니다.")

st.markdown("---")

st.subheader("2. 입력 요소")

with st.form("demo_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("이름", placeholder="홍길동")
        email = st.text_input("이메일", placeholder="name@example.com")
        age = st.number_input("나이", min_value=0, max_value=120, value=30)

    with col2:
        category = st.selectbox("분야", ["웹", "데이터", "AI", "운영"])
        due_date = st.date_input("예정일", value=date(2026, 7, 20))
        note = st.text_area("메모", "여기에 자유롭게 입력해 보세요.")

    submitted = st.form_submit_button("제출하기")

if submitted:
    st.success(f"{name}님, '{category}' 분야로 제출이 완료되었습니다.")
    st.json({
        "name": name,
        "email": email,
        "age": age,
        "due_date": str(due_date),
        "note": note,
    })

st.markdown("---")

st.subheader("3. 선택형 요소와 상태 표시")
left_col, right_col = st.columns(2)

with left_col:
    choice = st.radio("좋아하는 요소를 선택하세요", ["버튼", "차트", "테이블", "다운로드"])
    st.write(f"현재 선택: {choice}")

with right_col:
    checked = st.checkbox("추가 옵션을 켜두겠습니다.", value=True)
    if checked:
        st.caption("추가 옵션이 활성화되었습니다.")

    progress = st.progress(40)
    st.caption("Progress bar 예시")

st.markdown("---")

st.subheader("4. 시각화")

sample_df = pd.DataFrame(
    {
        "월": np.arange(1, 7),
        "매출": [120, 180, 160, 210, 250, 300],
        "방문자": [80, 120, 110, 140, 180, 200],
    }
)

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.line_chart(sample_df.set_index("월"))

with chart_col2:
    st.bar_chart(sample_df.set_index("월"))

st.area_chart(sample_df.set_index("월")["매출"])

st.markdown("---")

st.subheader("5. 데이터프레임과 확장 영역")

with st.expander("샘플 데이터 보기"):
    st.dataframe(sample_df, use_container_width=True)

st.download_button(
    label="샘플 CSV 다운로드",
    data=sample_df.to_csv(index=False),
    file_name="sample_data.csv",
    mime="text/csv",
)

st.markdown("---")

st.subheader("6. 메트릭과 컨테이너 조합")
metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.metric("매출", "₩3.2M", "+12.4%")

with metric_col2:
    st.metric("방문자", "1,245", "+8.1%")

with metric_col3:
    st.metric("전환율", "4.8%", "-0.2%")

st.markdown("---")

st.subheader("7. 탭과 스피너")

with st.spinner("데이터를 불러오는 중입니다..."):
    import time
    time.sleep(0.5)

Tab1, Tab2, Tab3 = st.tabs(["요약", "코드", "팁"])

with Tab1:
    st.write("이 페이지는 Streamlit 위젯을 종합적으로 보여주기 위한 예시입니다.")

with Tab2:
    st.code(
        "import streamlit as st\n\nst.title('Hello Streamlit')\nst.button('Click me')",
        language="python",
    )

with Tab3:
    st.markdown("- `st.form`으로 입력을 한 번에 받기\n- `st.columns`로 화면을 나누기\n- `st.tabs`로 구조를 분리하기")

st.markdown("---")

st.subheader("8. 마지막으로")

st.caption("이 예시는 단일 페이지에서 Streamlit의 다양한 요소를 보여주는 데 초점을 맞춘 템플릿입니다.")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("대멸종 시각화 비교 예시")
st.caption("다음 그래프는 같은 데이터를 바탕으로 matplotlib, seaborn, plotly로 각각 표현한 비교 예시입니다.")

sample_df = pd.DataFrame(
    {
        "시기": ["1단계", "2단계", "3단계", "4단계", "5단계"],
        "온도 변화": [2.1, 3.5, 4.8, 6.0, 5.2],
        "생물 다양성": [90, 72, 55, 38, 25],
    }
)

st.subheader("1. 비교 목적")
st.markdown(
    "이 예시는 세 라이브러리의 차이를 느끼기 위해 같은 데이터를 다른 방식으로 그린 것입니다.\n"
    "- matplotlib: 정적인 그래프 제작에 적합합니다.\n"
    "- seaborn: 통계적 스타일과 가독성이 좋습니다.\n"
    "- plotly: 인터랙티브한 확대/이동이 가능합니다."
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("matplotlib")
    st.write("기본적인 선 그래프 예시입니다. 정적 결과물에 적합합니다.")
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(sample_df["시기"], sample_df["온도 변화"], marker="o", color="tomato")
    ax.set_title("대멸종 시기별 온도 변화 (matplotlib)")
    ax.set_xlabel("시기")
    ax.set_ylabel("온도 변화")
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(rotation=15)
    st.pyplot(fig)

with col2:
    st.subheader("seaborn")
    st.write("통계적 디자인으로 보기 좋은 그래프입니다. 문서화 자료에 편합니다.")
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.lineplot(data=sample_df, x="시기", y="온도 변화", marker="o", ax=ax, color="royalblue")
    ax.set_title("대멸종 시기별 온도 변화 (seaborn)")
    ax.set_xlabel("시기")
    ax.set_ylabel("온도 변화")
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(rotation=15)
    st.pyplot(fig)

with col3:
    st.subheader("plotly")
    st.write("마우스로 확대하고 움직일 수 있는 인터랙티브 그래프입니다.")
    fig = px.line(
        sample_df,
        x="시기",
        y="온도 변화",
        title="대멸종 시기별 온도 변화 (plotly)",
        labels={"시기": "시기", "온도 변화": "온도 변화"},
    )
    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("2. 추가 비교 그래프")

left_col, right_col = st.columns(2)

with left_col:
    st.markdown("### matplotlib 막대 그래프")
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.bar(sample_df["시기"], sample_df["생물 다양성"], color="sandybrown")
    ax.set_title("생물 다양성 변화 (matplotlib)")
    ax.set_xlabel("시기")
    ax.set_ylabel("다양성 지수")
    plt.xticks(rotation=15)
    st.pyplot(fig)

with right_col:
    st.markdown("### seaborn 막대 그래프")
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.barplot(data=sample_df, x="시기", y="생물 다양성", palette="Set2", ax=ax)
    ax.set_title("생물 다양성 변화 (seaborn)")
    ax.set_xlabel("시기")
    ax.set_ylabel("다양성 지수")
    plt.xticks(rotation=15)
    st.pyplot(fig)

st.markdown("---")

st.subheader("3. 결론")
st.markdown(
    "- matplotlib는 정적인 그래프를 만들 때 편리합니다.\n"
    "- seaborn은 통계적 스타일을 빠르게 적용하기 좋습니다.\n"
    "- plotly는 웹에서 인터랙티브한 비교에 유리합니다."
)
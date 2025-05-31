import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="시가총액 TOP 10", layout="wide")

st.title("📈 전 세계 시가총액 TOP 10 기업 (2022~2024) 변화")

# 시가총액 단위: 조 달러 (예시 데이터)
data = {
    "기업": ["Apple", "Microsoft", "Saudi Aramco", "Alphabet", "Amazon",
            "Nvidia", "Berkshire Hathaway", "Meta", "TSMC", "Tesla"] * 3,
    "연도": [2022]*10 + [2023]*10 + [2024]*10,
    "시가총액": [
        2.9, 2.4, 2.3, 1.7, 1.5, 0.7, 0.7, 0.9, 0.6, 0.8,      # 2022
        2.8, 2.5, 2.1, 1.8, 1.6, 1.0, 0.8, 1.0, 0.65, 0.7,    # 2023
        3.0, 3.1, 2.0, 1.9, 1.8, 2.3, 0.85, 1.2, 0.7, 0.65    # 2024
    ]
}

df = pd.DataFrame(data)

# 기업 선택 (멀티셀렉트)
selected_companies = st.multiselect(
    "보고 싶은 기업을 선택하세요",
    options=df["기업"].unique(),
    default=df["기업"].unique()
)

filtered_df = df[df["기업"].isin(selected_companies)]

# Plotly 그래프
fig = px.line(
    filtered_df,
    x="연도",
    y="시가총액",
    color="기업",
    markers=True,
    title="전 세계 시가총액 TOP 10 기업의 연도별 변화 (단위: 조 달러)"
)

fig.update_layout(
    xaxis=dict(dtick=1),
    yaxis_title="시가총액 (조 달러)",
    legend_title="기업",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)


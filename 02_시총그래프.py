import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="시가총액 TOP 10", layout="wide")
st.title("📈 전 세계 시가총액 TOP 10 기업 (최근 3년) 변화 추이")

# 시총 Top 10 기업 (2024 기준)과 티커 매핑
companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta": "META",
    "TSMC": "TSM",
    "Tesla": "TSLA"
}

# 사용자 선택
selected = st.multiselect(
    "시가총액 추이를 보고 싶은 기업을 선택하세요",
    options=list(companies.keys()),
    default=list(companies.keys())
)

@st.cache_data
def load_market_caps(tickers):
    df_all = pd.DataFrame()
    for name, ticker in tickers.items():
        data = yf.Ticker(ticker).history(period="3y", interval="1mo")
        if "Close" in data.columns:
            # 시가총액 계산: Close * Shares Outstanding
            info = yf.Ticker(ticker).info
            shares = info.get("sharesOutstanding", None)
            if shares:
                data["Market Cap"] = data["Close"] * shares
                data["기업"] = name
                data["Date"] = data.index
                df_all = pd.concat([df_all, data[["Date", "Market Cap", "기업"]]])
    return df_all

selected_tickers = {name: ticker for name, ticker in companies.items() if name in selected}
data = load_market_caps(selected_tickers)

# 단위: 조 달러
data["시가총액(조 달러)"] = data["Market Cap"] / 1e12

# 그래프 그리기
fig = px.line(
    data,
    x="Date",
    y="시가총액(조 달러)",
    color="기업",
    title="최근 3년 시가총액 변화 추이 (조 달러)",
    markers=True
)

fig.update_layout(
    yaxis_title="시가총액 (조 달러)",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)


import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="시가총액 TOP 10", layout="wide")
st.title("📈 전 세계 시가총액 TOP 10 기업 (최근 3년) 변화 추이")

# 기업 및 티커 목록 (2024 기준, Aramco 제외)
companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta": "META",
    "TSMC": "TSM",
    "Tesla": "TSLA"
    # "Saudi Aramco": "2222.SR",  # 불안정하여 제외
}

# 사용자 선택
selected = st.multiselect(
    "시가총액 추이를 보고 싶은 기업을 선택하세요",
    options=list(companies.keys()),
    default=list(companies.keys())
)

@st.cache_data(ttl=3600)
def load_market_caps(ticker_dict):
    end_date = datetime.today()
    start_date = end_date - timedelta(days=3 * 365)
    all_data = []

    for name, ticker in ticker_dict.items():
        try:
            ticker_obj = yf.Ticker(ticker)
            hist = ticker_obj.history(start=start_date, end=end_date, interval="1mo")

            if hist.empty or "Close" not in hist.columns:
                continue

            mc = ticker_obj.fast_info.get("market_cap", None)
            so = ticker_obj.fast_info.get("shares_outstanding", None)

            # fallback: estimate shares from market cap and price
            if so is None and mc:
                price = hist["Close"][-1]
                so = mc / price if price > 0 else None

            if so is None:
                continue

            hist = hist.reset_index()
            hist["Market Cap"] = hist["Close"] * so
            hist["기업"] = name
            all_data.append(hist[["Date", "Market Cap", "기업"]])
        except Exception as e:
            print(f"{name} 데이터 로딩 실패: {e}")
            continue

    if all_data:
        return pd.concat(all_data, ignore_index=True)
    else:
        return pd.DataFrame(columns=["Date", "Market Cap", "기업"])

selected_tickers = {name: companies[name] for name in selected}
df = load_market_caps(selected_tickers)

# 시가총액 단위 변환
df["시가총액(조 달러)"] = df["Market Cap"] / 1e12

# 그래프 그리기
fig = px.line(
    df,
    x="Date",
    y="시가총액(조 달러)",
    color="기업",
    markers=True,
    title="최근 3년 시가총액 변화 추이 (조 달러 기준)"
)

fig.update_layout(
    xaxis_title="날짜",
    yaxis_title="시가총액 (조 달러)",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

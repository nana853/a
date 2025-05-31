import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="멀티 쇼핑몰 패션 추천", layout="wide")
st.title("👗 멀티 쇼핑몰 패션 추천기")

# 사용자 입력
gender = st.selectbox("성별 선택", ["남성", "여성"])
style = st.selectbox("스타일 선택", ["스트릿", "캐주얼", "덴디", "포멀", "스포티"])
color = st.selectbox("색감 선택", ["블랙", "화이트", "네이비", "파스텔", "비비드", "올리브", "베이지", "버건디"])
season = st.selectbox("계절 선택", ["봄", "여름", "가을", "겨울"])
fit = st.selectbox("핏 선택", ["슬림핏", "레귤러핏", "오버핏"])
category = st.selectbox("의류 종류 선택", ["상의", "하의", "아우터", "신발", "액세서리"])

st.markdown("---")

# === 무신사 API (가상 예시) ===
def fetch_musinsa_products(category, gender, style, color, season, fit):
    # 실제 무신사 API가 없으므로 예시 URL
    url = f"https://fake-musinsa-api.com/products?category={category}&gender={gender}&style={style}&color={color}&season={season}&fit={fit}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json().get("products", [])
        else:
            return []
    except:
        return []

# === 에이블리 크롤링 예시 ===
def fetch_ably_products(keyword):
    url = f"https://www.ably.co.kr/search?q={keyword}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        products = []
        items = soup.select("div.product-item")  # 실제 사이트 구조 확인 필요
        for item in items[:5]:  # 최대 5개만 가져오기
            name = item.select_one("div.product-name").get_text(strip=True)
            price = item.select_one("span.price").get_text(strip=True)
            link = item.select_one("a")["href"]
            img = item.select_one("img")["src"]
            if link.startswith("/"):
                link = "https://www.ably.co.kr" + link
            if img.startswith("//"):
                img = "https:" + img
            products.append({"name": name, "price": price, "link": link, "image": img})
        return products
    except:
        return []

# === 지그재그, 유어너스, 8세컨즈, 유니클로는 생략(구조 복잡하여 각자 크롤링 코드 작성 필요) ===

def show_products(shop_name, products):
    st.subheader(f"{shop_name} 추천 아이템")
    if not products:
        st.write("해당 조건에 맞는 상품이 없습니다.")
        return
    cols = st.columns(5)
    for i, product in enumerate(products):
        with cols[i % 5]:
            st.image(product['image'], use_column_width=True)
            st.markdown(f"**{product['name']}**")
            st.markdown(f"{product['price']}")
            st.markdown(f"[구매하기]({product['link']})")

# 키워드 생성 (단순 연결, 실제 추천 알고리즘 개선 필요)
keyword = f"{gender} {style} {color} {category}"

if st.button("추천 아이템 보기"):
    st.info("상품을 불러오는 중입니다... 잠시만 기다려 주세요!")

    # 1) 무신사 (가상 API 호출)
    musinsa_products = fetch_musinsa_products(category, gender, style, color, season, fit)
    show_products("무신사", musinsa_products)

    # 2) 에이블리 크롤링
    ably_products = fetch_ably_products(keyword)
    show_products("에이블리", ably_products)

    # 3) 지그재그, 유어너스, 8세컨즈, 유니클로 등은 유사 방식으로 크롤링 함수 추가 가능
    st.info("다른 쇼핑몰도 곧 추가할 예정입니다.")


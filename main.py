import streamlit as st

st.title("👗 스타일 & 색감 기반 옷 추천 (조건 완화 포함)")

gender = st.selectbox("성별 선택", ["남성", "여성"])
style = st.selectbox("스타일 선택", ["스트릿", "캐주얼", "덴디", "포멀", "스포티"])
color = st.selectbox("색감 선택", ["블랙", "화이트", "네이비", "파스텔", "비비드", "올리브", "베이지", "버건디"])
season = st.selectbox("계절 선택", ["봄", "여름", "가을", "겨울"])
fit = st.selectbox("핏 선택", ["슬림핏", "레귤러핏", "오버핏"])
category = st.selectbox("의류 종류 선택", ["상의", "하의", "아우터", "신발", "액세서리"])

st.markdown("---")

products = [
    {"name": "베이직 블랙 티셔츠", "gender": "남성", "style": "캐주얼", "color": "블랙", "season": "여름", "fit": "슬림핏", "category": "상의",
     "image": "https://image.musinsa.com/mfile_s01/_musinsa2023/20/1234567890_1.jpg", "link": "https://www.musinsa.com/app/goods/123456"},
    {"name": "올리브 카고 팬츠", "gender": "남성", "style": "스트릿", "color": "올리브", "season": "가을", "fit": "오버핏", "category": "하의",
     "image": "https://image.ably.co.kr/ably_img/01/1234567_1.jpg", "link": "https://www.ably.co.kr/item/1234567"},
    {"name": "버건디 니트 가디건", "gender": "여성", "style": "덴디", "color": "버건디", "season": "겨울", "fit": "레귤러핏", "category": "아우터",
     "image": "https://zigzagimage.com/12345678_1.jpg", "link": "https://zigzag.kr/product/12345678"},
    {"name": "베이지 캐주얼 셔츠", "gender": "남성", "style": "캐주얼", "color": "베이지", "season": "봄", "fit": "레귤러핏", "category": "상의",
     "image": "https://example.com/beige_casual_shirt.jpg", "link": "https://example.com/beige_casual_shirt"},
    {"name": "화이트 슬림핏 셔츠", "gender": "여성", "style": "포멀", "color": "화이트", "season": "봄", "fit": "슬림핏", "category": "상의",
     "image": "https://example.com/white_slim_shirt.jpg", "link": "https://example.com/white_slim_shirt"},
]

# 1차: 모든 조건 완벽 일치
filtered = [p for p in products if
            p["gender"] == gender and
            p["style"] == style and
            p["color"] == color and
            p["season"] == season and
            p["fit"] == fit and
            p["category"] == category]

# 2차: 조건 일부 완화 - 색감 무시하고 찾기
if not filtered:
    filtered = [p for p in products if
                p["gender"] == gender and
                p["style"] == style and
                p["season"] == season and
                p["fit"] == fit and
                p["category"] == category]

# 3차: 스타일과 색감 무시하고 찾기
if not filtered:
    filtered = [p for p in products if
                p["gender"] == gender and
                p["season"] == season and
                p["fit"] == fit and
                p["category"] == category]

# 4차: 최소한 성별과 카테고리만 맞는 상품 보여주기
if not filtered:
    filtered = [p for p in products if
                p["gender"] == gender and
                p["category"] == category]

st.write(f"### 총 {len(filtered)}개 추천 상품")

if filtered:
    cols = st.columns(min(5, len(filtered)))
    for i, product in enumerate(filtered):
        with cols[i % 5]:
            st.image(product["image"], use_column_width=True)
            st.markdown(f"**{product['name']}**")
            st.markdown(f"[구매하러 가기]({product['link']})")
else:
    st.write("죄송합니다. 조건에 맞는 상품이 없습니다.")


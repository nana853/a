import streamlit as st

st.title("👗 스타일 & 색감 기반 옷 추천")

# 사용자 입력
gender = st.selectbox("성별 선택", ["남성", "여성"])
style = st.selectbox("스타일 선택", ["스트릿", "캐주얼", "덴디", "포멀", "스포티"])
color = st.selectbox("색감 선택", ["블랙", "화이트", "네이비", "파스텔", "비비드", "올리브", "베이지", "버건디"])
season = st.selectbox("계절 선택", ["봄", "여름", "가을", "겨울"])
fit = st.selectbox("핏 선택", ["슬림핏", "레귤러핏", "오버핏"])
category = st.selectbox("의류 종류 선택", ["상의", "하의", "아우터", "신발", "액세서리"])

st.markdown("---")

# 미리 정의한 샘플 상품 데이터 (예시)
products = [
    {
        "name": "베이직 블랙 티셔츠",
        "gender": "남성",
        "style": "캐주얼",
        "color": "블랙",
        "season": "여름",
        "fit": "슬림핏",
        "category": "상의",
        "image": "https://image.musinsa.com/mfile_s01/_musinsa2023/20/1234567890_1.jpg",
        "link": "https://www.musinsa.com/app/goods/123456"
    },
    {
        "name": "올리브 카고 팬츠",
        "gender": "남성",
        "style": "스트릿",
        "color": "올리브",
        "season": "가을",
        "fit": "오버핏",
        "category": "하의",
        "image": "https://image.ably.co.kr/ably_img/01/1234567_1.jpg",
        "link": "https://www.ably.co.kr/item/1234567"
    },
    {
        "name": "버건디 니트 가디건",
        "gender": "여성",
        "style": "덴디",
        "color": "버건디",
        "season": "겨울",
        "fit": "레귤러핏",
        "category": "아우터",
        "image": "https://zigzagimage.com/12345678_1.jpg",
        "link": "https://zigzag.kr/product/12345678"
    },
    # 더 많은 샘플 데이터 추가 가능
]

# 필터링
filtered = [p for p in products if
            p["gender"] == gender and
            p["style"] == style and
            p["color"] == color and
            p["season"] == season and
            p["fit"] == fit and
            p["category"] == category]

st.write(f"### {len(filtered)}개 추천 상품")

if filtered:
    cols = st.columns(len(filtered))
    for i, product in enumerate(filtered):
        with cols[i]:
            st.image(product["image"], use_column_width=True)
            st.markdown(f"**{product['name']}**")
            st.markdown(f"[구매하기]({product['link']})")
else:
    st.write("조건에 맞는 상품이 없습니다.")

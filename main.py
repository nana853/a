import streamlit as st

st.title("👗 스타일 & 색감 기반 옷 추천 (조건 완화 포함)")

# 사용자 입력 받기
gender = st.selectbox("성별 선택", ["남성", "여성"])
style = st.selectbox("스타일 선택", ["스트릿", "캐주얼", "덴디", "포멀", "스포티", "빈티지", "미니멀"])
color = st.selectbox("색감 선택", ["블랙", "화이트", "네이비", "파스텔", "비비드", "올리브", "베이지", "버건디", "그레이", "브라운", "카멜", "카키"])
season = st.selectbox("계절 선택", ["봄", "여름", "가을", "겨울"])
fit = st.selectbox("핏 선택", ["슬림핏", "레귤러핏", "오버핏", "루즈핏"])
category = st.selectbox("의류 종류 선택", ["상의", "하의", "아우터", "신발", "액세서리", "원피스", "스커트"])

st.markdown("---")

# 제품 데이터 (남성/여성 구분, 스타일, 색감, 계절, 핏, 카테고리 포함)
products = [
    # 남성 상품 5개 이상
    {"name": "베이직 블랙 티셔츠", "gender": "남성", "style": "캐주얼", "color": "블랙", "season": "여름", "fit": "슬림핏", "category": "상의",
     "desc": "기본 중의 기본, 어디에나 잘 어울리는 블랙 티셔츠.",
     "image": "https://image.musinsa.com/mfile_s01/_musinsa2023/20/1234567890_1.jpg", "link": "https://www.musinsa.com/app/goods/123456"},
    {"name": "네이비 스트릿 후드티", "gender": "남성", "style": "스트릿", "color": "네이비", "season": "가을", "fit": "오버핏", "category": "상의",
     "desc": "편안하면서도 스타일리시한 네이비 후드티.",
     "image": "https://cdn.ably.co.kr/ably_img/01/navy_hoodie_1.jpg", "link": "https://www.ably.co.kr/item/987654"},
    {"name": "카멜 울 코트", "gender": "남성", "style": "덴디", "color": "카멜", "season": "겨울", "fit": "레귤러핏", "category": "아우터",
     "desc": "겨울철 따뜻하고 세련된 카멜 울 코트.",
     "image": "https://zigzag.kr/img/camel_coat_1.jpg", "link": "https://zigzag.kr/product/54321"},
    {"name": "카키 카고 팬츠", "gender": "남성", "style": "스트릿", "color": "카키", "season": "봄", "fit": "루즈핏", "category": "하의",
     "desc": "활동성 좋은 스트릿 감성의 카고 팬츠.",
     "image": "https://8seconds.co.kr/img/kaki_cargo_1.jpg", "link": "https://8seconds.co.kr/product/123123"},
    {"name": "블랙 가죽 스니커즈", "gender": "남성", "style": "미니멀", "color": "블랙", "season": "가을", "fit": "레귤러핏", "category": "신발",
     "desc": "깔끔하고 모던한 블랙 가죽 스니커즈.",
     "image": "https://uniqlo.com/img/black_sneakers_1.jpg", "link": "https://uniqlo.com/kr/black_sneakers"},
    {"name": "그레이 니트 비니", "gender": "남성", "style": "캐주얼", "color": "그레이", "season": "겨울", "fit": "레귤러핏", "category": "액세서리",
     "desc": "포근한 느낌의 그레이 니트 비니.",
     "image": "https://musinsa.com/img/gray_beanie_1.jpg", "link": "https://musinsa.com/app/goods/789101"},

    # 여성 상품 5개 이상
    {"name": "핑크 파스텔 블라우스", "gender": "여성", "style": "캐주얼", "color": "파스텔", "season": "봄", "fit": "슬림핏", "category": "상의",
     "desc": "봄 느낌 물씬 나는 사랑스러운 파스텔 블라우스.",
     "image": "https://ably.co.kr/img/123456_pink_blouse.jpg", "link": "https://ably.co.kr/item/123456"},
    {"name": "올리브 오버핏 자켓", "gender": "여성", "style": "스트릿", "color": "올리브", "season": "가을", "fit": "오버핏", "category": "아우터",
     "desc": "편안하면서 멋스러운 올리브색 오버핏 자켓.",
     "image": "https://musinsa.com/img/olive_jacket.jpg", "link": "https://musinsa.com/app/goods/123456"},
    {"name": "버건디 미니 스커트", "gender": "여성", "style": "덴디", "color": "버건디", "season": "겨울", "fit": "레귤러핏", "category": "스커트",
     "desc": "따뜻한 느낌의 버건디 미니 스커트.",
     "image": "https://zigzag.kr/img/123456_burgundy_skirt.jpg", "link": "https://zigzag.kr/product/123456"},
    {"name": "화이트 스포티 운동화", "gender": "여성", "style": "스포티", "color": "화이트", "season": "여름", "fit": "레귤러핏", "category": "신발",
     "desc": "가볍고 산뜻한 화이트 운동화.",
     "image": "https://8seconds.co.kr/img/white_sneakers_1.jpg", "link": "https://8seconds.co.kr/product/123456"},
    {"name": "베이지 롱 코트", "gender": "여성", "style": "포멀", "color": "베이지", "season": "겨울", "fit": "레귤러핏", "category": "아우터",
     "desc": "우아한 베이지 롱 코트.",
     "image": "https://uniqlo.com/img/beige_longcoat.jpg", "link": "https://uniqlo.com/kr/beige_longcoat"},
    {"name": "네이비 와이드 팬츠", "gender": "여성", "style": "캐주얼", "color": "네이비", "season": "봄", "fit": "오버핏", "category": "하의",
     "desc": "편안한 네이비 와이드 팬츠.",
     "image": "https://ably.co.kr/img/navy_widepants.jpg", "link": "https://ably.co.kr/item/654321"},
    {"name": "버건디 숄더백", "gender": "여성", "style": "포멀", "color": "버건디", "season": "가을", "fit": "레귤러핏", "category": "액세서리",
     "desc": "고급스러운 버건디 숄더백.",
     "image": "https://musinsa.com/img/burgundy_bag.jpg", "link": "https://musinsa.com/app/goods/654321"},
    {"name": "화이트 슬림핏 원피스", "gender": "여성", "style": "포멀", "color": "화이트", "season": "봄", "fit": "슬림핏", "category": "원피스",
     "desc": "클래식한 화이트 슬림핏 원피스.",
     "image": "https://uniqlo.com/img/white_dress_1.jpg", "link": "https://uniqlo.com/kr/white_dress"},
    {"name": "브라운 빈티지 가디건", "gender": "여성", "style": "빈티지", "color": "브라운", "season": "가을", "fit": "루즈핏", "category": "아우터",
     "desc": "포근한 느낌의 빈티지 브라운 가디건.",
     "image": "https://zigzag.kr/img/brown_vintage_cardigan.jpg", "link": "https://zigzag.kr/product/98765"},
    {"name": "카멜 와이드 팬츠", "gender": "여성", "style": "미니멀", "color": "카멜", "season": "봄", "fit": "레귤러핏", "category": "하의",
     "desc": "심플한 카멜 색상의 와이드 팬츠.",
     "image": "https://ably.co.kr/img/camel_widepants.jpg", "link": "https://ably.co.kr/item/98765"},
]

# 조건 완화 필터: 성별만 무조건 맞고 나머지는 일부만 맞으면 추천하도록
def match_condition(product):
    if product["gender"] != gender:
        return False
    
    score = 0
    # 조건 점수
    if product["style"] == style:
        score += 1
    if product["color"] == color:
        score += 1
    if product["season"] == season:
        score += 1
    if product["fit"] == fit:
        score += 1
    if product["category"] == category:
        score += 1
    
    # 점수 2 이상이면 추천
    return score >= 2

filtered_products = [p for p in products if match_condition(p)]

if filtered_products:
    st.write(f"총 {len(filtered_products)}개 추천 상품이 있습니다:")
    for p in filtered_products:
        st.subheader(p["name"])
        st.image(p["image"], width=300)
        st.write(p["desc"])
        st.markdown(f"[상품 바로가기]({p['link']})")
        st.markdown("---")
else:
    st.write("조건에 맞는 상품이 없습니다. 조건을 변경해보세요.")

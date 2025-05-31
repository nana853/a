import streamlit as st

st.title("🧥 무신사 스타일 추천기 (최소 3개 보장)")

# 사용자 입력
gender = st.selectbox("성별 선택", ["남성", "여성"])
style = st.selectbox("스타일 선택", ["스트릿", "캐주얼", "덴디", "미니멀", "포멀"])
color = st.selectbox("색감 선택", ["블랙", "화이트", "그레이", "네이비", "베이지", "카멜", "카키", "버건디"])
season = st.selectbox("계절 선택", ["봄", "여름", "가을", "겨울"])
fit = st.selectbox("핏 선택", ["슬림핏", "레귤러핏", "오버핏", "루즈핏"])
category = st.selectbox("의류 종류 선택", ["상의", "하의", "아우터", "신발", "액세서리", "가방"])

st.markdown("---")

# 상품 데이터 (무신사)
products = [
    {"name": "무신사 블랙 티셔츠", "gender": "남성", "style": "미니멀", "color": "블랙", "season": "여름", "fit": "슬림핏", "category": "상의",
     "desc": "기본 중의 기본 블랙 반팔 티셔츠. 무신사 스탠다드 제품.",
     "image": "https://image.musinsa.com/mfile_s01/2023/07/black_tee.jpg", "link": "https://www.musinsa.com/app/goods/12345"},
    {"name": "무신사 오버핏 후드티", "gender": "남성", "style": "스트릿", "color": "그레이", "season": "가을", "fit": "오버핏", "category": "상의",
     "desc": "무신사 인기 오버핏 후디. 가을에 딱 맞는 두께감.",
     "image": "https://image.musinsa.com/mfile_s01/2023/09/hoodie.jpg", "link": "https://www.musinsa.com/app/goods/67890"},
    {"name": "무신사 카멜 코트", "gender": "남성", "style": "덴디", "color": "카멜", "season": "겨울", "fit": "레귤러핏", "category": "아우터",
     "desc": "도시적인 감성의 카멜 싱글 코트. 겨울 정장 코디 추천.",
     "image": "https://image.musinsa.com/mfile_s01/2023/11/camelcoat.jpg", "link": "https://www.musinsa.com/app/goods/54321"},
    {"name": "무신사 네이비 슬랙스", "gender": "남성", "style": "포멀", "color": "네이비", "season": "봄", "fit": "슬림핏", "category": "하의",
     "desc": "오피스룩에 어울리는 네이비 슬랙스. 깔끔한 핏.",
     "image": "https://image.musinsa.com/mfile_s01/2023/04/navyslacks.jpg", "link": "https://www.musinsa.com/app/goods/34567"},
    {"name": "무신사 화이트 스니커즈", "gender": "남성", "style": "미니멀", "color": "화이트", "season": "여름", "fit": "레귤러핏", "category": "신발",
     "desc": "화이트 레더 스니커즈로 어디든 잘 어울립니다.",
     "image": "https://image.musinsa.com/mfile_s01/2023/06/sneakers.jpg", "link": "https://www.musinsa.com/app/goods/98765"},
    
    {"name": "무신사 버건디 니트", "gender": "여성", "style": "캐주얼", "color": "버건디", "season": "겨울", "fit": "루즈핏", "category": "상의",
     "desc": "겨울에 포인트 주기 좋은 니트웨어. 포근한 느낌.",
     "image": "https://image.musinsa.com/mfile_s01/2023/12/burgundyknit.jpg", "link": "https://www.musinsa.com/app/goods/55555"},
    {"name": "무신사 크림 팬츠", "gender": "여성", "style": "미니멀", "color": "베이지", "season": "봄", "fit": "레귤러핏", "category": "하의",
     "desc": "산뜻한 봄 컬러의 데일리 팬츠.",
     "image": "https://image.musinsa.com/mfile_s01/2023/03/beigepants.jpg", "link": "https://www.musinsa.com/app/goods/22222"},
    {"name": "무신사 카키 야상", "gender": "여성", "style": "스트릿", "color": "카키", "season": "가을", "fit": "오버핏", "category": "아우터",
     "desc": "스트릿 감성 넘치는 야상 자켓. 간절기에 좋아요.",
     "image": "https://image.musinsa.com/mfile_s01/2023/10/kakijacket.jpg", "link": "https://www.musinsa.com/app/goods/33333"},
    {"name": "무신사 블랙 로퍼", "gender": "여성", "style": "포멀", "color": "블랙", "season": "가을", "fit": "레귤러핏", "category": "신발",
     "desc": "깔끔한 실루엣의 포멀 블랙 로퍼.",
     "image": "https://image.musinsa.com/mfile_s01/2023/09/blackloafer.jpg", "link": "https://www.musinsa.com/app/goods/44444"},
    {"name": "무신사 미니 크로스백", "gender": "여성", "style": "덴디", "color": "베이지", "season": "여름", "fit": "슬림핏", "category": "가방",
     "desc": "작고 가벼운 미니백. 여름용 데일리 아이템.",
     "image": "https://image.musinsa.com/mfile_s01/2023/07/minibag.jpg", "link": "https://www.musinsa.com/app/goods/66666"},
]

# 점수 기반 필터링
def get_score(p):
    score = 0
    if p["style"] == style:
        score += 1
    if p["color"] == color:
        score += 1
    if p["season"] == season:
        score += 1
    if p["fit"] == fit:
        score += 1
    if p["category"] == category:
        score += 1
    return score

# 성별 우선 필터
filtered = [p for p in products if p["gender"] == gender]
# 점수 계산 후 정렬
scored = sorted(filtered, key=lambda x: get_score(x), reverse=True)
# 상위 3개 이상 추출
top_matches = scored[:max(3, len(scored))]

# 결과 출력
st.success(f"🎯 추천된 무신사 상품 {min(3, len(top_matches))}개 이상:")
for p in top_matches[:5]:  # 최대 5개까지 보여줌
    st.image(p["image"], width=300)
    st.subheader(p["name"])
    st.write(p["desc"])
    st.markdown(f"[👉 무신사 상품 보러가기]({p['link']})")
    st.markdown("---")


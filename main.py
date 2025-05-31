import streamlit as st

st.title("🧥 무신사 스타일 추천기")

# 사용자 입력 받기
gender = st.selectbox("성별을 선택하세요", ["남성", "여성"])
style = st.selectbox("스타일을 선택하세요", ["스트릿", "캐주얼", "덴디", "미니멀", "포멀"])
color = st.selectbox("색감을 선택하세요", ["블랙", "화이트", "그레이", "네이비", "베이지", "카멜", "카키", "버건디"])
season = st.selectbox("계절을 선택하세요", ["봄", "여름", "가을", "겨울"])
fit = st.selectbox("핏을 선택하세요", ["슬림핏", "레귤러핏", "오버핏", "루즈핏"])
category = st.selectbox("의류 종류를 선택하세요", ["상의", "하의", "아우터", "신발", "액세서리", "가방"])

st.markdown("---")

# 무신사 샘플 데이터
products = [
    {"name": "무신사 스탠다드 블랙 티셔츠", "gender": "남성", "style": "미니멀", "color": "블랙", "season": "여름", "fit": "슬림핏", "category": "상의",
     "desc": "무신사 베스트셀러 기본 티셔츠. 여름에 착용하기 좋은 시원한 소재.",
     "image": "https://image.musinsa.com/mfile_s01/2023/07/12345_1.jpg", "link": "https://www.musinsa.com/app/goods/12345"},
    {"name": "무신사 오버핏 후드티", "gender": "남성", "style": "스트릿", "color": "그레이", "season": "가을", "fit": "오버핏", "category": "상의",
     "desc": "스트릿 스타일의 데일리 오버핏 후드.",
     "image": "https://image.musinsa.com/mfile_s01/2023/09/hoodie123.jpg", "link": "https://www.musinsa.com/app/goods/67890"},
    {"name": "무신사 카멜 싱글 코트", "gender": "남성", "style": "덴디", "color": "카멜", "season": "겨울", "fit": "레귤러핏", "category": "아우터",
     "desc": "겨울에 어울리는 따뜻한 코트. 도회적이면서 단정한 인상.",
     "image": "https://image.musinsa.com/mfile_s01/2023/11/camelcoat.jpg", "link": "https://www.musinsa.com/app/goods/54321"},
    {"name": "무신사 네이비 슬랙스", "gender": "남성", "style": "포멀", "color": "네이비", "season": "봄", "fit": "슬림핏", "category": "하의",
     "desc": "포멀하면서 깔끔한 네이비 슬랙스.",
     "image": "https://image.musinsa.com/mfile_s01/2023/04/navyslacks.jpg", "link": "https://www.musinsa.com/app/goods/34567"},
    {"name": "무신사 레더 스니커즈", "gender": "남성", "style": "미니멀", "color": "화이트", "season": "여름", "fit": "레귤러핏", "category": "신발",
     "desc": "깔끔하고 클래식한 무신사 화이트 스니커즈.",
     "image": "https://image.musinsa.com/mfile_s01/2023/06/sneakers123.jpg", "link": "https://www.musinsa.com/app/goods/98765"},
    {"name": "무신사 여성 버건디 니트", "gender": "여성", "style": "캐주얼", "color": "버건디", "season": "겨울", "fit": "루즈핏", "category": "상의",
     "desc": "포근하고 따뜻한 겨울용 니트웨어.",
     "image": "https://image.musinsa.com/mfile_s01/2023/12/burgundyknit.jpg", "link": "https://www.musinsa.com/app/goods/55555"},
    {"name": "무신사 여성 크림 팬츠", "gender": "여성", "style": "미니멀", "color": "베이지", "season": "봄", "fit": "레귤러핏", "category": "하의",
     "desc": "편안한 착용감과 미니멀한 디자인.",
     "image": "https://image.musinsa.com/mfile_s01/2023/03/beigepants.jpg", "link": "https://www.musinsa.com/app/goods/22222"},
    {"name": "무신사 여성 카키 야상", "gender": "여성", "style": "스트릿", "color": "카키", "season": "가을", "fit": "오버핏", "category": "아우터",
     "desc": "가을 스트릿 필수템 카키 야상 자켓.",
     "image": "https://image.musinsa.com/mfile_s01/2023/10/kakijacket.jpg", "link": "https://www.musinsa.com/app/goods/33333"},
    {"name": "무신사 여성 포멀 로퍼", "gender": "여성", "style": "포멀", "color": "블랙", "season": "가을", "fit": "레귤러핏", "category": "신발",
     "desc": "오피스룩에 어울리는 세련된 블랙 로퍼.",
     "image": "https://image.musinsa.com/mfile_s01/2023/09/blackloafer.jpg", "link": "https://www.musinsa.com/app/goods/44444"},
    {"name": "무신사 미니 크로스백", "gender": "여성", "style": "덴디", "color": "베이지", "season": "여름", "fit": "슬림핏", "category": "가방",
     "desc": "가볍고 실용적인 미니백. 여름 데일리룩 완성!",
     "image": "https://image.musinsa.com/mfile_s01/2023/07/minibag.jpg", "link": "https://www.musinsa.com/app/goods/66666"},
]

# 조건 필터링
def match_condition(p):
    return (
        p["gender"] == gender and
        p["style"] == style and
        p["color"] == color and
        p["season"] == season and
        p["fit"] == fit and
        p["category"] == category
    )

matched = [p for p in products if match_condition(p)]

# 결과 출력
if matched:
    st.success(f"총 {len(matched)}개의 무신사 상품이 있습니다.")
    for item in matched:
        st.image(item["image"], width=300)
        st.subheader(item["name"]

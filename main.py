import streamlit as st

# 샘플 추천 데이터 (실제 추천 데이터는 더 추가하면 됨)
recommendations = {
    "남성": {
        "스트릿": {
            "블랙": {
                "봄": {
                    "오버핏": {
                        "상의": {"site": "https://musinsa.com", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_1.jpg"},
                        "하의": {"site": "https://musinsa.com", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_2.jpg"},
                        "아우터": {"site": "https://musinsa.com", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_3.jpg"},
                        "신발": {"site": "https://musinsa.com", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_4.jpg"},
                        "액세서리": {"site": "https://musinsa.com", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_5.jpg"}
                    }
                }
            }
        }
    },
    "여성": {
        "덴디": {
            "베이지": {
                "가을": {
                    "슬림핏": {
                        "상의": {"site": "https://wconcept.co.kr", "img": "https://image.wconcept.co.kr/productimg/2023/03/01/1.jpg"},
                        "하의": {"site": "https://wconcept.co.kr", "img": "https://image.wconcept.co.kr/productimg/2023/03/01/2.jpg"},
                        "아우터": {"site": "https://wconcept.co.kr", "img": "https://image.wconcept.co.kr/productimg/2023/03/01/3.jpg"},
                        "신발": {"site": "https://wconcept.co.kr", "img": "https://image.wconcept.co.kr/productimg/2023/03/01/4.jpg"},
                        "액세서리": {"site": "https://wconcept.co.kr", "img": "https://image.wconcept.co.kr/productimg/2023/03/01/5.jpg"}
                    }
                }
            }
        }
    }
}

# Streamlit UI 구성
st.set_page_config(page_title="패션 추천기", layout="wide")
st.title("🧥 스타일 기반 패션 추천기")
st.markdown("당신의 **성별, 스타일, 색감, 계절, 핏**을 골라보세요. 딱 맞는 아이템을 추천해드릴게요!")

# 입력 요소
gender = st.selectbox("👤 성별 선택", ["남성", "여성"])
style = st.selectbox("👗 스타일 선택", ["스트릿", "캐주얼", "덴디", "포멀", "스포티"])
color = st.selectbox("🎨 색감 선택", ["블랙", "화이트", "네이비", "파스텔", "비비드", "올리브", "베이지", "버건디"])
season = st.selectbox("🌤️ 계절 선택", ["봄", "여름", "가을", "겨울"])
fit = st.selectbox("📐 핏 선택", ["슬림핏", "레귤러핏", "오버핏"])

# 추천 결과 출력
if st.button("🎯 추천 아이템 보기"):
    try:
        items = recommendations[gender][style][color][season][fit]
        st.success(f"✨ [{gender}] {style} 스타일, {color}, {season}, {fit} 조합의 추천 결과입니다!")
        for category, info in items.items():
            st.subheader(f"🧩 {category}")
            st.image(info["img"], width=300, caption=f"{category}")
            st.markdown(f"[🔗 쇼핑몰 링크 바로가기]({info['site']})")
    except KeyError:
        st.warning("😢 해당 조합의 추천 정보가 아직 준비되지 않았어요. 다른 조합을 선택해보세요!")


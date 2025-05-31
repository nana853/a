import streamlit as st

# 전체 추천 데이터 샘플 (조합 일부만 포함 — 확장 가능)
recommendations = {
    "남성": {
        "스트릿": {
            "블랙": {
                "봄": {
                    "오버핏": {
                        "상의": {"site": "https://musinsa.com", "img": "https://image.musinsa.com/example1.jpg"},
                        "하의": {"site": "https://musinsa.com", "img": "https://image.musinsa.com/example2.jpg"},
                        "아우터": {"site": "https://musinsa.com", "img": "https://image.musinsa.com/example3.jpg"},
                        "신발": {"site": "https://musinsa.com", "img": "https://image.musinsa.com/example4.jpg"},
                        "액세서리": {"site": "https://musinsa.com", "img": "https://image.musinsa.com/example5.jpg"}
                    }
                }
            }
        },
        "캐주얼": {
            "파스텔": {
                "여름": {
                    "레귤러핏": {
                        "상의": {"site": "https://spao.com", "img": "https://image.spao.com/example1.jpg"},
                        "하의": {"site": "https://spao.com", "img": "https://image.spao.com/example2.jpg"},
                        "아우터": {"site": "https://spao.com", "img": "https://image.spao.com/example3.jpg"},
                        "신발": {"site": "https://spao.com", "img": "https://image.spao.com/example4.jpg"},
                        "액세서리": {"site": "https://spao.com", "img": "https://image.spao.com/example5.jpg"}
                    }
                }
            }
        }
    },
    "여성": {
        "덴디": {
            "화이트": {
                "가을": {
                    "슬림핏": {
                        "상의": {"site": "https://wconcept.co.kr", "img": "https://image.wconcept.co.kr/example1.jpg"},
                        "하의": {"site": "https://wconcept.co.kr", "img": "https://image.wconcept.co.kr/example2.jpg"},
                        "아우터": {"site": "https://wconcept.co.kr", "img": "https://image.wconcept.co.kr/example3.jpg"},
                        "신발": {"site": "https://wconcept.co.kr", "img": "https://image.wconcept.co.kr/example4.jpg"},
                        "액세서리": {"site": "https://wconcept.co.kr", "img": "https://image.wconcept.co.kr/example5.jpg"}
                    }
                }
            }
        }
    }
}

# 사용자 입력 받기
st.title("🧥 스타일 기반 의류 추천기")
st.write("성별, 스타일, 색감, 계절, 원하는 핏을 선택하면 그에 맞는 의류 아이템을 추천해드립니다.")

gender = st.selectbox("👤 성별을 선택하세요", ["남성", "여성"])
style = st.selectbox("👕 스타일을 선택하세요", ["스트릿", "캐주얼", "덴디", "포멀", "스포티"])
color = st.selectbox("🎨 색감을 선택하세요", ["블랙", "화이트", "그레이", "네이비", "파스텔", "비비드"])
season = st.selectbox("🌸 계절을 선택하세요", ["봄", "여름", "가을", "겨울"])
fit = st.selectbox("📏 원하는 핏을 선택하세요", ["슬림핏", "레귤러핏", "오버핏"])

# 결과 출력
if st.button("👀 추천 보기"):
    try:
        data = recommendations[gender][style][color][season][fit]
        st.subheader(f"🛒 {gender} - {style} 스타일 ({color}, {season}, {fit})")
        for category, item in data.items():
            st.markdown(f"### 🧩 {category}")
            st.image(item["img"], width=300)
            st.markdown(f"[🔗 바로가기]({item['site']})", unsafe_allow_html=True)
    except KeyError:
        st.error("❗ 현재 선택하신 조합에 대한 추천 정보가 없습니다. 다른 옵션을 시도해보세요.")

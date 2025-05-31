import streamlit as st

# 스타일, 색감, 성별, 계절, 핏, 의류 종류에 따른 추천 데이터
recommendations = {
    "남성": {
        "스트릿": {
            "블랙": {
                "봄": {
                    "슬림핏": {
                        "상의": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_1.jpg"},
                        "하의": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_2.jpg"},
                        "아우터": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_3.jpg"},
                        "신발": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_4.jpg"},
                        "액세서리": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_5.jpg"}
                    },
                    "오버핏": {
                        "상의": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_6.jpg"},
                        "하의": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_7.jpg"},
                        "아우터": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_8.jpg"},
                        "신발": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_9.jpg"},
                        "액세서리": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_10.jpg"}
                    }
                }
            }
        }
    },
    "여성": {
        "스트릿": {
            "블랙": {
                "봄": {
                    "슬림핏": {
                        "상의": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_1.jpg"},
                        "하의": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_2.jpg"},
                        "아우터": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_3.jpg"},
                        "신발": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_4.jpg"},
                        "액세서리": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_5.jpg"}
                    },
                    "오버핏": {
                        "상의": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_6.jpg"},
                        "하의": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_7.jpg"},
                        "아우터": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_8.jpg"},
                        "신발": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_9.jpg"},
                        "액세서리": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_10.jpg"}
                    }
                }
            }
        }
    }
}

# 앱 UI 시작
st.title("👗 맞춤형 패션 추천기")
st.write("성별, 스타일, 색감, 계절, 핏을 선택하면 어울리는 의류 아이템을 추천해드려요!")

# 사용자 입력
gender = st.selectbox("성별을 선택하세요:", ["남성", "여성"])
style = st.selectbox("스타일을 선택하세요:", ["스트릿", "캐주얼", "덴디", "포멀", "스포티"])
color = st.selectbox("색감을 선택하세요:", ["블랙", "화이트", "네이비", "파스텔", "비비드"])
season = st.selectbox("계절을 선택하세요:", ["봄", "여름", "가을", "겨울"])
fit = st.selectbox("핏을 선택하세요:", ["슬림
::contentReference[oaicite:0]{index=0}
 

import streamlit as st

# 스타일, 색감, 성별, 의류 종류에 따른 추천 데이터
recommendations = {
    "남성": {
        "스트릿": {
            "블랙": {
                "상의": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_1.jpg"},
                "하의": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_2.jpg"},
                "아우터": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_3.jpg"},
                "신발": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_4.jpg"},
                "액세서리": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_5.jpg"}
            },
            "파스텔": {
                "상의": {"site": "https://www.wconcept.co.kr/Mobile2/Shop/Brand/2106", "img": "https://image.wconcept.co.kr/2023/03/01/20230301_1.jpg"},
                "하의": {"site": "https://www.wconcept.co.kr/Mobile2/Shop/Brand/2106", "img": "https://image.wconcept.co.kr/2023/03/01/20230301_2.jpg"},
                "아우터": {"site": "https://www.wconcept.co.kr/Mobile2/Shop/Brand/2106", "img": "https://image.wconcept.co.kr/2023/03/01/20230301_3.jpg"},
                "신발": {"site": "https://www.wconcept.co.kr/Mobile2/Shop/Brand/2106", "img": "https://image.wconcept.co.kr/2023/03/01/20230301_4.jpg"},
                "액세서리": {"site": "https://www.wconcept.co.kr/Mobile2/Shop/Brand/2106", "img": "https://image.wconcept.co.kr/2023/03/01/20230301_5.jpg"}
            }
        },
        "캐주얼": {
            "블랙": {
                "상의": {"site": "https://www.uniqlo.com/kr/ko/men", "img": "https://image.uniqlo.com/2023/03/01/20230301_1.jpg"},
                "하의": {"site": "https://www.uniqlo.com/kr/ko/men", "img": "https://image.uniqlo.com/2023/03/01/20230301_2.jpg"},
                "아우터": {"site": "https://www.uniqlo.com/kr/ko/men", "img": "https://image.uniqlo.com/2023/03/01/20230301_3.jpg"},
                "신발": {"site": "https://www.uniqlo.com/kr/ko/men", "img": "https://image.uniqlo.com/2023/03/01/20230301_4.jpg"},
                "액세서리": {"site": "https://www.uniqlo.com/kr/ko/men", "img": "https://image.uniqlo.com/2023/03/01/20230301_5.jpg"}
            },
            "파스텔": {
                "상의": {"site": "https://www.ssfshop.com/8seconds/main", "img": "https://image.ssfshop.com/2023/03/01/20230301_1.jpg"},
                "하의": {"site": "https://www.ssfshop.com/8seconds/main", "img": "https://image.ssfshop.com/2023/03/01/20230301_2.jpg"},
                "아우터": {"site": "https://www.ssfshop.com/8seconds/main", "img": "https://image.ssfshop.com/2023/03/01/20230301_3.jpg"},
                "신발": {"site": "https://www.ssfshop.com/8seconds/main", "img": "https://image.ssfshop.com/2023/03/01/20230301_4.jpg"},
                "액세서리": {"site": "https://www.ssfshop.com/8seconds/main", "img": "https://image.ssfshop.com/2023/03/01/20230301_5.jpg"}
            }
        }
    },
    "여성": {
        "스트릿": {
            "블랙": {
                "상의": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_1.jpg"},
                "하의": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_2.jpg"},
                "아우터": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_3.jpg"},
                "신발": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_4.jpg"},
                "액세서리": {"site": "https://www.musinsa.com/categories/street", "img": "https://image.musinsa.com/mfile_s01/2023/03/01/20230301_5.jpg"}
            },
            "파스텔
::contentReference[oaicite:0]{index=0}
 

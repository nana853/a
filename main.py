import streamlit as st

# MBTI별 여행 추천 데이터
mbti_travel_recommendations = {
    "ISTJ": "조용하고 질서정연한 장소를 선호하므로, 교토의 전통 사찰 여행을 추천합니다.",
    "ISFJ": "사려 깊고 평화를 중시하므로, 스위스 루체른의 호숫가 휴양이 잘 어울립니다.",
    "INFJ": "깊이 있는 자기성찰을 좋아하므로, 아이슬란드의 자연 속 트레킹을 추천합니다.",
    "INTJ": "전략적 사고를 즐기기에, 독일의 역사 탐방 여행이 좋습니다.",
    "ISTP": "탐험을 좋아하므로, 뉴질랜드에서의 로드 트립이 제격입니다.",
    "ISFP": "자연과의 조화를 즐기므로, 발리의 자연 친화적 리조트가 잘 맞습니다.",
    "INFP": "감성을 중요시하므로, 프라하의 감성적인 골목 여행을 추천합니다.",
    "INTP": "호기심이 많아 유럽 도시들의 박물관 투어가 적합합니다.",
    "ESTP": "액티비티를 즐기므로, 캐나다의 스키 여행이 잘 어울립니다.",
    "ESFP": "사교적이고 즐거운 분위기를 선호하므로, 라스베이거스 여행이 적합합니다.",
    "ENFP": "새로운 사람과 장소를 좋아하므로, 동남아 배낭여행을 추천합니다.",
    "ENTP": "다양한 경험을 추구하므로, 도쿄의 도시 탐험 여행이 좋습니다.",
    "ESTJ": "계획적인 여행을 선호하므로, 런던의 역사적 명소 투어가 적합합니다.",
    "ESFJ": "사람들과 어울리는 것을 좋아하므로, 파리의 미식&문화 여행이 좋습니다.",
    "ENFJ": "타인을 돕고 싶어 하므로, 봉사 여행 형태의 여행이 적합합니다.",
    "ENTJ": "도전과 리더십을 즐기므로, 아프리카 사파리 같은 이색적 여행을 추천합니다."
}

# Streamlit 앱 UI 구성
st.title("🌍 MBTI 기반 여행 추천기")
st.write("당신의 MBTI를 선택하면 성격에 맞는 여행 코스를 추천해드려요!")

# MBTI 선택 드롭다운
mbti_types = list(mbti_travel_recommendations.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요:", mbti_types)

# 추천 결과 표시
if selected_mbti:
    recommendation = mbti_travel_recommendations[selected_mbti]
    st.subheader("✈️ 추천 여행 코스:")
    st.write(recommendation)

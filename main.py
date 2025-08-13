import streamlit as st
import random # 풍선 효과를 위한 라이브러리 (필수는 아니지만 트렌디함!)

# --- MBTI 궁합 데이터 (재미를 위한 예시이며, 실제와 다를 수 있습니다!) ---
# '찰떡 궁합'과 '의외의 궁합'으로 나누어 좀 더 풍성하게 표현해볼까요?
mbti_compatibility_data = {
    "ISTJ": {
        "best": ["ESFP", "ESTP"],
        "good": ["ISFP", "INFP"]
    },
    "ISTP": {
        "best": ["ESFJ", "ENFJ"],
        "good": ["ISFJ", "ENTP"]
    },
    "ISFJ": {
        "best": ["ESTP", "ESFP"],
        "good": ["ISTP", "ENFJ"]
    },
    "ISFP": {
        "best": ["ESTJ", "ENTJ"],
        "good": ["ESFJ", "INFP"]
    },
    "INFJ": {
        "best": ["ENFP", "ENTP"],
        "good": ["INFP", "INTJ"]
    },
    "INFP": {
        "best": ["ENFJ", "ESTJ"],
        "good": ["INFJ", "ESFP"]
    },
    "INTJ": {
        "best": ["ENFP", "ENTP"],
        "good": ["INFJ", "INTP"] # 같은 타입도 때로는 의외의 시너지!
    },
    "INTP": {
        "best": ["ENTJ", "ENFJ"],
        "good": ["INTJ", "ESTJ"]
    },
    "ESTJ": {
        "best": ["ISFP", "INFP"],
        "good": ["ISTJ", "ENTJ"]
    },
    "ESTP": {
        "best": ["ISFJ", "ISTJ"],
        "good": ["ESFP", "ENFJ"]
    },
    "ESFJ": {
        "best": ["ISTP", "INTP"],
        "good": ["ISFJ", "ENFP"]
    },
    "ESFP": {
        "best": ["ISTJ", "ISFJ"],
        "good": ["ESTP", "INFP"]
    },
    "ENFJ": {
        "best": ["INFP", "ISFP"],
        "good": ["INFJ", "ENTP"]
    },
    "ENFP": {
        "best": ["INFJ", "INTJ"],
        "good": ["ENFJ", "ISTP"]
    },
    "ENTJ": {
        "best": ["INTP", "ISFP"],
        "good": ["ESTJ", "ENFP"]
    },
    "ENTP": {
        "best": ["INFJ", "INTJ"],
        "good": ["ENFP", "ISTP"]
    }
}

# 모든 MBTI 타입 리스트 (selectbox에 사용)
all_mbti_types = sorted(list(mbti_compatibility_data.keys()))

# --- 웹앱 UI 설정 ---
st.set_page_config(
    page_title="💖 MBTI 궁합 탐색기 (트렌디 에디션) 💖",
    page_icon="✨",
    layout="centered" # wide로 설정하여 넓게 쓸 수도 있어요!
)

# 배경 이미지 또는 색상 (간단한 예시)
# 스트림릿에 직접적인 배경 이미지 삽입은 CSS를 사용해야 합니다.
# 여기서는 간단한 CSS 주입 방식으로 트렌디한 느낌을 줘볼게요!
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6; /* 밝은 회색 계열 */
        padding: 20px;
        border-radius: 10px;
    }
    .stApp {
        background-image: linear-gradient(to right bottom, #fde4e2, #fcd2d7, #f7c3dc, #e8b8e0, #d0b0e5); /* 은은한 그라데이션 */
        background-attachment: fixed;
        background-size: cover;
    }
    .stButton>button {
        background-color: #ff69b4; /* 핑크색 버튼 */
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background-color: #ff85c1; /* 호버 시 색상 변경 */
    }
    h1 {
        color: #6a0572; /* 보라색 계열 */
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .stText {
        font-size: 1.1em;
        line-height: 1.6;
    }
    .result-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        margin-top: 30px;
    }
    .mbti-type {
        font-weight: bold;
        color: #e60073; /* 진한 핑크색 */
        font-size: 1.2em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💖 MBTI 궁합 탐색기 🚀")
st.markdown("### ✨ 당신의 MBTI를 선택하고, 잘 맞는 운명의 상대를 찾아보세요! ✨")
st.write("") # 간격 띄우기

# 사용자 MBTI 입력 받기 (Selectbox로 선택하도록 변경하여 더 깔끔하고 오류 방지)
st.markdown("---")
col1, col2 = st.columns([1, 2]) # 컬럼을 나누어 좀 더 예쁘게 배치
with col1:
    st.image("https://www.flaticon.com/svg/static/icons/svg/3001/3001423.svg", width=100) # 귀여운 아이콘! (링크가 유효하지 않을 경우 작동하지 않음)
with col2:
    selected_mbti = st.selectbox(
        "🔮 나의 MBTI는?",
        ["-- MBTI를 선택해주세요 --"] + all_mbti_types # 첫 번째 옵션 추가
    )
st.markdown("---")

# 궁합 찾기 버튼
if st.button("🌟 궁합 찾기! 🌟"):
    if selected_mbti == "-- MBTI를 선택해주세요 --":
        st.error("앗! MBTI를 선택해주셔야 궁합을 찾아드릴 수 있어요! 😅")
    else:
        # 결과 표시 (애니메이션 효과 추가)
        st.write("### 당신의 MBTI는...", selected_mbti, "이시군요! 🤔")
        st.spinner("💖 최적의 궁합을 찾는 중...")
        st.balloons() # 풍선 애니메이션 추가!
        st.snow() # 눈 내리는 애니메이션도 추가! (둘 중 하나만 사용해도 좋아요!)

        if selected_mbti in mbti_compatibility_data:
            match_info = mbti_compatibility_data[selected_mbti]

            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.markdown(f"## 🥳 {selected_mbti}님의 완벽 궁합! 🥳")

            # 찰떡 궁합
            st.subheader("💗 찰떡같이 잘 맞는 BEST 궁합! (Feat. 천생연분💖)")
            if match_info["best"]:
                for mbti_type in match_info["best"]:
                    st.markdown(f"- <span class='mbti-type'>{mbti_type}</span>", unsafe_allow_html=True)
                st.info("이 타입들과는 소름 끼치게 잘 맞을 수 있어요! ✨")
            else:
                st.write("아직 찰떡 궁합 데이터가 없네요... 당신이 첫 번째일 수도! 🤫")

            st.write("---")

            # 의외의 궁합
            st.subheader("💡 의외의 시너지를 내는 꿀조합! (Feat. 매력 부자🤝)")
            if match_info["good"]:
                for mbti_type in match_info["good"]:
                    st.markdown(f"- <span class='mbti-type'>{mbti_type}</span>", unsafe_allow_html=True)
                st.info("새로운 관계를 탐색하고 싶다면 이 타입들을 주목해주세요! 🚀")
            else:
                st.write("의외의 궁합은 우연히 만나는 즐거움이겠죠? 😉")

            st.markdown("</div>", unsafe_allow_html=True) # result-box 닫기

            st.markdown("---")
            st.success("✨ 이 모든 결과는 재미와 통찰을 위한 것이며, 실제 관계는 개인의 노력과 이해가 중요하답니다! ✨")

        else:
            st.error("죄송해요, 알 수 없는 MBTI 타입이에요. 다시 확인해주세요! 😥")

# 푸터 (Footer)
st.write("") # 간격
st.markdown(
    """
    <div style="text-align: center; color: #7f8c8d; font-size: 0.9em; margin-top: 50px;">
        <p>© 2025 CreativeMongoose5351. Made with Streamlit ❤️</p>
        <p>⚠️ 이 서비스는 MBTI 궁합에 대한 일반적인 재미 요소를 제공하며, 전문가의 조언이 아닙니다.</p>
    </div>
    """,
    unsafe_allow_html=True
)

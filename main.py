import streamlit as st
import random # 풍선 효과를 위한 라이브러리

# --- MBTI 궁합 데이터 (재미를 위한 예시이며, 실제와 다를 수 있습니다!) ---
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
        "good": ["INFJ", "INTP"]
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

# 배경 이미지 또는 색상 (CSS 주입 방식)
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
        transition: all 0.3s ease; /* 부드러운 전환 효과 */
    }
    .stButton>button:hover {
        background-color: #ff85c1; /* 호버 시 색상 변경 */
        transform: translateY(-2px); /* 살짝 위로 뜨는 효과 */
    }
    h1 {
        color: #6a0572; /* 보라색 계열 */
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        font-family: 'Arial Black', sans-serif; /* 더 강조된 폰트 */
    }
    h3 {
        color: #8A2BE2; /* 보라색 */
    }
    h2 {
        color: #E61A5F; /* 진한 핑크 */
    }
    .stText {
        font-size: 1.1em;
        line-height: 1.6;
    }
    .result-box {
        background-color: rgba(255, 255, 255, 0.9); /* 반투명 흰색 */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        margin-top: 30px;
        border: 2px solid #ff69b4; /* 테두리 추가 */
    }
    .mbti-type {
        font-weight: bold;
        color: #e60073; /* 진한 핑크색 */
        font-size: 1.2em;
        background-color: #fff0f5; /* 연한 핑크 배경 */
        padding: 3px 8px;
        border-radius: 5px;
        display: inline-block; /* 라인 전체 차지하지 않도록 */
        margin: 2px;
    }
    .stInfo, .stSuccess, .stError, .stWarning {
        border-radius: 10px;
        padding: 10px 15px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💖 MBTI 궁합 탐색기 🚀")
st.markdown("### ✨ 당신의 MBTI를 선택하고, 잘 맞는 운명의 상대를 찾아보세요! ✨")
st.write("") # 간격 띄우기

# --- 이미지 파일을 현재 폴더에 준비해주세요! ---
# 예: 'mbti_icon.png' 파일을 이 스크립트 파일과 같은 폴더에 넣어주세요.
# 만약 파일이 없다면 이 부분에서 에러가 날 수 있습니다.
# 인터넷에서 귀여운 아이콘 이미지를 다운로드 받아 사용하시면 됩니다.
image_path = "mbti_icon.png" # <--- 이미지 파일 경로를 여기에 정확히 입력해주세요!
try:
    st.image(image_path, width=150) # 중앙 정렬은 st.columns와 함께 사용하거나 CSS 추가
except FileNotFoundError:
    st.warning("아이콘 이미지 파일이 없네요! 🤔 'mbti_icon.png' 파일을 이 스크립트 파일과 같은 폴더에 넣어주세요. ")
    st.image("https://raw.githubusercontent.com/streamlit/streamlit/develop/lib/streamlit/static/assets/logo.svg", width=150) # 기본 Streamlit 로고 대체

st.markdown("---")
# 사용자 MBTI 입력 받기 (Selectbox로 선택하도록 변경)
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
        st.markdown(f"### 당신의 MBTI는 <span style='color:#6a0572; font-weight:bold;'>{selected_mbti}</span> 이시군요! 🤔", unsafe_allow_html=True)

        with st.spinner("💖 최적의 궁합을 찾는 중... 잠시만 기다려 주세요! ✨"):
            st.balloons() # 풍선 애니메이션 추가!
            # st.snow() # 눈 내리는 애니메이션도 추가! (둘 중 하나만 사용해도 좋아요!)
            import time
            time.sleep(2) # 검색하는 척 시간 지연

        if selected_mbti in mbti_compatibility_data:
            match_info = mbti_compatibility_data[selected_mbti]

            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.markdown(f"## 🥳 <span style='color:#e60073;'>{selected_mbti}</span>님의 완벽 궁합은? 🥳", unsafe_allow_html=True)
            st.write(" ") # 간격

            # 찰떡 궁합
            st.subheader("💗 찰떡같이 잘 맞는 BEST 궁합! (Feat. 천생연분💖)")
            if match_info["best"]:
                st.write("이 타입들과는 소름 끼치게 잘 맞을 수 있어요! ✨")
                for mbti_type in match_info["best"]:
                    st.markdown(f"- <span class='mbti-type'>{mbti_type}</span>", unsafe_allow_html=True)
            else:
                st.info("아직 찰떡 궁합 데이터가 없네요... 당신이 첫 번째일 수도! 🤫")

            st.write("---")

            # 의외의 궁합
            st.subheader("💡 의외의 시너지를 내는 꿀조합! (Feat. 매력 부자🤝)")
            if match_info["good"]:
                st.write("새로운 관계를 탐색하고 싶다면 이 타입들을 주목해주세요! 🚀")
                for mbti_type in match_info["good"]:
                    st.markdown(f"- <span class='mbti-type'>{mbti_type}</span>", unsafe_allow_html=True)
            else:
                st.info("의외의 궁합은 우연히 만나는 즐거움이겠죠? 😉")

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

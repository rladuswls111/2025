import streamlit as st

# 위에 정의한 mbti_compatibility 딕셔너리를 여기에 붙여넣으세요.
mbti_compatibility = {
    "ISTJ": ["ESFP", "ESTP"],
    "ISTP": ["ESFJ", "ENFJ"],
    "ISFJ": ["ESTP", "ESFP"],
    "ISFP": ["ESTJ", "ENTJ"],
    "INFJ": ["ENFP", "ENTP"],
    "INFP": ["ENFJ", "ENTJ"],
    "INTJ": ["ENFP", "INTP"],
    "INTP": ["ENTJ", "INTJ"],
    "ESTJ": ["ISFP", "INFP"],
    "ESTP": ["ISFJ", "ISTJ"],
    "ESFJ": ["ISTP", "INTP"],
    "ESFP": ["ISTJ", "ISFJ"],
    "ENFJ": ["INFP", "ENFJ"],
    "ENFP": ["INFJ", "INTJ"],
    "ENTJ": ["INTP", "ISFP"],
    "ENTP": ["INFJ", "ENTP"]
}

st.title("💖 나의 MBTI 궁합 찾기 💖")
st.write("자신의 MBTI를 입력하고, 잘 맞는 MBTI를 찾아보세요!")

# 사용자 MBTI 입력 받기
user_mbti = st.text_input("당신의 MBTI를 입력해주세요 (예: ENFP):", "").upper() # 대문자로 변환

# 버튼 클릭 시 궁합 찾기
if st.button("궁합 찾기"):
    if user_mbti in mbti_compatibility:
        compatible_mbti = mbti_compatibility[user_mbti]
        st.success(f"**{user_mbti}** 님과 잘 맞는 MBTI 유형은 바로... 두구두구! 🥁")
        for mbti_type in compatible_mbti:
            st.write(f"- **{mbti_type}**")
        st.info("이 결과는 재미로 봐주세요! 😊")
    elif user_mbti == "":
        st.warning("MBTI를 입력해주세요!")
    else:
        st.error("죄송해요, 입력하신 MBTI 타입은 아직 제 데이터에 없거나 올바르지 않은 형식 같아요. 다시 확인해주세요. 😅")

st.markdown("---")
st.caption("제작: 창의적인몽구스5351님")

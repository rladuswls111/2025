import streamlit as st

# 🎀 앱 기본 설정 및 핑크 테마 적용하기 🎀
st.set_page_config(
    page_title="💖 내게 딱! 퍼스널 컬러 화장품 💖",
    page_icon="✨",
    layout="centered"
)

# 🌸 커스텀 핑크 테마 CSS (전체적인 배경과 텍스트 색상을 조절해요!) 🌸
# Streamlit은 직접 CSS를 주입할 수 있어서 원하는 색상으로 마음껏 꾸밀 수 있어요!
st.markdown(
    """
    <style>
    /* 전체 배경색을 연한 핑크로 설정 */
    .stApp {
        background-color: #ffeef2; /* 연한 핑크 */
    }
    /* 사이드바 배경색 설정 */
    .stSidebar {
        background-color: #ffdae3; /* 조금 더 진한 핑크 */
    }
    /* 헤더 폰트 색상 및 폰트 변경 (더 트렌디하게!) */
    h1, h2, h3, h4, h5, h6 {
        color: #e91e63; /* 핫핑크 계열 */
        font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif; /* 한글 폰트 */
    }
    /* 일반 텍스트 색상 */
    div.stMarkdown p {
        color: #5d3f6a; /* 보라빛이 감도는 세련된 색상 */
        font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
    }
    /* 선택 박스 및 버튼 스타일링 */
    .stSelectbox>div>div, .stButton>button {
        border-color: #ff7299; /* 버튼 테두리 핑크 */
        color: #e91e63; /* 버튼 텍스트 핑크 */
        background-color: #fff0f5; /* 버튼 배경 연한 핑크 */
    }
    .stSelectbox>div>div:hover, .stButton>button:hover {
        background-color: #ffbed3; /* 호버 시 진한 핑크 */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💖 내 퍼스널 컬러에 찰떡! 화장품 추천 앱 💖")
st.markdown("✨ **창의적인몽구스5351님만의 특별한 뷰티 가이드!** ✨")

# 💄 샘플 화장품 데이터 (데이터베이스 대신 예시로 사용!) 💄
# 실제 앱에서는 이 부분을 데이터베이스나 CSV 파일 등으로 관리하면 더욱 편리해요!
cosmetics_data = [
    {
        "name": "립틴트 (코랄블러쉬)",
        "brand": "베스트뷰티",
        "suitable_for": ["봄 웜톤"],
        "description": "생기 넘치는 코랄빛이 봄 웜톤 피부에 화사함을 더해줘요!",
        "image_url": "https://via.placeholder.com/150/FFC0CB/000000?text=CoralTint" # 더미 이미지 URL
    },
    {
        "name": "아이섀도우 팔레트 (라벤더 드림)",
        "brand": "쿨톤뮤즈",
        "suitable_for": ["여름 쿨톤"],
        "description": "시원하고 청량한 라벤더와 그레이시 핑크 조합이 여름 쿨톤 눈매를 돋보이게 해요.",
        "image_url": "https://via.placeholder.com/150/CCCCFF/000000?text=LavenderShadow"
    },
    {
        "name": "매트 립스틱 (칠리 브릭)",
        "brand": "가을감성",
        "suitable_for": ["가을 웜톤"],
        "description": "깊이 있는 칠리 브릭 컬러로 가을 웜톤의 분위기를 더욱 풍성하게 연출해보세요.",
        "image_url": "https://via.placeholder.com/150/B87333/FFFFFF?text=ChilliLip"
    },
    {
        "name": "블러셔 (차가운 핑크)",
        "brand": "겨울여왕",
        "suitable_for": ["겨울 쿨톤"],
        "description": "얼굴에 생기를 불어넣는 차가운 핑크빛 블러셔로 겨울 쿨톤의 시크함을 표현해요.",
        "image_url": "https://via.placeholder.com/150/FF69B4/000000?text=CoolPinkBlusher"
    },
    {
        "name": "피치 블러셔 (맑은 피치)",
        "brand": "베스트뷰티",
        "suitable_for": ["봄 웜톤"],
        "description": "맑고 상큼한 피치 색상이 봄 웜톤 피부에 생기를 더해줍니다!",
        "image_url": "https://via.placeholder.com/150/FFDAB9/000000?text=PeachBlusher"
    },
    {
        "name": "아이라이너 (딥 브라운)",
        "brand": "공용템",
        "suitable_for": ["봄 웜톤", "가을 웜톤", "여름 쿨톤", "겨울 쿨톤"], # 모든 톤에 어울리는 예시
        "description": "또렷한 눈매를 연출하는 데일리 딥 브라운 아이라이너입니다.",
        "image_url": "https://via.placeholder.com/150/8B4513/FFFFFF?text=BrownEyeliner"
    }
]

# 👩‍🎤 퍼스널 컬러 선택하기 👩‍🎤
personal_colors = ["퍼스널 컬러를 선택해주세요!", "봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"]
selected_color = st.selectbox(
    "💡 당신의 퍼스널 컬러는 무엇인가요?",
    personal_colors
)

if selected_color == "퍼스널 컬러를 선택해주세요!":
    st.info("⬆️ 위에 있는 드롭다운 메뉴에서 당신의 퍼스널 컬러를 선택해주세요! ⬆️")
else:
    st.write(f"🎉 **{selected_color}** 이시군요! 당신을 위한 화장품을 찾아볼까요? 🎉")

    # 🛍️ 화장품 추천하기 🛍️
    recommended_cosmetics = [
        item for item in cosmetics_data if selected_color in item["suitable_for"]
    ]

    if recommended_cosmetics:
        st.subheader(f"{selected_color}을 위한 추천템! 🎁")
        
        # 컬럼을 사용하여 화장품을 나란히 배열 (더 깔끔하고 보기 좋게!)
        num_cols = 2 # 한 줄에 표시할 컬럼 수
        cols = st.columns(num_cols)
        
        for i, cosmetic in enumerate(recommended_cosmetics):
            with cols[i % num_cols]: # 현재 컬럼에 내용 추가
                st.image(cosmetic["image_url"], width=100) # 이미지 크기 조절
                st.markdown(f"**{cosmetic['name']}**")
                st.markdown(f"브랜드: *{cosmetic['brand']}*")
                st.caption(cosmetic["description"])

                # 🔗 올리브영 검색 링크 생성하기 🔗
                # 실제 제품 페이지 링크는 제품 ID 등을 알아야 하지만,
                # 여기서는 제품명을 검색하는 링크로 대체했어요!
                search_query = cosmetic['name'].replace(" ", "+") # 공백을 +로 바꿔서 URL에 넣기
                oliveyoung_search_link = f"https://www.oliveyoung.co.kr/store/search/searchResult.do?query={search_query}"
                
                st.markdown(f"[올리브영에서 **{cosmetic['name']}** 찾아보기 🛒]({oliveyoung_search_link})")
                st.markdown("---") # 각 아이템 사이에 구분선 추가

    else:
        st.warning("아쉽지만, 해당 퍼스널 컬러에 맞는 추천 제품이 아직 없어요. 😢")

st.markdown("---")
st.markdown("개발 문의: **관능적인 맹꽁이** 🐸")


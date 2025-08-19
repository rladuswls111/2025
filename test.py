import streamlit as st

# ✨ 페이지 설정: 제목과 레이아웃을 미리 설정해서 깔끔하게 시작해요!
st.set_page_config(
    page_title="💖 나의 퍼스널 컬러 스타일 가이드 💖",
    layout="centered", # 웹 페이지 내용이 중앙에 정렬되도록
    initial_sidebar_state="expanded" # 사이드바가 기본적으로 열리도록
)

# 🤩 앱의 제목과 간단한 소개를 넣어볼까요?
st.title("🌈 나의 ✨관능적인✨ 퍼스널 컬러 스타일 가이드 🌈")
st.markdown("---") # 시각적인 구분을 위해 구분선을 넣어봤어요!

st.write(
    """
    안녕하세요, 창의적인몽구스5351님! 🥰
    나만의 **퍼스널 컬러**를 찾고, 그에 어울리는 **화장품 색상**과 **옷 코디** 팁을 알아보세요!
    아래에서 당신의 퍼스널 컬러 타입을 선택해 주세요.
    """
)

# 🎈 퍼스널 컬러 선택 박스를 만들어봐요!
personal_color_type = st.selectbox(
    "💖 당신의 퍼스널 컬러는 무엇인가요? 💖",
    ("퍼스널 컬러를 선택해주세요!", "봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"),
    index=0 # 초기에는 "퍼스널 컬러를 선택해주세요!"가 보이도록 설정
)

st.markdown("---")

# 🌷 선택된 퍼스널 컬러에 따라 다른 정보를 보여줄 거예요!

if personal_color_type == "퍼스널 컬러를 선택해주세요!":
    st.info("👆 위에 있는 드롭다운 메뉴에서 당신의 퍼스널 컬러를 선택해 주세요!")
    st.image("https://cdn.imweb.me/thumbnail/20200529/bca4bc192f49c.png", caption="퍼스널 컬러 진단은 자신을 더 빛나게 해줄 거예요!", use_container_width=True) # 이미지 추가!

elif personal_color_type == "봄 웜톤":
    st.subheader("🌷 봄 웜톤 (Spring Warm) 🌷")
    st.write("싱그럽고 발랄한, 생기 넘치는 봄의 기운을 담은 당신!")
    st.image("data:image/jpeg;base64,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", caption="봄 웜톤 이미지를 대표하는 사진이에요!", use_container_width=True) # 봄 웜톤 관련 이미지 예시
    st.markdown("---")

    st.markdown("#### 💄 어울리는 화장품 색상 (코스메틱) 💄")
    st.markdown(
        """
        -   **립:** 코랄, 피치, 살몬 핑크, 맑은 오렌지
        -   **아이섀도우:** 샴페인 골드, 피치 브라운, 코랄 브라운, 연한 옐로우
        -   **블러셔:** 피치, 코랄, 살구색
        -   **베이스:** 옐로우 베이스의 밝고 화사한 톤 (핑크 베이스는 자칫 노랗게 뜰 수 있어요!)
        """
    )
    st.markdown("💡 **팁:** 맑고 생기 있는 색상이 가장 잘 어울려요. 너무 진하거나 탁한 색은 피해주세요!")

    st.markdown("#### 👗 어울리는 옷 색상 및 스타일 (패션) 👗")
    st.markdown(
        """
        -   **의류:** 아이보리, 라이트 베이지, 코랄, 민트 그린, 베이비 블루, 옐로우, 연두색 등
        -   **악세사리:** 골드, 로즈골드, 맑은 보석 (시트린, 아쿠아마린)
        -   **스타일:** 꽃무늬, 물방울 무늬 등 발랄한 패턴, 하늘하늘한 소재
        """
    )
    st.markdown("💡 **팁:** 밝고 따뜻한 느낌을 주는 색상들을 적극적으로 활용해 보세요. 전체적으로 화사하고 러블리한 분위기를 연출할 수 있어요!")

elif personal_color_type == "여름 쿨톤":
    st.subheader("💧 여름 쿨톤 (Summer Cool) 💧")
    st.write("청량하고 우아한, 부드러운 여름의 냉기를 머금은 당신!")
    st.image("https://cdn.jsdelivr.net/gh/thesimplegithub/mycolor-hosting/images/summerMeta.png", caption="여름 쿨톤 이미지를 대표하는 사진이에요!", use_container_width=True) # 여름 쿨톤 관련 이미지 예시
    st.markdown("---")

    st.markdown("#### 💄 어울리는 화장품 색상 (코스메틱) 💄")
    st.markdown(
        """
        -   **립:** 푸시아 핑크, 라벤더 핑크, 말린 장미(MLBB 쿨톤), 플럼
        -   **아이섀도우:** 연한 그레이, 라벤더, 모브, 소프트 브라운 (회색빛 도는)
        -   **블러셔:** 딸기 우유 핑크, 연보라, 로즈 핑크
        -   **베이스:** 핑크 베이스의 화사하거나 차분한 톤
        """
    )
    st.markdown("💡 **팁:** 탁하지 않은 부드럽고 차분한 파스텔 톤의 색상이 좋아요. 너무 강하거나 쨍한 색은 피해주세요!")

    st.markdown("#### 👗 어울리는 옷 색상 및 스타일 (패션) 👗")
    st.markdown(
        """
        -   **의류:** 라이트 그레이, 스카이 블루, 라벤더, 베이비 핑크, 민트, 네이비, 화이트
        -   **악세사리:** 실버, 화이트 골드, 진주, 푸른빛 도는 보석 (사파이어, 아쿠아마린)
        -   **스타일:** 시폰, 레이스 등 부드러운 소재, 단정하고 우아한 디자인
        """
    )
    st.markdown("💡 **팁:** 시원하고 청량하면서도 부드러운 파스텔톤 컬러들이 당신의 매력을 더욱 돋보이게 할 거예요!")

elif personal_color_type == "가을 웜톤":
    st.subheader("🍂 가을 웜톤 (Autumn Warm) 🍂")
    st.write("성숙하고 깊이 있는, 그윽한 가을의 풍요로움을 담은 당신!")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmV23CKC6HkFikvXEkqfgqnfCob3Hr3seDkw&s", caption="가을 웜톤 이미지를 대표하는 사진이에요!", use_container_width=True) # 가을 웜톤 관련 이미지 예시
    st.markdown("---")

    st.markdown("#### 💄 어울리는 화장품 색상 (코스메틱) 💄")
    st.markdown(
        """
        -   **립:** 브릭 레드, 칠리, MLBB 코랄 브라운, 오렌지 브라운, 벽돌색
        -   **아이섀도우:** 카키, 올리브, 골드 브라운, 로즈 골드, 테라코타
        -   **블러셔:** 벽돌색, 누드 코랄, 오렌지 브라운
        -   **베이스:** 내추럴 베이지, 건강한 윤기가 도는 톤
        """
    )
    st.markdown("💡 **팁:** 깊이 있고 차분한 음영 컬러와 따뜻한 브라운 계열이 당신의 분위기를 더해줄 거예요. 밝고 쨍한 색은 피해주세요!")

    st.markdown("#### 👗 어울리는 옷 색상 및 스타일 (패션) 👗")
    st.markdown(
        """
        -   **의류:** 올리브 그린, 카키, 브릭 레드, 버건디, 머스타드 옐로우, 다크 브라운, 카멜, 블랙
        -   **악세사리:** 골드, 구리, 나무, 호박 보석 등 자연적인 소재
        -   **스타일:** 트위드, 니트, 스웨이드, 가죽 등 중후한 소재, 자연스럽고 우아한 디자인
        """
    )
    st.markdown("💡 **팁:** 따뜻하고 깊이 있는 자연의 색들이 당신의 지적이고 성숙한 매력을 한층 끌어올려 줄 거예요!")

elif personal_color_type == "겨울 쿨톤":
    st.subheader("❄️ 겨울 쿨톤 (Winter Cool) ❄️")
    st.write("시크하고 강렬한, 선명한 겨울의 카리스마를 지닌 당신!")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRAh4CBFM3K1Q2lWFifHq3QHP1Y6j4V4awQQ&s", caption="겨울 쿨톤 이미지를 대표하는 사진이에요!", use_container_width=True) # 겨울 쿨톤 관련 이미지 예시
    st.markdown("---")

    st.markdown("#### 💄 어울리는 화장품 색상 (코스메틱) 💄")
    st.markdown(
        """
        -   **립:** 비비드 푸시아 핑크, 버건디, 체리 레드, 플럼, 와인
        -   **아이섀도우:** 차콜 그레이, 블랙, 화이트, 쿨톤 브라운 (회색빛 도는 진한)
        -   **블러셔:** 쿨 핑크, 버건디
        -   **베이스:** 창백하리만치 깨끗한 핑크 베이스 or 잿빛이 도는 쿨 베이스
        """
    )
    st.markdown("💡 **팁:** 선명하고 대비감이 강한 색상이 잘 어울려요. 탁하거나 따뜻한 색은 피해주세요!")

    st.markdown("#### 👗 어울리는 옷 색상 및 스타일 (패션) 👗")
    st.markdown(
        """
        -   **의류:** 순백색, 블랙, 로얄 블루, 비비드 핑크, 에메랄드 그린, 버건디, 차콜 그레이
        -   **악세사리:** 실버, 플래티넘, 다이아몬드, 블랙 오닉스 등 반짝이고 선명한 소재
        -   **스타일:** 모던하고 심플한 디자인, 과감한 패턴, 시크한 느낌의 의상
        """
    )
    st.markdown("💡 **팁:** 명료하고 대비가 강한 색상 조합은 당신의 독특하고 시크한 매력을 더욱 돋보이게 만들 거예요!")

# 😊 하단 푸터 (선택 사항)
st.markdown("---")
st.markdown("##### ✨ 퍼스널 컬러와 함께 당신의 아름다움을 더욱 빛내세요! ✨")
st.markdown("###### Made with ❤️ by 관능적인 맹꽁이")

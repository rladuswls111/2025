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
    st.image("https://cdn.jsdelivr.net/gh/thesimplegithub/mycolor-hosting/images/springMeta.png", caption="봄 웜톤 이미지를 대표하는 사진이에요!", use_container_width=True) # 봄 웜톤 관련 이미지 예시
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

import streamlit as st
import time
import random

# 페이지 설정
st.set_page_config(page_title="반응속도 측정기", page_icon="⚡", layout="centered")

st.title("⚡ 반응속도 측정기")
st.write("초록색으로 바뀌는 순간 버튼을 클릭하세요!")

# 세션 상태 초기화 (Streamlit은 매번 코드를 다시 실행하므로 상태 저장 필요)
if "state" not in st.session_state:
    st.session_state.state = "waiting"   # waiting, ready, go, result
if "start_time" not in st.session_state:
    st.session_state.start_time = 0
if "target_time" not in st.session_state:
    st.session_state.target_time = 0
if "reaction_time" not in st.session_state:
    st.session_state.reaction_time = 0
if "records" not in st.session_state:
    st.session_state.records = []  # 기록 저장 리스트

# 상태에 따른 화면 표시
state = st.session_state.state

# 색상 박스 표시 영역
box_placeholder = st.empty()

if state == "waiting":
    box_placeholder.markdown(
        """
        <div style='background-color:#e74c3c; height:300px; border-radius:20px;
                    display:flex; justify-content:center; align-items:center;
                    color:white; font-size:28px; font-weight:bold;'>
            아래 '시작' 버튼을 누르세요!
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button("🎮 시작하기", use_container_width=True):
        # 1~5초 사이 랜덤 대기 시간 설정
        delay = random.uniform(1.0, 5.0)
        st.session_state.target_time = time.time() + delay
        st.session_state.state = "ready"
        st.rerun()

elif state == "ready":
    # 아직 대기 시간이 안 됨
    if time.time() < st.session_state.target_time:
        box_placeholder.markdown(
            """
            <div style='background-color:#f39c12; height:300px; border-radius:20px;
                        display:flex; justify-content:center; align-items:center;
                        color:white; font-size:28px; font-weight:bold;'>
                ⏳ 초록색이 될 때까지 기다리세요...
            </div>
            """,
            unsafe_allow_html=True
        )
        
        if st.button("클릭! (너무 빨리 누르지 마세요)", use_container_width=True):
            st.session_state.state = "too_early"
            st.rerun()
        
        # 화면 자동 갱신을 위해 잠시 대기 후 rerun
        time.sleep(0.1)
        st.rerun()
    else:
        # 초록색으로 전환
        st.session_state.start_time = time.time()
        st.session_state.state = "go"
        st.rerun()

elif state == "go":
    box_placeholder.markdown(
        """
        <div style='background-color:#2ecc71; height:300px; border-radius:20px;
                    display:flex; justify-content:center; align-items:center;
                    color:white; font-size:40px; font-weight:bold;'>
            🟢 지금 클릭!
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button("⚡ 클릭!", use_container_width=True, type="primary"):
        end_time = time.time()
        reaction_time = int((end_time - st.session_state.start_time) * 1000)
        st.session_state.reaction_time = reaction_time
        st.session_state.records.append(reaction_time)
        st.session_state.state = "result"
        st.rerun()

elif state == "too_early":
    box_placeholder.markdown(
        """
        <div style='background-color:#c0392b; height:300px; border-radius:20px;
                    display:flex; justify-content:center; align-items:center;
                    color:white; font-size:28px; font-weight:bold;'>
            ❌ 너무 빨라요! 다시 시도하세요.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button("🔄 다시 시도", use_container_width=True):
        st.session_state.state = "waiting"
        st.rerun()

elif state == "result":
    rt = st.session_state.reaction_time
    
    # 반응속도에 따른 평가 메시지
    if rt < 200:
        message = "🏆 놀라워요! 프로 게이머급!"
        color = "#9b59b6"
    elif rt < 300:
        message = "🥇 매우 빠른 반응속도!"
        color = "#3498db"
    elif rt < 400:
        message = "🥈 평균 이상이에요!"
        color = "#2ecc71"
    elif rt < 500:
        message = "🥉 평균 수준이에요."
        color = "#f39c12"
    else:
        message = "💪 조금 더 연습해봐요!"
        color = "#e67e22"
    
    box_placeholder.markdown(
        f"""
        <div style='background-color:{color}; height:300px; border-radius:20px;
                    display:flex; flex-direction:column; justify-content:center; align-items:center;
                    color:white; font-size:32px; font-weight:bold;'>
            ⏱️ {rt} ms<br>
            <span style='font-size:22px;'>{message}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button("🔄 다시 도전!", use_container_width=True):
        st.session_state.state = "waiting"
        st.rerun()

# 기록 표시
st.markdown("---")
if st.session_state.records:
    st.subheader("📊 나의 기록")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("최고 기록", f"{min(st.session_state.records)} ms")
    with col2:
        avg = sum(st.session_state.records) // len(st.session_state.records)
        st.metric("평균", f"{avg} ms")
    with col3:
        st.metric("시도 횟수", f"{len(st.session_state.records)}회")
    
    # 최근 기록 5개 표시
    st.write("**최근 기록:**")
    recent = st.session_state.records[-5:][::-1]
    for i, record in enumerate(recent, 1):
        st.write(f"{i}. {record} ms")
    
    if st.button("🗑️ 기록 초기화"):
        st.session_state.records = []
        st.rerun()

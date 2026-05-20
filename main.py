import time

def on_button_click():
    # 1. 측정 시작 (초 단위로 반환됨)
    start_time = time.perf_counter()
    
    # ---------------------------------------------
    # 2. 여기에 반응 속도를 측정하고 싶은 앱 로직을 넣으세요.
    # 예: 데이터베이스 조회, 이미지 처리, API 호출 등
    print("앱 로직 수행 중...")
    time.sleep(0.123)  # 데모를 위한 0.123초 대기
    # ---------------------------------------------
    
    # 3. 측정 종료
    end_time = time.perf_counter()
    
    # 4. 결과 계산 (초 단위 -> 밀리초(ms) 단위로 변환)
    duration_ms = (end_time - start_time) * 1000
    
    print(f"⏱️ 반응 속도: {duration_ms:.2f} ms")
    
    if duration_ms > 200:
        print("⚠️ 경고: 반응 속도가 200ms를 넘었습니다. 사용자가 느리다고 느낄 수 있습니다.")

# 테스트 실행
on_button_click()

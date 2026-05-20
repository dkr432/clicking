import time
import random
import statistics

def reaction_test():
    results = []
    
    print("=" * 40)
    print("       반응속도 테스트")
    print("=" * 40)
    print("초록색 신호가 뜨면 Enter를 누르세요!\n")
    
    rounds = int(input("몇 번 테스트할까요? (기본 5): ") or 5)
    print()
    
    for i in range(rounds):
        print(f"[{i+1}/{rounds}] 준비하세요...", end="", flush=True)
        
        delay = random.uniform(1.5, 4.0)
        time.sleep(delay)
        
        print("\r🟢 지금 Enter!")
        start = time.perf_counter()
        
        try:
            input()
        except KeyboardInterrupt:
            print("\n테스트 중단됨")
            break
        
        elapsed = (time.perf_counter() - start) * 1000  # ms 변환
        results.append(elapsed)
        
        if elapsed < 200:
            grade = "⚡ 엄청 빠르네요!"
        elif elapsed < 280:
            grade = "👍 빠른 편이에요"
        elif elapsed < 380:
            grade = "😊 보통이에요"
        else:
            grade = "🐢 조금 느린 편이에요"
        
        print(f"   → {elapsed:.1f} ms  {grade}\n")
    
    if not results:
        return
    
    print("=" * 40)
    print("           결과 요약")
    print("=" * 40)
    print(f"  시도 횟수 : {len(results)}회")
    print(f"  최고 기록 : {min(results):.1f} ms")
    print(f"  최저 기록 : {max(results):.1f} ms")
    print(f"  평  균    : {statistics.mean(results):.1f} ms")
    if len(results) > 1:
        print(f"  표준편차  : {statistics.stdev(results):.1f} ms")
    print("=" * 40)
    
    print("\n📊 기록 막대그래프")
    max_ms = max(results)
    for idx, ms in enumerate(results, 1):
        bar_len = int((ms / max_ms) * 30)
        bar = "█" * bar_len
        print(f"  {idx}회차 | {bar:<30} {ms:.1f} ms")

if __name__ == "__main__":
    reaction_test()

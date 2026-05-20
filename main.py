import tkinter as tk
import time
import random

class ReactionTimeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("반응속도 측정기")
        self.root.geometry("500x500")
        
        self.state = "waiting"  # waiting, ready, go
        self.start_time = 0
        
        # 메인 버튼 (전체 화면 영역)
        self.button = tk.Button(
            root,
            text="클릭해서 시작하세요!",
            font=("Arial", 20),
            bg="red",
            fg="white",
            command=self.on_click
        )
        self.button.pack(expand=True, fill="both", padx=20, pady=20)
        
        # 결과 표시 라벨
        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 16)
        )
        self.result_label.pack(pady=10)
    
    def on_click(self):
        if self.state == "waiting":
            # 대기 상태로 전환
            self.button.config(bg="orange", text="초록색이 되면 클릭하세요!")
            self.state = "ready"
            # 1~5초 사이 랜덤 대기
            delay = random.randint(1000, 5000)
            self.root.after(delay, self.show_green)
        
        elif self.state == "ready":
            # 너무 빨리 클릭한 경우
            self.button.config(bg="red", text="너무 빨라요! 다시 시도하세요.")
            self.state = "waiting"
        
        elif self.state == "go":
            # 반응속도 계산
            end_time = time.time()
            reaction_time = int((end_time - self.start_time) * 1000)
            self.button.config(bg="red", text="다시 시도하기")
            self.result_label.config(text=f"당신의 반응속도: {reaction_time}ms")
            self.state = "waiting"
    
    def show_green(self):
        if self.state == "ready":
            self.button.config(bg="green", text="클릭!")
            self.start_time = time.time()
            self.state = "go"

if __name__ == "__main__":
    root = tk.Tk()
    app = ReactionTimeApp(root)
    root.mainloop()

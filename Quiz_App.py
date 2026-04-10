import tkinter as tk
import random

# ---------------- QUESTIONS ---------------- #
questions = [
    {"q": "Python function keyword?", "opt": ["func","define","def","function"], "ans": 2},
    {"q": "File extension of Python?", "opt": [".pyth",".pt",".pyt",".py"], "ans": 3},
    {"q": "Immutable type?", "opt": ["List","Dict","Tuple","Set"], "ans": 2},
    {"q": "2 ** 3 = ?", "opt": ["6","8","9","5"], "ans": 1},
    {"q": "'10' + '20' = ?", "opt": ["30","1020","Error","None"], "ans": 1},
]
# ---------------- APP ---------------- #
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        # 👉 हर बार नए order के लिए यहाँ shuffle
        self.questions = random.sample(questions, len(questions))

        self.qn = 0
        self.score = 0

        self.q_label = tk.Label(root, font=("Arial", 14), wraplength=400)
        self.q_label.pack(pady=20)

        self.var = tk.IntVar()

        self.buttons = []
        for i in range(4):
            btn = tk.Radiobutton(root, variable=self.var, value=i, font=("Arial", 12))
            btn.pack(anchor="w")
            self.buttons.append(btn)

        self.next_btn = tk.Button(root, text="Next", command=self.next_q)
        self.next_btn.pack(pady=20)

        self.show_q()

    def show_q(self):
        q = self.questions[self.qn]
        self.q_label.config(text=f"Q{self.qn+1}: {q['q']}")
        self.var.set(-1)

        for i, opt in enumerate(q["opt"]):
            self.buttons[i].config(text=opt)

    def next_q(self):
        if self.var.get() == self.questions[self.qn]["ans"]:
            self.score += 1

        self.qn += 1

        if self.qn < len(self.questions):
            self.show_q()
        else:
            self.show_result()

    def show_result(self):
        for w in self.root.winfo_children():
            w.destroy()

        tk.Label(self.root, text=f"Score: {self.score}/{len(self.questions)}",
                 font=("Arial", 16)).pack(pady=30)

        tk.Button(self.root, text="Exit", command=self.root.quit).pack()

# ---------------- RUN ---------------- #
root = tk.Tk()
root.geometry("400x300")
app = QuizApp(root)
root.mainloop()
import tkinter as tk
from tkinter import messagebox

# Corrected question data with proper syntax
questions = [
    {"question": "Who is the Prime Minister in 2024?", "options": ["Narendra Modi", "Rahul Gandhi", "Amit Shah", "Arvind Kejriwal"], "answer": "Narendra Modi"},
    {"question": "What is 8 + 6 - 2?", "options": ["0", "8", "5", "6"], "answer": "12"},
    {"question": "What is the color of the Ashoka Chakra?", "options": ["Dark Blue", "Green", "Red", "Yellow"], "answer": "Dark Blue"},
    {"question": "Who is a famous football player in India?", "options": ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Sunil Chhetri"], "answer": "Sunil Chhetri"}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Platform")
        self.root.geometry("400x300")
        self.root.config(bg="blue")
        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="", wraplength=300, justify="center", bg="blue", fg="white")
        self.question_label.pack(pady=20)

        self.options = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.options, value="", wraplength=300, justify="center", bg="blue", fg="white", selectcolor="blue")
            rb.pack(anchor="w", padx=20, pady=5)
            self.radio_buttons.append(rb)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, bg="white", fg="blue")
        self.submit_button.pack(pady=20)

        self.result_label = tk.Label(root, text="", wraplength=300, justify="center", bg="blue", fg="white")
        self.result_label.pack(pady=20)

        self.display_question()

    def display_question(self):
        if self.current_question < len(questions):
            q = questions[self.current_question]
            self.question_label.config(text=q["question"])
            for i, option in enumerate(q["options"]):
                self.radio_buttons[i].config(text=option, value=option)
            self.options.set(None)
        else:
            self.display_result()

    def check_answer(self):
        selected_option = self.options.get()
        if selected_option == questions[self.current_question]["answer"]:
            self.score += 1
        self.current_question += 1
        self.display_question()

    def display_result(self):
        self.question_label.config(text="")
        for rb in self.radio_buttons:
            rb.pack_forget()
        self.submit_button.pack_forget()
        self.result_label.config(text=f"Quiz Over! Your score is {self.score}/{len(questions)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

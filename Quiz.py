from tkinter import*
from tkinter import messagebox as mb
import json

class Quiz:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x450")
        self.window.title("Liverpool FC Quiz")

        with open('data.json') as f:
            data = json.load(f)

        self.question = (data['question'])
        self.options = (data['options'])
        self.answer = (data['answer'])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    quiz = Quiz()
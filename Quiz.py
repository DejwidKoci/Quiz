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

        self.q_number = 0
        self.display_title()
        self.display_question()

        self.run()



    def display_title(self):
        self.title = Label(self.window, text = "LIVERPOOL FC QUIZ", width = 50, bg = "red",
                      fg = "white", font = ("ariel", 20, "bold"))
        self.title.place(x = 0, y = 2)

    def display_question(self):
        
        self.dis_question = Label(self.window, text = self.question[self.q_number], width = 60,
                                font=("ariel" ,16, "bold" ), anchor = 'w' )
         
        self.dis_question.place(x = 70, y = 100)



    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    quiz = Quiz()
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

        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()

        self.buttons()
        self.data_size = len(self.question)

        self.correct = 0

        self.run()


    def display_title(self):
        self.title = Label(self.window, text = "LIVERPOOL FC QUIZ", width = 50, bg = "red",
                      fg = "white", font = ("ariel", 20, "bold"))
        self.title.place(x = 0, y = 2)

    def display_question(self):
        
        self.dis_question = Label(self.window, text = self.question[self.q_number], width = 60,
                                font=("ariel" ,16, "bold" ), anchor = 'w' )
         
        self.dis_question.place(x = 70, y = 100)

    def radio_buttons(self):
         
        q_list = []
        y_pos = 180
         
        while len(q_list) < 4:
             
            radio_btn = Radiobutton(self.window, text=" ", variable = self.opt_selected,
            value = len(q_list) + 1, font = ("ariel", 14))
             
            q_list.append(radio_btn)
             
            radio_btn.place(x = 100, y = y_pos)
            y_pos += 40
        
        return q_list

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
         
        for option in self.options[self.q_number]:
            self.opts[val]['text'] = option
            val += 1

    def buttons(self):
         
        next_button = Button(self.window, text = "Next", command = self.next_btn,
        width = 10, bg = "blue", fg = "white", font = ("ariel", 16, "bold"))
         
        next_button.place(x = 350, y = 380)
         
        quit_button = Button(self.window, text = "Quit", command = self.window.destroy,
        width = 5, bg = "black", fg = "white", font = ("ariel",16," bold"))
         
        quit_button.place(x = 700, y = 50)    

    def next_btn(self):
         
        if self.check_ans(self.q_number):
            self.correct += 1
         
        self.q_number += 1
         
        if self.q_number == self.data_size:
            self.display_result()
            self.window.destroy()
        else:
            self.dis_question.destroy()
            self.display_question()
            self.display_options()

    def check_ans(self, q_number):
         
        if self.opt_selected.get() == self.answer[q_number]:
            return True

    def display_result(self):
         
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
         
        mb.showinfo("Result", f"{result} \n {correct} \n {wrong}")
    

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    quiz = Quiz()
from tkinter import Tk, Label, StringVar
from tkinter.messagebox import showinfo
from customtkinter import CTkRadioButton, CTkButton
import mcq_data


class MCQquiz:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x400+200+100')
        self.root.title('Multiple Choice Question')
        self.root.configure(background='#99ffff')

        self.questions = mcq_data.questions
        self.current_question = 0
        self.score = 0

        self.question_label = Label(self.root, text='', padx=10, pady=10, font=('Arial', 18), bg='orange')
        self.question_label.place(x=170, y=30)

        self.answerVar = StringVar()
        self.option_btns = []

        for i in range(4):
            button = CTkRadioButton(self.root, text='',
                                    variable=self.answerVar, 
                                    value=i,
                                    text_color='black',
                                    font=('Roboto', 18),
                                    hover_color='green',
                                    border_width_checked=8,
                                    border_color='green',
                                    corner_radius=10
                                    )
            button.configure(text=self.questions[self.current_question]['options'][i])
            self.option_btns.append(button)

        self.option_btns[0].place(x=200, y=100)
        self.option_btns[1].place(x=200, y=140)
        self.option_btns[2].place(x=200, y=180)
        self.option_btns[3].place(x=200, y=220)

        self.next_btn = CTkButton(self.root, text='Next',
                                 font=('Arial', 20, 'bold'),
                                 width=300, height=40,
                                 corner_radius=8,
                                 hover_color='blue',
                                 command=self.check_answer)
        self.next_btn.place(x=250, y=300)
        
        
        self.show_question()

    def check_answer(self):
        selected_answer = self.answerVar.get()
        
        if selected_answer == '':
            # Show an error message or take appropriate action
            root.lift()
            showinfo('quiz', 'Please Select an Option!', parent=root)
            return
        
        selected_answer = int(selected_answer)
        correct_answer_index = self.questions[self.current_question]['options'].index(self.questions[self.current_question]['correct_answer'])
        
        if selected_answer == correct_answer_index:
            self.score += 1
        
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_question(self):
        self.question_label.config(text=f"{self.current_question + 1}. {self.questions[self.current_question]['question']}")
        
        for i in range(4):
            self.option_btns[i].configure(text=self.questions[self.current_question]['options'][i])

        self.answerVar.set('')

    def show_result(self):
        self.question_label.config(text=f'Quiz completed! Your score: {self.score}/{len(self.questions)}')
        self.next_btn.configure(state='disabled')
        
        for button in self.option_btns:
            button.configure(state='disabled')


if __name__ == '__main__':
    root = Tk()
    mcq_app = MCQquiz(root)
    root.mainloop()

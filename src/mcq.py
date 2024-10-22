from tkinter import Tk, Label, StringVar
from tkinter.messagebox import showinfo
from customtkinter import CTkRadioButton, CTkButton
import mcq_data


class MCQquiz:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x400+200+100')
        self.root.title('Multiple Choice Question')
        self.root.configure(background='#1e1e1e')  # Dark background

        self.questions = mcq_data.questions
        self.current_question = 0
        self.score = 0

        self.question_label = Label(self.root, text='', padx=10, pady=10, font=('Arial', 18), bg='#2e2e2e', fg='white')
        self.question_label.place(x=170, y=30)

        self.answerVar = StringVar()
        self.option_btns = []

        for i in range(4):
            button = CTkRadioButton(self.root, text='',
                                    variable=self.answerVar, 
                                    value=i,
                                    text_color='white',
                                    font=('Roboto', 16),
                                    hover_color='green',
                                    border_width_checked=10,
                                    border_color='blue',
                                    corner_radius=10
                                    )
            self.option_btns.append(button)
        
        # Position the buttons in a loop
        for i in range(4):
            self.option_btns[i].place(x=200, y=100 + i * 40)

        self.next_btn = CTkButton(self.root, text='Next',
                                   font=('Arial', 20, 'bold'),
                                   width=300, height=40,
                                   corner_radius=8,
                                   hover_color='#007acc',
                                   command=self.check_answer)
        self.next_btn.place(x=250, y=300)

        self.show_question()

    def check_answer(self):
        selected_answer = self.answerVar.get()

        if selected_answer == '':
            self.root.lift()
            showinfo('Quiz', 'Please Select an Option!', parent=self.root)
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

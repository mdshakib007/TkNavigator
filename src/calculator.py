from tkinter import Tk
from customtkinter import CTkEntry, CTkButton

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x700+700+100')
        self.root.title("Calculator")
        self.root.configure(background='#111')
        self.root.resizable(False, False)

        self.create_display()
        self.create_buttons()
        self.root.mainloop()

    def create_display(self):
        self.output_display = CTkEntry(self.root, width=380, height=80,
                                       fg_color='black',
                                       bg_color='black',
                                       corner_radius=0,
                                       text_color='white',
                                       border_width=1,
                                       border_color='black',
                                       font=('Arial', 26, 'bold'))
        self.output_display.place(x=10, y=10)

        self.input_display = CTkEntry(self.root, width=380, height=80,
                                      fg_color='black',
                                      bg_color='black',
                                      corner_radius=0,
                                      text_color='white',
                                      border_color='black',
                                      border_width=1,
                                      font=('Arial', 36, 'bold'))
        self.input_display.place(x=10, y=70)

    def create_buttons(self):
        buttons = [
            ('C', self.cut_one, 0, 200, 'grey'),
            ('%', self.insert_mod, 100, 200, 'grey'),
            ('^', self.insert_pow, 200, 200, 'grey'),
            ('÷', self.insert_div, 300, 200, 'orange'),
            ('7', self.insert_seven, 0, 300, 'skyblue'),
            ('8', self.insert_eight, 100, 300, 'skyblue'),
            ('9', self.insert_nine, 200, 300, 'skyblue'),
            ('×', self.insert_mul, 300, 300, 'orange'),
            ('4', self.insert_four, 0, 400, 'skyblue'),
            ('5', self.insert_five, 100, 400, 'skyblue'),
            ('6', self.insert_six, 200, 400, 'skyblue'),
            ('−', self.insert_sub, 300, 400, 'orange'),
            ('1', self.insert_one, 0, 500, 'skyblue'),
            ('2', self.insert_two, 100, 500, 'skyblue'),
            ('3', self.insert_three, 200, 500, 'skyblue'),
            ('+', self.insert_plus, 300, 500, 'orange'),
            ('AC', self.clear_all, 0, 600, 'red'),
            ('0', self.insert_zero, 100, 600, 'skyblue'),
            ('.', self.insert_dot, 200, 600, 'skyblue'),
            ('=', self.result_output, 300, 600, 'orange')
        ]

        for (text, command, x, y, color) in buttons:
            CTkButton(self.root, text=text,
                      font=('Roboto', 35),
                      width=99, height=99,
                      corner_radius=0,
                      text_color='white' if color != 'skyblue' else 'black',
                      fg_color=color,
                      hover_color='grey40',
                      bg_color='#111',
                      command=command).place(x=x, y=y)

    ## Commands
    def cut_one(self):
        current = self.input_display.get()
        self.input_display.delete(0, 'end')
        self.input_display.insert('end', current[:-1])

    def insert_mod(self):
        self.input_display.insert('end', '%')

    def insert_pow(self):
        self.input_display.insert('end', '^')

    def insert_div(self):
        self.input_display.insert('end', '÷')

    def insert_seven(self):
        self.input_display.insert('end', '7')

    def insert_eight(self):
        self.input_display.insert('end', '8')

    def insert_nine(self):
        self.input_display.insert('end', '9')

    def insert_mul(self):
        self.input_display.insert('end', '×')

    def insert_four(self):
        self.input_display.insert('end', '4')

    def insert_five(self):
        self.input_display.insert('end', '5')

    def insert_six(self):
        self.input_display.insert('end', '6')

    def insert_sub(self):
        self.input_display.insert('end', '−')

    def insert_one(self):
        self.input_display.insert('end', '1')

    def insert_two(self):
        self.input_display.insert('end', '2')

    def insert_three(self):
        self.input_display.insert('end', '3')

    def insert_dot(self):
        self.input_display.insert('end', '.')

    def insert_plus(self):
        self.input_display.insert('end', '+')

    def insert_zero(self):
        self.input_display.insert('end', '0')

    def clear_all(self):
        self.input_display.delete(0, 'end')

    def result_output(self):
        content = self.input_display.get()
        content = content.replace('×', '*').replace('÷', '/').replace('^', '**').replace('−', '-')
        
        try:
            result = eval(content)
            self.output_display.delete(0, 'end')
            self.output_display.insert('end', result)
        except:
            self.output_display.delete(0, 'end')
            self.output_display.insert('end', 'Expression Error')

if __name__ == '__main__':
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()

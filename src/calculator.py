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
        clear = CTkButton(self.root, text='C',
                              font=('Roboto', 26, 'bold'),
                              width=99, height=99,
                              corner_radius=0,
                              text_color='white',
                              fg_color='grey',
                              hover=False,
                              bg_color='#111',
                              command=self.cut_one)
        clear.place(x=0, y=200)

        modulus = CTkButton(self.root, text='%',
                                font=('Roboto', 26, 'bold'),
                                width=99, height=99,
                                corner_radius=0,
                                text_color='white',
                                fg_color='grey',
                                hover=False,
                                bg_color='#111',
                                command=self.insert_mod)
        modulus.place(x=100, y=200)

        power = CTkButton(self.root, text='^',
                              font=('Roboto', 26, 'bold'),
                              width=99, height=99,
                              corner_radius=0,
                              text_color='white',
                              fg_color='grey',
                              hover=False,
                              bg_color='#111',
                              command=self.insert_pow)
        power.place(x=200, y=200)

        div = CTkButton(self.root, text='/',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='white',
                            fg_color='orange',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_div)
        div.place(x=300, y=200)

        seven = CTkButton(self.root, text='7',
                              font=('Roboto', 26, 'bold'),
                              width=99, height=99,
                              corner_radius=0,
                              text_color='black',
                              fg_color='skyblue',
                              hover=False,
                              bg_color='#111',
                              command=self.insert_seven)
        seven.place(x=0, y=300)

        eight = CTkButton(self.root, text='8',
                              font=('Roboto', 26, 'bold'),
                              width=99, height=99,
                              corner_radius=0,
                              text_color='black',
                              fg_color='skyblue',
                              hover=False,
                              bg_color='#111',
                              command=self.insert_eight)
        eight.place(x=100, y=300)

        nine = CTkButton(self.root, text='9',
                             font=('Roboto', 26, 'bold'),
                             width=99, height=99,
                             corner_radius=0,
                             text_color='black',
                             fg_color='skyblue',
                             hover=False,
                             bg_color='#111',
                             command=self.insert_nine)
        nine.place(x=200, y=300)

        mul = CTkButton(self.root, text='*',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='white',
                            fg_color='orange',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_mul)
        mul.place(x=300, y=300)

        four = CTkButton(self.root, text='4',
                             font=('Roboto', 26, 'bold'),
                             width=99, height=99,
                             corner_radius=0,
                             text_color='black',
                             fg_color='skyblue',
                             hover=False,
                             bg_color='#111',
                             command=self.insert_four)
        four.place(x=0, y=400)

        five = CTkButton(self.root, text='5',
                             font=('Roboto', 26, 'bold'),
                             width=99, height=99,
                             corner_radius=0,
                             text_color='black',
                             fg_color='skyblue',
                             hover=False,
                             bg_color='#111',
                             command=self.insert_five)
        five.place(x=100, y=400)

        six = CTkButton(self.root, text='6',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='black',
                            fg_color='skyblue',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_six)
        six.place(x=200, y=400)

        sub = CTkButton(self.root, text='-',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='white',
                            fg_color='orange',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_sub)
        sub.place(x=300, y=400)

        one = CTkButton(self.root, text='1',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='black',
                            fg_color='skyblue',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_one)
        one.place(x=0, y=500)

        two = CTkButton(self.root, text='2',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='black',
                            fg_color='skyblue',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_two)
        two.place(x=100, y=500)

        three = CTkButton(self.root, text='3',
                              font=('Roboto', 26, 'bold'),
                              width=99, height=99,
                              corner_radius=0,
                              text_color='black',
                              fg_color='skyblue',
                              hover=False,
                              bg_color='#111',
                              command=self.insert_three)
        three.place(x=200, y=500)

        plus = CTkButton(self.root, text='+',
                             font=('Roboto', 26, 'bold'),
                             width=99, height=99,
                             corner_radius=0,
                             text_color='white',
                             fg_color='orange',
                             hover=False,
                             bg_color='#111',
                             command=self.insert_plus)
        plus.place(x=300, y=500)

        all_clear = CTkButton(self.root, text='AC',
                                  font=('Roboto', 26, 'bold'),
                                  width=99, height=99,
                                  corner_radius=0,
                                  text_color='black',
                                  fg_color='red',
                                  hover=False,
                                  bg_color='#111',
                                  command=self.clear_all)
        all_clear.place(x=0, y=600)

        zero = CTkButton(self.root, text='0',
                             font=('Roboto', 26, 'bold'),
                             width=99, height=99,
                             corner_radius=0,
                             text_color='black',
                             fg_color='skyblue',
                             hover=False,
                             bg_color='#111',
                             command=self.insert_zero)
        zero.place(x=100, y=600)

        dot = CTkButton(self.root, text='.',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='black',
                            fg_color='skyblue',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_dot)
        dot.place(x=200, y=600)

        equal = CTkButton(self.root, text='=',
                              font=('Roboto', 35),
                              width=99, height=99,
                              corner_radius=0,
                              text_color='white',
                              fg_color='orange',
                              hover=False,
                              bg_color='#111',
                              command=self.result_output)
        equal.place(x=300, y=600)



    ## commands
    def cut_one(self):
        current = self.input_display.get()
        self.input_display.delete(0, 'end')
        self.input_display.insert('end', current[:-1])

    def insert_mod(self):
        self.input_display.insert('end', '%')

    def insert_pow(self):
        self.input_display.insert('end', '**')

    def insert_div(self):
        self.input_display.insert('end', '/')

    def insert_seven(self):
        self.input_display.insert('end', '7')

    def insert_eight(self):
        self.input_display.insert('end', '8')

    def insert_nine(self):
        self.input_display.insert('end', '9')

    def insert_mul(self):
        self.input_display.insert('end', '*')

    def insert_four(self):
        self.input_display.insert('end', '4')

    def insert_five(self):
        self.input_display.insert('end', '5')

    def insert_six(self):
        self.input_display.insert('end', '6')

    def insert_sub(self):
        self.input_display.insert('end', '-')

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


from tkinter import *
import customtkinter as ctk


class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x700+700+100')
        self.root.title("Calculator")
        self.root.configure(background='#111')
        self.root.resizable(False, False)

        self.create_display()
        self.create_buttons()

        self.root.mainloop()

    def create_display(self):
        self.output_display = ctk.CTkEntry(self.root, width=380, height=80,
                                           fg_color='black',
                                           bg_color='black',
                                           corner_radius=0,
                                           text_color='white',
                                           border_width=1,
                                           border_color='black',
                                           font=('Arial', 26, 'bold'))
        self.output_display.place(x=10, y=10)

        self.input_display = ctk.CTkEntry(self.root, width=380, height=80,
                                          fg_color='black',
                                          bg_color='black',
                                          corner_radius=0,
                                          text_color='white',
                                          border_color='black',
                                          border_width=1,
                                          font=('Arial', 36, 'bold'))
        self.input_display.place(x=10, y=70)

    def create_buttons(self):
        clear = ctk.CTkButton(self.root, text='C',
                              font=('Roboto', 26, 'bold'),
                              width=99, height=99,
                              corner_radius=0,
                              text_color='white',
                              fg_color='grey',
                              hover=False,
                              bg_color='#111',
                              command=self.cut_one)
        clear.place(x=0, y=200)

        modulus = ctk.CTkButton(self.root, text='%',
                                font=('Roboto', 26, 'bold'),
                                width=99, height=99,
                                corner_radius=0,
                                text_color='white',
                                fg_color='grey',
                                hover=False,
                                bg_color='#111',
                                command=self.insert_mod)
        modulus.place(x=100, y=200)

        power = ctk.CTkButton(self.root, text='^',
                              font=('Roboto', 26, 'bold'),
                              width=99, height=99,
                              corner_radius=0,
                              text_color='white',
                              fg_color='grey',
                              hover=False,
                              bg_color='#111',
                              command=self.insert_pow)
        power.place(x=200, y=200)

        div = ctk.CTkButton(self.root, text='/',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='white',
                            fg_color='orange',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_div)
        div.place(x=300, y=200)

        seven = ctk.CTkButton(self.root, text='7',
                              font=('Roboto', 26, 'bold'),
                              width=99, height=99,
                              corner_radius=0,
                              text_color='black',
                              fg_color='skyblue',
                              hover=False,
                              bg_color='#111',
                              command=self.insert_seven)
        seven.place(x=0, y=300)

        eight = ctk.CTkButton(self.root, text='8',
                              font=('Roboto', 26, 'bold'),
                              width=99, height=99,
                              corner_radius=0,
                              text_color='black',
                              fg_color='skyblue',
                              hover=False,
                              bg_color='#111',
                              command=self.insert_eight)
        eight.place(x=100, y=300)

        nine = ctk.CTkButton(self.root, text='9',
                             font=('Roboto', 26, 'bold'),
                             width=99, height=99,
                             corner_radius=0,
                             text_color='black',
                             fg_color='skyblue',
                             hover=False,
                             bg_color='#111',
                             command=self.insert_nine)
        nine.place(x=200, y=300)

        mul = ctk.CTkButton(self.root, text='*',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='white',
                            fg_color='orange',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_mul)
        mul.place(x=300, y=300)

        four = ctk.CTkButton(self.root, text='4',
                             font=('Roboto', 26, 'bold'),
                             width=99, height=99,
                             corner_radius=0,
                             text_color='black',
                             fg_color='skyblue',
                             hover=False,
                             bg_color='#111',
                             command=self.insert_four)
        four.place(x=0, y=400)

        five = ctk.CTkButton(self.root, text='5',
                             font=('Roboto', 26, 'bold'),
                             width=99, height=99,
                             corner_radius=0,
                             text_color='black',
                             fg_color='skyblue',
                             hover=False,
                             bg_color='#111',
                             command=self.insert_five)
        five.place(x=100, y=400)

        six = ctk.CTkButton(self.root, text='6',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='black',
                            fg_color='skyblue',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_six)
        six.place(x=200, y=400)

        sub = ctk.CTkButton(self.root, text='-',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='white',
                            fg_color='orange',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_sub)
        sub.place(x=300, y=400)

        one = ctk.CTkButton(self.root, text='1',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='black',
                            fg_color='skyblue',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_one)
        one.place(x=0, y=500)

        two = ctk.CTkButton(self.root, text='2',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='black',
                            fg_color='skyblue',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_two)
        two.place(x=100, y=500)

        three = ctk.CTkButton(self.root, text='3',
                              font=('Roboto', 26, 'bold'),
                              width=99, height=99,
                              corner_radius=0,
                              text_color='black',
                              fg_color='skyblue',
                              hover=False,
                              bg_color='#111',
                              command=self.insert_three)
        three.place(x=200, y=500)

        plus = ctk.CTkButton(self.root, text='+',
                             font=('Roboto', 26, 'bold'),
                             width=99, height=99,
                             corner_radius=0,
                             text_color='white',
                             fg_color='orange',
                             hover=False,
                             bg_color='#111',
                             command=self.insert_plus)
        plus.place(x=300, y=500)

        all_clear = ctk.CTkButton(self.root, text='AC',
                                  font=('Roboto', 26, 'bold'),
                                  width=99, height=99,
                                  corner_radius=0,
                                  text_color='black',
                                  fg_color='red',
                                  hover=False,
                                  bg_color='#111',
                                  command=self.clear_all)
        all_clear.place(x=0, y=600)

        zero = ctk.CTkButton(self.root, text='0',
                             font=('Roboto', 26, 'bold'),
                             width=99, height=99,
                             corner_radius=0,
                             text_color='black',
                             fg_color='skyblue',
                             hover=False,
                             bg_color='#111',
                             command=self.insert_zero)
        zero.place(x=100, y=600)

        dot = ctk.CTkButton(self.root, text='.',
                            font=('Roboto', 26, 'bold'),
                            width=99, height=99,
                            corner_radius=0,
                            text_color='black',
                            fg_color='skyblue',
                            hover=False,
                            bg_color='#111',
                            command=self.insert_dot)
        dot.place(x=200, y=600)

        equal = ctk.CTkButton(self.root, text='=',
                              font=('Roboto', 35),
                              width=99, height=99,
                              corner_radius=0,
                              text_color='white',
                              fg_color='orange',
                              hover=False,
                              bg_color='#111',
                              command=self.result_output)
        equal.place(x=300, y=600)

    def run(self):
        self.root.mainloop()

    ## commands
    def cut_one(self):
        current = self.input_display.get()
        self.input_display.delete(0, END)
        self.input_display.insert(END, current[:-1])

    def insert_mod(self):
        self.input_display.insert(END, '%')

    def insert_pow(self):
        self.input_display.insert(END, '**')

    def insert_div(self):
        self.input_display.insert(END, '/')

    def insert_seven(self):
        self.input_display.insert(END, '7')

    def insert_eight(self):
        self.input_display.insert(END, '8')

    def insert_nine(self):
        self.input_display.insert(END, '9')

    def insert_mul(self):
        self.input_display.insert(END, '*')

    def insert_four(self):
        self.input_display.insert(END, '4')

    def insert_five(self):
        self.input_display.insert(END, '5')

    def insert_six(self):
        self.input_display.insert(END, '6')

    def insert_sub(self):
        self.input_display.insert(END, '-')

    def insert_one(self):
        self.input_display.insert(END, '1')

    def insert_two(self):
        self.input_display.insert(END, '2')

    def insert_three(self):
        self.input_display.insert(END, '3')

    def insert_dot(self):
        self.input_display.insert(END, '.')

    def insert_plus(self):
        self.input_display.insert(END, '+')

    def insert_zero(self):
        self.input_display.insert(END, '0')

    def clear_all(self):
        self.input_display.delete(0, END)

    def result_output(self):
        content = self.input_display.get()
        try:
            result = eval(content)
            self.output_display.delete(0, END)
            self.output_display.insert(END, result)
        except:
            self.output_display.delete(0, END)
            self.output_display.insert(END, 'Expression Error')



if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()


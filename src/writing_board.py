from tkinter import Tk, Canvas, DoubleVar
from tkinter import colorchooser
import customtkinter as ctk


class WritingBoard(Tk):
    def __init__(self):
        super().__init__()
        self.title('Writing Board')
        self.geometry('1050x570+150+50')
        self.resizable(False, False)
        self.configure(background='#d4c1e6')

        self.current_x = 0
        self.current_y = 0
        self.color = 'black'

        ### eraser ###
        ctk.CTkButton(self,
                      cursor='hand2',
                      text='Clear',
                      text_color='black',
                      hover_color='red',
                      fg_color='#f2f3f5',
                      height=30,
                      width=50,
                      command=self.new_canvas,
                      ).place(x=24, y=390)

        # canvas of the color
        self.colors = Canvas(self, bg='#ffffff', width=37, height=310, bd=0)
        self.colors.place(x=30, y=60)

        ctk.CTkButton(self, text='Custom',
                      fg_color='skyblue',
                      width=60, height=40,
                      corner_radius=10,
                      text_color='black',
                      hover_color='blue',
                      font=('Arial', 15),
                      command=self.choose_color).place(x=15, y=455)

        self.display_color()

        ############ canvas, where we can draw ###########
        canvas = Canvas(self, width=930, height=500, bg='white', cursor='hand2')
        canvas.place(x=100, y=10)
        self.canvas = canvas  # Initialize self.canvas

        canvas.bind('<Button-1>', self.locate_xy)
        canvas.bind('<B1-Motion>', self.add_line)

        ############ slider, for changing the width of pen ###########

        self.current_value = DoubleVar()

        slider = ctk.CTkSlider(self, from_=1, to=100,
                               variable=self.current_value,
                               button_color='blue',
                               fg_color='red',
                               progress_color='blue',
                               height=20)
        slider.place(x=30, y=530)

    def run(self):
        self.mainloop()

    def new_canvas(self):
        self.canvas.delete('all')
        self.display_color()

    def locate_xy(self, event):
        self.current_x = event.x
        self.current_y = event.y

    def add_line(self, event):
        self.canvas.create_line((self.current_x, self.current_y, event.x, event.y),
                                width=self.get_current_value(), fill=self.color, capstyle='round', smooth=True)
        self.current_x, self.current_y = event.x, event.y

    def show_color(self, new_color):
        self.color = new_color

    def choose_color(self):
        self.lift()
        new_color = colorchooser.askcolor(parent=self)
        self.color = new_color[1]

    def display_color(self):
        id = self.colors.create_rectangle((10, 10, 30, 30), fill='aqua')
        self.colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('aqua'))

        id = self.colors.create_rectangle((10, 40, 30, 60), fill='purple')
        self.colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('purple'))

        id = self.colors.create_rectangle((10, 70, 30, 90), fill='blue')
        self.colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('blue'))

        id = self.colors.create_rectangle((10, 100, 30, 120), fill='green')
        self.colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('green'))

        id = self.colors.create_rectangle((10, 130, 30, 150), fill='yellow')
        self.colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('yellow'))

        id = self.colors.create_rectangle((10, 160, 30, 180), fill='orange')
        self.colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('orange'))

        id = self.colors.create_rectangle((10, 190, 30, 210), fill='red')
        self.colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('red'))

        id = self.colors.create_rectangle((10, 220, 30, 240), fill='brown')
        self.colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('brown'))

        id = self.colors.create_rectangle((10, 250, 30, 270), fill='grey')
        self.colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('grey'))

        id = self.colors.create_rectangle((10, 280, 30, 300), fill='black')
        self.colors.tag_bind(id, '<Button-1>', lambda x: self.show_color('black'))

    def get_current_value(self):
        return self.current_value.get()


if __name__ == '__main__':
    wb = WritingBoard()
    wb.run()

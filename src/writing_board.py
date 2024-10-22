from tkinter import Tk, Canvas, DoubleVar, Frame
from tkinter import colorchooser
import customtkinter as ctk

class WritingBoard(Tk):
    def __init__(self):
        super().__init__()
        self.title('Writing Board')
        self.geometry('1050x570+150+50')
        self.configure(background='#2E2E2E')  # Dark background for the main window

        self.current_x = 0
        self.current_y = 0
        self.color = 'white'

        ### Eraser Button ###
        ctk.CTkButton(self,
                      cursor='hand2',
                      font=('Arial', 14, 'bold'),
                      text='Clear',
                      text_color='white',
                      hover_color='red',
                      fg_color='#3B3B3B',
                      height=30,
                      width=50,
                      command=self.new_canvas,
                      ).place(x=24, y=390)

        # Canvas of the color palette
        self.colors = Canvas(self, bg='#3B3B3B', width=37, height=310, bd=0)
        self.colors.place(x=30, y=60)

        ctk.CTkButton(self, text='Custom',
                      fg_color='skyblue',
                      width=60, height=40,
                      corner_radius=10,
                      text_color='black',
                      hover_color='white',
                      font=('Arial', 14, 'bold'),
                      command=self.choose_color).place(x=15, y=455)

        self.display_color()

        ############ Canvas, where we can draw ###########
        self.canvas_frame = Frame(self, bg='#3B3B3B')
        self.canvas_frame.place(x=100, y=50, relwidth=0.94, relheight=0.95)  # Set relative width and height

        self.canvas = Canvas(self.canvas_frame, bg='#4B4B4B', cursor='hand2')
        self.canvas.pack(fill='both', expand=True)  # Allow the canvas to fill the frame


        self.canvas.bind('<Button-1>', self.locate_xy)
        self.canvas.bind('<B1-Motion>', self.add_line)

        ############ Slider, for changing the width of pen ###########
        self.current_value = DoubleVar()

        slider = ctk.CTkSlider(self, from_=1, to=100,
                               variable=self.current_value,
                               button_color='white',
                               fg_color='skyblue',
                               progress_color='white',
                               hover=False,
                               height=20)
        slider.place(x=30, y=10)

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
        if new_color[1]:  # Check if the user selected a color
            self.color = new_color[1]

    def display_color(self):
        # Create a grid of color rectangles and bind them to show_color
        colors = ['aqua', 'purple', 'blue', 'green', 'yellow', 'orange', 'red', 'brown', 'grey', 'black']
        for i, color in enumerate(colors):
            id = self.colors.create_rectangle((10, 10 + i * 30, 30, 30 + i * 30), fill=color)
            self.colors.tag_bind(id, '<Button-1>', lambda x, color=color: self.show_color(color))

    def get_current_value(self):
        return self.current_value.get()

if __name__ == '__main__':
    wb = WritingBoard()
    wb.run()

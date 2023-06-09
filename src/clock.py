from tkinter import *
from datetime import datetime
from customtkinter import CTkSwitch
from tkcalendar import Calendar


class Clock(Tk):
    """This class contains a simple digital Clock"""

    def __init__(self):
        super().__init__()
        self.geometry('400x200+100+100')
        self.configure(bg='white')
        self.title('Clock')

        self.time_label = Label(self, font=('Arial', 25), fg='black', bg='white')
        self.time_label.pack(padx=10, pady=40)

        self.date_label = Label(self, font=('Arial', 18), fg='black', bg='white')
        self.date_label.pack(padx=10, pady=0)

        # Create a switch for showing/hiding the calendar
        self.switch = CTkSwitch(self,
                                text='Show Calendar',
                                text_color='black',
                                offvalue=False, onvalue=True,
                                progress_color='blue',
                                button_color='grey',
                                hover=False,
                                command=self.toggle_calendar)  # Call toggle_calendar method when switch state changes
        self.switch.place(x=10, y=10)

        self.calendar_frame = None  # Initialize calendar frame as None

        # Update time
        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime('%I:%M:%S %p')  # Get current time
        current_date = datetime.now().strftime('%B %d, %Y')  # Get current date
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.after(200, self.update_time)  # Set 200 milliseconds update time

    def toggle_calendar(self):
        if self.switch.get():
            # If switch is on, expand window and show calendar frame
            self.geometry('500x400+100+100')
            self.title('Clock & Calendar')
            
            #make calendar frame
            self.calendar_frame = Frame(self, 
                                        height=200,
                                        width=200,
                                        border=1,
                                        )
            self.calendar_frame.pack(padx=10, pady=10)
            
            # create calendar widget
            cal1 = Calendar(self.calendar_frame, 
                            selectmode='day',
                            date_pattern='d/m/yy')
            cal1.pack(fill='both', expand=True) 
            
        else:
            # If switch is off, reset window size and position, and remove calendar frame
            self.geometry('400x200+100+100')
            if self.calendar_frame:
                self.calendar_frame.destroy()
                self.calendar_frame = None

    def main(self):
        self.mainloop()



if __name__ == '__main__':
    c1 = Clock()
    c1.main()

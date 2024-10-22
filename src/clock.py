from customtkinter import CTk, CTkLabel, CTkFrame, CTkSwitch, set_appearance_mode, set_default_color_theme
from datetime import datetime
from tkcalendar import Calendar


class Clock(CTk):
    """This class contains a simple digital Clock with Dark Theme"""

    def __init__(self):
        super().__init__()
        
        set_appearance_mode("dark")  # Switch to dark theme
        set_default_color_theme("blue")
        
        self.geometry('400x200')
        self.title('Clock')
        self.configure(fg_color='gray20')

        # Digital clock label
        self.time_label = CTkLabel(self, font=('Arial', 35), text_color='white')
        self.time_label.pack(padx=10, pady=40)

        # Date label
        self.date_label = CTkLabel(self, font=('Arial', 30), text_color='white')
        self.date_label.pack(padx=10, pady=0)

        # Calendar switch button
        self.switch = CTkSwitch(self,
                                text='Show Calendar',
                                text_color='white',
                                offvalue=False, onvalue=True,
                                progress_color='blue',
                                button_color='gray40',
                                command=self.toggle_calendar)  # Call toggle_calendar method when switch state changes
        self.switch.place(x=10, y=10)

        self.calendar_frame = None  # Initialized calendar frame as None

        # Update time
        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime('%I:%M:%S %p')  # Get current time
        current_date = datetime.now().strftime('%B %d, %Y')  # Get current date
        self.time_label.configure(text=current_time)
        self.date_label.configure(text=current_date)
        self.after(200, self.update_time)  # 200 milliseconds update time

    def toggle_calendar(self):
        if self.switch.get():
            # If switch is on, expand window and show calendar frame
            self.geometry('650x550')
            self.title('Clock & Calendar')

            # Create calendar frame with larger dimensions
            self.calendar_frame = CTkFrame(self, 
                                           height=350,  # Increased height
                                           width=350,   # Increased width
                                           fg_color='gray25',  # Darker background for frame
                                           border_width=2, border_color='gray40')
            self.calendar_frame.pack(padx=10, pady=10)

            # Larger calendar widget
            cal1 = Calendar(self.calendar_frame, 
                            selectmode='day',
                            date_pattern='d/m/yy',
                            font=("Arial", 25))  # Make the font bigger
            cal1.pack(fill='both', expand=True) 

        else:
            self.geometry('500x300')
            if self.calendar_frame:
                self.calendar_frame.destroy()
                self.calendar_frame = None

    def main(self):
        self.mainloop()


if __name__ == '__main__':
    c1 = Clock()
    c1.main()

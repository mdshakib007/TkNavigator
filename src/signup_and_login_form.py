from tkinter import Tk, Label
import customtkinter as ctk
import csv
import re
import random



### signup class
class SignUp(Tk):
    def __init__(self):
        super().__init__()
        
        # binding with protocol
        def on_closing():
            self.destroy()
        
        self.title("Sign up")
        self.geometry('600x700+150+100')
        self.configure(background='#aacbff')
        
        self.username = None
        
        # call the main method
        self.main()
        
        # close window event
        self.protocol('WM_DELETE_WINDOW', on_closing)
        
        self.mainloop()
        
    
    def main(self):
        self.bgframe = ctk.CTkFrame(self, width=300, height=650,
                                    border_width=1,
                                    fg_color='#fff'
                                    )
        
        self.bgframe.pack(padx=20, pady=80, fill='both', expand=True)
        
        
        ## title
        ctk.CTkLabel(master=self.bgframe, text='SIGN UP',
                     font=("Arial", 30),
                     bg_color='white',
                     fg_color='white',
                     text_color='black'
                     ).pack(padx=10, pady=30, side='top', fill='x')
        
        
        ## firstname
        self.firstname = ctk.CTkEntry(self.bgframe, width=300, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='First Name', 
                         corner_radius=100,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
        self.firstname.pack(padx=10, pady=10)
        
        
        
        ## lastname
        self.lastname = ctk.CTkEntry(self.bgframe, width=300, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='Last Name', 
                         corner_radius=100,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
        self.lastname.pack(padx=10, pady=10)
        
        
        ## email
        self.email = ctk.CTkEntry(self.bgframe, width=300, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='E-mail', 
                         corner_radius=100,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
        self.email.pack(padx=10, pady=10)
        
        
        ## password
        self.password = ctk.CTkEntry(self.bgframe, width=300, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='Password', 
                         corner_radius=100,
                         bg_color='white',
                         fg_color='white',
                         text_color='black',
                         show='▪️'
                         )
        self.password.pack(padx=10, pady=10)
        
        
        ### go to login page
        ctk.CTkButton(self.bgframe, text="Already have an Account?",
                     font=('Arial', 12),
                     bg_color='#fff',
                     text_color='blue',
                     fg_color='#ffffff',
                     hover=False,
                     command=self.login_page
                     ).pack()
        
        
        ### signup button
        ctk.CTkButton(self.bgframe, text='SIGN UP', 
                      width=200, height=40,
                      font=('Arial', 18),
                      corner_radius=100,
                      bg_color='#fff',
                      command=self.get_data,
                      hover_color='blue'
                      ).pack(padx=10, pady=20)
        
        
        
        # output label
        self.show = Label(self.bgframe, font=("Arial", 18),
                          bg='white')
        self.show.pack()
        
        
    def login_page(self):
        self.destroy()
        login = Login()
    
    def get_data(self):
        first_name = self.firstname.get()
        last_name = self.lastname.get()
        email_data = self.email.get()
        pass_data = self.password.get()
        
        if first_name and last_name and email_data and pass_data != '':
            if len(pass_data) < 6:
                self.show['text'] = 'Password Must Be 6 Characters.'
            
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email_data):
                self.show['text'] = 'Invalid E-mail'
            
            else:
                number = random.randint(1000, 9999)
                num = str(number)
                self.username = first_name + last_name + num
                
                # Save signup data to CSV file
                with open('.signup_data.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([first_name, last_name, self.username, email_data, pass_data])
                
                self.show['text'] = f'Signup Successful!\nUsername: @{self.username}'
                
                # Delete all text
                self.firstname.delete(0, 'end')
                self.lastname.delete(0, 'end')
                self.email.delete(0, 'end')
                self.password.delete(0, 'end')
        
        elif first_name == '':
            self.show['text'] = 'First Name Cannot Be Empty!'
            
        elif last_name == '':
            self.show['text'] = 'Last Name Cannot Be Empty!'
            
        elif email_data == '':
            self.show['text'] = 'E-mail Cannot Be Empty!'
            
        elif pass_data == '':
            self.show['text'] = 'Password Cannot Be Empty!'
            
        else:
            self.show['text'] = 'An Error Occurred.'
            

### login class
class Login(Tk):
    def __init__(self):
        super().__init__()
        
        def on_closing():
            self.destroy()
            
        self.title("Sign In")
        self.geometry("500x600+150+50")
        self.configure(background='#aacbff')  
        

        # call the main function
        self.main()
        
        
        # bind window destroy event
        self.protocol('WM_DELETE_WINDOW', on_closing)

        # call mainloop
        self.mainloop()


    def main(self):
        self.bgframe = ctk.CTkFrame(self, width=300, height=600,
                                    border_width=1,
                                    fg_color='#fff'
                                    )
        
        self.bgframe.pack(padx=20, pady=100, fill='both', expand=True)
        
        ctk.CTkLabel(master=self.bgframe, text='SIGN IN',
                     font=("Arial", 30),
                     bg_color='white',
                     fg_color='white',
                     text_color='black'
                     ).pack(padx=10, pady=20, side='top', fill='x')
        
        
        ### Entry of email and password
        # email entry
        self.email = ctk.CTkEntry(self.bgframe, width=300, 
                    font=('Arial', 18), 
                    height=40, 
                    border_width=1, 
                    placeholder_text='E-mail', 
                    corner_radius=100,
                    bg_color='white',
                    fg_color='white',
                    text_color='black'
                    )
        self.email.pack(padx=10, pady=10)
        
        # password entry
        self.password = ctk.CTkEntry(self.bgframe, width=300, 
                    font=('Arial', 18), 
                    height=40, 
                    border_width=1, 
                    placeholder_text='Password', 
                    corner_radius=100,
                    bg_color='white',
                    fg_color='white',
                    text_color='black',
                    show='▪️'
                    )
        self.password.pack(padx=10, pady=10)
        
        
        ### go to registration page
        ctk.CTkButton(self.bgframe, text="Don't have an Account?",
                     font=('Arial', 12),
                     bg_color='#fff',
                     text_color='blue',
                     fg_color='#ffffff',
                     hover=False,
                     command=self.registration_form
                     ).pack()
        
        
        ### LOGIN button
        ctk.CTkButton(self.bgframe, text='LOGIN', 
                      width=200, height=40,
                      font=('Arial', 18),
                      corner_radius=100,
                      bg_color='#fff', 
                      command=self.get_data,
                      hover_color='blue'
                      ).pack(padx=10, pady=20)
        
        
        
        # output label
        self.show = Label(self.bgframe, font=("Arial", 18),
                          bg='white')
        self.show.pack()
    
    
        
    def registration_form(self):
        self.destroy()
        signup = SignUp()
    
    
    def get_data(self):
        email = self.email.get()
        password = self.password.get()
        
        if email and password != '':
            # Read signup data from CSV file
            with open('.signup_data.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[3] == email and row[4] == password:
                        self.show['text'] = 'Login Successful!'
                        break
                else:
                    self.show['text'] = 'Invalid Email or Password!'
            
            # Delete all text
            self.email.delete(0, 'end')
            self.password.delete(0, 'end')
            
            
        elif email == '':
            self.show['text'] = 'E-mail Cannot Be Empty!'
            
        elif password == '':
            self.show['text'] = 'Password Cannot Be Empty!'
        
        else:
            self.show['text'] = 'An Error Occurred.'


if __name__ == '__main__':
    signup = SignUp()

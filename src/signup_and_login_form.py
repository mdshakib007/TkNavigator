from tkinter import Tk
import customtkinter as ctk


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
        
        # call the main method
        self.main()
        
        # close window event
        self.protocol('WM_DELETE_WINDOW', on_closing)
        
        self.mainloop()
        
    
    def main(self):
        self.bgframe = ctk.CTkFrame(self, width=300, height=600,
                                    border_width=1,
                                    fg_color='#fff'
                                    )
        
        self.bgframe.pack(padx=20, pady=100, fill='both', expand=True)
        
        
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
                         text_color='black'
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
        
        
    def login_page(self):
        self.destroy()
        login = Login()
    
    def get_data(self):
        first_name = self.firstname.get()
        last_name = self.lastname.get()
        email_data = self.email.get()
        pass_data = self.password.get()
        
        if first_name and last_name and email_data and pass_data != '':
            ctk.CTkLabel(self.bgframe, text="Sing Up Successful!", 
                         fg_color='white', 
                         text_color='green', 
                         font=('Roboto', 14)).pack()
            
            
            # delete all text 
            self.firstname.delete(0, 'end')
            self.lastname.delete(0, 'end')
            self.email.delete(0, 'end')
            self.password.delete(0, 'end')
        
        else:
            ctk.CTkLabel(self.bgframe, text="* Data Cannot Be Empty.", 
                         fg_color='white', 
                         text_color='red', 
                         font=('Roboto', 14)).pack()



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
        
        
        ### Entry of username and password
        # username entry
        self.username = ctk.CTkEntry(self.bgframe, width=300, 
                    font=('Arial', 18), 
                    height=40, 
                    border_width=1, 
                    placeholder_text='E-mail', 
                    corner_radius=100,
                    bg_color='white',
                    fg_color='white',
                    text_color='black'
                    )
        self.username.pack(padx=10, pady=10)
        
        # password entry
        self.password = ctk.CTkEntry(self.bgframe, width=300, 
                    font=('Arial', 18), 
                    height=40, 
                    border_width=1, 
                    placeholder_text='Password', 
                    corner_radius=100,
                    bg_color='white',
                    fg_color='white',
                    text_color='black'
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
        
        
        
    def registration_form(self):
        self.destroy()
        signup = SignUp()
    
    
    def get_data(self):
        username = self.username.get()
        password = self.password.get()
        
        if username and password != '':
            ctk.CTkLabel(self.bgframe, text="Login Successful!", 
                         fg_color='white', 
                         text_color='green', 
                         font=('Roboto', 14)).pack()
            
            
            # delete all text 
            self.username.delete(0, 'end')
            self.password.delete(0, 'end')
            
            
        else:
            ctk.CTkLabel(self.bgframe, text="* Data Cannot Be Empty.", 
                         fg_color='white', 
                         text_color='red', 
                         font=('Roboto', 14)).pack()


if __name__ == '__main__':
    signup = SignUp()
    
from tkinter import *
import customtkinter as ctk
import mysql.connector 

mydb = mysql.connector.connect(
    host='localhost',
    user= 'root',
    password='***********',
    database='project_delta'
)

report_cursor = mydb.cursor()

sql_formula = '''
    INSERT INTO report_data (name, email, issue)
    VALUES (%s, %s, %s)
'''




class Report(Tk):
    def __init__(self):
        super().__init__()
        self.title("Report an issue")
        self.geometry("500x650+150+100")
        self.configure(background='#f74')  

        # call the main function
        self.main()

        # call mainloop
        self.mainloop()


    def main(self):
        self.bgframe = ctk.CTkFrame(self, width=300, height=600,
                                    border_width=1,
                                    fg_color='#fff'
                                    )
        
        self.bgframe.pack(padx=20, pady=100, fill='both', expand=True)
        
        ctk.CTkLabel(master=self.bgframe, text='Report An Issue',
                     font=("Arial", 30),
                     bg_color='white',
                     fg_color='white',
                     text_color='black'
                     ).pack(padx=10, pady=20, side='top', fill='x')
        
        
        ### Entry of username and issue
        # username entry
        self.username = ctk.CTkEntry(self.bgframe, width=300, 
                    font=('Arial', 18), 
                    height=40, 
                    border_width=1, 
                    placeholder_text='Name', 
                    corner_radius=1,
                    bg_color='white',
                    fg_color='white',
                    text_color='black'
                    )
        self.username.pack(padx=10, pady=10)
        
        
        # username entry
        self.email = ctk.CTkEntry(self.bgframe, width=300, 
                    font=('Arial', 18), 
                    height=40, 
                    border_width=1, 
                    placeholder_text='E-mail', 
                    corner_radius=1,
                    bg_color='white',
                    fg_color='white',
                    text_color='black'
                    )
        self.email.pack(padx=10, pady=10)
        
        
        # issue entry
        self.issue = ctk.CTkTextbox(self.bgframe, width=300, 
                    font=('Arial', 18), 
                    height=100, 
                    border_width=1,  
                    corner_radius=1,
                    bg_color='white',
                    fg_color='white',
                    text_color='black'
                    )
        self.issue.pack(padx=10, pady=10)
        
        
        ### submit button
        ctk.CTkButton(self.bgframe, text='SUBMIT', 
                      width=200, height=40,
                      font=('Arial', 18),
                      corner_radius=100,
                      bg_color='#fff', 
                      hover_color='#f74',
                      command=self.get_data
                      ).pack(padx=10, pady=20)
        
        
        
        
        # output label
        self.show = Label(self.bgframe, font=("Arial", 18),
                          bg='white')
        self.show.pack()
        
        
    
    
    def get_data(self):
        username = self.username.get()
        email = self.email.get()
        issue = self.issue.get(1.0, 'end').replace('\n', ' ')
        
        if username and email and issue != '':
            # insert data in mysql database
            data = (username, email, issue)
            report_cursor.execute(sql_formula, data)
            mydb.commit()
            
            
            self.show['text'] = 'Report Sent!'
            
            # delete all text 
            self.username.delete(0, 'end')
            self.email.delete(0, 'end')
            self.issue.delete(1.0, 'end')
            
        elif username == '':
            self.show['text'] = 'Username Required!'
            
        elif email == '':
            self.show['text'] = 'E-mail Required!'
            
        else:
            pass


if __name__ == '__main__':
    report = Report()

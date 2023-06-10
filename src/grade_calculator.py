from tkinter import *
from customtkinter import CTkEntry, CTkButton




class Grade:
    @staticmethod
    def grade_calculate():    
        root = Tk()
        root.geometry('600x700')
        root.title('Calculaton Of GPA')
        root.configure(background='#e2d8eb')


        # get all values
        def get_cgpa_show_output():
            '''this function calculate the value and show output'''

            try:
                one = float(first_sem.get())
                two = float(second_sem.get())
                three = float(third_sem.get())
                four = float(fourth_sem.get())
                five = float(fifth_sem.get())
                six = float(sixth_sem.get())
                seven = float(seventh_sem.get())
                eight = float(eight_sem.get())

                if one and two and three and four and five and six and seven and eight != '':
                    try:
                        cgpa = ((one * 0.05) + (two * 0.05) + (three * 0.1) + (four * 0.1) + (five * 0.2) + (six * 0.2) + (seven * 0.2) + (eight * 0.1))
                        
                        show['text'] = f"Your CGPA: {cgpa:.2f}"
                        
                        # clear the entries
                        first_sem.delete(0, 'end')
                        second_sem.delete(0, 'end')
                        third_sem.delete(0, 'end')
                        fourth_sem.delete(0, 'end')
                        fifth_sem.delete(0, 'end')
                        sixth_sem.delete(0, 'end')
                        seventh_sem.delete(0, 'end')
                        eight_sem.delete(0, 'end')
                        
                    
                    except Exception as e:
                        show['text'] = 'Invalid Input!'
                
                else:
                    show['text'] = 'Please Enter CGPA.'
            
            except Exception as e:
                show['text'] = 'Invalid Input!\nPlease Enter Valid CGPA.'
                
                # clear the entries
                first_sem.delete(0, 'end')
                second_sem.delete(0, 'end')
                third_sem.delete(0, 'end')
                fourth_sem.delete(0, 'end')
                fifth_sem.delete(0, 'end')
                sixth_sem.delete(0, 'end')
                seventh_sem.delete(0, 'end')
                eight_sem.delete(0, 'end')
                        



        # title
        Label(root, text='Calculation Of GPA(2022)',
            font=('Arial', 34),
            bg='#e2d8eb'
            ).pack(padx=5, pady=20)


        # Entries
        first_sem = CTkEntry(root, width=300,
                            font=('Arial', 18),
                            height=40,
                            border_width=0,
                            placeholder_text="Enter 1'st Semester's GPA",
                            corner_radius=10,
                            fg_color='white',
                            text_color='black'
                            )
        first_sem.pack(padx=5, pady=1)


        second_sem = CTkEntry(root, width=300,
                            font=('Arial', 18),
                            height=40,
                            border_width=0,
                            placeholder_text="Enter 2'nd Semester's GPA",
                            corner_radius=10,
                            fg_color='white',
                            text_color='black'
                            )
        second_sem.pack(padx=5, pady=1)


        third_sem = CTkEntry(root, width=300,
                            font=('Arial', 18),
                            height=40,
                            border_width=0,
                            placeholder_text="Enter 3'rd Semester's GPA",
                            corner_radius=10,
                            fg_color='white',
                            text_color='black'
                            )
        third_sem.pack(padx=5, pady=1)


        fourth_sem = CTkEntry(root, width=300,
                            font=('Arial', 18),
                            height=40,
                            border_width=0,
                            placeholder_text="Enter 4'th Semester's GPA",
                            corner_radius=10,
                            fg_color='white',
                            text_color='black'
                            )
        fourth_sem.pack(padx=5, pady=1)


        fifth_sem = CTkEntry(root, width=300,
                            font=('Arial', 18),
                            height=40,
                            border_width=0,
                            placeholder_text="Enter 5'th Semester's GPA",
                            corner_radius=10,
                            fg_color='white',
                            text_color='black'
                            )
        fifth_sem.pack(padx=5, pady=1)


        sixth_sem = CTkEntry(root, width=300,
                            font=('Arial', 18),
                            height=40,
                            border_width=0,
                            placeholder_text="Enter 6'th Semester's GPA",
                            corner_radius=10,
                            fg_color='white',
                            text_color='black'
                            )
        sixth_sem.pack(padx=5, pady=1)


        seventh_sem = CTkEntry(root, width=300,
                            font=('Arial', 18),
                            height=40,
                            border_width=0,
                            placeholder_text="Enter 7'th Semester's GPA",
                            corner_radius=10,
                            fg_color='white',
                            text_color='black'
                            )
        seventh_sem.pack(padx=5, pady=1)


        eight_sem = CTkEntry(root, width=300,
                            font=('Arial', 18),
                            height=40,
                            border_width=0,
                            placeholder_text="Enter 8'th Semester's GPA",
                            corner_radius=10,
                            fg_color='white',
                            text_color='black'
                            )
        eight_sem.pack(padx=5, pady=1)


        # button
        CTkButton(root, text='SUBMIT',
                width=200, height=40,
                font=('Arial', 18),
                corner_radius=100,
                hover_color='#f74',
                command=get_cgpa_show_output
                ).pack(padx=10, pady=20)


        # output label
        show = Label(root,
                    font=('Arial', 24),
                    bg='#e2d8eb'
                    )
        show.pack(padx=5, pady=20)


        root.mainloop()


if __name__ == '__main__':
    g = Grade()
    g.grade_calculate()
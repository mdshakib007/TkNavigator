from tkinter import Tk, Label
from tkinter.messagebox import showinfo
from customtkinter import CTkEntry, CTkButton


class Grade:
    @staticmethod
    def grade_calculate():
        root = Tk()
        root.geometry('600x700')
        root.title('Calculation Of GPA')
        root.configure(background='#1E1E1E')  # Dark background

        # Get all values
        def get_cgpa_show_output():
            '''This function calculates the GPA and shows the output'''
            try:
                # Read values from entries
                gpas = [
                    float(first_sem.get()), float(second_sem.get()), 
                    float(third_sem.get()), float(fourth_sem.get()), 
                    float(fifth_sem.get()), float(sixth_sem.get()), 
                    float(seventh_sem.get()), float(eight_sem.get())
                ]

                # Check if all entries are filled
                if all(gpas):
                    cgpa = (
                        (gpas[0] * 0.05) + (gpas[1] * 0.05) + 
                        (gpas[2] * 0.1) + (gpas[3] * 0.1) + 
                        (gpas[4] * 0.2) + (gpas[5] * 0.2) + 
                        (gpas[6] * 0.2) + (gpas[7] * 0.1)
                    )
                    show['text'] = f"Your CGPA: {cgpa:.2f}"

                    # Clear the entries
                    for entry in [first_sem, second_sem, third_sem, fourth_sem, fifth_sem, sixth_sem, seventh_sem, eight_sem]:
                        entry.delete(0, 'end')

                else:
                    root.lift()
                    showinfo('CGPA', 'Please Enter CGPA for All Semesters!', parent=root)

            except ValueError:
                root.lift()
                showinfo('CGPA', 'Please Enter Valid GPA!', parent=root)
                # Clear the entries if there's an error
                for entry in [first_sem, second_sem, third_sem, fourth_sem, fifth_sem, sixth_sem, seventh_sem, eight_sem]:
                    entry.delete(0, 'end')

        # Title
        Label(root, text='Calculation Of GPA (2022)',
              font=('Arial', 34), bg='#1E1E1E', fg='white').pack(padx=5, pady=20)

        # Create a list of entry placeholders
        placeholders = [
            "Enter 1'st Semester's GPA", "Enter 2'nd Semester's GPA", 
            "Enter 3'rd Semester's GPA", "Enter 4'th Semester's GPA", 
            "Enter 5'th Semester's GPA", "Enter 6'th Semester's GPA", 
            "Enter 7'th Semester's GPA", "Enter 8'th Semester's GPA"
        ]
        
        # Create entries
        entries = []
        for placeholder in placeholders:
            entry = CTkEntry(root, width=300,
                             font=('Arial', 18),
                             height=40,
                             border_width=0,
                             placeholder_text=placeholder,
                             corner_radius=10,
                             fg_color='#2E2E2E',  # Darker entry background
                             text_color='white')
            entry.pack(padx=5, pady=1)
            entries.append(entry)

        # Unpack entries for later use
        first_sem, second_sem, third_sem, fourth_sem, fifth_sem, sixth_sem, seventh_sem, eight_sem = entries

        # Button
        CTkButton(root, text='Calculate',
                   width=200, height=40,
                   font=('Arial', 18),
                   corner_radius=100,
                   hover_color='#456745',
                   command=get_cgpa_show_output
                   ).pack(padx=10, pady=20)

        # Output label
        show = Label(root,
                     font=('Arial', 24),
                     bg='#1E1E1E', fg='white')
        show.pack(padx=5, pady=20)

        root.mainloop()


if __name__ == '__main__':
    g = Grade()
    g.grade_calculate()

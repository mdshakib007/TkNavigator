from tkinter import Tk, Frame, messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd
from customtkinter import CTkButton, CTkFrame


class ExcelViewer:
    @staticmethod
    def excel_view():
        root = Tk()
        root.geometry('1000x500+200+200')
        root.title('Excel Viewer')
        root.configure(background='#2E2E2E')  # Set dark theme

        def open_file():
            root.lift()
            file = askopenfilename(
                title='Open A File',
                filetypes=(('Excel Files', '*.xlsx'), ('CSV Files', '*.csv')),
                parent=root
            )

            if file:
                try:
                    df = pd.read_excel(file)
                except Exception as e:
                    messagebox.showerror('Error', f"You can't access this file: {e}")
                    return  # Return early if there's an error

                # Clear previous data and enter new data
                tree.delete(*tree.get_children())

                # Set dataset's heading
                tree['column'] = list(df.columns)
                tree['show'] = 'headings'

                # Heading title
                for col in tree['column']:
                    tree.heading(col, text=col)

                # Enter data
                df_rows = df.to_numpy().tolist()
                for row in df_rows:
                    tree.insert('', 'end', values=row)

        # Create a frame for the Treeview
        frame = CTkFrame(root, fg_color='#3E3E3E')  # Darker frame
        frame.pack(pady=10, padx=10, fill='both', expand=True)

        # Treeview setup
        tree = ttk.Treeview(frame, style="Treeview", show='headings')
        tree.pack(fill='both', expand=True)

        # Scrollbars
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        # Button to open file
        open_button = CTkButton(root, text='Open Excel File', 
                                 command=open_file, 
                                 fg_color='#007BFF', 
                                 text_color='white',
                                 width=200,
                                 corner_radius=5)
        open_button.pack(pady=10)

        # Styling Treeview
        style = ttk.Style()
        style.configure("Treeview", background="#3E3E3E", foreground="white", rowheight=25, fieldbackground="#3E3E3E")
        style.configure("Treeview.Heading", background="#5C5C5C", foreground="white")

        root.mainloop()


if __name__ == '__main__':
    excel = ExcelViewer()
    excel.excel_view()

from tkinter import Tk, Frame, Button
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename
import pandas as pd


class ExcelViewer:
    @staticmethod
    def excel_view():
        root = Tk()
        root.geometry('1000x500+200+200')
        root.title('Excel Viewer')
        root.configure(background='#fff')


        def open_file():
            root.lift()
            file = askopenfilename(
                    title='Open A File',
                    filetypes=(
                        ('xlsx files', '*.xlsx'),
                        ('csv file', '*.csv')
                    ),
                    parent=root
                )
            

            if file:
                try:
                    file = r"{}".format(file)
                    df = pd.read_excel(file)
                except:
                    messagebox.showerror('Error', "You can't access this file")
                    return  # Return early if there's an error

                # clear previous data and enter new data
                tree.delete(*tree.get_children())

                # dataset's heading
                tree['column'] = list(df.columns)
                tree['show'] = 'headings'

                # heading title
                for col in tree['column']:
                    tree.heading(col, text=col)

                # enter data
                df_rows = df.to_numpy().tolist()
                for row in df_rows:
                    tree.insert('', 'end', values=row)


        # frame
        f1 = Frame(root)
        f1.pack()

        # tree view
        tree = ttk.Treeview(f1)
        tree.pack()

        # button
        Button(root, text='Open', width=50, height=2,font=30, fg='white',bg='blue',
            command=open_file).pack(padx=10, pady=10, side='bottom')

        root.mainloop()


if __name__ == '__main__':
    excel = ExcelViewer()
    excel.excel_view()

import customtkinter as ctk
from tkinter import *
from tkinter import ttk


class KeyboardShortcuts(Tk):
    def __init__(self):
        super().__init__()
    
        self.geometry('600x500')
        self.title('Keyboard Shortcuts  -  Tiny-iDE')
        self.configure(background='skyblue')
        self.minsize(300, 430)

        # call main method
        self.main()

        self.mainloop()


    def main(self):
        ctk.CTkLabel(self, text='Keyboard Shortcuts', 
                     text_color='black',
                     font=('Arial', 28, 'underline')).pack()
        
        # make a table
        tree = ttk.Treeview(self, cursor='hand2',
                            show='headings',
                            height=17, padding=10,
                            columns=('name', 'shortcuts'))
        tree.pack(padx=10, pady=5)
        
        # headings
        tree.heading('name', text='Name')
        tree.heading('shortcuts', text='Shortcuts')
        
        # insert data
        tree.insert('', 'end', values=('New File', 'Ctrl+N'))
        tree.insert('', 'end', values=('Python File', 'Ctrl+P'))
        tree.insert('', 'end', values=('Open File', 'Ctrl+O'))
        tree.insert('', 'end', values=('Save', 'Ctrl+S'))
        tree.insert('', 'end', values=('Save As...', 'Ctrl+S'))
        tree.insert('', 'end', values=('Exit Window', 'Ctrl+Q'))
        tree.insert('', 'end', values=('Undo', 'Ctrl+Z'))
        tree.insert('', 'end', values=('Redo', 'Ctrl+Y'))
        tree.insert('', 'end', values=('Cut', 'Ctrl+X'))
        tree.insert('', 'end', values=('Copy', 'Ctrl+C'))
        tree.insert('', 'end', values=('Paste', 'Ctrl+V'))
        tree.insert('', 'end', values=('Start Debugging', 'Ctrl+R'))
        tree.insert('', 'end', values=('Run Withut Debugging', 'Ctrl+R'))
        tree.insert('', 'end', values=('Expand Output Window', 'Ctrl+E'))
        tree.insert('', 'end', values=('Max Window', 'Alt+M'))
        tree.insert('', 'end', values=('Source Code', 'Alt+S'))
        tree.insert('', 'end', values=('About', 'Alt+A'))
        

if __name__ == '__main__':
    k1 = KeyboardShortcuts()
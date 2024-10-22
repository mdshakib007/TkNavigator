import customtkinter as ctk
from tkinter import *
from tkinter import ttk


class KeyboardShortcuts(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('600x500')
        self.title('Keyboard Shortcuts - Tiny-iDE')
        self.configure(background='#2E2E2E')  # Dark background
        self.minsize(300, 430)

        # Call main method
        self.main()

        self.mainloop()

    def main(self):
        ctk.CTkLabel(self, text='Keyboard Shortcuts',
                     text_color='white',
                     font=('Arial', 28, 'underline')).pack(pady=10)

        # Make a table
        tree = ttk.Treeview(self, cursor='hand2',
                            show='headings',
                            height=17, padding=10,
                            columns=('name', 'shortcuts'))

        # Configure the treeview
        tree.pack(padx=10, pady=5)

        # Style for the treeview
        style = ttk.Style()
        style.configure("Treeview", 
                        background='#2E2E2E',  # Dark background for table
                        foreground='white',     # White text color
                        rowheight=25,
                        fieldbackground='#2E2E2E')
        style.configure("Treeview.Heading", 
                        background='#3C3C3C',  # Darker background for headers
                        foreground='white',
                        font=('Arial', 12, 'bold'))  # Header font style

        # Headings
        tree.heading('name', text='Name')
        tree.heading('shortcuts', text='Shortcuts')

        # Insert data
        shortcuts = [
            ('New File', 'Ctrl+N'),
            ('Python File', 'Ctrl+P'),
            ('Open File', 'Ctrl+O'),
            ('Save', 'Ctrl+S'),
            ('Save As...', 'Ctrl+S'),
            ('Exit Window', 'Ctrl+Q'),
            ('Undo', 'Ctrl+Z'),
            ('Redo', 'Ctrl+Y'),
            ('Cut', 'Ctrl+X'),
            ('Copy', 'Ctrl+C'),
            ('Paste', 'Ctrl+V'),
            ('Start Debugging', 'Ctrl+R'),
            ('Run Without Debugging', 'Ctrl+R'),
            ('Expand Output Window', 'Ctrl+E'),
            ('Max Window', 'Alt+M'),
            ('Source Code', 'Alt+S'),
            ('About', 'Alt+A')
        ]

        for name, shortcut in shortcuts:
            tree.insert('', 'end', values=(name, shortcut))

        # Set the font color for the rows
        tree.tag_configure('oddrow', background='#2E2E2E', foreground='white')
        tree.tag_configure('evenrow', background='#3C3C3C', foreground='white')

        # Alternate row colors
        for index, item in enumerate(tree.get_children()):
            tree.item(item, tags=('oddrow' if index % 2 == 0 else 'evenrow',))


if __name__ == '__main__':
    k1 = KeyboardShortcuts()

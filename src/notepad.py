from tkinter import *
from tkinter import messagebox, colorchooser, filedialog
import os
import webbrowser
import datetime
import clock
import calculator
import definition




class NotePad(Tk):
    def __init__(self):
        super().__init__()
    # global variables for changing the text area's font, size etc.
        self.name = 'Arial'
        self.size = 12
        self.file = None
        self.font_list = [self.name, self.size]

        # Initial widgets
        self.title("* Untitled  -  Notepad")
        self.minsize(422, 233)
        self.geometry("888x555")


        # Define the text area
        self.text_area = Text(self, font=self.font_list, undo=True)
        self.text_area.pack(expand=True, fill='both')

        # Make Scrollbar
        scroll = Scrollbar(self.text_area)
        scroll.pack(side='right', fill='y')
        scroll.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=scroll.set)
        
        
        # Bind keyboard shortcuts to menu items
        self.bind("<Control-n>", self.new_file)   # Ctrl + N for new file
        self.bind("<Control-o>", self.open_file)  # Ctrl + O for open file
        self.bind("<Control-s>", self.save)       # Ctrl + S for save
        self.bind("<Alt-s>", self.share)          # Alt + S for share
        self.bind("<Control-q>", self.exit_editor)  # Ctrl + Q for exit editor
        self.bind("<Control-z>", self.undo)       # Ctrl + Z for undo
        self.bind("<Control-y>", self.redo)       # Ctrl + Y for redo
        self.bind("<Control-x>", self.cut)        # Ctrl + X for cut
        self.bind("<Control-c>", self.copy)       # Ctrl + C for copy
        self.bind("<Control-v>", self.paste)      # Ctrl + V for paste
        self.bind("<Escape>", self.exit_editor)   # Escape key for exit editor
        self.bind("<Control-b>", self.bold_text)  # get bolded text
        self.bind("<Control-i>", self.italic_text)  # italic text
        self.bind("<Alt-c>", self.qv_clock)       # and so on.....
        self.bind("<Alt-a>", self.qv_calculator)
        self.bind("<Control-w>", self.welcome)
        self.bind("<Control-F2>", self.source_code)
        self.bind("<Control-a>", self.about)
        self.bind("<Alt-d>", self.dict_def)


        main_menu = Menu(self)  # this is main menu
        # This is 'File' menu
        file_menu = Menu(main_menu, tearoff=0, font='Arial 14')
        file_menu.add_command(label='New Text File',
                            accelerator='Ctrl+N', command=self.new_file)
        file_menu.add_command(label='New File', accelerator='Ctrl+N', command=self.new_file)
        file_menu.add_command(label='Open File...',
                            accelerator='Ctrl+O', command=self.open_file)
        file_menu.add_command(label='Open Recent',
                            accelerator='Ctrl+O', command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label='Save', accelerator='Ctrl+S', command=self.save)
        file_menu.add_command(label='Save As...',
                            accelerator='Ctrl+S', command=self.save_as)
        file_menu.add_command(label='Save All', command=self.save_all)
        file_menu.add_separator()
        file_menu.add_command(label='Share', accelerator='Alt+S', command=self.share)
        file_menu.add_separator()
        # this is built in command.
        file_menu.add_command(label='Exit', accelerator='Ctrl+Q', command=self.exit_editor)
        
        # configuring the 'File' menu
        main_menu.add_cascade(label='File', menu=file_menu, font='Arial 15')


        # 'Edit' menu
        edit_menu = Menu(main_menu, tearoff=0, font='Arial 14')
        edit_menu.add_command(label='Undo', command=self.undo, accelerator='Ctrl+Z')
        edit_menu.add_command(label='Redo', command=self.redo, accelerator='Ctrl+Y')
        edit_menu.add_separator()
        edit_menu.add_command(label='Cut', command=self.cut, accelerator='Ctrl+X')
        edit_menu.add_command(label='Copy', command=self.copy, accelerator='Ctrl+C')
        edit_menu.add_command(label='Paste', command=self.paste, accelerator='Ctrl+V')
        edit_menu.add_separator()
        edit_menu.add_command(label='Expand', command=self.expand_editor)
        edit_menu.add_command(label='Resize', command=self.resize_editor)
        edit_menu.add_separator()
        edit_menu.add_command(label='Exit Editor',
                            command=self.exit_editor, accelerator='Ctrl+Q')

        # configuring 'Edit' menu
        main_menu.add_cascade(label='Edit', menu=edit_menu, font='Arial 15')

        # 'Selection' menu
        selection_menu = Menu(main_menu, tearoff=0, font='Arial 14')
        selection_menu.add_command(label='Change Background', command=self.change_bg)
        selection_menu.add_command(label='Font Color', command=self.font_color)
        selection_menu.add_separator()
        # sub menu(for font)
        font_menu = Menu(selection_menu, tearoff=0, font='Arial 14')

        font_menu.add_command(label='Arial', accelerator='Default',
                            command=lambda: self.select_font('Arial'))
        font_menu.add_command(label='Calibri',
                            command=lambda: self.select_font('Calibri'))
        font_menu.add_command(label='Courier New', accelerator='New',
                            command=lambda: self.select_font('Courier'))
        font_menu.add_command(label='Garamond',
                            command=lambda: self.select_font('Garamond'))
        font_menu.add_command(label='Georgia',
                            command=lambda: self.select_font('Georgia'))
        font_menu.add_command(label='Helvetica',
                            command=lambda: self.select_font('Helvetica'))
        font_menu.add_command(label='monospace', accelerator='Pro',
                            command=lambda: self.select_font('monospace'))
        font_menu.add_command(label='Serif',
                            command=lambda: self.select_font('Serif'))
        font_menu.add_command(label='Verdana',
                            command=lambda: self.select_font('Verdana'))
        font_menu.add_command(label='Tahoma', command=lambda: self.select_font(
            'Tahoma'))  # english submenu ends
        font_menu.add_separator()
        font_menu.add_command(label='SolaimanLipi', accelerator='বাংলা')
        font_menu.add_command(label='Nikosh', accelerator='বাংলা',)
        font_menu.add_command(label='Siyamrupali', accelerator='বাংলা')
        font_menu.add_command(label='Vrinda Lohit Bengali', accelerator='বাংলা')
        font_menu.add_command(label='Mukti Narrow', accelerator='বাংলা')
        font_menu.add_command(label='Kalpurush', accelerator='বাংলা')  # submenu ends
        selection_menu.add_cascade(label='Font', menu=font_menu)

        # Font Size
        font_size = Menu(selection_menu, tearoff=0, font='Arial 14')

        font_size.add_command(label='8', command=lambda: self.f_size(8))
        font_size.add_command(label='9', command=lambda: self.f_size(9))
        font_size.add_command(label='10', command=lambda: self.f_size(10))
        font_size.add_command(label='11', command=lambda: self.f_size(11))
        font_size.add_command(label='12', command=lambda: self.f_size(12))
        font_size.add_command(label='14', command=lambda: self.f_size(14))
        font_size.add_command(label='15', command=lambda: self.f_size(15))
        font_size.add_command(label='16', command=lambda: self.f_size(16))
        font_size.add_command(label='18', command=lambda: self.f_size(18))
        font_size.add_command(label='20', command=lambda: self.f_size(20))
        font_size.add_command(label='22', command=lambda: self.f_size(22))
        font_size.add_command(label='25', command=lambda: self.f_size(25))
        font_size.add_command(label='27', command=lambda: self.f_size(27))
        font_size.add_command(label='30', command=lambda: self.f_size(30))
        font_size.add_command(label='35', command=lambda: self.f_size(35))
        font_size.add_command(label='40', command=lambda: self.f_size(40))
        font_size.add_command(label='46', command=lambda: self.f_size(46))
        font_size.add_command(label='50', command=lambda: self.f_size(50))
        font_size.add_command(label='60', command=lambda: self.f_size(60))  # size

        selection_menu.add_cascade(label='Size', menu=font_size, font='Arial 14')

        selection_menu.add_separator()
        selection_menu.add_command(
            label='Bold', command=self.bold_text, accelerator='Ctrl+B')
        selection_menu.add_command(
            label='Italic', command=self.italic_text, accelerator='Ctrl+I')
        selection_menu.add_command(label='Underline', command=self.underline_text)
        selection_menu.add_separator()
        selection_menu.add_command(
            label='Close', command=self.exit_editor, accelerator='Ctrl+Q')

        main_menu.add_cascade(label='Selection', menu=selection_menu, font='Arial 15')


        # 'Tools' menu
        tools_menu = Menu(main_menu, tearoff=0, font='Arial 14')

        tools_menu.add_command(label='Quick Calculation',
                            command=self.qv_calculator, accelerator='Alt+A')
        tools_menu.add_command(label='Clock', command=self.qv_clock, accelerator='Alt+C')

        tools_menu.add_command(label='Dictionary definition',
                            command=self.dict_def, accelerator='Alt+D')
        tools_menu.add_separator()
        tools_menu.add_command(label='Quick Exit', command=exit)

        main_menu.add_cascade(menu=tools_menu, label='Tools', font='Arial 15')

        # 'Help' menu
        help_menu = Menu(main_menu, tearoff=0, font='Arial 14')

        help_menu.add_command(label='Welcome', command=self.welcome, accelerator='Ctrl+W')
        help_menu.add_command(label='Documentation', command=self.documentation)
        help_menu.add_separator()
        help_menu.add_command(label='Website', command=self.website)
        help_menu.add_command(label='Tutorial', command=self.tutorial)
        help_menu.add_command(label='Get Source Code',
                            command=self.source_code, accelerator='Ctrl+F2')
        help_menu.add_command(label='GitHub', command=self.github)

        help_menu.add_separator()
        help_menu.add_command(label='Check For Updates', command=self.update)
        help_menu.add_separator()
        help_menu.add_command(label='About', command=self.about, accelerator='Ctrl+A')

        main_menu.add_cascade(label='Help', menu=help_menu, font='Arial 15')
        self.config(menu=main_menu)


        self.mainloop()
        


    # Logic's or functions for command

    def new_file(self, *args):
        '''this function just erase all text from self.text_area'''
        content = self.text_area.get(1.0, END)
        if content != '\n':
            self.lift()
            save_change = messagebox.askquestion(
                'Save Change', 'Do you want to save change?', parent=self)

            if save_change == 'yes':
                self.save()
            self.text_area.delete(1.0, END)

        # configure self.font_list to default
        self.font_list = ['Arial', 12]
        self.text_area.config(font=self.font_list)

        self.title('* Untitled  -  Notepad')


    def open_file(self, *args):
        '''for open a file'''
        self.lift()
        self.file = filedialog.askopenfilename(
            defaultextension='.txt',
            filetypes=[
                ('All Files', '*.*'), ('Text Documents',
                                    '*.txt'), ('Python File', '*.py')
            ],
            parent=self)

        if self.file == '':
            self.file = None
        else:
            self.title(os.path.basename(self.file) + '  -  Notepad')
            self.text_area.delete(1.0, END)

            f = open(self.file, 'r')
            self.text_area.insert(1.0, f.read())

            f.close()

            # configure self.font_list to default
            self.font_list = ['Arial', 12]
            self.text_area.config(font=self.font_list)


    def save(self, *args):
        '''if file exist, this function simply save the changes. else this function ask for saving.'''
        if self.file == None:
            self.lift()
            self.file = filedialog.asksaveasfilename(
                initialfile='Untitled.txt',
                defaultextension='.txt',
                filetypes=[
                    ('All Files', '*.*'), ('Text Document',
                                        '*.txt'), ('Python File', '*.py')
                ],
                parent=self
            )

            if self.file == '':
                self.file = None
            else:
                f = open(self.file, 'w')
                f.write(self.text_area.get(1.0, END))
                f.close()

                self.title(os.path.basename(self.file) + '  -  Notepad')

        else:
            f = open(self.file, 'w')
            f.write(self.text_area.get(1.0, END))
            f.close()


    def save_as(self, *args):
        '''every time ask for saving to a new file.'''
        self.lift()
        self.file = filedialog.asksaveasfilename(
            initialfile='Untitled.txt',
            defaultextension='.txt',
            filetypes=[
                ('All Files', '*.*'), ('Text Document',
                                    '*.txt'), ('Python File', '*.py')
            ],
            parent=self
        )

        if self.file == '':
            self.file = None
        else:
            f = open(self.file, 'w')
            f.write(self.text_area.get(1.0, END))
            f.close()

            self.title(os.path.basename(self.file) + '  -  Notepad')


    def save_all(self):
        self.lift()
        messagebox.showerror('Error', 'No such file or directory!', parent=self)


    def share(self, *args):
        self.lift()
        ans = messagebox.askquestion('Share', 'Share on facebook?', parent=self)

        if ans == 'yes':
            webbrowser.open('facebook.com')


    def exit_editor(self, *args):
        self.lift()
        ans = messagebox.askquestion('Exit', 'Are you sure to Exit?', parent=self)

        if ans == 'yes':
            self.destroy()


    def undo(self, *args):
        try:
            self.text_area.edit_undo()  # just i defined undo=True in self.text_area
        except:  # this undo and redo method show error when nothing to undo and redo.
            pass


    def redo(self, *args):
        try:
            self.text_area.edit_redo()
        except:
            pass


    def cut(self, *args):
        self.text_area.event_generate("<<Cut>>")


    def copy(self, *args):
        self.text_area.event_generate("<<Copy>>")


    def paste(self, *args):
        self.text_area.event_generate("<<Paste>>")


    def expand_editor(self):
        self.geometry('1400x700')


    def resize_editor(self):
        self.geometry('888x555')


    def change_bg(self):
        '''this function ask for changing color, and change'''
        color = colorchooser.askcolor()
        self.text_area.config(bg=color[1])


    def font_color(self):
        '''ask for change color of font'''
        self.lift()
        color = colorchooser.askcolor(parent=self)
        self.text_area.config(fg=color[1])


    def select_font(self, font_name):
        '''this function simply change the font name, the others are not change'''
        self.font_list[0] = font_name

        self.text_area.config(font=self.font_list)


    def f_size(self, size):
        '''change only the size from self.font_list.'''
        self.font_list[1] = size

        self.text_area.config(font=self.font_list)


    def bold_text(self, *args):
        '''get bold text without changing other'''
        if 'bold' in self.font_list:
            self.font_list.remove('bold')

        else:
            self.font_list.append('bold')

        self.text_area.config(font=self.font_list)


    def italic_text(self, *args):
        '''get italic text without change others'''
        if 'italic' in self.font_list:
            self.font_list.remove('italic')

        else:
            self.font_list.append('italic')

        self.text_area.config(font=self.font_list)  # at last time to apply configuration


    def underline_text(self):
        '''for underline'''

        if 'underline' in self.font_list:
            self.font_list.remove('underline')

        else:
            self.font_list.append('underline')

        self.text_area.config(font=self.font_list)


    def qv_clock(self, *args):
        '''this is imported class, this function open a window to show time'''
        clock1 = clock.Clock()
        clock1.main()


    def qv_calculator(self, *args):
        '''imported function, this will called a simple GUI canculator for simple calculations'''
        root = Toplevel()
        calc = calculator.Calculator(root)
        
        
        
    def dict_def(self, *args):
        root = Toplevel()
        definition1 = definition.DictionaryDefinition(root)
        root.mainloop()


    def welcome(self, *args):
        self.lift()
        messagebox.showinfo(
            'Welcome message', 'Welcome to python notepad, this is a notepad made with Python(Tkinter) by @Shakib.', parent=self)


    def documentation(self):
        self.lift()
        messagebox.askokcancel('Unavailable', 'Sorry, documentation not ready.', parent=self)


    def website(self):
        self.lift()
        ans = messagebox.askokcancel('Website', "Open developer's website?", parent=self)
        if ans == True:
            webbrowser.open('https://mdshakib007.github.io/')


    def tutorial(self):
        self.lift()
        messagebox.showwarning(
            'Unavailable', 'Sorry, there is no tutorial at this moment!', parent=self)


    def source_code(self, *args):
        webbrowser.open('https://github.com/mdshakib007/Tkinter-Projects')


    def github(self):
        webbrowser.open('https://github.com/mdshakib007')



    def update(self):
        self.lift()
        messagebox.showwarning(
            'Update', 'You are using the letest version of Text Editor.', parent=self)


    def about(self, *args):
        self.lift()
        messagebox.showinfo(
            'Info', 
    f"""
    Version: 1.01.2
    Date: {datetime.date.today()}
    Language: Python3
    OS: Linux x64
    Sandboxed: No
    """,
    parent=self)


    
if __name__ == '__main__':
    np = NotePad()
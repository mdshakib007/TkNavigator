from tkinter import *
import googletrans
from googletrans import Translator
from tkinter import ttk
import customtkinter as ctk



class PythonTranslator:
    def __init__(self):
        self.root = Tk()
        self.root.title('Translator')
        self.root.geometry('1000x500')
        self.root.resizable(False, False)
        self.root.configure(background='#d4c1e6')

        self.language = googletrans.LANGUAGES
        self.lang_val = list(self.language.values())

        self.create_widgets()

    def create_widgets(self):
        # First combobox
        self.combo1 = ttk.Combobox(self.root,
                                   values=self.lang_val,
                                   font='Roboto 14',
                                   cursor='hand2',
                                   state='readonly',
                                   )
        self.combo1.place(x=110, y=20)
        self.combo1.set('auto')

        self.label1 = Label(self.root, font='Roboto 30 bold',
                            background='white', width=16, borderwidth=0, relief='groove')
        self.label1.place(x=45, y=70)

        # Middle text
        Label(self.root,
                  font=('Roboto', 30, 'bold'),
                  text='TO',
                  bg='#d4c1e6'
                  ).place(x=465, y=70)


        # Second combobox
        self.combo2 = ttk.Combobox(self.root,
                                   values=self.lang_val,
                                   font='Roboto 14',
                                   cursor='hand2',
                                   state='readonly'
                                   )
        self.combo2.place(x=610, y=20)
        self.combo2.set('bangla')

        self.label2 = Label(self.root, font='Roboto 30 bold',
                            background='white', width=16, borderwidth=0, relief='groove')
        self.label2.place(x=545, y=70)

        # First frame for input and output
        self.f1 = Frame(self.root, borderwidth=0)
        self.f1.place(x=45, y=150, width=400, height=200)

        self.text1 = ctk.CTkTextbox(self.f1,
                                    font=('Arial', 20),
                                    height=200,
                                    width=400,
                                    fg_color='white',
                                    text_color='black',
                                    wrap='word')
        self.text1.place(x=0, y=0)

        # Second frame for input and output
        self.f2 = Frame(self.root, borderwidth=0)
        self.f2.place(x=545, y=150, width=400, height=200)

        self.text2 = ctk.CTkTextbox(self.f2,
                                    font=('Arial', 20),
                                    height=200,
                                    width=400,
                                    fg_color='white',
                                    text_color='black',
                                    wrap='word')
        self.text2.place(x=0, y=0)

        # Translate button
        self.btn = ctk.CTkButton(self.root,
                                 text='Translate',
                                 cursor='hand2',
                                 height=50,
                                 width=200,
                                 bg_color='#d4c1e6',
                                 corner_radius=10,
                                 font=('Arial', 20),
                                 command=self.translate_now)
        self.btn.place(x=390, y=400)

    def change_show(self):
        c1 = self.combo1.get()
        c2 = self.combo2.get()
        self.label1['text'] = c1
        self.label2['text'] = c2
        self.root.after(1000, self.change_show)

    def translate_now(self):
        try:
            get_text = self.text1.get(1.0, 'end')
            t1 = Translator()
            translate_text = t1.translate(
                get_text, src=self.combo1.get(), dest=self.combo2.get())
            translate_text = translate_text.text

            self.text2.delete(1.0, 'end')
            self.text2.insert('end', translate_text)

        except Exception as e:
            self.text2.delete(1.0, 'end')
            self.text2.insert(
                'end', 'Error: An error occurred.\n\nPlease check your internet connection and try again.')

    def run(self):
        self.change_show()
        self.root.mainloop()


if __name__ == '__main__':
    tran = PythonTranslator()
    tran.run()
    
    
    
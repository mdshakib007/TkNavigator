import requests
from tkinter import Tk, Menu
from tkinter import messagebox
from customtkinter import CTkEntry, CTkButton, CTkTextbox


class DictionaryDefinition:
    def __init__(self, window):
        self.window = window
        self.window.title("Dictionary Definition")
        self.window.geometry('800x400+200+200')
        self.window.configure(background='white')
        

        def how_work():
            self.window.lift()
            messagebox.showinfo('Help', "This is a text definition for quick needs. You can search any meaningful 'Word' and see the definition.", parent=self.window)

        main_menu = Menu(self.window)
        help_menu = Menu(main_menu, tearoff=0)

        help_menu.add_command(label="How it works", command=how_work)
        help_menu.add_separator()
        help_menu.add_command(label="Exit", command=exit)

        main_menu.add_cascade(menu=help_menu, label='Help', font='Arial 13')
        self.window.config(menu=main_menu)


        # search box
        self.search_box = CTkEntry(self.window,  
                                       placeholder_text='Type To Search...',
                                       width=300, height=50, 
                                       bg_color='#d4c1e6',
                                       text_color='black',
                                       fg_color='white',
                                       corner_radius=0,
                                       border_width=1,
                                       font=('Arial', 20))
        self.search_box.place(x=220, y=50)

        search_button = CTkButton(self.window,
                                      text="Search",
                                      height=50, width=100,
                                      corner_radius=0, 
                                      hover_color='blue',
                                      font=('Arial', 16),
                                      fg_color='skyblue',
                                      text_color='black',
                                      border_width=1,
                                      command=self.search_word)
        search_button.place(x=520, y=50)
        

        self.search_result = CTkTextbox(self.window,
                                            height=200,
                                            font=('Arial', 20),
                                            width=760,
                                            fg_color='white',
                                            border_width=0,
                                            text_color='black'
                                            )
        self.search_result.place(x=20, y=150)
        

    def search_word(self):
        self.search_result.delete('1.0', 'end')

        word = self.search_box.get().lower()
        if word:
            try:
                url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}"
                response = requests.get(url)
                data = response.json()

                if isinstance(data, list) and len(data) > 0:
                    if "meanings" in data[0] and isinstance(data[0]["meanings"], list) and len(data[0]["meanings"]) > 0:
                        if "definitions" in data[0]["meanings"][0] and isinstance(data[0]["meanings"][0]["definitions"], list) and len(data[0]["meanings"][0]["definitions"]) > 0:
                            definition = data[0]["meanings"][0]["definitions"][0]["definition"]
                            self.search_result.insert('end', definition)
                            return

                self.search_result.insert('end', "Sorry, we could not find a definition for that word.")
            except requests.exceptions.RequestException:
                self.search_result.insert('end', "An error occurred while making the request. please check your network connection.")
        else:
            self.search_result.insert('end', "Please enter a word to search.")



if __name__ == '__main__':
    root = Tk()
    d1 = DictionaryDefinition(root)
    root.mainloop()

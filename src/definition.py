import requests
from tkinter import Tk, Menu
from tkinter import messagebox
from customtkinter import CTkEntry, CTkButton, CTkTextbox


class DictionaryDefinition:
    def __init__(self, window):
        self.window = window
        self.window.title("Dictionary Definition")
        self.window.geometry('800x400+200+200')
        self.window.configure(background='#1f1f1f')  # Dark background

        # Menu bar
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

        # Search box
        self.search_box = CTkEntry(self.window,  
                                   placeholder_text='Type To Search...',
                                   width=300, height=50, 
                                   bg_color='#1f1f1f',
                                   text_color='#d4d4d4',  # Light text for dark theme
                                   fg_color='#2e2e2e',
                                   corner_radius=5,
                                   border_width=1,
                                   font=('Arial', 20))
        self.search_box.place(x=220, y=50)

        # Search button
        search_button = CTkButton(self.window,
                                  text="Search",
                                  height=50, width=100,
                                  corner_radius=5, 
                                  hover_color='#007acc',
                                  font=('Arial', 18),
                                  fg_color='#007acc',  # Button color for dark theme
                                  text_color='white',
                                  border_width=1,
                                  command=self.search_word)
        search_button.place(x=520, y=50)

        # Textbox for displaying results
        self.search_result = CTkTextbox(self.window,
                                        height=200,
                                        font=('Arial', 18),
                                        width=760,
                                        fg_color='#2e2e2e',  # Darker textbox background
                                        border_width=1,
                                        text_color='#d4d4d4',  # Light text for dark theme
                                        corner_radius=5)
        self.search_result.place(x=20, y=150)

    def search_word(self):
        self.search_result.delete('1.0', 'end')

        word = self.search_box.get().strip().lower()
        if not word:
            self.search_result.insert('end', "Please enter a word to search.")
            return

        url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if isinstance(data, list) and data:
                meaning = data[0].get("meanings", [])
                if meaning and "definitions" in meaning[0]:
                    definition = meaning[0]["definitions"][0].get("definition", "No definition found.")
                    self.search_result.insert('end', definition)
                else:
                    self.search_result.insert('end', "No definitions available.")
            else:
                self.search_result.insert('end', "Sorry, we could not find a definition for that word.")
        
        except requests.exceptions.RequestException:
            self.search_result.insert('end', "Error: Unable to fetch data. Please check your network.")
        except Exception as e:
            self.search_result.insert('end', f"An error occurred: {str(e)}")


if __name__ == '__main__':
    root = Tk()
    d1 = DictionaryDefinition(root)
    root.mainloop()

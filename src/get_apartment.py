from tkinter import Tk, Frame, Label, StringVar
from tkinter.ttk import Combobox
import customtkinter as ctk
from tabulate import tabulate
import variable
from pandas import read_csv


class Apartment:
    @staticmethod
    def find_apartment():
        
        # get locations from variable file
        locations = variable.values

        data = read_csv('apartment.csv')  # read csv file

        # functions
        def search():
            selected_location = comboVar.get()
            if selected_location != 'Select Area...':
                # Filter the data based on the selected location
                filtered_data = data[data['Location'] == selected_location]

                if not filtered_data.empty:
                    # Format the filtered data as a table
                    table = tabulate(filtered_data, headers='keys', tablefmt='psql')

                    # Display the table in the text area
                    text_area.delete(1.0, 'end')
                    text_area.configure(font=('Courier', 20))  # Adjust font size for readability
                    text_area.insert('end', table)
                else:
                    # If no data is available for the selected location, display a message
                    text_area.delete(1.0, 'end')
                    text_area.insert('end', "[No data available for the selected location.]")
            else:
                # If no location is selected, clear the text area
                text_area.delete(1.0, 'end')
                text_area.insert('end', "[Please search an area to find your best match!]")
            
        # Create the main window
        root = Tk()
        root.title("Dhaka's Apartment Prices")
        root.geometry('1200x600')
        root.minsize(400, 200)
        root.config(background='#1E1E1E')  # Dark background

        f1 = Frame(root, bg='#2E2E2E', height=100)  # Darker frame
        f1.pack(fill='x')

        Label(f1, text="Dhaka's Apartment Price.", bg='#2E2E2E',
              font=("Arial", 25), fg='white').pack(padx=20, pady=10, side='left')  # White text

        # Search button
        ctk.CTkButton(f1, width=100, height=40, corner_radius=10, text="Search",
                       font=('Arial', 19, 'bold'), cursor='hand2', hover_color='#456745',
                       fg_color='#007BFF', text_color='white', command=search).pack(padx=10, pady=10, side='right')

        # Search box
        comboVar = StringVar(f1, value='Select Area...')
        combo = Combobox(f1, values=locations, width=50, height=20, textvariable=comboVar,
                         cursor='hand2', background='#2E2E2E', foreground='white')
        combo.pack(padx=1, pady=10, side='right')

        # Text area
        text_area = ctk.CTkTextbox(root, font=('Courier', 20), fg_color='#2E2E2E',
                                    text_color='white', height=300)  # Darker textbox
        text_area.pack(padx=10, pady=10, fill='both')

        root.mainloop()


if __name__ == '__main__':
    a = Apartment()
    a.find_apartment()

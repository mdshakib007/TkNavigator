from tkinter import *
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

        data = read_csv('apartment.csv') # read csv file


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
                    text_area.delete(1.0, END)
                    text_area.configure(font=('Courier', 20))
                    text_area.insert(END, table)
                    
                else:
                    # If no data is available for the selected location, display a message
                    text_area.delete(1.0, END)
                    text_area.insert(END, "[No data available for the selected location.]")
            else:
                # If no location is selected, clear the text area
                text_area.delete(1.0, END)
                text_area.insert(END, "[Please search an area to find your best match!]")
            
                
        root = Tk()
        root.title("Dhaka's Apartment Prices")
        root.geometry('1200x600')
        root.minsize(400, 200)
        root.config(background='#aa67ff')

        f1 = Frame(root, bg='orange', height=100)
        f1.pack(fill='x')

        Label(f1, text="Dhaka's Apartment Price.", bg='orange',
            font=("Arial", 25)).pack(padx=20, pady=10, side='left')


        # search button
        ctk.CTkButton(f1, width=100, height=40, corner_radius=10, text="Search",
                    font=('Arial', 19, 'bold'), cursor='hand2', hover_color='#456745',
                    text_color='white', command=search).pack(padx=10, pady=10, side='right')

        # search box
        comboVar = StringVar(f1, value='Select Area...')

        Combobox(f1, values=locations, width=50, height=40, textvariable=comboVar,
                cursor='hand2').pack(padx=1, pady=10, side='right')


        # Text area
        text_area = ctk.CTkTextbox(root, font=('Arial', 20), fg_color='white',
                    text_color='black', height=1000)
        text_area.pack(padx=10, pady=10, fill='both')



        root.mainloop()



if __name__ == '__main__':
    a = Apartment()
    a.find_apartment()

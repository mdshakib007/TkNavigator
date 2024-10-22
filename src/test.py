from tkinter import Tk, Toplevel, Button
from tkinter.messagebox import showinfo

def open_child_window():
    child_window = Toplevel(root)
    child_window.title("Child Window")
    child_window.geometry("600x400")
    
    def showmessage():
        child_window.lift()
        showinfo('test' ,'this is child', parent=child_window)
    
    Button(child_window, text='Show Message',command=showmessage).pack()


root = Tk()
root.title("Main Window")
root.geometry("600x400")

button = Button(root, text="Open Child Window", command=open_child_window)
button.pack(pady=50)

root.mainloop()


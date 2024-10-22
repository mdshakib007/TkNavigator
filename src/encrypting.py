from tkinter import Tk, Toplevel, Label
from customtkinter import CTkTextbox, CTkButton, CTkFrame, CTkEntry
import base64
from tkinter.messagebox import showerror


class EncryptDecrypt:
    
    @staticmethod
    def encrypt_decrypt():
        root = Tk()
        root.title('Data Encryption App')
        root.geometry('700x660')
        root.configure(background='#2c2c2c')  # Dark background
        root.resizable(False, False)

        ### All executable functions
        def encryptdata():
            password_data = password.get()
            
            if password_data == '1234':
                screen1 = Toplevel()
                screen1.title('Encryption')
                screen1.geometry('600x300')
                screen1.config(background='#2c2c2c')  # Dark background
                
                msg = text_area.get(1.0, 'end')
                
                encode_msg = msg.encode('ascii')
                b64_bytes = base64.b64encode(encode_msg)
                encrypt = b64_bytes.decode('ascii')
                
                Label(screen1, text='ENCRYPT',
                    font='Arial 16',
                    fg='#e6e6e6',  # Light text
                    bg='#2c2c2c').place(x=10, y=1)
                
                text_encode = CTkTextbox(screen1,
                                font=('Arial', 20),
                                width=550, height=260, 
                                fg_color='#3b3b3b',  # Slightly lighter background for textbox
                                border_width=0,
                                text_color='#e6e6e6')  # Light text color
                text_encode.place(x=10, y=30)
                
                text_encode.insert('end', encrypt)
                
                
            elif password_data == '':
                root.lift()
                showerror('Error', 'Please Enter Root Password.', parent=root)

            else:
                root.lift()
                showerror('Password', 'Invalid Password!', parent=root)

        def decryptdata():
            password_data = password.get()
            
            if password_data == '1234':
                screen2 = Toplevel()
                screen2.title('Decryption')
                screen2.geometry('600x300')
                screen2.config(background='#2c2c2c')
                
                msg = text_area.get(1.0, 'end')
                decode_msg = msg.encode('ascii')
                b64_bytes = base64.b64decode(decode_msg)
                decrypt = b64_bytes.decode('ascii')
                
                Label(screen2, text='DECRYPT',
                    font='Arial 16',
                    fg='#e6e6e6',
                    bg='#2c2c2c').place(x=10, y=1)
                
                text_encode = CTkTextbox(screen2,
                                font=('Arial', 20),
                                width=550, height=260, 
                                fg_color='#3b3b3b', 
                                border_width=0,
                                text_color='#e6e6e6')
                text_encode.place(x=10, y=30)
                
                text_encode.insert('end', decrypt)
                
            elif password_data == '':
                root.lift()
                showerror('Password', 'Invalid Password!', parent=root)

            else:
                root.lift()
                showerror('Password', 'Invalid Password!', parent=root)

        def reset_window():
            text_area.delete(1.0, 'end')
            password.delete(0, 'end')

        # Title label
        Label(root, text='Enter Text To Encrypt or Decrypt:',
              font=('Arial', 14),
              fg='#e6e6e6',  # Light text color
              background='#2c2c2c').place(x=15, y=50)

        # Text fill frame
        text_frame = CTkFrame(root, height=300, width=670, fg_color='#2c2c2c')
        text_frame.place(x=15, y=80)

        text_area = CTkTextbox(text_frame, height=300, width=670, font=('Arial', 25),
                               fg_color='#3b3b3b',  # Slightly lighter dark for the textbox
                               text_color='#e6e6e6')  # Light text color
        text_area.place(x=1, y=1)

        # Password entry
        password = CTkEntry(root, width=670, font=('Arial', 20), height=60,
                            border_width=0, placeholder_text="Enter Root Password To Encrypt Or Decrypt...",
                            corner_radius=5, fg_color='#3b3b3b', text_color='#e6e6e6', show='*')
        password.place(x=15, y=430)

        # Decrypt button
        decrypt_data = CTkButton(root, text='DECRYPT', width=200, height=40,
                                 font=('Arial', 18), corner_radius=5,
                                 bg_color='#2c2c2c', hover_color='#1e1e1e',  # Dark hover effect
                                 fg_color='#00bd56', text_color='#e6e6e6', cursor='hand2',
                                 command=decryptdata)
        decrypt_data.place(x=120, y=500)

        # Encrypt button
        encrypt_data = CTkButton(root, text='ENCRYPT', width=200, height=40,
                                 font=('Arial', 18), corner_radius=5,
                                 bg_color='#2c2c2c', hover_color='#1e1e1e',
                                 fg_color='#ed3833', text_color='#e6e6e6', cursor='hand2',
                                 command=encryptdata)
        encrypt_data.place(x=370, y=500)

        # Reset button
        reset_data = CTkButton(root, text='RESET', width=450, height=40,
                               font=('Arial', 18), corner_radius=5,
                               bg_color='#2c2c2c', hover_color='#1e1e1e', cursor='hand2',
                               fg_color='#3b3b3b', text_color='#e6e6e6',  # Matches dark theme
                               command=reset_window)
        reset_data.place(x=120, y=560)

        root.mainloop()


if __name__ == '__main__':
    EncryptDecrypt().encrypt_decrypt()

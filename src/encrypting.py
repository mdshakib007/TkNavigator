from tkinter import *
from customtkinter import CTkTextbox, CTkButton, CTkFrame, CTkEntry
import base64


class EncryptDecrypt:
    
    @staticmethod
    def encrypt_decrypt():
        root = Tk()
        root.title('Data Encryption App')
        root.geometry('700x660')
        root.configure(background='#bf9ee8')
        root.resizable(False, False)


        ### all executable functions
        def encryptdata():
            password_data = password.get()
            
            if password_data == '1234':
                screen1 = Toplevel()
                screen1.title('Encryption')
                screen1.geometry('600x300')
                screen1.config(background='#ed3833')
                
                msg = text_area.get(1.0, 'end')
                
                encode_msg = msg.encode('ascii')
                b64_bytes = base64.b64encode(encode_msg)
                encrypt = b64_bytes.decode('ascii')
                
                Label(screen1, text='ENCRYPT',
                    font='Arial 16',
                    fg='white',
                    bg='#ed3833').place(x=10, y=1)
                
                text_encode = CTkTextbox(screen1,
                                font=('Arial', 20),
                                width=550, height=260, 
                                fg_color='white', 
                                border_width=0,
                                text_color='black')
                text_encode.place(x=10, y=30)
                
                text_encode.insert('end', encrypt)
                
                
            elif password_data == '':
                show_['text'] = "Please Enter Root Password."
                
            else:
                show_['text'] = "Invalid Password."
                



        def decryptdata():
            password_data = password.get()
            
            if password_data == '1234':
                screen2 = Toplevel()
                screen2.title('Decryption')
                screen2.geometry('600x300')
                screen2.config(background='#00bd56')
                
                msg = text_area.get(1.0, 'end')
                decode_msg = msg.encode('ascii')
                b64_bytes = base64.b64decode(decode_msg)
                decrypt = b64_bytes.decode('ascii')
                
                Label(screen2, text='DECRYPT',
                    font='Arial 16',
                    fg='white',
                    bg='#00bd56').place(x=10, y=1)
                
                text_encode = CTkTextbox(screen2,
                                font=('Arial', 20),
                                width=550, height=260, 
                                fg_color='white', 
                                border_width=0,
                                text_color='black')
                text_encode.place(x=10, y=30)
                
                text_encode.insert('end', decrypt)
                
                
            elif password_data == '':
                show_['text'] = "Please Enter Root Password."
                
            else:
                show_['text'] = "Invalid Password."
                



        def reset_window():
            text_area.delete(1.0, 'end')
            password.delete(0, 'end')




        # title label
        Label(root, text='Enter Text To Encrypt or Decrypt:',
            font=('Arial', 14),
            background='#bf9ee8'
            ).place(x=15, y=50)



        # text fill frame
        text_frame = CTkFrame(root, 
                        height=300, 
                        width=670,
                        fg_color='#bf9ee8'
                        )

        text_frame.place(x=15, y=80)

        text_area = CTkTextbox(text_frame,
                        height=300,
                        width=670,
                        font=('Arial', 25),
                        fg_color='#624f73'
                        )
        text_area.place(x=1, y=1)



        ## password entry
        password = CTkEntry(root, width=670,
                                    font=('Arial', 20),
                                    height=60,
                                    border_width=0,
                                    placeholder_text="Enter Root Password To Encrypt Or Decrypt...",
                                    corner_radius=5,
                                    fg_color='#624f73',
                                    text_color='black',
                                    show='*'
                                    )
        password.place(x=15, y=430)


        # Decrypt
        decrypt_data = CTkButton(root, text='DECRYPT', 
                            width=200, height=40,
                            font=('Arial', 18),
                            corner_radius=5,
                            bg_color='#bf9ee8', 
                            hover_color='blue',
                            fg_color='#00bd56',
                            cursor='hand2',
                            command=decryptdata
                            )
        decrypt_data.place(x=120, y=500)



        # encrypt Data
        encrypt_data = CTkButton(root, text='ENCRYPT', 
                            width=200, height=40,
                            font=('Arial', 18),
                            corner_radius=5,
                            bg_color='#bf9ee8', 
                            hover_color='blue',
                            fg_color='#ed3833',
                            cursor='hand2',
                            command=encryptdata
                            )
        encrypt_data.place(x=370, y=500)


        # reset data
        reset_data = CTkButton(root, text='RESET', 
                            width=450, height=40,
                            font=('Arial', 18),
                            corner_radius=5,
                            bg_color='#bf9ee8', 
                            hover_color='black',
                            cursor='hand2',
                            command=reset_window
                            )
        reset_data.place(x=120, y=560)


        show_ = Label(root, bg='#bf9ee8', fg='red',
                    font='Arial 15')
        show_.place(x=200, y=610)


        root.mainloop()



if __name__ == '__main__':
    EncryptDecrypt().encrypt_decrypt()
    
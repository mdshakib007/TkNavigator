from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import customtkinter as ctk




class VideoDownloader:
    def __init__(self):
        self.root = Tk()
        self.root.title("Youtube Video Downloader")
        self.root.geometry('660x500+600+50')
        self.root.resizable(False, False)
        
        self.plot_all()
        
        self.root.mainloop()
    
    
    def plot_all(self):
        
        # Frame for entry and button
        self.frame1 = ctk.CTkFrame(self.root, height=400,
                            width=600, 
                            fg_color='#f07b5d',
                            corner_radius=10,
                            border_width=0,
                            )
        self.frame1.place(x=30, y=30)


            
        ### how it's work
        self.how = ctk.CTkButton(self.frame1, text="How it's work?",
                        command=self.how_works,
                        cursor='hand2',
                        fg_color='#f07b5d',
                        text_color='blue',
                        border_width=0,
                        hover=False)
        self.how.place(x=230, y=140)



        ctk.CTkLabel(self.frame1, text='Download Highest Resolution Video!',
                    fg_color='#f07b5d',
                    text_color='black',
                    font=('Arial', 22)).place(x=110, y=10)

        self.link_entry = ctk.CTkEntry(self.frame1, width=450,
                                height=40, 
                                fg_color='white',
                                text_color='blue',
                                border_width=0,
                                placeholder_text='Enter Youtube Video Link...',
                                font=('Arial', 16), 
                                )
        self.link_entry.place(x=70, y=40)


        
        ctk.CTkButton(self.frame1,
                    fg_color='#f07b5d', 
                    cursor='hand2',
                    text='Download',
                    text_color='black',
                    width=50,
                    hover_color='skyblue',
                    font=('Arial', 18, 'bold'),
                    corner_radius=100,
                    command=self.download_video).place(x=170, y=100)


        # Button for show info
        
        ctk.CTkButton(self.frame1,
            fg_color='#f07b5d',
            cursor='hand2',
            text='Information',
            text_color='black',
            width=50,
            hover_color='skyblue',
            font=('Arial', 18, 'bold'),
            corner_radius=100,
            command=self.information).place(x=320, y=100)



        # Label for show output message
        self.lbl_output = ctk.CTkTextbox(self.frame1,
                                    font=('Arial', 18), 
                                    fg_color='#f07b5d',
                                    width=565,
                                    border_color='black',
                                    border_spacing=5,
                                    border_width=1,
                                    height=200,
                                    text_color='black')
        self.lbl_output.place(x=20, y=180)
        self.lbl_output.insert(1.0, "[ This can provide you Highest Resolution of download ]")



    def run(self):
        self.root.mainloop()



    def how_works(self):
        messagebox.showinfo("How it's work", "This is just a YouTube video downloader. You need to put video link in the entry widget and press 'information' to see details. Then press 'download' and 'yes' to download video in Highest resolution.")



    def download_video(self):
        link = self.link_entry.get()
        
        try:
            video = YouTube(link)
        except Exception as e:
            self.lbl_output.delete('1.0', END)
            self.lbl_output.insert(END, "[ Invalid Link ]")
            return
        
        self.information()

        while True:
            try:
                choice = messagebox.askquestion("Confirmation", "Do you want to download the video?")
                
                if choice == "yes":
                    self.lbl_output.delete('1.0', END)
                    self.lbl_output.insert(END, "[ Downloading. Please wait... ]")
                    
                    stream = video.streams.get_highest_resolution()
                    stream.download()
                    
                    self.lbl_output.delete('1.0', END)
                    self.lbl_output.insert(END, "[ Download complete. ]")
                    break
                
                elif choice == "no":
                    self.lbl_output.delete('1.0', END)
                    self.lbl_output.insert(END, "[ Download canceled. ]")
                    break
                
                else:
                    self.lbl_output.delete('1.0', END)
                    self.lbl_output.insert(END, "[ Download failed. ]")
                    
                    
            except:
                self.lbl_output.delete('1.0', END)
                self.lbl_output.insert(END, "[ An error occurred. Download failed. ]")
                break
            
            
        
    def information(self):
        link = self.link_entry.get()

        try:
            video = YouTube(link)
        except Exception as e:
            self.lbl_output.delete('1.0', END)
            self.lbl_output.insert(END, "[ Invalid Link ]")
            return

        txt = f"Title     : '{video.title}'\n"

        if video.length is not None:
            txt += f"Length : {video.length // 60}m {video.length % 60}s\n"
        else:
            txt += "Length : N/A\n"

        if video.rating is not None:
            txt += f"Rating  : {video.rating:.2f}/5.00\n"
        else:
            txt += "Rating  : N/A\n"

        # Get highest resolution
        stream = video.streams.get_highest_resolution()
        highest_resolution = stream.resolution

        txt += f"Views   : {video.views}\n"

        # Get size of highest resolution
        total_size = stream.filesize
        size_in_mb = total_size / (1024 * 1024)
        txt += f"Size      : {size_in_mb:.2f} MB, {highest_resolution}"

        self.lbl_output.delete('1.0', END)
        self.lbl_output.insert(END, txt)

        

        

if __name__ == '__main__':
    v1 = VideoDownloader()
    v1.run()
    
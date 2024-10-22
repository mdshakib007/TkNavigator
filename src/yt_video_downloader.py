from tkinter import Tk
from tkinter.messagebox import showinfo, askquestion
from pytube import YouTube
import customtkinter as ctk

class VideoDownloader:
    def __init__(self):
        # Initialize the main window
        self.root = Tk()
        self.root.title("YouTube Video Downloader")
        self.root.geometry('700x400+600+50')
        self.root.resizable(False, False)
        self.root.configure(background='#2E2E2E')

        # Set dark appearance mode and theme
        ctk.set_appearance_mode("dark")  # Use dark mode
        ctk.set_default_color_theme("dark-blue")  # Set a suitable color theme
        

        self.plot_all()  # Create UI components
        
        self.root.mainloop()

    def plot_all(self):
        # Title label
        title_label = ctk.CTkLabel(self.root, text='Download Highest Resolution Video!', font=('Arial', 24))
        title_label.pack(pady=(30, 10))

        # Entry for YouTube link
        self.link_entry = ctk.CTkEntry(self.root, width=400, height=40, 
                                        placeholder_text='Enter YouTube Video Link...',
                                        font=('Arial', 16))
        self.link_entry.pack(pady=10)

        # Download button
        download_button = ctk.CTkButton(self.root, text='Download', height=40,
                                         command=self.download_video, 
                                         font=('Arial', 18, 'bold'))
        download_button.pack(pady=10)

        # Information button
        info_button = ctk.CTkButton(self.root, text='Information', height=40,
                                     command=self.information, 
                                     font=('Arial', 18, 'bold'))
        info_button.pack(pady=10)

        # Output label for messages
        self.lbl_output = ctk.CTkLabel(self.root, text="", font=('Arial', 16), text_color="white")
        self.lbl_output.pack(pady=(20, 0))

    def how_works(self):
        self.root.lift()
        showinfo("How it works", "This is just a YouTube video downloader. Enter the video link and click 'Information' to see details, then 'Download' to download the highest resolution.", parent=self.root)

    def download_video(self):
        link = self.link_entry.get()

        try:
            video = YouTube(link)
        except Exception:
            self.lbl_output.configure(text="[ Invalid Link ]")
            return

        self.information()

        choice = askquestion("Confirmation", "Do you want to download the video?", parent=self.root)
        
        if choice == "yes":
            self.lbl_output.configure(text="[ Downloading. Please wait... ]")
            try:
                stream = video.streams.get_highest_resolution()
                stream.download()
                self.lbl_output.configure(text="[ Download complete. ]")
            except Exception:
                self.lbl_output.configure(text="[ Download failed. ]")
        else:
            self.lbl_output.configure(text="[ Download canceled. ]")

    def information(self):
        link = self.link_entry.get()

        try:
            video = YouTube(link)
        except Exception as e:
            self.lbl_output.configure(text="[ Invalid Link or Unable to fetch video details ]")
            return

        try:
            details = f"Title     : '{video.title}'\n"
            details += f"Length    : {video.length // 60}m {video.length % 60}s\n"
            details += f"Rating    : {video.rating:.2f}/5.00\n"
            details += f"Views     : {video.views}\n"

            stream = video.streams.get_highest_resolution()
            total_size = stream.filesize / (1024 * 1024)  # Convert bytes to MB
            details += f"Size      : {total_size:.2f} MB, {stream.resolution}"

            self.lbl_output.configure(text=details)
        except KeyError:
            self.lbl_output.configure(text="[ Error retrieving video details. Try again later. ]")
        except Exception as e:
            self.lbl_output.configure(text="[ An unexpected error occurred. ]")


if __name__ == '__main__':
    VideoDownloader()

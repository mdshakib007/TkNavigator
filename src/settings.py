from tkinter import *
import customtkinter as ctk 


class Settings(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('900x600')
        self.title('Settings  -  Tiny-iDE')
        self.configure(background='white')
        
        # call main method
        self.main()
        
        
        self.mainloop()
        
        
    def main(self):
        '''This function return the tabview'''
        tabs = ctk.CTkTabview(self,
                              width=850, height=550, 
                              fg_color='grey', 
                              bg_color='white',
                              corner_radius=10,
                              text_color='black',
                              segmented_button_fg_color='white',
                              segmented_button_selected_color='#8accff',
                              segmented_button_selected_hover_color='#b29ee8',
                              segmented_button_unselected_color='white',
                              segmented_button_unselected_hover_color='#b29ee8',
                              )
        tabs.pack(padx=10, pady=20)
        
        # add tabs
        add_github = tabs.add('GitHub Page')
        profiles = tabs.add('Profile')
        appearance = tabs.add('Appearance')
        key_shortcuts = tabs.add('Keyboard Shortcuts')
        report_issue = tabs.add('Report')
        share_app = tabs.add('Share')

        
        # call all methods
        self.add_github_content(add_github)
        self.profile_content(profiles)
        self.appearance_content(appearance)
        self.keyboard_shortcuts(key_shortcuts)
        self.report_content(report_issue)
        self.share_content(share_app)
        
        
        
    # define the methods for contents
    def add_github_content(self, tab1):
        '''this method add all necessary element of the topic of github'''
        def get_link():
            g_link = link.get()
            show_output['text'] = g_link
            
        ctk.CTkLabel(tab1, text='Link Your GitHub Account To Easy Access!',
                     font=('Arial', 24, 'underline'),
                     text_color='black').pack(padx=5, pady=10)
        
        ## entry box
        link = ctk.CTkEntry(tab1, fg_color='black',
                     placeholder_text='Enter Your GitHub Link...',
                     text_color='blue',
                     height=40,
                     width=300,
                     corner_radius=30,
                     font=('Arial', 18)
                     )
        link.pack(padx=10, pady=30)
        
        
        ## button
        ctk.CTkButton(tab1, text='ADD', 
                      width=150, height=40,
                      font=('Arial', 18, 'bold'),
                      corner_radius=100,
                      bg_color='grey',
                      hover_color='#b29ee8',
                      text_color='black',
                      command=get_link
                      ).pack(padx=10, pady=0)
        
        
        # show output label 
        f1 = ctk.CTkFrame(tab1)
        f1.pack(padx=5, pady=70)
        
        show_output = Label(f1,
                            bg='grey', fg='black', 
                            font='Arial 16')
        show_output.pack()
        
        
        
    
    def profile_content(self, tab2):
        pass
    
    
    def appearance_content(self, tab3):
        pass
    
    
    def keyboard_shortcuts(self, tab4):
        pass
    
    def report_content(self, tab5):
        pass
    
    
    def share_content(self, tab6):
        pass
    
    
    
    
        
if __name__ == '__main__':
    Settings()
    
    
import customtkinter as ctk
from settings import *

class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__(fg_color=GREEN)
        # Setup
        self.iconbitmap('empty.ico')
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.resizable(False,False)

        # Run
        self.mainloop()



App('', (400,400))
import customtkinter as ctk
from settings import *

class App(ctk.CTk):
    def __init__(self, title, size):

        # Main Setup
        super().__init__(fg_color=GREEN)
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.resizable(False, False)
        self.iconbitmap('empty.ico')

        # Layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1,2,3), weight=1, uniform='a')

        # Data
        self.height_int = ctk.IntVar(value=170)
        self.weight_float = ctk.DoubleVar(value=65)
        self.BMI_string = ctk.StringVar()
        self.update_BMI()

        # Tracing
        self.height_int.trace('w', self.update_BMI)
        self.weight_float.trace('w', self.update_BMI)

        # Widgets
        ResultText(self, self.BMI_string)
        WeightInput(self, self.weight_float)
        HeightInput(self, self.height_int)
        UnitSwitcher(self)

        # Run
        self.mainloop()

    def update_BMI(self, *args):
        height_meter = self.height_int.get() / 100
        weight_kg = self.weight_float.get()
        BMI_result = round(weight_kg / (height_meter**2), 2)
        self.BMI_string.set(BMI_result)

class ResultText(ctk.CTkLabel):
    def __init__(self, parent, bmi_string):
        font = ctk.CTkFont(family=FONT, size=MAIN_TEXT_SIZE, weight='bold')
        super().__init__(master=parent, text=22.5, font=font, text_color=WHITE, textvariable=bmi_string)
        self.grid(column=0, row=0, rowspan=2, sticky='nswe')

class WeightInput(ctk.CTkFrame):
    def __init__(self, parent, weight_float):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(column=0, row=2, sticky='nswe', padx=10, pady=10)
        self.weight_float = weight_float

        # Layout
        self.columnconfigure((0,4), weight=2, uniform='b')
        self.columnconfigure((1,3), weight=1, uniform='b')
        self.columnconfigure((2), weight=1, uniform='b')
        self.rowconfigure((0), weight=1, uniform='b')

        # Text
        font = ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, text='70Kg', text_color=BLACK, font=font)
        label.grid(row=0, column = 2)

        # Buttons
        def create_button(pos, text, st):
            button = ctk.CTkButton(master=self, text=str(text), hover_color=GRAY, fg_color=L_GRAY, text_color=BLACK, corner_radius=6)
            button.grid(column=pos[0], row=pos[1], padx=8, pady=8, sticky=st)
            return button
        big_minnus_btn = create_button((0, 0), '-', st='nswe')
        sml_minnus_btn = create_button((1, 0), '-', st='')
        big_plus_btn = create_button((4, 0), '+', st='nswe')
        small_plus_btn = create_button((3, 0), '+', st='')

        big_minnus_btn.configure(command= lambda : self.update_weight(('minus', 'large')))
        sml_minnus_btn.configure(command= lambda : self.update_weight(('minus', 'small')))
        big_plus_btn.configure(command= lambda : self.update_weight(('plus', 'large')))
        small_plus_btn.configure(command= lambda : self.update_weight(('plus', 'small')))

    def update_weight(self, info=None):
        amount = 1 if info[1] == 'large' else 0.1
        if info[0] == 'plus':
            self.weight_float.set(round((self.weight_float.get() + amount), 2)) 
        else:
            self.weight_float.set(round((self.weight_float.get() - amount), 2)) 
        
class HeightInput(ctk.CTkFrame):
    def __init__(self, parent, height_int):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(row = 3, column=0, sticky='nswe', padx=10, pady=10)

        # Widgets
        slider = ctk.CTkSlider(
            master = self, 
            command=self.update_txt,
            button_color=GREEN,
            button_hover_color=GRAY,
            progress_color=GREEN,
            fg_color=L_GRAY,
            variable=height_int,
            from_=100,
            to = 250)
        slider.pack(side='left', fill='x', expand=True, pady=10, padx=10)

        self.output_txt_str = ctk.StringVar()
        self.update_txt(height_int.get())
        output_txt = ctk.CTkLabel(
            master=self,
            textvariable=self.output_txt_str, 
            text='1.80m', 
            text_color=BLACK, 
            font=ctk.CTkFont(
                family=FONT, 
                size=INPUT_FONT_SIZE))
        output_txt.pack(side='left', padx=20)

    def update_txt(self,amount):
        text_str = str(int(amount))
        meter = text_str[0]
        cm = text_str[1:]
        self.output_txt_str.set(f'{meter}.{cm}m')

class UnitSwitcher(ctk.CTkLabel):
    def __init__(self, parent):
        super().__init__(
            master=parent,
            text='metric',
            text_color=DARK_GREEN,
            font=ctk.CTkFont(family=FONT, size=SWITCH_FONT_SIZE, weight='bold'))
        self.place(relx=0.9, rely=0.01, anchor='n')

if __name__ == '__main__':
    App('', (400,400))
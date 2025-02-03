from customtkinter import *

import os

os.environ['TCL_LIBRARY'] = r"C:\Users\Família\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Família\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

app = CTk()

combobox_var = StringVar(value="option 2")  # set initial value

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = CTkComboBox(master=app,
values=["option 1", "option 2"], command=combobox_callback, variable=combobox_var)
combobox.pack(padx=20, pady=10)

app.mainloop()
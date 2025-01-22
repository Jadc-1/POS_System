import __init__
#código da biblioteca os para corrigir erro de importação do customtkinter
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\Família\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Família\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("856x645")

set_appearance_mode("light")



sidebar_frame = CTkFrame(master=app, fg_color="#69F0AE",  width=250, height=650, corner_radius=0) # Criei a sidebar, que tem como pai o app
sidebar_frame.pack_propagate(0) ## Não deixa o conteúdo da sidebar aumentar o tamanho dela
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("images\logo_2.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(120, 120))

CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")


sidebar_inventory = CTkButton(master= sidebar_frame, text="Inventory", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font =("Roboto", 15, "bold"), hover_color="#007900").pack(pady=(150,10), padx=30, anchor="center")
sidebar_sales_report = CTkButton(master=sidebar_frame, text="Sales Report", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font =("Roboto", 15, "bold"), hover_color="#007900").pack(pady=10, padx=30, anchor="center") 
sidebar_employees = CTkButton(master=sidebar_frame, text= "Employees", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font =("Roboto", 15, "bold"), hover_color="#007900").pack(pady=10, padx=30, anchor="center") 
sidebar_cash_closing = CTkButton(master=sidebar_frame, text="Cash Closing", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font =("Roboto", 15, "bold"), hover_color="#007900").pack(pady=10, padx=30, anchor="center") 
sidebar_pos = CTkButton(master=sidebar_frame, text = "Point of Sale System", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font =("Roboto", 15, "bold"), hover_color="#007900").pack(pady=10, padx=30, anchor="center") 


app.mainloop()
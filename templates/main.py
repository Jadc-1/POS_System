import __init__
#código da biblioteca os para corrigir erro de importação do customtkinter
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\Família\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Família\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("856x645")
app.title("UniFruti")
app.iconbitmap(r"images\logo_2.ico")
set_appearance_mode("light")



sidebar_frame = CTkFrame(master=app, fg_color="#69F0AE",  width=250, height=650, corner_radius=0) # Criei a sidebar, que tem como pai o app
sidebar_frame.pack_propagate(0) ## Não deixa o conteúdo da sidebar aumentar o tamanho dela
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open(r"images\logo_2.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(120, 120))

CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

def button_onclick(button):
    button.configure(fg_color="#007900")

sidebar_inventory = CTkButton(master= sidebar_frame, text="Inventory", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font =("Roboto", 15, "bold"), hover_color="#007900", command=lambda: button_onclick(sidebar_inventory)) ##O lambda permite que só execute essa função caso eu aperte esse botão
sidebar_inventory.pack(pady=(150,10), padx=30, anchor="center")

sidebar_sales_report = CTkButton(master=sidebar_frame, text="Sales Report", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font =("Roboto", 15, "bold"), hover_color="#007900", command=lambda: button_onclick(sidebar_sales_report))
sidebar_sales_report.pack(pady=10, padx=30, anchor="center") 

sidebar_employees = CTkButton(master=sidebar_frame, text= "Employees", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font =("Roboto", 15, "bold"), hover_color="#007900", command=lambda: button_onclick(sidebar_employees))
sidebar_employees.pack(pady=10, padx=30, anchor="center") 

sidebar_cash_closing = CTkButton(master=sidebar_frame, text="Cash Closing", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font =("Roboto", 15, "bold"), hover_color="#007900", command=lambda: button_onclick(sidebar_cash_closing))
sidebar_cash_closing.pack(pady=10, padx=30, anchor="center") 

sidebar_pos = CTkButton(master=sidebar_frame, text = "Point of Sale System", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font =("Roboto", 15, "bold"), hover_color="#007900", command=lambda: button_onclick(sidebar_pos))
sidebar_pos.pack(pady=10, padx=30, anchor="center") 



app.mainloop()
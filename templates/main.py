import __init__
#código da biblioteca os para corrigir erro de importação do customtkinter
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\Família\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Família\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

import customtkinter as ctk
from PIL import Image
from templates.inventory_app import inventory_app
from templates.sales_report import sales_report_app
from templates.pos_system import pos_system
from views.inventory_view import InventoryManagement


class mainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.create_main_app()
        self.create_side_bar()

    def create_main_app(self):
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}+-7+0") ##Pega a informação da largura e altura da tela e passa para o geometry
        self.title("UniFruti")
        self.iconbitmap(r"images\logo_2.ico")
        ctk.set_appearance_mode("light")

    def create_side_bar(self):    
        self.text_font = ctk.CTkFont(family="Verdana", size = 15, weight="bold")
        self.sidebar_frame = ctk.CTkFrame(master=self, fg_color="#69F0AE", width=250, height=650, corner_radius=0) # Criei a sidebar, que tem como pai o app
        self.sidebar_frame.pack_propagate(0) ## Não deixa o conteúdo da sidebar aumentar o tamanho dela
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")
        self.logo_img_data = Image.open(r"images\logo_2.png")
        self.logo_img = ctk.CTkImage(dark_image=self.logo_img_data, light_image=self.logo_img_data, size=(120, 120))
        self.logo_img_label = ctk.CTkLabel(master=self.sidebar_frame, text="", image=self.logo_img)
        self.logo_img_label.pack(pady=(38, 0), anchor="center")

        #Criei uma frame para colocar o conteúdo dos botões
        self.content = ctk.CTkFrame(self, height= 70, width= 70, corner_radius=0, fg_color="#F7EBE7")
        self.content.pack(fill = "both", expand = True)

        def button_onclick(button, parent):
            for i in (self.sidebar_inventory, self.sidebar_sales_report, self.sidebar_employees, self.sidebar_cash_closing, self.sidebar_pos):
                i.configure(fg_color="#4CAF50")
                
            button.configure(fg_color="#007900")

            for item in self.content.winfo_children():
                item.destroy() #Esse laço vai pegar a informação do
            if button == self.sidebar_inventory:
                inventory_app(parent) ## O parente se refere ao app, ou seja, vai criar a tela dentro do parent, que estamos passando no botão
            elif button == self.sidebar_sales_report:
                sales_report_app(parent)
            elif button == self.sidebar_pos:
                pos_system(parent)
                
        self.button_frame_bg = "#4CAF50"

        self.inventory_image_data = Image.open(r"images\inventory_button.png")
        self.inventory_image = ctk.CTkImage(dark_image=self.inventory_image_data, light_image= self.inventory_image_data, size=(25,25))
        self.sidebar_inventory = ctk.CTkButton(master= self.sidebar_frame, text="Inventory", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font=self.text_font, hover_color="#007900", command=lambda: button_onclick(self.sidebar_inventory, self.content), image = self.inventory_image, anchor="w") ##O lambda permite que só execute essa função caso eu aperte esse botão
        self.sidebar_inventory.pack(pady=(150,10), padx=(30))

        self.sales_report_image_data = Image.open(r"images\sales_report_image.png")
        self.sales_report_image = ctk.CTkImage(dark_image=self.sales_report_image_data, light_image= self.sales_report_image_data, size=(25,25))
        self.sidebar_sales_report = ctk.CTkButton(master=self.sidebar_frame, text="Sales Report", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font=self.text_font, hover_color="#007900", command=lambda: button_onclick(self.sidebar_sales_report, self.content), image = self.sales_report_image, anchor="w")
        self.sidebar_sales_report.pack(pady=10, padx=30, anchor="center") 
        ##

        self.employees_image_data = Image.open(r"images\employees_image.png")
        self.employees_image = ctk.CTkImage(dark_image=self.employees_image_data, light_image= self.employees_image_data, size=(25,25))
        self.sidebar_employees = ctk.CTkButton(master=self.sidebar_frame, text= "Employees", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font= self.text_font, hover_color="#007900", command=lambda: button_onclick(self.sidebar_employees, self.content), image = self.employees_image, anchor="w")
        self.sidebar_employees.pack(pady=10, padx=30, anchor="center") 

        self.cash_closing_image_data = Image.open(r"images\currency.png")
        self.cash_closing_image = ctk.CTkImage(dark_image=self.cash_closing_image_data, light_image= self.cash_closing_image_data, size=(25,25))
        self.sidebar_cash_closing = ctk.CTkButton(master=self.sidebar_frame, text="Cash Closing", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font=self.text_font, hover_color="#007900", command=lambda: button_onclick(self.sidebar_cash_closing, self.content), image = self.cash_closing_image, anchor="w")
        self.sidebar_cash_closing.pack(pady=10, padx=30, anchor="center") 

        self.pos_image_data = Image.open(r"images\shopping_cart.png")
        self.pos_image = ctk.CTkImage(dark_image=self.pos_image_data, light_image= self.pos_image_data, size=(25,25))
        self.sidebar_pos = ctk.CTkButton(master=self.sidebar_frame, text = "POS System", text_color="#FFFFFF", fg_color="#4CAF50", corner_radius=15, height=40, width=400, font=self.text_font, hover_color="#007900", command=lambda: button_onclick(self.sidebar_pos, self.content), image = self.pos_image, anchor="w")
        self.sidebar_pos.pack(pady=10, padx=30, anchor="center") 


if __name__ == "__main__":
    app = mainApp()
    app.mainloop()
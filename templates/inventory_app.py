import __init__

from customtkinter import *
from PIL import Image
from tkinter import ttk
from views.inventory_view import InventoryManagement
from models.database import engine
from CTkTable import CTkTable


def inventory_app(parent):
    products_management = InventoryManagement(engine)
    frame_bg_color = "#57C590"
    title_font = CTkFont(family="Verdana", size = 35, weight= "bold")
    add_button_font = CTkFont(family="Verdana", size = 23, weight= "bold")
    page_title_frame = CTkFrame(parent, width = 100, height= 15, fg_color="#F7EBE7")
    page_title_frame.pack(fill = "x", anchor = "center")
    page_title = CTkLabel(page_title_frame, text = "Inventory", font = title_font, text_color= "#39853C")
    page_title.pack(padx = 50, pady = 30, side="left", anchor = "nw", fill="x" )
    
    create_button = CTkButton(page_title_frame, text = "+ Add", text_color= "white", font=add_button_font, corner_radius=20, height=55, fg_color=frame_bg_color, hover_color="#4CAF50",anchor= "center", command=lambda: add_product_app() )
    create_button.pack(padx=50, pady = (25,30), anchor = "ne")

    infos_frame = CTkFrame(parent, height= 200, width= 880, fg_color="#F7EBE7")
    infos_frame.pack(side="top")
    infos_frame.pack_propagate(0)

    infos_frame_font = CTkFont(family = "Verdana", size = 18, weight = "bold")


    total_value_frame = CTkFrame(master=infos_frame, height=50, width=50,  fg_color=frame_bg_color, corner_radius=20)
    total_value_frame.pack(padx = 20, fill = "both", side = "left", expand = True, anchor="center")
    total_value_frame.pack_propagate(0)
    inventory_image_data = Image.open(r"images\inventory.png")
    inventory_image = CTkImage(dark_image=inventory_image_data, light_image= inventory_image_data, size=(70, 70))
    inventory_image_label = CTkLabel(master=total_value_frame, text= "", image=inventory_image)
    inventory_image_label.pack(pady = (15, 5), padx = 0)
    total_text_label = CTkLabel(master = total_value_frame, text = "Products Available", font = infos_frame_font, text_color= "#FFFFFF")
    total_text_label.place(relx = 0.5, rely = 0.5, anchor = "center")
    total_text_label.pack(pady = 3)
    total_products = CTkLabel(master = total_value_frame, text = f"{products_management.count_products()}", font =("Verdana", 25, "bold"), text_color= "#FFFFFF")
    total_products.pack(padx = 5, pady = (5, 15), anchor = "s", side = "bottom")
    

    frame_2 = CTkFrame(infos_frame, height=50, width=50, fg_color=frame_bg_color, corner_radius=20)
    frame_2.pack(padx = 20, fill = "both", side="left", expand = True)
    frame_3 = CTkFrame(infos_frame, height=50, width=50, fg_color=frame_bg_color, corner_radius=20)
    frame_3.pack(padx = 20, fill = "both", side= "left", expand = True)

    query_frame = CTkFrame(parent, height= 50, width=1270)
    query_frame.pack(padx=10, pady=(70, 0))

    table_frame = CTkScrollableFrame(parent, width= 1270, fg_color= "transparent", scrollbar_button_color=frame_bg_color)
    table_frame.pack(padx= 0, pady = (0, 80))
    

    def create_table():
        row = products_management.list_rows_table()

        table_data = []

        # for column in columns:
        #         table_data.append(column)

        for value in row: 
            table_data.append(value)
        
        return table_data
    
    table_column_data = [
        ['ID', 'Name', 'Unit Price', 'Quantity', 'Expiration Date', 'Enter Date', 'Active', 'Category ID']
    ]


    table_column = CTkTable(table_frame, values= table_column_data, corner_radius = 0, text_color= "white", width = 155, header_color=frame_bg_color, font=('Verdana', 12, 'bold'))
    table_column.pack(padx = 0, pady= 0, expand = True, fill= "both")
    table = CTkTable(table_frame, values = create_table(), hover_color="#B4B4B4", width = 155, corner_radius = 0, fg_color = "#F7EBE7")
    table.pack(fill = "both",expand = True)

def add_product_app():
    product_app = CTk()
    name_font = CTkFont("Verdana", 13, "normal")
    product_app.title("Add Product")
    product_app.geometry("500x600")
    product_app.resizable(0,0)
    product_app.iconbitmap(r"images\mais.ico")
    
    
    product_app_frame = CTkFrame(product_app, height=70, width=70, fg_color="white")
    product_app_frame.pack(fill = "both", expand = True)

    main_title_frame = CTkFrame(product_app_frame, height=60, width=60, fg_color="white")
    main_title_frame.pack(anchor="center", fill= "x")

    main_title = CTkLabel(main_title_frame, height= 30, width= 30, text = "Add new product", text_color="#5E5E5E", font=("Arial", 20, "bold"))
    main_title.pack(padx= 10, pady= 10)
    

    name_frame = CTkFrame(product_app_frame, height=50,width=60, fg_color="white")
    name_frame.pack(anchor = "center", fill="x", pady=(30,0))
    product_name = CTkLabel(name_frame, text="Name", font=("Verdana", 14, "normal"), text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
    product_name.pack(padx=(30,0), fill="x", anchor="nw")
    name_input = CTkEntry(name_frame, placeholder_text="Enter product name", height=40, width= 400, corner_radius=0, border_color= "#57C590")
    name_input.pack(pady=(1,10), padx=(30,0), anchor="w", side="bottom")


    unit_price_frame = CTkFrame(product_app_frame, height=50,width=60, fg_color="white")
    unit_price_frame.pack(anchor = "center", fill="x", pady=(15,0))
    unit_price = CTkLabel(unit_price_frame, text="Unit Price", font=name_font, text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
    unit_price.pack(padx=(30,0), fill="x", anchor="nw")
    unit_price_input = CTkEntry(unit_price_frame, placeholder_text="Enter unit price", height=40, width= 400, corner_radius=0, border_color= "#57C590")
    unit_price_input.pack(pady=(1,10), padx=(30,0), anchor="w", side="bottom")


    quantity_frame = CTkFrame(product_app_frame, height=50,width=60, fg_color="white")
    quantity_frame.pack(anchor = "center", fill="x", pady=(15,0))
    quantity = CTkLabel(quantity_frame, text="Quantity", font=name_font, text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
    quantity.pack(padx=(30,0), fill="x", anchor="nw")
    quantity_input = CTkEntry(quantity_frame, placeholder_text="Enter quantity", height=40, width= 400, corner_radius=0, border_color= "#57C590")
    quantity_input.pack(pady=(1,10), padx=(30,0), anchor="w", side="bottom")

    category_frame = CTkFrame(product_app_frame, height=50,width=150, fg_color="white")
    category_frame.pack(anchor="w", padx = (30,0), pady=(25,10))

    category = CTkLabel(category_frame, text="Category", font=name_font, text_color= "#5E5E5E", anchor="nw", fg_color="white", width= 70, height= 20)
    category.pack(fill="x", anchor="nw")
    category_option = CTkOptionMenu(category_frame, height=32, width= 60, fg_color="#57C590", button_color="#57C590", button_hover_color="#4CAF50")
    category_option.pack(pady=(1,10))



    product_app.mainloop()



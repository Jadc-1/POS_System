import __init__

from customtkinter import *
from models.model import Products,Categorys
from PIL import Image, ImageTk
from views.inventory_view import InventoryManagement
from models.database import engine
from CTkTable import CTkTable
from datetime import date,datetime
from tkcalendar import Calendar,DateEntry
from tkinter import PhotoImage


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

    table_column_frame = CTkFrame(parent, width=1270, height=25, fg_color= "transparent")
    table_column_frame.pack(padx=(0,8),pady=(3,0))
    table_column_frame.pack_propagate(0)
    table_frame = CTkScrollableFrame(parent, width= 1270, height = 500, fg_color= "transparent", scrollbar_button_color=frame_bg_color,)
    table_frame.pack(padx= 0, pady = (0, 80), expand= True, anchor='n',)
    

    def create_table():
        row = products_management.list_rows_table()

        table_data = []

        # for column in columns:
        #         table_data.append(column)

        for value in row: 
            table_data.append(value)
            
        
        return table_data
    
    table_column_data = [
        ['ID', 'Name', 'Unit Price', 'Quantity', 'Expiration Date', 'Enter Date', 'Active', 'Category']
    ]


    table_column = CTkTable(table_column_frame, values= table_column_data, corner_radius = 0, text_color= "white", width = 155, header_color=frame_bg_color, font=('Verdana', 12, 'bold'))
    table_column.pack(padx = 0, pady= 0, expand = True, fill= "both")
    table = CTkTable(table_frame, values = create_table(), hover_color="#B4B4B4", width = 155, corner_radius = 0, fg_color = "#F7EBE7")
    table.pack(fill = "both",expand = True, pady=0)


def add_product_app():
    products_management = InventoryManagement(engine)
    product_app = CTkToplevel()
    product_app.focus()
    name_font = CTkFont("Verdana", 13, "normal")
    product_app.title("Add Product")
    product_app.geometry("500x600+700+150")
    product_app.resizable(0,0)
    product_app.config(background="#F6F6F6")
    #Depois de abrir totalmente a janela, ela será o foco, ou seja, vai sobrepor a janela
    product_app.after(100, lambda: product_app.focus())
    
    
    product_app_frame = CTkFrame(product_app, fg_color="white")
    product_app_frame.pack(fill = "both", expand = True)

    main_title_frame = CTkFrame(product_app_frame, height=60, width=60, fg_color="white")
    main_title_frame.pack(anchor="center", fill= "x")

    main_title = CTkLabel(main_title_frame, height= 30, width= 30, text = "Add new product", text_color="#5E5E5E", font=("Arial", 20, "bold"))
    main_title.pack(padx= 10, pady= (30,10))
    

    name_frame = CTkFrame(product_app_frame, height=50,width=60, fg_color="white")
    name_frame.pack(anchor = "center", fill="x", pady=(30,0))
    product_name = CTkLabel(name_frame, text="Name*", font=("Verdana", 14, "normal"), text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
    product_name.pack(padx=(30,0), fill="x", anchor="nw")
    name_input = CTkEntry(name_frame, placeholder_text="Enter product name", height=40, width= 435, corner_radius=0, border_color= "#57C590", border_width=1)
    name_input.pack(pady=(1,10), padx=(30,0), anchor="w", side="bottom")


    unit_price_frame = CTkFrame(product_app_frame, height=50,width=60, fg_color="white")
    unit_price_frame.pack(anchor = "center", fill="x", pady=(15,0))
    unit_price = CTkLabel(unit_price_frame, text="Unit Price*", font=name_font, text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
    unit_price.pack(padx=(30,0), fill="x", anchor="nw")
    unit_price_input = CTkEntry(unit_price_frame, placeholder_text="Enter unit price", height=40, width= 435, corner_radius=0, border_color= "#57C590", border_width=1)
    unit_price_input.pack(pady=(1,10), padx=(30,0), anchor="w", side="bottom")

    quantity_frame = CTkFrame(product_app_frame, height=50,width=60, fg_color="white")
    quantity_frame.pack(anchor = "center", fill="x", pady=(15,0))
    quantity = CTkLabel(quantity_frame, text="Quantity*", font=name_font, text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
    quantity.pack(padx=(30,0), fill="x", anchor="nw")
    quantity_input = CTkEntry(quantity_frame, placeholder_text="Enter quantity", height=40, width= 435, corner_radius=0, border_color= "#57C590", border_width=1)
    quantity_input.pack(pady=(1,10), padx=(30,0), anchor="w", side="bottom")

    category_frame = CTkFrame(product_app_frame, height=50,width=150, fg_color="white")
    category_frame.pack(anchor="w", padx = (30,0), pady=(25,10))
    category = CTkLabel(category_frame, text="Category*(write or choose)", font=name_font, text_color= "#5E5E5E", anchor="nw", fg_color="white", width= 70, height= 20)
    category.pack(anchor="nw")
    category_option = CTkComboBox(category_frame, values = products_management.list_categorys_name(), text_color="#5E5E5E", font = ("Verdana", 13, "bold"), height=32, width= 200, fg_color="#DEDEDE", button_color="#DEDEDE", button_hover_color="#BCBCBC", corner_radius= 10, dropdown_fg_color="#DEDEDE", dropdown_text_color="#5E5E5E", dropdown_font=("Verdana", 13, "bold"), border_width=0)
    category_option.pack(pady=(5,10))

    calendar_image_data = Image.open(r"images\calendar_1.png")
    calendar_image = CTkImage(light_image=calendar_image_data, dark_image=calendar_image_data)
    expiration_date_frame = CTkFrame(product_app_frame, height=60, width=180, fg_color="white")
    expiration_date_frame.place(relx = 0.93, rely=0.62, anchor="ne")
    expiration_date = CTkLabel(expiration_date_frame, text="Expiration date*", font=name_font, text_color= "#5E5E5E", anchor="nw", fg_color="white", width= 70, height= 20)
    expiration_date.pack(anchor="ne")

    def create_calendar():
        calendar_screen = CTkToplevel()
        calendar_screen.geometry("250x200+1035+607")
        calendar_screen.overrideredirect(True)
        calendar = Calendar(calendar_screen, mindate=date.today(), showweeknumbers=False, showothermonthdays=False, showcurrent=True, date_pattern="dd/mm/yyyy", locale="en_US", background="#56C46A", headersbackground="#53BC89", headersforeground="white", weekendbackground = "white", weekendforeground="black", selectbackground="#56C46A", selectforeground="white", font=("Arial black", 10,"normal"))
        calendar.pack(expand=True, fill="both")
        #lambda necessário, pois after precisa de uma função para rodar apos 100 ms
        calendar_screen.grab_set()
        calendar_screen.after(100, lambda: product_app.focus())
        def date_updated(event):
            global date_choosed
            date_choosed = calendar.get_date()
            calendar_label.configure(text=date_choosed)
            calendar_screen.after(100, lambda:calendar_screen.destroy())
        #o método bind automaticamente passa um objeto de evento como argumento para a função date_updated quando o evento ocorre
        calendar.bind("<<CalendarSelected>>", date_updated)

        
        
    calendar_frame = CTkFrame(expiration_date_frame, height=32, width= 165, fg_color="#DEDEDE", border_width=2, border_color="#57C590")
    calendar_frame.pack(anchor="e")
    calendar_label = CTkLabel(calendar_frame, height=32, width= 165, fg_color="#DEDEDE", text="", corner_radius=10, anchor="e", font=("Verdana", 11.5, "normal"), text_color="#5E5E5E")
    calendar_label.pack(side="left", fill="x")
    calendar_button = CTkButton(calendar_frame, height=32, width=35, text="", corner_radius=0, border_width=1, fg_color="#DEDEDE" , border_color= "#57C590", hover_color="#BCBCBC", anchor="center", image=calendar_image, command=lambda:create_calendar())
    calendar_button.pack(anchor="ne", side="left")
    
    add_frame = CTkFrame(product_app_frame, height=45, width=190, fg_color="white", corner_radius=15)
    add_frame.pack(side="bottom", pady=(0,45))
    add_frame.pack_propagate(0)
    add_label = CTkButton(add_frame, text="Add", text_color="white", font=("Verdana", 15, "bold"), anchor="center", corner_radius=15, fg_color="#57C590", hover_color="#4FB483", command=lambda: product_add())
    add_label.pack(expand=True, fill="both")
    


    def product_add():
        name_value = name_input.get()
        unit_price_value = unit_price_input.get()
        quantity_value = quantity_input.get()
        category_value = category_option.get()
        expiration_date = datetime.strptime(date_choosed, "%d/%m/%Y")
        category_id = products_management.get_category_id_by_name(category_value)

        product = Products(name=name_value, kg_price=unit_price_value, quantity=quantity_value, enter_date= date.today() ,expiration_date = expiration_date, category_id= category_id)
        
        products_management.create_product(product)
        product_app_frame.after(300,product_app.destroy())
        #confirm_frame = CTkFrame(product_app, fg_color="#57C590")
        # confirm_frame.pack(anchor="center", fill="both", expand=True)
        # confirm_frame.pack_propagate(0)
        # confirm = CTkLabel(confirm_frame, text="Product Created!", fg_color="#57C590", font=("Verdana", 25, "bold"), text_color="white", anchor="center")
        # confirm.pack()
        # confirm.place(rely=0.45, relx=0.25)
        
        
      

        



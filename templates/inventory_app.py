import __init__

from customtkinter import *
from models.model import Products,Categorys
from PIL import Image, ImageTk
from views.inventory_view import InventoryManagement
from models.database import engine
from CTkTable import CTkTable
from datetime import date,datetime
from tkcalendar import Calendar
from CTkMessagebox import CTkMessagebox


global date_choosed
date_choosed = None
def inventory_app(parent):
    products_management = InventoryManagement(engine)
    frame_bg_color = "#57C590"
    title_font = CTkFont(family="Verdana", size = 35, weight= "bold")
    add_button_font = CTkFont(family="Verdana", size = 13, weight= "bold")
    page_title_frame = CTkFrame(parent, width = 100, height= 15, fg_color="#F7EBE7")
    page_title_frame.pack(fill = "x", anchor = "center")
    page_title = CTkLabel(page_title_frame, text = "Inventory", font = title_font, text_color= "#39853C")
    page_title.pack(padx = 50, pady = 30, side="left", anchor = "nw", fill="x" )
    

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
    

    category_frame = CTkFrame(infos_frame, height=50, width=50, fg_color=frame_bg_color, corner_radius=20)
    category_frame.pack(padx = 20, fill = "both", side="left", expand = True)
    category_frame.pack_propagate(0)
    category_image_data = Image.open(r"images\categorization.png")
    category_image = CTkImage(light_image=category_image_data, dark_image=category_image_data, size=(70,70))
    category_image_label = CTkLabel(category_frame, text="", image = category_image)
    category_image_label.pack(pady = (15, 5), padx = 0)
    category_text_label = CTkLabel(category_frame, font=infos_frame_font, text_color="#FFFFFF", text="Total Categories")
    category_text_label.place(relx = 0.5, rely = 0.5, anchor = "center")
    category_text_label.pack(pady = 3)
    category_total = CTkLabel(master = category_frame, text = f"{products_management.get_total_categories()}", font =("Verdana", 25, "bold"), text_color= "#FFFFFF")
    category_total.pack(padx = 5, pady = (5, 15), anchor = "s", side = "bottom")

    stock_value_frame = CTkFrame(infos_frame, height=50, width=50, fg_color=frame_bg_color, corner_radius=20)
    stock_value_frame.pack(padx = 20, fill = "both", side="left", expand = True)
    stock_value_frame.pack_propagate(0)
    stock_value_image_data = Image.open(r"images\increase.png")
    stock_value_image = CTkImage(light_image=stock_value_image_data, dark_image=stock_value_image_data, size=(70,70))
    stock_value_image_label = CTkLabel(stock_value_frame, text="", image = stock_value_image)
    stock_value_image_label.place(relx = 0.5, rely = 0.5, anchor = "center")
    stock_value_image_label.pack(pady = (15, 5), padx = 0)
    stock_value_text_label = CTkLabel(stock_value_frame, font=infos_frame_font, text_color="#FFFFFF", text="Stock Value")
    stock_value_text_label.place(relx = 0.5, rely = 0.5, anchor = "center")
    stock_value_text_label.pack(pady = 3)
    stock_value = CTkLabel(master = stock_value_frame, text = f"{products_management.get_stock_value()}", font =("Verdana", 25, "bold"), text_color= "#FFFFFF")
    stock_value.pack(padx = 5, pady = (5, 15), anchor = "s", side = "bottom")





    query_frame = CTkFrame(parent, height= 50, width=1270, fg_color="#F7EBE7")
    query_frame.pack(padx=(0,10), pady=(70, 0)) #"#F7EBE7"#EFE4E1
    query_frame.pack_propagate(0)

    query_entry = CTkEntry(query_frame, corner_radius=10, fg_color="white", placeholder_text="Search by product...", width=400)
    query_entry.pack(pady=(7,5), fill = "y", anchor="w", side="left")

    def search_table():
        query = query_entry.get()
        table.configure(values = products_management.list_query_products(query))

    def search_category():
        query = choose_category.get()
        table.configure(values = products_management.list_query_categories(query))

    def clear_entry():
        change_focus()
        query_entry.delete(0, "end") #Deleta do primeiro caracter até o final
        table.configure(values = products_management.create_table_view())
        choose_category.set("Categories")
    
    def change_focus():
        return total_value_frame.focus_set()

    search_data = Image.open(r"images\search.png")
    search_image = CTkImage(light_image=search_data, dark_image=search_data, size=(25,25))    
    query_search = CTkButton(query_frame, corner_radius=10, width = 40, anchor="w", text="", fg_color="#57C590", hover_color="#49A578", image=search_image, command=search_table)
    query_search.pack_propagate(0)
    query_search.pack(pady=(9,7), padx=(2,0), fill = "y", side="left", anchor="center")

   

    clean_data = Image.open(r"images\clean.png")
    clean_image = CTkImage(light_image=clean_data, dark_image=clean_data, size=(25,25))    
    query_clean = CTkButton(query_frame, corner_radius=10, width = 40, anchor="w", text="", fg_color="#57C590", hover_color="#49A578", image=clean_image, command=clear_entry) ##Sem parentes pois não queremos que a função seja chamada direto, apenas quando clicar no botão
    query_clean.pack_propagate(0)
    query_clean.pack(pady=(9,7), padx=(2,0), fill = "y", side="left", anchor="center")


    choose_category = CTkComboBox(query_frame, values = products_management.list_categories_name(), text_color="#5E5E5E", font = ("Verdana", 12, "bold"), fg_color="white", button_color="#CECECE", button_hover_color="#B7B7B7", corner_radius= 10, dropdown_fg_color="white", dropdown_text_color="#5E5E5E", dropdown_font=("Verdana", 12, "bold"), border_color="#CECECE", width= 200, height=40)
    choose_category.pack(padx = (150,0), pady=(9,5), side="left", anchor= "w")
    choose_category.set("Categories")
    category_search = CTkButton(query_frame, corner_radius=10, width = 20, height= 30, anchor="w", text="", fg_color="#57C590", hover_color="#49A578", image=search_image, command=search_category)
    category_search.pack_propagate(0)
    category_search.pack(pady=(9,3), padx=(3,0), side="left", anchor="center")

    delete_button = CTkButton(query_frame, text = "- Delete", text_color= "white", font=add_button_font, corner_radius=20, fg_color="#AA3939", hover_color="#8B2F2F",anchor= "center", command=lambda: delete_product_app(), width = 25)
    delete_button.pack(padx=3,pady = (9,7), anchor = "ne", side="right", fill="y")
    autocreate_button = CTkButton(query_frame, text = "+ AutoAdd", text_color= "white", font=add_button_font, corner_radius=20, fg_color=frame_bg_color, hover_color="#4CAF50",anchor= "center", command=lambda: autoadd_product(), width = 25)
    autocreate_button.pack(padx=3,pady = (9,7), anchor = "ne", side="right", fill="y")
    create_button = CTkButton(query_frame, text = "+ Add", text_color= "white", font=add_button_font, corner_radius=20, fg_color=frame_bg_color, hover_color="#4CAF50",anchor= "center", command=lambda: add_product_app(), width = 25)
    create_button.pack(padx=3,pady = (9,7), anchor = "ne", side="right", fill="y")
    



    table_column_frame = CTkFrame(parent, width=1269, height=25, fg_color= "transparent")
    table_column_frame.pack(padx=(0,8),pady=(3,0))
    table_column_frame.pack_propagate(0)
    table_frame = CTkScrollableFrame(parent, width= 1270, height = 500, fg_color= "transparent", scrollbar_button_color=frame_bg_color,)
    table_frame.pack(padx= 0, pady = (0, 80), expand= True, anchor='n',)
    
    table_column_data = [
        ['ID', 'Name', 'Unit Price', 'Quantity', 'Expiration Date', 'Enter Date', 'Active', 'Category']

    ]

    table_column = CTkTable(table_column_frame, values= table_column_data, corner_radius = 0, text_color= "white", width = 155, header_color=frame_bg_color, font=('Verdana', 12, 'bold'))
    table_column.pack(padx = 0, pady= 0, expand = True, fill= "both")
    table = CTkTable(table_frame, values = products_management.create_table_view(), hover_color="#B4B4B4", width = 155, corner_radius = 0, fg_color = "#F7EBE7")
    table.pack(fill = "both",expand = True, pady=0)


    def add_product_app():
        products_management = InventoryManagement(engine)
        product_app = CTkToplevel()
        name_font = CTkFont("Verdana", 13, "normal")
        product_app.title("Add Product")
        product_app.geometry("500x600+750+200")
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
        name_frame.pack(anchor = "center", fill="x", pady=(40,0))
        product_name = CTkLabel(name_frame, text="Name*", font=("Verdana", 14, "normal"), text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
        product_name.pack(padx=(30,0), fill="x", anchor="nw")
        name_intern_frame = CTkFrame(name_frame, fg_color="white")
        name_intern_frame.pack(fill="x")
        name_input = CTkEntry(name_intern_frame, placeholder_text="Enter product name", height=40, width= 435, corner_radius=0, border_color= "#57C590", border_width=1)
        name_input.pack(pady=(1), padx=(30,0), anchor="w", side="top")
        name_error = CTkLabel(name_intern_frame, text_color="red", height=25)


        unit_price_frame = CTkFrame(product_app_frame, height=50,width=60, fg_color="white")
        unit_price_frame.pack(anchor = "center", fill="x", pady=(25,0))
        unit_price = CTkLabel(unit_price_frame, text="Unit Price*", font=name_font, text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
        unit_price.pack(padx=(30,0), fill="x", anchor="nw")
        unit_price_intern_frame = CTkFrame(unit_price_frame, fg_color="white")
        unit_price_intern_frame.pack(fill="x")
        unit_price_input = CTkEntry(unit_price_intern_frame, placeholder_text="Enter unit price", height=40, width= 435, corner_radius=0, border_color= "#57C590", border_width=1)
        unit_price_input.pack(pady=(1), padx=(30,0), anchor="w", side="top")
        unit_price_error = CTkLabel(unit_price_intern_frame, text_color="red", height=25)

        quantity_frame = CTkFrame(product_app_frame, height=50,width=60, fg_color="white")
        quantity_frame.pack(anchor = "center", fill="x", pady=(25,0))
        quantity = CTkLabel(quantity_frame, text="Quantity*", font=name_font, text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
        quantity.pack(padx=(30,0), fill="x", anchor="nw")
        quantity_intern_frame = CTkFrame(quantity_frame, fg_color="white")
        quantity_intern_frame.pack(fill="x")
        quantity_input = CTkEntry(quantity_intern_frame, placeholder_text="Enter quantity", height=40, width= 435, corner_radius=0, border_color= "#57C590", border_width=1)
        quantity_input.pack(pady=(1), padx=(30,0), anchor="w", side="top")
        #So chama esse quando dar algum erro!
        quantity_error = CTkLabel(quantity_intern_frame, text_color="red", height=25)


        options_frame = CTkFrame(product_app_frame, fg_color="white")
        options_frame.pack(fill="x")

        category_frame = CTkFrame(options_frame, height=50,width=150, fg_color="white")
        category_frame.pack(anchor="w", padx = (30,0), pady=(25,10), side="left")
        category = CTkLabel(category_frame, text="Category*(write or choose)", font=name_font, text_color= "#5E5E5E", anchor="nw", fg_color="white", width= 70, height= 20)
        category.pack(anchor="nw")
        category_option = CTkComboBox(category_frame, values = products_management.list_categories_name(), text_color="#5E5E5E", font = ("Verdana", 13, "bold"), height=34, width= 200, fg_color="#DEDEDE", button_color="#DEDEDE", button_hover_color="#BCBCBC", corner_radius= 10, dropdown_fg_color="#DEDEDE", dropdown_text_color="#5E5E5E", dropdown_font=("Verdana", 13, "bold"), border_width=0)
        category_option.pack(pady=(1,10))

        calendar_image_data = Image.open(r"images\calendar_1.png")
        calendar_image = CTkImage(light_image=calendar_image_data, dark_image=calendar_image_data)
        expiration_date_frame = CTkFrame(options_frame, height=60, width=180, fg_color="white")
        expiration_date_frame.pack(side="right", padx=(0,35), pady=(6,0))
        expiration_date = CTkLabel(expiration_date_frame, text="Expiration date(optional)", font=name_font, text_color= "#5E5E5E", anchor="nw", fg_color="white", width= 70, height= 20)
        expiration_date.pack(anchor="ne")

        def create_calendar():
            calendar_screen = CTkToplevel()
            calendar_screen.geometry("250x200+1035+607")
            calendar_screen.overrideredirect(True)
            calendar_screen.resizable(0,0)
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
        add_button = CTkButton(add_frame, text="Add", text_color="white", font=("Verdana", 15, "bold"), anchor="center", corner_radius=15, fg_color="#57C590", hover_color="#4FB483", command=lambda: product_add())
        add_button.pack(expand=True, fill="both")



        def product_add():
            global date_choosed
            name_value = ""
            name_value = name_input.get().strip()
            if name_value == "":
                name_error.configure(text="Name entry can not be empty!")
                name_error.pack(side="bottom", anchor="w", padx=(30,0))
                name_error.pack_propagate(0)
                return
            else:
                name_error.pack_forget()
            #Tratando o que o usuario digitar em Unit Price e Quantity, para só aceitar números e evitar campos vazios
            try:
                unit_price_value = float(unit_price_input.get().strip())
            except ValueError:
                unit_price_error.configure(text="Invalid input: The unit price must be a numeric value.")
                unit_price_error.pack(side="bottom", anchor="w", padx=(30,0))
                unit_price_error.pack_propagate(0)
            else:
                unit_price_error.pack_forget()

            try:
                quantity_value = int(quantity_input.get().strip())
            except ValueError:
                quantity_error.configure(text="Invalid input: The quantity must be a numeric value.")
                quantity_error.pack(side="bottom", anchor="w", padx=(30,0))
                quantity_error.pack_propagate(0)

            else:
                quantity_error.pack_forget()
            
            category_value = category_option.get().strip()
            if date_choosed:
                expiration_date = datetime.strptime(date_choosed, "%d/%m/%Y")
            else:
                expiration_date = None
            category_id = products_management.get_category_id_by_name(category_value)

            try:
                product = Products(name=name_value, kg_price=unit_price_value, quantity=quantity_value, enter_date= date.today() ,expiration_date = expiration_date, category_id= category_id)
                products_management.create_product(product)
                confirm_message = CTkMessagebox(master = product_app, message=f"{name_value} created!", icon="check", button_color= "#57C590",option_1="Close", title = "", button_text_color="white", button_hover_color="#76C793", font=("Verdana", 12, "bold"))
                confirm_message.after(100, lambda: confirm_message.focus())
                if confirm_message.get() =="Close":
                    product_app_frame.after(300,product_app.destroy())
            except UnboundLocalError:
                unit_price_error.configure(text="Invalid input: The unit price must be a numeric value.")


    def delete_product_app(): 
        products_management = InventoryManagement(engine)
        delete_app = CTkToplevel()
        delete_app.title("Delete products")
        delete_app.geometry("500x300+750+350")
        delete_app.after(100, lambda: delete_app.focus())
    

        delete_app_mainframe = CTkFrame(delete_app, fg_color="white")
        delete_app_mainframe.pack(fill="both", expand=True)
        delete_app_mainframe.pack_propagate(0)

        delete_tab = CTkTabview(delete_app_mainframe, fg_color="white", segmented_button_selected_color="red", segmented_button_selected_hover_color="#8B2F2F", segmented_button_unselected_hover_color="#8B2F2F", text_color="#FFFFFF", anchor="nw")  
        delete_tab.pack(fill="both", expand=True, padx= 3, pady=3)
        delete_tab.pack_propagate(0)


        #Tag do produto ====================

        products_tab = delete_tab.add("    Products    ")

        delete_product_frame = CTkFrame(products_tab, fg_color="white")
        delete_product_frame.pack_propagate(0)
        delete_product_frame.pack(fill = "both", expand = True)

        name_frame = CTkFrame(delete_product_frame, height=50,width=60, fg_color="white")
        name_frame.pack(anchor = "center", fill="x", pady=(30,0))
        product_name = CTkLabel(name_frame, text="Name", font=("Verdana", 16, "bold"), text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
        product_name.pack(padx=(15,0), pady=(0,3), fill="x", anchor="nw")
        name_intern_frame = CTkFrame(delete_product_frame, fg_color="white")
        name_intern_frame.pack(fill="x")
        name_input = CTkEntry(name_intern_frame, placeholder_text="Enter product name to delete", height=40, width= 435, corner_radius=0, border_color= "#AA3939", border_width=1)
        name_input.pack(pady=(1,10), padx=(15,0), anchor="w", side="top")

        def get_product_to_delete():
            delete_input = name_input.get()
            if products_management.search_delete_product(delete_input):
                products_management.delete_product(delete_input)
                name_confirm = CTkMessagebox(master=delete_app, message=f"Product {delete_input} deleted!", icon="check", option_1="Ok", title="", button_color= "#57C590",button_text_color="white", button_hover_color="#76C793", font=("Verdana", 12, "bold"))
            else:
                name_error = CTkMessagebox(master=delete_app, message=f"Product {delete_input} not found!", icon="cancel", option_1="Ok", title="", button_color= "#57C590",button_text_color="white", button_hover_color="#76C793", font=("Verdana", 12, "bold"))
                name_error.after(100, lambda: name_error.focus())
                if name_error.get() == "Ok":
                    name_error.destroy()
                return
            delete_app.after(100, delete_app.destroy())
            return delete_input

        delete_frame = CTkFrame(delete_product_frame, height=45, width=190, fg_color="white", corner_radius=15)
        delete_frame.pack(side="bottom", pady=(0,45))
        delete_frame.pack_propagate(0)
        product_button = CTkButton(delete_frame, text="Delete", text_color="white", font=("Verdana", 15, "bold"), anchor="center", corner_radius=15, fg_color="#AA3939", hover_color="#8B2F2F", command=lambda: get_product_to_delete())
        product_button.pack(expand=True, fill="both")

        #Tab da categoria ==============

        categories_tab = delete_tab.add("    Categories    ")

        delete_category_frame = CTkFrame(categories_tab, fg_color="white")
        delete_category_frame.pack_propagate(0)
        delete_category_frame.pack(fill = "both", expand = True)


        category_frame = CTkFrame(delete_category_frame, height=50,width=60, fg_color="white")
        category_frame.pack(anchor = "center", fill="x", pady=(30,0))
        category_name = CTkLabel(category_frame, text="Category", font=("Verdana", 16, "bold"), text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
        category_name.pack(padx=(15,0), pady=(0,3), fill="x", anchor="nw")
        category_input = CTkEntry(category_frame, placeholder_text="Enter category name to delete", height=40, width= 435, corner_radius=0, border_color= "#AA3939", border_width=1)
        category_input.pack(pady=(1,10), padx=(15,0), anchor="w", side="bottom")

        def get_category_to_delete():
            delete_input = category_input.get()
            if products_management.search_delete_category(delete_input):
                category_confirm = CTkMessagebox(master=delete_app, message=f"Category {delete_input} deleted!", icon="check", option_1="Ok", title="", button_color= "#57C590",button_text_color="white", button_hover_color="#76C793", font=("Verdana", 12, "bold"))
                products_management.delete_category(delete_input)
            else:
                category_error = CTkMessagebox(master=delete_app, message=f"Category {delete_input} not found!", icon="cancel", option_1="Ok", title="", button_color= "#57C590",button_text_color="white", button_hover_color="#76C793", font=("Verdana", 12, "bold"))
                category_error.after(100, lambda: category_error.focus())
                if category_error.get() == "Ok":
                    category_error.destroy()
                return
            delete_app.after(100, delete_app.destroy())
            return delete_input

        delete_category = CTkFrame(delete_category_frame, height=45, width=190, fg_color="white", corner_radius=15)
        delete_category.pack(side="bottom", pady=(0,45))
        delete_category.pack_propagate(0)
        category_button = CTkButton(delete_category, text="Delete", text_color="white", font=("Verdana", 15, "bold"), anchor="center", corner_radius=15, fg_color="#AA3939", hover_color="#8B2F2F", command=lambda: get_category_to_delete())
        category_button.pack(expand=True, fill="both")
                
        delete_tab._segmented_button.configure(height = 30, font =("Verdana", 12, "bold"))  
        
    def autoadd_product():
        products_management = InventoryManagement(engine)
        autoadd_app = CTkToplevel()
        autoadd_app.title("Add products automatic")
        autoadd_app.geometry("500x300+750+350")
        autoadd_app.after(100, lambda: autoadd_app.focus())
        autoadd_app.pack_propagate(0)

        autoadd_frame = CTkFrame(autoadd_app, fg_color = "white")
        autoadd_frame.pack(fill="both", expand= True)
        
        autoadd_label = CTkLabel(autoadd_frame, text="Upload an Excel file to register products...", text_color="#5E5E5E", font=("Arial", 20, "bold"), anchor="center")
        autoadd_label.pack(pady=(100,0))
        autoadd_button = CTkButton(autoadd_frame, text="Submit", fg_color="#57C590", hover_color="#49A578", font=("Verdana", 15, "bold"), text_color="white",height=35, width=150, command=lambda:products_management.choose_file())
        autoadd_button.pack(anchor="center", pady= (20,0))
        
        created_label = CTkLabel(autoadd_frame, height=30,width=250, font=("Verdana", 12, "bold"), text_color="green", text="Products Created")
        created_label.pack_forget()

        question_data = Image.open(r"images\question.png")
        question_image = CTkImage(light_image=question_data, dark_image=question_data, size=(18,18))    
        question_button = CTkButton(autoadd_frame, width = 18, height=18, corner_radius=4, anchor="w", text="", fg_color="#57C590", hover_color="#49A578", image=question_image)
        question_button.pack_propagate(0)
        question_button.pack(pady=10, padx=10, side="bottom", anchor="se")

    





# def close_app():
#     delete_button.configure(image = delete_image_white)
#     delete_app.after(50,delete_app.destroy)

# delete_image_data_white = Image.open(r"images\close_white.png")
# delete_image_white = CTkImage(light_image=delete_image_data_white, dark_image=delete_image_data_white, size=(25,25))
# delete_image_data = Image.open(r"images\clear.png")
# delete_image_frame = CTkFrame(delete_app_mainframe, fg_color="white")
# delete_image_frame.pack(padx=(5,0), pady=(6,0))
# delete_image_frame.place(relx=0.89, rely=0.01)
# delete_image = CTkImage(light_image=delete_image_data, dark_image=delete_image_data, size=(15,15))
# delete_button = CTkButton(delete_image_frame, image=delete_image, text="", anchor="center", width=40, fg_color="white", hover_color="white", command=close_app)
# delete_button.pack(pady=(10,0))

            



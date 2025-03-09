import __init__
import customtkinter as ctk
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
class InventoryApp():
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.products_management = InventoryManagement(engine)
        self.create_main_info()
        self.create_table()
    

    def create_main_info(self):
        self.frame_bg_color = "#57C590"
        self.title_font = ctk.CTkFont(family="Verdana", size = 35, weight= "bold")
        self.add_button_font = ctk.CTkFont(family="Verdana", size = 13, weight= "bold")
        self.page_title_frame = ctk.CTkFrame(self.parent, width = 100, height= 15, fg_color="#F7EBE7")
        self.page_title_frame.pack(fill = "x", anchor = "center")
        self.page_title = ctk.CTkLabel(self.page_title_frame, text = "Inventory", font = self.title_font, text_color= "#39853C")
        self.page_title.pack(padx = 50, pady = 30, side="left", anchor = "nw", fill="x" )
        

        self.infos_frame = ctk.CTkFrame(self.parent, height= 200, width= 880, fg_color="#F7EBE7")
        self.infos_frame.pack(side="top")
        self.infos_frame.pack_propagate(0)

        self.infos_frame_font = ctk.CTkFont(family = "Verdana", size = 18, weight = "bold")


        self.total_value_frame = ctk.CTkFrame(master=self.infos_frame, height=50, width=50,  fg_color=self.frame_bg_color, corner_radius=20)
        self.total_value_frame.pack(padx = 20, fill = "both", side = "left", expand = True, anchor="center")
        self.total_value_frame.pack_propagate(0)
        self.inventory_image_data = Image.open(r"images\inventory.png")
        self.inventory_image = ctk.CTkImage(dark_image=self.inventory_image_data, light_image= self.inventory_image_data, size=(70, 70))
        self.inventory_image_label = ctk.CTkLabel(master=self.total_value_frame, text= "", image=self.inventory_image)
        self.inventory_image_label.pack(pady = (15, 5), padx = 0)
        self.total_text_label = ctk.CTkLabel(master = self.total_value_frame, text = "Products Available", font = self.infos_frame_font, text_color= "#FFFFFF")
        self.total_text_label.place(relx = 0.5, rely = 0.5, anchor = "center")
        self.total_text_label.pack(pady = 3)
        self.total_products = ctk.CTkLabel(master = self.total_value_frame, text = f"{self.products_management.count_products()}", font =("Verdana", 25, "bold"), text_color= "#FFFFFF")
        self.total_products.pack(padx = 5, pady = (5, 15), anchor = "s", side = "bottom")
        

        self.category_frame = ctk.CTkFrame(self.infos_frame, height=50, width=50, fg_color=self.frame_bg_color, corner_radius=20)
        self.category_frame.pack(padx = 20, fill = "both", side="left", expand = True)
        self.category_frame.pack_propagate(0)
        self.category_image_data = Image.open(r"images\categorization.png")
        self.category_image = ctk.CTkImage(light_image=self.category_image_data, dark_image=self.category_image_data, size=(70,70))
        self.category_image_label = ctk.CTkLabel(self.category_frame, text="", image = self.category_image)
        self.category_image_label.pack(pady = (15, 5), padx = 0)
        self.category_text_label = ctk.CTkLabel(self.category_frame, font=self.infos_frame_font, text_color="#FFFFFF", text="Total Categories")
        self.category_text_label.place(relx = 0.5, rely = 0.5, anchor = "center")
        self.category_text_label.pack(pady = 3)
        self.category_total = ctk.CTkLabel(master = self.category_frame, text = f"{self.products_management.get_total_categories()}", font =("Verdana", 25, "bold"), text_color= "#FFFFFF")
        self.category_total.pack(padx = 5, pady = (5, 15), anchor = "s", side = "bottom")

        self.stock_value_frame = ctk.CTkFrame(self.infos_frame, height=50, width=50, fg_color=self.frame_bg_color, corner_radius=20)
        self.stock_value_frame.pack(padx = 20, fill = "both", side="left", expand = True)
        self.stock_value_frame.pack_propagate(0)
        self.stock_value_image_data = Image.open(r"images\increase.png")
        self.stock_value_image = ctk.CTkImage(light_image=self.stock_value_image_data, dark_image=self.stock_value_image_data, size=(70,70))
        self.stock_value_image_label = ctk.CTkLabel(self.stock_value_frame, text="", image = self.stock_value_image)
        self.stock_value_image_label.place(relx = 0.5, rely = 0.5, anchor = "center")
        self.stock_value_image_label.pack(pady = (15, 5), padx = 0)
        self.stock_value_text_label = ctk.CTkLabel(self.stock_value_frame, font=self.infos_frame_font, text_color="#FFFFFF", text="Stock Value")
        self.stock_value_text_label.place(relx = 0.5, rely = 0.5, anchor = "center")
        self.stock_value_text_label.pack(pady = 3)
        self.stock_value = ctk.CTkLabel(master = self.stock_value_frame, text = f"{self.products_management.get_stock_value()}", font =("Verdana", 25, "bold"), text_color= "#FFFFFF")
        self.stock_value.pack(padx = 5, pady = (5, 15), anchor = "s", side = "bottom")




    def create_table(self):
        self.query_frame = ctk.CTkFrame(self.parent, height= 50, width=1270, fg_color="#F7EBE7")
        self.query_frame.pack(padx=(0,10), pady=(70, 0)) #"#F7EBE7"#EFE4E1
        self.query_frame.pack_propagate(0)

        self.query_entry = ctk.CTkEntry(self.query_frame, corner_radius=10, fg_color="white", placeholder_text="Search by product...", width=400)
        self.query_entry.pack(pady=(7,5), fill = "y", anchor="w", side="left")

        def search_table():
            self.query = self.query_entry.get()
            self.table.configure(values = self.products_management.list_query_products(self.query))

        def search_category():
            self.query = self.choose_category.get()
            self.table.configure(values = self.products_management.list_query_categories(self.query))

        def clear_entry():
            change_focus()
            self.query_entry.delete(0, "end") #Deleta do primeiro caracter até o final
            self.table.configure(values = self.products_management.create_table_view())
            self.choose_category.set("Categories")
        
        def change_focus():
            return self.total_value_frame.focus_set()

        self.search_data = Image.open(r"images\search.png")
        self.search_image = ctk.CTkImage(light_image=self.search_data, dark_image=self.search_data, size=(25,25))    
        self.query_search = ctk.CTkButton(self.query_frame, corner_radius=10, width = 40, anchor="w", text="", fg_color="#57C590", hover_color="#49A578", image=self.search_image, command=search_table)
        self.query_search.pack_propagate(0)
        self.query_search.pack(pady=(9,7), padx=(2,0), fill = "y", side="left", anchor="center")

    

        self.clean_data = Image.open(r"images\clean.png")
        self.clean_image = ctk.CTkImage(light_image=self.clean_data, dark_image=self.clean_data, size=(25,25))    
        self.query_clean = ctk.CTkButton(self.query_frame, corner_radius=10, width = 40, anchor="w", text="", fg_color="#57C590", hover_color="#49A578", image=self.clean_image, command=clear_entry) ##Sem parentes pois não queremos que a função seja chamada direto, apenas quando clicar no botão
        self.query_clean.pack_propagate(0)
        self.query_clean.pack(pady=(9,7), padx=(2,0), fill = "y", side="left", anchor="center")


        self.choose_category = ctk.CTkComboBox(self.query_frame, values = self.products_management.list_categories_name(), text_color="#5E5E5E", font = ("Verdana", 12, "bold"), fg_color="white", button_color="#CECECE", button_hover_color="#B7B7B7", corner_radius= 10, dropdown_fg_color="white", dropdown_text_color="#5E5E5E", dropdown_font=("Verdana", 12, "bold"), border_color="#CECECE", width= 200, height=40)
        self.choose_category.pack(padx = (150,0), pady=(9,5), side="left", anchor= "w")
        self.choose_category.set("Categories")
        self.category_search = ctk.CTkButton(self.query_frame, corner_radius=10, width = 20, height= 30, anchor="w", text="", fg_color="#57C590", hover_color="#49A578", image=self.search_image, command=search_category)
        self.category_search.pack_propagate(0)
        self.category_search.pack(pady=(9,3), padx=(3,0), side="left", anchor="center")

        self.delete_button = ctk.CTkButton(self.query_frame, text = "- Delete", text_color= "white", font=self.add_button_font, corner_radius=20, fg_color="#AA3939", hover_color="#8B2F2F",anchor= "center", command=lambda: self.delete_product_app(), width = 25)
        self.delete_button.pack(padx=3,pady = (9,7), anchor = "ne", side="right", fill="y")
        self.autocreate_button = ctk.CTkButton(self.query_frame, text = "+ AutoAdd", text_color= "white", font=self.add_button_font, corner_radius=20, fg_color=self.frame_bg_color, hover_color="#4CAF50",anchor= "center", command=lambda: self.autoadd_product(), width = 25)
        self.autocreate_button.pack(padx=3,pady = (9,7), anchor = "ne", side="right", fill="y")
        self.create_button = ctk.CTkButton(self.query_frame, text = "+ Add", text_color= "white", font=self.add_button_font, corner_radius=20, fg_color=self.frame_bg_color, hover_color="#4CAF50",anchor= "center", command=lambda: self.add_product_app(), width = 25)
        self.create_button.pack(padx=3,pady = (9,7), anchor = "ne", side="right", fill="y")

        self.table_column_frame = ctk.CTkFrame(self.parent, width=1269, height=25, fg_color= "transparent")
        self.table_column_frame.pack(padx=(0,8),pady=(3,0))
        self.table_column_frame.pack_propagate(0)
        self.table_frame = ctk.CTkScrollableFrame(self.parent, width= 1270, height = 500, fg_color= "transparent", scrollbar_button_color=self.frame_bg_color,)
        self.table_frame.pack(padx= 0, pady = (0, 80), expand= True, anchor='n',)
        
        self.table_column_data = [
            ['ID', 'Name', 'Unit Price', 'Quantity', 'Expiration Date', 'Enter Date', 'Active', 'Category']

        ]

        self.table_column = CTkTable(self.table_column_frame, values= self.table_column_data, corner_radius = 0, text_color= "white", width = 155, header_color=self.frame_bg_color, font=('Verdana', 12, 'bold'))
        self.table_column.pack(padx = 0, pady= 0, expand = True, fill= "both")
        self.table = CTkTable(self.table_frame, values = self.products_management.create_table_view(), hover_color="#B4B4B4", width = 155, corner_radius = 0, fg_color = "#F7EBE7")
        self.table.pack(fill = "both",expand = True, pady=0)


    def add_product_app(self):
        self.product_app = ctk.CTkToplevel()
        self.name_font = ctk.CTkFont("Verdana", 13, "normal")
        self.product_app.title("Add Product")
        self.product_app.geometry("500x600+750+200")
        self.product_app.resizable(0,0)
        self.product_app.config(background="#F6F6F6")
        #Depois de abrir totalmente a janela, ela será o foco, ou seja, vai sobrepor a janela
        self.product_app.after(100, lambda: self.product_app.deiconify)
        self.product_app.after(150, lambda: self.product_app.focus())
        
        
        self.product_app_frame = ctk.CTkFrame(self.product_app, fg_color="white")
        self.product_app_frame.pack(fill = "both", expand = True)

        self.main_title_frame = ctk.CTkFrame(self.product_app_frame, height=60, width=60, fg_color="white")
        self.main_title_frame.pack(anchor="center", fill= "x")

        self.main_title = ctk.CTkLabel(self.main_title_frame, height= 30, width= 30, text = "Add new product", text_color="#5E5E5E", font=("Arial", 20, "bold"))
        self.main_title.pack(padx= 10, pady= (30,10))
        

        self.name_frame = ctk.CTkFrame(self.product_app_frame, height=50,width=60, fg_color="white")
        self.name_frame.pack(anchor = "center", fill="x", pady=(40,0))
        self.product_name = ctk.CTkLabel(self.name_frame, text="Name*", font=("Verdana", 14, "normal"), text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
        self.product_name.pack(padx=(30,0), fill="x", anchor="nw")
        self.name_intern_frame = ctk.CTkFrame(self.name_frame, fg_color="white")
        self.name_intern_frame.pack(fill="x")
        self.name_input = ctk.CTkEntry(self.name_intern_frame, placeholder_text="Enter product name", height=40, width= 435, corner_radius=0, border_color= "#57C590", border_width=1)
        self.name_input.pack(pady=(1), padx=(30,0), anchor="w", side="top")
        self.name_error = ctk.CTkLabel(self.name_intern_frame, text_color="red", height=25)


        self.unit_price_frame = ctk.CTkFrame(self.product_app_frame, height=50,width=60, fg_color="white")
        self.unit_price_frame.pack(anchor = "center", fill="x", pady=(25,0))
        self.unit_price = ctk.CTkLabel(self.unit_price_frame, text="Unit Price*", font=self.name_font, text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
        self.unit_price.pack(padx=(30,0), fill="x", anchor="nw")
        self.unit_price_intern_frame = ctk.CTkFrame(self.unit_price_frame, fg_color="white")
        self.unit_price_intern_frame.pack(fill="x")
        self.unit_price_input = ctk.CTkEntry(self.unit_price_intern_frame, placeholder_text="Enter unit price", height=40, width= 435, corner_radius=0, border_color= "#57C590", border_width=1)
        self.unit_price_input.pack(pady=(1), padx=(30,0), anchor="w", side="top")
        self.unit_price_error = ctk.CTkLabel(self.unit_price_intern_frame, text_color="red", height=25)

        self.quantity_frame = ctk.CTkFrame(self.product_app_frame, height=50,width=60, fg_color="white")
        self.quantity_frame.pack(anchor = "center", fill="x", pady=(25,0))
        self.quantity = ctk.CTkLabel(self.quantity_frame, text="Quantity*", font=self.name_font, text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
        self.quantity.pack(padx=(30,0), fill="x", anchor="nw")
        self.quantity_intern_frame = ctk.CTkFrame(self.quantity_frame, fg_color="white")
        self.quantity_intern_frame.pack(fill="x")
        self.quantity_input = ctk.CTkEntry(self.quantity_intern_frame, placeholder_text="Enter quantity", height=40, width= 435, corner_radius=0, border_color= "#57C590", border_width=1)
        self.quantity_input.pack(pady=(1), padx=(30,0), anchor="w", side="top")
        #So chama esse quando dar algum erro!
        self.quantity_error = ctk.CTkLabel(self.quantity_intern_frame, text_color="red", height=25)


        self.options_frame = ctk.CTkFrame(self.product_app_frame, fg_color="white")
        self.options_frame.pack(fill="x")

        self.category_frame = ctk.CTkFrame(self.options_frame, height=50,width=150, fg_color="white")
        self.category_frame.pack(anchor="w", padx = (30,0), pady=(25,10), side="left")
        self.category = ctk.CTkLabel(self.category_frame, text="Category*(write or choose)", font=self.name_font, text_color= "#5E5E5E", anchor="nw", fg_color="white", width= 70, height= 20)
        self.category.pack(anchor="nw")
        self.category_option = ctk.CTkComboBox(self.category_frame, values = self.products_management.list_categories_name(), text_color="#5E5E5E", font = ("Verdana", 13, "bold"), height=34, width= 200, fg_color="#DEDEDE", button_color="#DEDEDE", button_hover_color="#BCBCBC", corner_radius= 10, dropdown_fg_color="#DEDEDE", dropdown_text_color="#5E5E5E", dropdown_font=("Verdana", 13, "bold"), border_width=0)
        self.category_option.pack(pady=(1,10))
        self.category_option.set("Outros")

        self.calendar_image_data = Image.open(r"images\calendar_1.png")
        self.calendar_image = ctk.CTkImage(light_image=self.calendar_image_data, dark_image=self.calendar_image_data)
        self.expiration_date_frame = ctk.CTkFrame(self.options_frame, height=60, width=180, fg_color="white")
        self.expiration_date_frame.pack(side="right", padx=(0,35), pady=(6,0))
        self.expiration_date = ctk.CTkLabel(self.expiration_date_frame, text="Expiration date(optional)", font=self.name_font, text_color= "#5E5E5E", anchor="nw", fg_color="white", width= 70, height= 20)
        self.expiration_date.pack(anchor="ne")

        def create_calendar():
            self.calendar_screen = ctk.CTkToplevel()
            self.calendar_screen.geometry("250x200+1035+607")
            self.calendar_screen.overrideredirect(True)
            self.calendar_screen.resizable(0,0)
            self.calendar = Calendar(self.calendar_screen, mindate=date.today(), showweeknumbers=False, showothermonthdays=False, showcurrent=True, date_pattern="dd/mm/yyyy", locale="en_US", background="#56C46A", headersbackground="#53BC89", headersforeground="white", weekendbackground = "white", weekendforeground="black", selectbackground="#56C46A", selectforeground="white", font=("Arial black", 10,"normal"))
            self.calendar.pack(expand=True, fill="both")
            #lambda necessário, pois after precisa de uma função para rodar apos 100 ms
            self.calendar_screen.grab_set()
            self.calendar_screen.after(100, lambda: self.product_app.focus())
            

            def date_updated(event):
                global date_choosed
                date_choosed = self.calendar.get_date()
                self.calendar_label.configure(text=date_choosed)
                self.calendar_screen.after(100, lambda:self.calendar_screen.destroy())
                #o método bind automaticamente passa um objeto de evento como argumento para a função date_updated quando o evento ocorre
            self.calendar.bind("<<CalendarSelected>>", date_updated)
        

            
            
        self.calendar_frame = ctk.CTkFrame(self.expiration_date_frame, height=32, width= 165, fg_color="#DEDEDE", border_width=2, border_color="#57C590")
        self.calendar_frame.pack(anchor="e")
        self.calendar_label = ctk.CTkLabel(self.calendar_frame, height=32, width= 165, fg_color="#DEDEDE", text="", corner_radius=10, anchor="e", font=("Verdana", 11.5, "normal"), text_color="#5E5E5E")
        self.calendar_label.pack(side="left", fill="x")
        self.calendar_button = ctk.CTkButton(self.calendar_frame, height=32, width=35, text="", corner_radius=0, border_width=1, fg_color="#DEDEDE" , border_color= "#57C590", hover_color="#BCBCBC", anchor="center", image=self.calendar_image, command=lambda:create_calendar())
        self.calendar_button.pack(anchor="ne", side="left")
        
        self.add_frame = ctk.CTkFrame(self.product_app_frame, height=45, width=190, fg_color="white", corner_radius=15)
        self.add_frame.pack(side="bottom", pady=(0,45))
        self.add_frame.pack_propagate(0)
        self.add_button = ctk.CTkButton(self.add_frame, text="Add", text_color="white", font=("Verdana", 15, "bold"), anchor="center", corner_radius=15, fg_color="#57C590", hover_color="#4FB483", command=lambda: product_add())
        self.add_button.pack(expand=True, fill="both")



        def product_add():
            global date_choosed
            self.name_value = ""
            self.name_value = self.name_input.get().strip()
            if self.name_value == "":
                self.name_error.configure(text="Name entry can not be empty!")
                self.name_error.pack(side="bottom", anchor="w", padx=(30,0))
                self.name_error.pack_propagate(0)
                return
            else:
                self.name_error.pack_forget()
            #Tratando o que o usuario digitar em Unit Price e Quantity, para só aceitar números e evitar campos vazios
            try:  
                self.unit_price_value = float(self.unit_price_input.get().strip())
            except ValueError:
                self.unit_price_error.configure(text="Invalid input: The unit price must be a numeric value.")
                self.unit_price_error.pack(side="bottom", anchor="w", padx=(30,0))
                self.unit_price_error.pack_propagate(0)
            else:
                self.unit_price_error.pack_forget()

            try:
                self.quantity_value = int(self.quantity_input.get().strip())
            except ValueError:
                self.quantity_error.configure(text="Invalid input: The quantity must be a numeric value.")
                self.quantity_error.pack(side="bottom", anchor="w", padx=(30,0))
                self.quantity_error.pack_propagate(0)
                return
            else:
                self.quantity_error.pack_forget()
            
            category_value = self.category_option.get().strip()
            if date_choosed:
                self.expiration_date = datetime.strptime(date_choosed, "%d/%m/%Y")
            else:
                self.expiration_date = None
            self.category_id = self.products_management.get_category_id_by_name(category_value)

            try:
                product = Products(name=self.name_value, kg_price=self.unit_price_value, quantity=self.quantity_value, enter_date= date.today() ,expiration_date = self.expiration_date, category_id= self.category_id)
                self.products_management.create_product(product)
                self.confirm_message = CTkMessagebox(master = self.product_app, message=f"{self.name_value} created!", icon="check", button_color= "#57C590",option_1="Close", title = "", button_text_color="white", button_hover_color="#76C793", font=("Verdana", 12, "bold"))
                self.confirm_message.after(100, lambda: self.confirm_message.focus())
                if self.confirm_message.get() =="Close":
                    self.product_app_frame.after(300,self.product_app.destroy())
            except UnboundLocalError:
                self.unit_price_error.configure(text="Invalid input: The unit price must be a numeric value.")
            except AttributeError:
                self.unit_price_error.configure(text="Invalid input: The unit price must be a numeric value.")

    def delete_product_app(self): 
        self.delete_app = ctk.CTkToplevel()
        self.delete_app.title("Delete products")
        self.delete_app.geometry("500x300+750+350")
        self.delete_app.after(100, lambda: self.delete_app.deiconify)
        self.delete_app.after(150, lambda: self.delete_app.focus())
    

        self.delete_app_mainframe = ctk.CTkFrame(self.delete_app, fg_color="white")
        self.delete_app_mainframe.pack(fill="both", expand=True)
        self.delete_app_mainframe.pack_propagate(0)

        self.delete_tab = ctk.CTkTabview(self.delete_app_mainframe, fg_color="white", segmented_button_selected_color="red", segmented_button_selected_hover_color="#8B2F2F", segmented_button_unselected_hover_color="#8B2F2F", text_color="#FFFFFF", anchor="nw")  
        self.delete_tab.pack(fill="both", expand=True, padx= 3, pady=3)
        self.delete_tab.pack_propagate(0)


        #Tag do produto ====================

        self.products_tab = self.delete_tab.add("    Products    ")

        self.delete_product_frame = ctk.CTkFrame(self.products_tab, fg_color="white")
        self.delete_product_frame.pack_propagate(0)
        self.delete_product_frame.pack(fill = "both", expand = True)

        self.name_frame = ctk.CTkFrame(self.delete_product_frame, height=50,width=60, fg_color="white")
        self.name_frame.pack(anchor = "center", fill="x", pady=(30,0))
        self.product_name = ctk.CTkLabel(self.name_frame, text="Name", font=("Verdana", 16, "bold"), text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
        self.product_name.pack(padx=(15,0), pady=(0,3), fill="x", anchor="nw")
        self.name_intern_frame = ctk.CTkFrame(self.delete_product_frame, fg_color="white")
        self.name_intern_frame.pack(fill="x")
        self.name_input = ctk.CTkEntry(self.name_intern_frame, placeholder_text="Enter product name to delete", height=40, width= 435, corner_radius=0, border_color= "#AA3939", border_width=1)
        self.name_input.pack(pady=(1,10), padx=(15,0), anchor="w", side="top")

        def get_product_to_delete():
            self.delete_input = self.name_input.get()
            if self.products_management.search_delete_product(self.delete_input):
                self.products_management.delete_product(self.delete_input)
                self.name_confirm = CTkMessagebox(master=self.delete_app, message=f"Product {self.delete_input} deleted!", icon="check", option_1="Ok", title="", button_color= "#57C590",button_text_color="white", button_hover_color="#76C793", font=("Verdana", 12, "bold"))
                if self.name_confirm.get() == "Ok":
                    self.name_confirm.destroy()
            else:
                self.name_error = CTkMessagebox(master=self.delete_app, message=f"Product {self.delete_input} not found!", icon="cancel", option_1="Ok", title="", button_color= "#57C590",button_text_color="white", button_hover_color="#76C793", font=("Verdana", 12, "bold"))
                self.name_error.after(100, lambda: self.name_error.focus())
                if self.name_error.get() == "Ok":
                    self.name_error.destroy()
                return
            self.delete_app.after(100, self.delete_app.destroy())
            return self.delete_input

        self.delete_frame = ctk.CTkFrame(self.delete_product_frame, height=45, width=190, fg_color="white", corner_radius=15)
        self.delete_frame.pack(side="bottom", pady=(0,45))
        self.delete_frame.pack_propagate(0)
        self.product_button = ctk.CTkButton(self.delete_frame, text="Delete", text_color="white", font=("Verdana", 15, "bold"), anchor="center", corner_radius=15, fg_color="#AA3939", hover_color="#8B2F2F", command=lambda: get_product_to_delete())
        self.product_button.pack(expand=True, fill="both")

        #Tab da categoria ==============

        self.categories_tab = self.delete_tab.add("    Categories    ")

        self.delete_category_frame = ctk.CTkFrame(self.categories_tab, fg_color="white")
        self.delete_category_frame.pack_propagate(0)
        self.delete_category_frame.pack(fill = "both", expand = True)


        self.category_frame = ctk.CTkFrame(self.delete_category_frame, height=50,width=60, fg_color="white")
        self.category_frame.pack(anchor = "center", fill="x", pady=(30,0))
        self.category_name = ctk.CTkLabel(self.category_frame, text="Category", font=("Verdana", 16, "bold"), text_color= "#5E5E5E",anchor="nw", fg_color="white", width= 70, height= 20)
        self.category_name.pack(padx=(15,0), pady=(0,3), fill="x", anchor="nw")
        self.category_input = ctk.CTkEntry(self.category_frame, placeholder_text="Enter category name to delete", height=40, width= 435, corner_radius=0, border_color= "#AA3939", border_width=1)
        self.category_input.pack(pady=(1,10), padx=(15,0), anchor="w", side="bottom")

        def get_category_to_delete():
            self.delete_input = self.category_input.get()
            if self.products_management.search_delete_category(self.delete_input):
                self.category_confirm = CTkMessagebox(master=self.delete_app, message=f"Category {self.delete_input} deleted!", icon="check", option_1="Ok", title="", button_color= "#57C590",button_text_color="white", button_hover_color="#76C793", font=("Verdana", 12, "bold"))
                if self.category_confirm.get() == "Ok":
                    self.category_confirm.destroy()
                self.products_management.delete_category(self.delete_input)
            else:
                self.category_error = CTkMessagebox(master=self.delete_app, message=f"Category {self.delete_input} not found!", icon="cancel", option_1="Ok", title="", button_color= "#57C590",button_text_color="white", button_hover_color="#76C793", font=("Verdana", 12, "bold"))
                self.category_error.after(100, lambda: self.category_error.focus())
                if self.category_error.get() == "Ok":
                    self.category_error.destroy()
                return
            self.delete_app.after(100, self.delete_app.destroy())
            return self.delete_input

        self.delete_category = ctk.CTkFrame(self.delete_category_frame, height=45, width=190, fg_color="white", corner_radius=15)
        self.delete_category.pack(side="bottom", pady=(0,45))
        self.delete_category.pack_propagate(0)
        self.category_button = ctk.CTkButton(self.delete_category, text="Delete", text_color="white", font=("Verdana", 15, "bold"), anchor="center", corner_radius=15, fg_color="#AA3939", hover_color="#8B2F2F", command=lambda: get_category_to_delete())
        self.category_button.pack(expand=True, fill="both")
                
        self.delete_tab._segmented_button.configure(height = 30, font =("Verdana", 12, "bold"))  
        
    def autoadd_product(self):
        self.autoadd_app = ctk.CTkToplevel()
        self.autoadd_app.title("Add products automatic")
        self.autoadd_app.geometry("500x300+750+350")
        self.autoadd_app.after(100, lambda: self.autoadd_app.focus_force())
        self.autoadd_app.pack_propagate(0)

        self.autoadd_frame = ctk.CTkFrame(self.autoadd_app, fg_color = "white")
        self.autoadd_frame.pack(fill="both", expand= True)
        
        self.autoadd_label = ctk.CTkLabel(self.autoadd_frame, text="Upload an Excel file to register products...", text_color="#5E5E5E", font=("Arial", 20, "bold"), anchor="center")
        self.autoadd_label.pack(pady=(100,0))
        self.autoadd_button = ctk.CTkButton(self.autoadd_frame, text="Submit", fg_color="#57C590", hover_color="#49A578", font=("Verdana", 15, "bold"), text_color="white",height=35, width=150, command=lambda: on_choose_file())
        self.autoadd_button.pack(anchor="center", pady= (20,0))
        
        def on_choose_file():
            if self.products_management.choose_file():
                self.autoadd_confirm = CTkMessagebox(master=self.autoadd_app, message=f"Products from excel created!", icon="check", option_1="Ok", title="", button_color= "#57C590",button_text_color="white", button_hover_color="#76C793", font=("Verdana", 12, "bold"))
                if self.autoadd_confirm.get() == "Ok":
                    self.autoadd_app.destroy()
                    return
            else:
                self.autoadd_error = CTkMessagebox(master=self.autoadd_app, message=f"Please Upload a Valid File", icon="warning", option_1="Ok", title="", button_color= "#57C590",button_text_color="white", button_hover_color="#76C793", font=("Verdana", 12, "bold"))
                if self.autoadd_error.get() == "Ok":
                    self.autoadd_app.after(400, lambda: self.autoadd_app.deiconify())
                    self.autoadd_app.after(500, lambda: self.autoadd_app.focus_force())

        self.question_data = Image.open(r"images\question.png")
        self.question_image = ctk.CTkImage(light_image=self.question_data, dark_image=self.question_data, size=(18,18))    
        self.question_button = ctk.CTkButton(self.autoadd_frame, width = 18, height=18, corner_radius=4, anchor="w", text="", fg_color="#57C590", hover_color="#49A578", image=self.question_image)
        self.question_button.pack_propagate(0)
        self.question_button.pack(pady=10, padx=10, side="bottom", anchor="se")
   


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

            



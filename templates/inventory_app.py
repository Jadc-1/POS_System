from customtkinter import *
from PIL import Image


def inventory_app(parent):
    title_font = CTkFont(family="Arial Black", size = 35, weight= "bold")
    page_title_frame = CTkFrame(parent, width = 100, height= 15, fg_color="#F7EBE7")
    page_title_frame.pack(fill = "x")
    page_title = CTkLabel(page_title_frame, text = "Inventory", font = title_font, text_color= "#39853C")
    page_title.pack(padx = 50, pady = 30, side="left", anchor = "nw", fill="x" )
    
    infos_frame = CTkFrame(parent, height= 200, width= 880, fg_color="#F7EBE7")
    infos_frame.pack(side="top")
    infos_frame.pack_propagate(0)

    infos_frame_font = CTkFont(family = "Arial Black", size = 17, weight = "bold")


    total_value_frame = CTkFrame(master=infos_frame, height=50, width=50,  fg_color="#57C590", corner_radius=20)
    total_value_frame.pack(padx = 20, fill = "both", side = "left", expand = True, anchor="center")
    total_value_frame.pack_propagate(0)
    inventory_image_data = Image.open(r"images\inventory.png")
    inventory_image = CTkImage(dark_image=inventory_image_data, light_image= inventory_image_data, size=(70, 70))
    inventory_image_label = CTkLabel(master=total_value_frame, text= "", image=inventory_image)
    inventory_image_label.pack(pady = (15, 5), padx = 0)
    total_text_label = CTkLabel(master = total_value_frame, text = "Products Available", font = infos_frame_font, text_color= "#FFFFFF")
    total_text_label.place(relx = 0.5, rely = 0.5, anchor = "center")
    total_text_label.pack(pady = 3)
    total_products = CTkLabel(master = total_value_frame, text = "123", font =("Arial Black", 25, "bold"), text_color= "#FFFFFF")
    total_products.pack(padx = 5, pady = (5, 15), anchor = "s", side = "bottom")
    

    frame_2 = CTkFrame(infos_frame, height=50, width=50, fg_color="#57C590", corner_radius=20)
    frame_2.pack(padx = 20, fill = "both", side="left", expand = True)
    frame_3 = CTkFrame(infos_frame, height=50, width=50, fg_color="#57C590", corner_radius=20)
    frame_3.pack(padx = 20, fill = "both", side= "left", expand = True)





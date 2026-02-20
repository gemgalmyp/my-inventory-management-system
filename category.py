from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from employees import connect_database

def category_form(window):
    global back_image, logo
    category_frame = Frame(window, width=1100, height=680, bg="white")
    category_frame.place(x=320, y=130, width=1100, height=680)

    heading_label = Label(
        category_frame, 
        text="Manage Category Details", 
        font=("Franklin Gothic Book (Headings)", 17, "bold"), 
        bg="#045517", 
        fg="white"
    )
    heading_label.place(x=0, y=0, relwidth=1)

    back_image = PhotoImage(file="back_button.png")

    back_button = Button(
        category_frame,
        image=back_image,
        bd = 0,
        cursor = "hand2",
        bg="white",
        command=lambda: category_frame.place_forget() 
    )
    back_button.place(x=10, y=50)
    
    logo = PhotoImage(file="background_category.png")
    background_label = Label(category_frame, image=logo, bg="white")
    background_label.place(x=20, y=95)

    details_frame = Frame(category_frame, bg="white")
    details_frame.place(x=570, y=50)

    id_label = Label(details_frame, 
                          text="ID", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    id_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
    id_entry = Entry(details_frame, 
                     font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                     width=30, 
                     bg="lightyellow"
    )
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    category_name_label = Label(details_frame, 
                          text="Category Name", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    category_name_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
    category_name_entry = Entry(details_frame, 
                     font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                     width=30, 
                     bg="lightyellow"
    )
    category_name_entry.grid(row=1, column=1, padx=10, pady=10)

    description_label = Label(details_frame, 
                          text="Description", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    description_label.grid(row=2, column=0, padx=20, pady=20, sticky="nw")
    description_text = Text(details_frame, 
                            font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                            width=30, 
                            height=5, 
                            bg="white", 
                            bd=2
    )
    description_text.grid(row=2, column=1, padx=10, pady=15)

    button_frame = Frame(category_frame, bg="white")
    button_frame.place(x=680, y=300)

    add_button = Button(
        button_frame, 
        text="Add", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=9,
        cursor="hand2", 
        bg="white", 
        fg="#045517" 
        
    )
    add_button.grid(row=0, column=0, padx=20, pady=9)


    delete_button = Button(
        button_frame, 
        text="Delete", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=9,
        cursor="hand2", 
        bg="white", 
        fg="#045517" 
        
    )
    delete_button.grid(row=0, column=1, padx=20, pady=9)

    treeview_frame = Frame(category_frame, bg="white")
    treeview_frame.place(x=570, y=350, height=300, width=500)

    scrolly = Scrollbar(treeview_frame, orient=VERTICAL)
    scrollx = Scrollbar(treeview_frame, orient=HORIZONTAL)
    treeview = ttk.Treeview(treeview_frame, column=('ID', 'name', 'description'), show='headings', yscrollcommand=scrolly.set, xscrollcommand=scrollx.set) 
    scrolly.pack(side=RIGHT, fill=Y)
    scrollx.pack(side=BOTTOM, fill=X)
    scrollx.config(command=treeview.xview)
    scrolly.config(command=treeview.yview)
    treeview.pack(fill=BOTH, expand=True)

    treeview.heading('ID', text='ID')
    treeview.heading('name', text='Category Name')
    treeview.heading('description', text='Description')
    treeview.column('ID', width=80)
    treeview.column('name', width=180)
    treeview.column('description', width=300)
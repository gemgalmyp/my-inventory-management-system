from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from employees import connect_database


def product_form(window):
    global back_image
    product_frame = Frame(window, width=1100, height=680, bg="white")
    product_frame.place(x=320, y=130)

    back_image = PhotoImage(file="back_button.png")

    back_button = Button(
        product_frame,
        image=back_image,
        bd = 0,
        cursor = "hand2",
        bg="white",
        command=lambda: product_frame.place_forget() 
    )
    back_button.place(x=10, y=15)

    # LEFT FRAME
    left_frame = Frame(product_frame, bg="white", bd=2, relief=GROOVE)
    left_frame.place(x=20, y=65)

    heading_label = Label(
        left_frame, 
        text="Manage Product Details", 
        font=("Franklin Gothic Book (Headings)", 17, "bold"), 
        bg="#045517", 
        fg="white"
    )
    heading_label.grid(row=0, columnspan=2, sticky="we")

    category_label = Label(left_frame, 
                          text="Category:", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    category_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
    category_combobox = ttk.Combobox(left_frame,
                                     font=("Franklin Gothic Book (Headings)", 13, "bold"),
                                     state="readonly",                                 
                                     width=28
    )
    category_combobox.grid(row=1, column=1, padx=20, pady=20)
    category_combobox.set("Empty")

    supplier_label = Label(left_frame, 
                          text="Supplier:", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    supplier_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
    supplier_combobox = ttk.Combobox(left_frame,
                                     font=("Franklin Gothic Book (Headings)", 13, "bold"),
                                     state="readonly",                                 
                                     width=28
    )
    supplier_combobox.grid(row=2, column=1, padx=20, pady=20)
    supplier_combobox.set("Empty")

    name_label = Label(left_frame, 
                          text="Name:", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    name_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
    name_entry = Entry(left_frame, 
                     font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                     width=30, 
                     bg="lightyellow"
    )
    name_entry.grid(row=3, column=1, padx=10, pady=20)

    price_label = Label(left_frame, 
                          text="Price:", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    price_label.grid(row=4, column=0, padx=20, pady=20, sticky="w")
    price_entry = Entry(left_frame, 
                     font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                     width=30, 
                     bg="lightyellow"
    )
    price_entry.grid(row=4, column=1, padx=10, pady=20)

    quantity_label = Label(left_frame, 
                          text="Quantity:", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    quantity_label.grid(row=5, column=0, padx=20, pady=20, sticky="w")
    quantity_entry = Entry(left_frame, 
                     font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                     width=30, 
                     bg="lightyellow"
    )
    quantity_entry.grid(row=5, column=1, padx=10, pady=20)

    status_label = Label(left_frame, 
                          text="Status:", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    status_label.grid(row=6, column=0, padx=20, pady=20, sticky="w")
    status_combobox = ttk.Combobox(left_frame,
                                   values=("Active", "Inactive"),
                                   font=("Franklin Gothic Book (Headings)", 13, "bold"),
                                   state="readonly",                                 
                                   width=28
    )
    status_combobox.grid(row=6, column=1, padx=20, pady=20)
    status_combobox.set("Select Status")

    button_frame = Frame(left_frame, bg="white")
    button_frame.grid(row=7, columnspan=2, pady=10)

    add_button = Button(
        button_frame, 
        text="Add", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="white", 
        fg="#045517"
        # command=lambda: add_category(category_id_entry.get(), category_name_entry.get(), description_text.get("1.0", END).strip(), treeview)
        
    )
    add_button.grid(row=0, column=0, padx=10, pady=9)

    update_button = Button(
        button_frame, 
        text="Update", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="white", 
        fg="#045517"
        # command=lambda: add_category(category_id_entry.get(), category_name_entry.get(), description_text.get("1.0", END).strip(), treeview)
        
    )
    update_button.grid(row=0, column=1, padx=10, pady=9)

    delete_button = Button(
        button_frame, 
        text="Delete", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="white", 
        fg="#045517"
        # command=lambda: add_category(category_id_entry.get(), category_name_entry.get(), description_text.get("1.0", END).strip(), treeview)
        
    )
    delete_button.grid(row=0, column=2, padx=10, pady=9)

    clear_button = Button(
        button_frame, 
        text="Clear", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="white", 
        fg="#045517"
        # command=lambda: add_category(category_id_entry.get(), category_name_entry.get(), description_text.get("1.0", END).strip(), treeview)
        
    )
    clear_button.grid(row=0, column=3, padx=10, pady=9)

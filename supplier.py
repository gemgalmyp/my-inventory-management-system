from tkinter import *



def supplier_form(window):
    global back_image  
    supplier_frame = Frame(window, width=1100, height=680, bg="white")
    supplier_frame.place(x=320, y=130, width=1100, height=680)
    heading_label = Label(
        supplier_frame, 
        text="Manage Supplier Details", 
        font=("Franklin Gothic Book (Headings)", 17, "bold"), 
        bg="#045517", 
        fg="white"
    )
    heading_label.place(x=0, y=0, relwidth=1)

    back_image = PhotoImage(file="back_button.png")

    back_button = Button(
        supplier_frame,
        image=back_image,
        bd = 0,
        cursor = "hand2",
        bg="white",
        command=lambda: supplier_frame.place_forget() 
    )
    back_button.place(x=10, y=50)

    left_frame = Frame(supplier_frame, bg="#045517")
    left_frame.place(x=10, y=90, width=485, height=565)

    invoice_label = Label(left_frame, 
                          text="Invoice No.", 
                          font=("Franklin Gothic Book (Headings)", 12, "bold"), 
                          bg="#045517", 
                          fg="white"
    )
    invoice_label.grid(row=0, column=0, padx=(10, 20), pady=40, sticky="w")
    invoice_entry = Entry(left_frame, font=("Franklin Gothic Book (Headings)", 12, "bold"), width=30, bg="lightyellow")
    invoice_entry.grid(row=0, column=1, padx=10, pady=15)

    name_label = Label(left_frame, 
                          text="Supplier Name: ", 
                          font=("Franklin Gothic Book (Headings)", 12, "bold"), 
                          bg="#045517", 
                          fg="white"
    )
    name_label.grid(row=1, column=0, padx=(10, 20), pady=15, sticky="w")
    name_entry = Entry(left_frame, font=("Franklin Gothic Book (Headings)", 12, "bold"), width=30, bg="lightyellow")
    name_entry.grid(row=1, column=1, padx=10, pady=15)

    contact_label = Label(left_frame, 
                          text="Supplier Contact: ", 
                          font=("Franklin Gothic Book (Headings)", 12, "bold"), 
                          bg="#045517", 
                          fg="white"
    )
    contact_label.grid(row=2, column=0, padx=(10, 20), pady=15, sticky="w")
    contact_entry = Entry(left_frame, font=("Franklin Gothic Book (Headings)", 12, "bold"), width=30, bg="lightyellow")
    contact_entry.grid(row=2, column=1, padx=10, pady=15)

    description_label = Label(left_frame, 
                          text="Description: ", 
                          font=("Franklin Gothic Book (Headings)", 12, "bold"), 
                          bg="#045517", 
                          fg="white"
    )
    description_label.grid(row=3, column=0, padx=(10, 20), pady=15, sticky="nw")
    description_text = Text(left_frame, font=("Franklin Gothic Book (Headings)", 12, "bold"), width=30, height=5, bg="lightyellow", bd=2)
    description_text.grid(row=3, column=1, padx=10, pady=15)

    button_frame = Frame(left_frame, bg="#045517")
    button_frame.grid(row=4, column=0, columnspan=4, pady=30)

    add_button = Button(
        button_frame, 
        text="Add", 
        font=("Franklin Gothic Book (Headings)", 12, "bold"), width=8,
        cursor="hand2", 
        bg="white", 
        fg="#045517", 
        padx=10

    )
    add_button.grid(row=0, column=0, padx=20, pady=10)

    update_button = Button(
        button_frame, 
        text="Update", 
        font=("Franklin Gothic Book (Headings)", 12, "bold"), width=8,
        cursor="hand2", 
        bg="white", 
        fg="#045517", 
        padx=10

    )
    update_button.grid(row=0, column=1, padx=20, pady=10)

    delete_button = Button(
        button_frame, 
        text="Delete", 
        font=("Franklin Gothic Book (Headings)", 12, "bold"), width=8,
        cursor="hand2", 
        bg="white", 
        fg="#045517", 
        padx=10

    )
    delete_button.grid(row=1, column=0, padx=20, pady=10)

    clear_button = Button(
        button_frame, 
        text="Clear", 
        font=("Franklin Gothic Book (Headings)", 12, "bold"), width=8,
        cursor="hand2", 
        bg="white", 
        fg="#045517", 
        padx=10

    )
    clear_button.grid(row=1, column=1, padx=20, pady=10)

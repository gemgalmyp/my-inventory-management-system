from tkinter import *
from tkinter import ttk



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


    # LEFT FRAME DESIGN
    left_frame = Frame(supplier_frame, bg="#045517")
    left_frame.place(x=10, y=90, width=485, height=565)

    invoice_label = Label(left_frame, 
                          text="Invoice No.", 
                          font=("Franklin Gothic Book (Headings)", 12, "bold"), 
                          bg="#045517", 
                          fg="white"
    )
    invoice_label.grid(row=0, column=0, padx=(10, 20), pady=20, sticky="w")
    invoice_entry = Entry(left_frame, font=("Franklin Gothic Book (Headings)", 12, "bold"), width=30, bg="white")
    invoice_entry.grid(row=0, column=1, padx=10, pady=15)

    name_label = Label(left_frame, 
                          text="Supplier Name: ", 
                          font=("Franklin Gothic Book (Headings)", 12, "bold"), 
                          bg="#045517", 
                          fg="white"
    )
    name_label.grid(row=1, column=0, padx=(10, 20), pady=20, sticky="w")
    name_entry = Entry(left_frame, font=("Franklin Gothic Book (Headings)", 12, "bold"), width=30, bg="white")
    name_entry.grid(row=1, column=1, padx=10, pady=15)

    contact_label = Label(left_frame, 
                          text="Supplier Contact: ", 
                          font=("Franklin Gothic Book (Headings)", 12, "bold"), 
                          bg="#045517", 
                          fg="white"
    )
    contact_label.grid(row=2, column=0, padx=(10, 20), pady=20, sticky="w")
    contact_entry = Entry(left_frame, font=("Franklin Gothic Book (Headings)", 12, "bold"), width=30, bg="white")
    contact_entry.grid(row=2, column=1, padx=10, pady=15)

    description_label = Label(left_frame, 
                          text="Description: ", 
                          font=("Franklin Gothic Book (Headings)", 12, "bold"), 
                          bg="#045517", 
                          fg="white"
    )
    description_label.grid(row=3, column=0, padx=(10, 20), pady=20, sticky="nw")
    description_text = Text(left_frame, font=("Franklin Gothic Book (Headings)", 12, "bold"), width=30, height=5, bg="white", bd=2)
    description_text.grid(row=3, column=1, padx=10, pady=15)

    button_frame = Frame(left_frame, bg="#045517")
    button_frame.grid(row=4, column=0, columnspan=4, pady=50)

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

    # RIGHT FRAME DESIGN
    right_frame = Frame(supplier_frame, bg="#7a7979")
    right_frame.place(x=505, y=90, width=585, height=565)

    search_frame = Frame(right_frame)
    search_frame.pack(fill=X, pady=10)

    number_label = Label(search_frame, 
                          text="Invoice No.", 
                          font=("Franklin Gothic Book (Headings)", 12, "bold"),
                          fg="#045517"
    )
    number_label.grid(row=0, column=0, padx=15, sticky="w")
    search_entry = Entry(search_frame, font=("Franklin Gothic Book (Headings)", 12, "bold"), width=18, bg="lightyellow")
    search_entry.grid(row=0, column=1, padx=30, pady=10)

    search_button = Button(
        search_frame, 
        text="Search", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=7,
        cursor="hand2", 
        bg="gray90", 
        fg="#045517"
      

    )
    search_button.grid(row=0, column=2, padx=15)

    show_button = Button(
        search_frame, 
        text="Show All", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=7,
        cursor="hand2", 
        bg="gray90", 
        fg="#045517", 
        padx=10

    )
    show_button.grid(row=0, column=3, padx=15)


    scrolly = Scrollbar(right_frame, orient=VERTICAL)
    scrollx = Scrollbar(right_frame, orient=HORIZONTAL)

    treeview = ttk.Treeview(right_frame, column=('invoice', 'name', 'contact', 'description'), show='headings', yscrollcommand=scrolly.set, xscrollcommand=scrollx.set) # show = 'headings' is used to remove the extra first column
    scrolly.pack(side=RIGHT, fill=Y)
    scrollx.pack(side=BOTTOM, fill=X)
    scrollx.config(command=treeview.xview)
    scrolly.config(command=treeview.yview)

    treeview.pack(fill=BOTH, expand=True, padx=10, pady=10)
    treeview.heading('invoice', text='Invoice ID')
    treeview.heading('name', text='Supplier Name')
    treeview.heading('contact', text='Supplier Contact')
    treeview.heading('description', text='Description')

    treeview.column('invoice', width=80)
    treeview.column('name', width=200)
    treeview.column('contact', width=150)
    treeview.column('description', width=300)




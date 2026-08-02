from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from employees import connect_database

def sales_form(window):
    global back_image
    sales_frame = Frame(window, width=1100, height=680, bg="white")
    sales_frame.place(x=320, y=130)
    
    back_image = PhotoImage(file="back_button.png")
    
    back_button = Button(
        sales_frame,
        image=back_image,
        bd = 0,
        cursor = "hand2",
        bg="white",
        command=lambda: sales_frame.place_forget() 
    )
    back_button.place(x=10, y=15)


    # search_frame = Frame(top_frame, bg="white")
    # search_frame.pack()
    # search_combobox = ttk.Combobox(
    #     search_frame, 
    #     values=('Emp ID', 'Name', 'Gender', 'Email', 'Contact', 'DOB', 'Address'),
    #     font=("Franklin Gothic Book (Headings)", 11),
    #     state='readonly',
    #     cursor="hand2"
    # )
    # search_combobox.set('Search By')
    # search_combobox.grid(row=0, column=0, padx=20)
    # search_entry = Entry(
    #     search_frame, 
    #     font=("Franklin Gothic Book (Headings)", 11), width=20,
    #     bg="lemon chiffon"
    # )
    # search_entry.grid(row=0, column=1, padx=20)
    # search_button = Button(
    #     search_frame, 
    #     text="Search", 
    #     font=("Franklin Gothic Book (Headings)", 11), width=10,  
    #     cursor="hand2", 
    #     bg="#045517", 
    #     fg="white", 
    #     padx=10,
    #     command=lambda: search_employee(search_combobox.get(), search_entry.get())
    # )
    # search_button.grid(row=0, column=2, padx=20)

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import pyodbc


# Functionality Part
def employee_form(window):
    global back_image
    employee_frame = Frame(window, width=1100, height=680, bg="white")
    employee_frame.place(x=320, y=130, width=1100, height=680)
    heading_label = Label(
        employee_frame, 
        text="Manage Employee Details", 
        font=("Franklin Gothic Book (Headings)", 17, "bold"), 
        bg="#045517", 
        fg="white"
    )
    heading_label.place(x=0, y=0, relwidth=1)
    back_image = PhotoImage(file="back_button.png")

    

    top_frame = Frame(employee_frame, bg="white")
    top_frame.place(x=0, y=50, relwidth=1, height=235)

    back_button = Button(
        top_frame,
        image=back_image,
        bd = 0,
        cursor = "hand2",
        bg="white",
        command=lambda: employee_frame.place_forget()   
    )
    back_button.place(x=10, y=0)


    search_frame = Frame(top_frame, bg="white")
    search_frame.pack()
    search_combobox = ttk.Combobox(
        search_frame, 
        values=('ID', 'Name', 'Email', 'Contact'),
        font=("Franklin Gothic Book (Headings)", 11),
        state='readonly',
        cursor="hand2"
    )
    search_combobox.set('Search By')
    search_combobox.grid(row=0, column=0, padx=20)
    search_entry = Entry(
        search_frame, 
        font=("Franklin Gothic Book (Headings)", 11), width=20,
        bg="lemon chiffon"
    )
    search_entry.grid(row=0, column=1, padx=20)
    search_button = Button(
        search_frame, 
        text="Search", 
        font=("Franklin Gothic Book (Headings)", 11), width=10,
        cursor="hand2", 
        bg="#045517", 
        fg="white", 
        padx=10
    )
    search_button.grid(row=0, column=2, padx=20)
    show_all_button = Button(
        search_frame, 
        text="Show All", 
        font=("Franklin Gothic Book (Headings)", 11), width=10,
        cursor="hand2", 
        bg="#045517", 
        fg="white", 
        padx=10
    )
    show_all_button.grid(row=0, column=3)

    horizontal_scrollbar = Scrollbar(top_frame, orient=HORIZONTAL)
    vertical_scrollbar = Scrollbar(top_frame, orient=VERTICAL)

    employee_treeview = ttk.Treeview(
        top_frame, 
        columns=('emp_id', 'name', 'gender', 'email', 'contact', 'dob', 'address', 'usertype', 'password'),
        show='headings',
        yscrollcommand=vertical_scrollbar.set,
        xscrollcommand=horizontal_scrollbar.set
    )
    horizontal_scrollbar.pack(side=BOTTOM, fill=X)
    vertical_scrollbar.pack(side=RIGHT, fill=Y, pady=(10,0))
    horizontal_scrollbar.config(command=employee_treeview.xview)
    vertical_scrollbar.config(command=employee_treeview.yview)

    employee_treeview.pack(pady=(10,0))
    employee_treeview.heading('emp_id', text='Employee ID')
    employee_treeview.heading('name', text='Name')
    employee_treeview.heading('gender', text='Gender')
    employee_treeview.heading('email', text='Email')
    employee_treeview.heading('contact', text='Contact')
    employee_treeview.heading('dob', text='Date of Birth')
    employee_treeview.heading('address', text='Address')
    employee_treeview.heading('usertype', text='User Type')
    employee_treeview.heading('password', text='Password')

    employee_treeview.column('emp_id', width=60)
    employee_treeview.column('name', width=200)
    employee_treeview.column('gender', width=60)
    employee_treeview.column('email', width=200)
    employee_treeview.column('contact', width=120)
    employee_treeview.column('dob', width=100)
    employee_treeview.column('address', width=200)
    employee_treeview.column('usertype', width=120)
    employee_treeview.column('password', width=100)

    detail_frame = Frame(employee_frame, bg="white")
    detail_frame.place(x=8, y=330, relwidth=1, height=370)


    empid_label = Label(detail_frame, text="Employee ID:", font=("Franklin Gothic Book (Headings)", 10), bg="white")
    empid_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
    empid_entry = Entry(detail_frame, font=("Franklin Gothic Book (Headings)", 10), width=28, bg="lemon chiffon")
    empid_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

    name_label = Label(detail_frame, text="Name:", font=("Franklin Gothic Book (Headings)", 10), bg="white")
    name_label.grid(row=0, column=2, padx=20, pady=10, sticky="w")
    name_entry = Entry(detail_frame, font=("Franklin Gothic Book (Headings)", 10), width=28, bg="lemon chiffon")
    name_entry.grid(row=0, column=3, padx=20, pady=10, sticky="w")

    gender_label = Label(detail_frame, text="Gender:", font=("Franklin Gothic Book (Headings)", 10), bg="white")
    gender_label.grid(row=0, column=4, padx=20, pady=10, sticky="w")
    gender_combobox = ttk.Combobox(
        detail_frame, 
        values=('Male', 'Female'), 
        font=("Franklin Gothic Book (Headings)", 10), 
        width=25, 
        state='readonly', 
        cursor="hand2"
    )
    gender_combobox.set('Select Gender')
    gender_combobox.grid(row=0, column=5, padx=20, pady=10, sticky="w")

    email_label = Label(detail_frame, text="Email:", font=("Franklin Gothic Book (Headings)", 10), bg="white")
    email_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
    email_entry = Entry(detail_frame, font=("Franklin Gothic Book (Headings)", 10), width=28, bg="lemon chiffon")
    email_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

    contact_label = Label(detail_frame, text="Contact:", font=("Franklin Gothic Book (Headings)", 10), bg="white")
    contact_label.grid(row=1, column=2, padx=20, pady=10, sticky="w")
    contact_entry = Entry(detail_frame, font=("Franklin Gothic Book (Headings)", 10), width=28, bg="lemon chiffon")
    contact_entry.grid(row=1, column=3, padx=20, pady=10)

    dob_label = Label(detail_frame, text="Date of Birth:", font=("Franklin Gothic Book (Headings)", 10), bg="white")
    dob_label.grid(row=1, column=4, padx=20, pady=10, sticky="w")
    dob_date_entry = DateEntry(
        detail_frame, 
        width=25, font=("Franklin Gothic Book (Headings)", 10),  
        state='readonly', 
        cursor="hand2",
        date_pattern='mm/dd/yyyy'
        
    )
    dob_date_entry.grid(row=1, column=5, padx=20, pady=10, sticky="w")

    address_label = Label(detail_frame, text="Address:", font=("Franklin Gothic Book (Headings)", 10), bg="white")
    address_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
    address_text= Text(detail_frame, font=("Franklin Gothic Book (Headings)", 10), width=28, height=5, bg="lemon chiffon")
    address_text.grid(row=2, column=1, padx=20, pady=10, sticky="w", rowspan=3)  

    user_label = Label(detail_frame, text="User Type:", font=("Franklin Gothic Book (Headings)", 10), bg="white")
    user_label.grid(row=2, column=2, padx=20, pady=10, sticky="w")
    usertype_combobox = ttk.Combobox(
        detail_frame, values=('Admin', 'Employee'), 
        font=("Franklin Gothic Book (Headings)", 10), 
        width=25, 
        state='readonly', 
        cursor="hand2"
    )
    usertype_combobox.set('Select User Type')
    usertype_combobox.grid(row=2, column=3, padx=20, pady=10, sticky="w")

    password_label = Label(detail_frame, text="Password:", font=("Franklin Gothic Book (Headings)", 10), bg="white")
    password_label.grid(row=2, column=4, padx=20, pady=10, sticky="w")
    password_entry = Entry(detail_frame, font=("Franklin Gothic Book (Headings)", 10), width=28, bg="lemon chiffon")
    password_entry.grid(row=2, column=5, padx=20, pady=10)


    button_frame = Frame(employee_frame, bg="white")
    button_frame.place(x=200, y=600)

    add_button = Button(
        button_frame, 
        text="Add", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="#045517", 
        fg="white", 
        padx=10
    )
    add_button.grid(row=0, column=0, padx=20)

    update_button = Button(
        button_frame, 
        text="Update", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="#045517", 
        fg="white", 
        padx=10
    )
    update_button.grid(row=0, column=1, padx=20)

    delete_button = Button(
        button_frame, 
        text="Delete", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="#045517", 
        fg="white", 
        padx=10
    )
    delete_button.grid(row=0, column=2, padx=20)

    clear_button = Button(
        button_frame, 
        text="Clear", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="#045517", 
        fg="white", 
        padx=10
    )
    clear_button.grid(row=0, column=3, padx=20)
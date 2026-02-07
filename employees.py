from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import pyodbc


server = 'DESKTOP-UF7FUTA\\SQLEXPRESS'
database = 'IMS'
username = 'sa'  # Change to your SQL Server username
password = 'DBpass100'  # Change to your SQL Server password
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"

def connect_database():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        print("Connection successful using SQL Authentication!")
        # Create database and table if they don't exist (SQL Server syntax)
        cursor.execute("IF DB_ID('IMS') IS NULL CREATE DATABASE IMS")
        cursor.execute("USE IMS")
        cursor.execute("""
        IF OBJECT_ID('dbo.employee_data', 'U') IS NULL
        CREATE TABLE dbo.employee_data (
            emp_id INT PRIMARY KEY,
            name VARCHAR(100),
            gender VARCHAR(50),
            email VARCHAR(100),
            contact VARCHAR(15),
            dob VARCHAR(30),
            address VARCHAR(150),
            usertype VARCHAR(50),
            password VARCHAR(50)
        )
        """)
        conn.commit()

        cursor.execute("SELECT @@version;")
        row = cursor.fetchone()
        if row:
            print(f"Server version: {row[0]}")

        return cursor, conn
    except pyodbc.Error as ex:
        print(f"Database connection failed: {ex}")
        return None, None
    
def create_database_and_table():
    # `connect_database` already ensures the database and table exist for SQL Server.
    # Call it to trigger creation logic and then close the connection.
    cursor, conn = connect_database()
    if not cursor or not conn:
        return
    try:
        # No-op: connect_database performed the necessary setup
        pass
    finally:
        try:
            cursor.close()
        except Exception:
            pass
        try:
            conn.close()
        except Exception:
            pass

def treeview_data():
    cursor, conn = connect_database()
    if not cursor or not conn:
        return
    cursor.execute('USE IMS')
    try:
        cursor.execute("SELECT * FROM employee_data")
        employee_records = cursor.fetchall()
        employee_treeview.delete(*employee_treeview.get_children())
        for records in employee_records:
            employee_treeview.insert('', END, values=tuple(records))

    except Exception as e:
        messagebox.showerror("Error", f"Error due to {e}")
    finally:
        cursor.close()
        conn.close()

def select_data(event, 
                emp_id_entry, 
                name_entry, 
                gender_combobox, 
                email_entry, 
                contact_entry, 
                dob_date_entry, 
                address_text, 
                usertype_combobox, 
                password_entry):
    index = employee_treeview.selection()
    content = employee_treeview.item(index)
    row = content['values']
    clear_employee_fields(emp_id_entry, 
                          name_entry, 
                          gender_combobox, 
                          email_entry, contact_entry, 
                          dob_date_entry, 
                          address_text, 
                          usertype_combobox, 
                          password_entry, False)
    emp_id_entry.insert(0, row[0])
    name_entry.insert(0, row[1])
    gender_combobox.set(row[2])
    email_entry.insert(0, row[3])
    contact_entry.insert(0, row[4])
    dob_date_entry.set_date(row[5])
    address_text.insert("1.0", row[6])
    usertype_combobox.set(row[7])
    password_entry.insert(0, row[8])

    

def add_employee(emp_id, name, gender, email, contact, dob, address, usertype, password):
    if emp_id == "" or name == "" or gender == "Select Gender" or email == "" or contact == "" or address.strip() == "" or usertype == "Select User Type" or password == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    # Ensure employee id is an integer
    try:
        emp_id_int = int(emp_id)
    except Exception:
        messagebox.showerror("Error", "Employee ID must be an integer")
        return
    

    cursor, conn = connect_database()
    if not cursor or not conn:
        return
    cursor.execute('USE IMS')
    try:
        cursor.execute("SELECT emp_id FROM employee_data WHERE emp_id=?", (emp_id_int,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Employee ID already exists!")
            return
        address = address.strip()
        cursor.execute("INSERT INTO employee_data VALUES (?,?,?,?,?,?,?,?,?)", (emp_id_int, name, gender, email, contact, dob, address, usertype, password))
        conn.commit()
        treeview_data()
        messagebox.showinfo("Success", "Employee added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error due to {e}")
    finally:
        cursor.close()
        conn.close()

def clear_employee_fields(emp_id_entry, name_entry, gender_combobox, email_entry, contact_entry, dob_date_entry, address_text, usertype_combobox, password_entry, check):
    emp_id_entry.delete(0, END)
    name_entry.delete(0, END)
    gender_combobox.set('Select Gender')
    email_entry.delete(0, END)
    contact_entry.delete(0, END)
    from datetime import date
    dob_date_entry.set_date(date.today())
    address_text.delete("1.0", END)
    usertype_combobox.set('Select User Type')
    password_entry.delete(0, END)
    if check:
        employee_treeview.selection_remove(employee_treeview.selection())

def update_employee(emp_id, name, gender, email, contact, dob, address, usertype, password):
    selected = employee_treeview.selection()
    if not selected:
        messagebox.showerror("Error", "Please select an employee to update...")
        return
    else:
        cursor, conn = connect_database()
        if not cursor or not conn:
            return
        cursor.execute('USE IMS')
        cursor.execute("SELECT * FROM employee_data WHERE emp_id=?", (emp_id,))
        current_data = cursor.fetchone()
        current_data = current_data[1:]
        print(current_data)
        address = address.strip()

        new_data = (name, gender, email, contact, dob, address, usertype, password)
        print(new_data)

        if current_data == new_data:
            messagebox.showinfo("Information", "No changes detected to update!")
            return

        cursor.execute('UPDATE employee_data SET name=?, gender=?, email=?, contact=?, dob=?, address=?, usertype=?, password=? WHERE emp_id=?', (name, gender, email, contact, dob, address, usertype, password, emp_id))
        conn.commit()
        
        messagebox.showinfo("Success", "Employee updated successfully!")
        treeview_data()



# Functionality Part
def employee_form(window):
    global back_image, employee_treeview
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

    employee_treeview.column('emp_id', width=80)
    employee_treeview.column('name', width=200)
    employee_treeview.column('gender', width=80)
    employee_treeview.column('email', width=200)
    employee_treeview.column('contact', width=120)
    employee_treeview.column('dob', width=100)
    employee_treeview.column('address', width=200)
    employee_treeview.column('usertype', width=130)
    employee_treeview.column('password', width=150)

    treeview_data()
   

    detail_frame = Frame(employee_frame, bg="white")
    detail_frame.place(x=8, y=330, relwidth=1, height=370)


    emp_id_label = Label(detail_frame, text="Employee ID:", font=("Franklin Gothic Book (Headings)", 10), bg="white")
    emp_id_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
    emp_id_entry = Entry(detail_frame, font=("Franklin Gothic Book (Headings)", 10), width=28, bg="lemon chiffon")
    emp_id_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

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
        width=25, 
        font=("Franklin Gothic Book (Headings)", 10), 
        state='readonly', 
        cursor="hand2",
        date_pattern='mm/dd/yyyy',
        background='chartreuse4',
        foreground='white'
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
        padx=10, 
        command = lambda: add_employee(emp_id_entry.get(), name_entry.get(), gender_combobox.get(), email_entry.get(), contact_entry.get(), dob_date_entry.get(), address_text.get("1.0", END).strip(), usertype_combobox.get(), password_entry.get())
    )
    add_button.grid(row=0, column=0, padx=20)

    update_button = Button(
        button_frame, 
        text="Update", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="#045517", 
        fg="white", 
        padx=10,
        command=lambda: update_employee(emp_id_entry.get(), name_entry.get(), gender_combobox.get(), email_entry.get(), contact_entry.get(), dob_date_entry.get(), address_text.get("1.0", END).strip(), usertype_combobox.get(), password_entry.get())
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
        padx=10,
        command=lambda: clear_employee_fields(emp_id_entry, name_entry, gender_combobox, email_entry, contact_entry, dob_date_entry, address_text, usertype_combobox, password_entry, True)
    )
    clear_button.grid(row=0, column=3, padx=20)

    employee_treeview.bind('<ButtonRelease-1>', lambda event: select_data(event,emp_id_entry, name_entry, gender_combobox, email_entry, contact_entry, dob_date_entry, address_text, usertype_combobox, password_entry))

create_database_and_table()
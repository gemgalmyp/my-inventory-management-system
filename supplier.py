from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from employees import connect_database


def search_supplier(search_value, treeview):
    search_value = search_value.strip()
    if search_value == "":
        messagebox.showerror("Error", "Please enter an invoice number to search!")
        return
    
    cursor, conn = connect_database()
    if not cursor or not conn:
        messagebox.showerror("Error", "Failed to connect to database!")
        return
    
    try:
        cursor.execute("USE IMS")
        cursor.execute("SELECT * FROM supplier_data WHERE invoice LIKE ?", (f"%{search_value}%",))
        records = cursor.fetchall()
        
        treeview.delete(*treeview.get_children())
        
        if not records:
            messagebox.showerror("Error", "No suppliers found with that invoice number!")
            return
        
        for record in records:
            treeview.insert('', END, values=tuple(record))
        messagebox.showinfo("Success", f"Found {len(records)} supplier(s)!")

    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        cursor.close()
        conn.close()

def show_all_suppliers(treeview, search_entry):
    treeview_data(treeview)
    search_entry.delete(0, END)

def delete_supplier(invoice, treeview):
    index = treeview.selection()
    if not index:
        messagebox.showerror('Error', 'Please select a supplier to delete!')
        return
    else:
        cursor, conn = connect_database()
        if not cursor or not conn:
            return
        try: 
            cursor.execute('USE IMS')
            cursor.execute('DELETE FROM supplier_data WHERE invoice=?', (treeview.item(index)['values'][0],))
            conn.commit()
            treeview_data(treeview)

            messagebox.showinfo('Success', 'Supplier deleted successfully!')
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            conn.close()

def clear_fields(invoice_entry, name_entry, contact_entry, description_text, treeview):
    invoice_entry.delete(0, END)
    name_entry.delete(0, END)
    contact_entry.delete(0, END)
    description_text.delete("1.0", END)
    treeview.selection_remove(treeview.selection())


def update_supplier(invoice, name, contact, description, treeview):
    index = treeview.selection()
    if not index:
        messagebox.showerror('Error', 'Please select a supplier to update!')
        return
    else:
        cursor, conn = connect_database()
        if not cursor or not conn:
            return
        try:
            cursor.execute('USE IMS')
            cursor.execute('SELECT * FROM supplier_data WHERE invoice=?', (invoice,))
            row = cursor.fetchone()
            if not row:
                messagebox.showerror('Error', 'Selected supplier not found in database!')
                return
            
            current_data = tuple((str(v).strip() if v is not None else "") for v in row[1:4])
            new_data = tuple((str(v).strip() if v is not None else "") for v in (name, contact, description))

            if current_data == new_data:
                messagebox.showinfo('Information', 'No changes detected to update!')
                return
            
            cursor.execute('UPDATE supplier_data SET name=?, contact=?, description=? WHERE invoice=?', (name, contact, description, invoice))
            conn.commit()
            messagebox.showinfo('Success', 'Supplier updated successfully!')
            
            treeview_data(treeview)

        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            conn.close()

def select_data(event, 
                invoice_entry, 
                name_entry, 
                contact_entry, 
                description_text, 
                treeview):
    
    index = treeview.selection()
    content = treeview.item(index)
    data = content['values']
    invoice_entry.delete(0, END)
    invoice_entry.insert(0, data[0])
    name_entry.delete(0, END)
    name_entry.insert(0, data[1])
    contact_entry.delete(0, END)
    contact_entry.insert(0, data[2])
    description_text.delete("1.0", END)
    description_text.insert("1.0", data[3])

def treeview_data(treeview):
    cursor, conn = connect_database()
    if not cursor or not conn:
        return
    try:
        cursor.execute('USE IMS')
        cursor.execute('SELECT * FROM supplier_data')
        records = cursor.fetchall()
        try:
            treeview.delete(*treeview.get_children())
        except Exception:
            pass
        for rec in records:
            try:
                treeview.insert('', END, values=tuple(rec))
            except Exception:
                pass
    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        cursor.close()
        conn.close()

def create_suppliers_table():
    cursor, conn = connect_database()
    if not cursor or not conn:
        return
    try:
        cursor.execute('USE IMS')
        cursor.execute("""
        IF OBJECT_ID('dbo.supplier_data', 'U') IS NULL
        CREATE TABLE dbo.supplier_data (
            invoice VARCHAR(20) PRIMARY KEY,
            name VARCHAR(100),
            contact VARCHAR(20),
            description TEXT,
            created_at DATETIME DEFAULT GETDATE()
        )
        """)
        conn.commit()
    except Exception as e:
        messagebox.showerror("Error", f"Error creating suppliers table: {e}")
    finally:
        cursor.close()
        conn.close()


def add_supplier(invoice, name, contact, description, treeview):
    if invoice == "" or name == "" or contact == "" or description == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    cursor, conn = connect_database()
    if not cursor or not conn:
        messagebox.showerror("Database Error", "Failed to connect to the database.")
        return
    try:
        cursor.execute('USE IMS')
        # ensure table exists
        cursor.execute("""
        IF OBJECT_ID('dbo.supplier_data', 'U') IS NULL
        CREATE TABLE dbo.supplier_data (
            invoice VARCHAR(20) PRIMARY KEY,
            name VARCHAR(100),
            contact VARCHAR(20),
            description TEXT,
            created_at DATETIME DEFAULT GETDATE()
        )
        """)

        # check for existing invoice
        cursor.execute('SELECT * FROM supplier_data WHERE invoice=?', (invoice,))
        if cursor.fetchone():
            messagebox.showerror('Error', 'Invoice already exists!')
            return

        cursor.execute('INSERT INTO supplier_data (invoice, name, contact, description) VALUES (?,?,?,?)', (invoice, name, contact, description))
        conn.commit()
        messagebox.showinfo('Success', 'Supplier added successfully!')
        treeview_data(treeview)

    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        cursor.close()
        conn.close()


def supplier_form(window):
    global back_image, supplier_treeview
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

    save_button = Button(
        button_frame, 
        text="Save", 
        font=("Franklin Gothic Book (Headings)", 12, "bold"), width=8,
        cursor="hand2", 
        bg="white", 
        fg="#045517", 
        padx=10, 
        command = lambda: add_supplier(invoice_entry.get(), name_entry.get(), contact_entry.get(), description_text.get("1.0", END).strip(), treeview)

    )
    save_button.grid(row=0, column=0, padx=20, pady=10)

    update_button = Button(
        button_frame, 
        text="Update", 
        font=("Franklin Gothic Book (Headings)", 12, "bold"), width=8,
        cursor="hand2", 
        bg="white", 
        fg="#045517", 
        padx=10,
        command = lambda: update_supplier(invoice_entry.get(), name_entry.get(), contact_entry.get(), description_text.get("1.0", END).strip(), treeview)

    )
    update_button.grid(row=0, column=1, padx=20, pady=10)

    delete_button = Button(
        button_frame, 
        text="Delete", 
        font=("Franklin Gothic Book (Headings)", 12, "bold"), width=8,
        cursor="hand2", 
        bg="white", 
        fg="#045517", 
        padx=10,
        command = lambda: delete_supplier(invoice_entry.get(), treeview)

    )
    delete_button.grid(row=1, column=0, padx=20, pady=10)

    clear_button = Button(
        button_frame, 
        text="Clear", 
        font=("Franklin Gothic Book (Headings)", 12, "bold"), width=8,
        cursor="hand2", 
        bg="white", 
        fg="#045517", 
        padx=10,
        command = lambda: clear_fields(invoice_entry, name_entry, contact_entry, description_text, treeview)

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
        fg="#045517",
        command=lambda: search_supplier(search_entry.get(), treeview)
    )
    search_button.grid(row=0, column=2, padx=15)

    show_button = Button(
        search_frame, 
        text="Show All", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=7,
        cursor="hand2", 
        bg="gray90", 
        fg="#045517", 
        padx=10,
        command=lambda: show_all_suppliers(treeview, search_entry)
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
    treeview.heading("invoice", text="Invoice ID")
    treeview.heading("name", text="Supplier Name")
    treeview.heading("contact", text="Supplier Contact")
    treeview.heading("description", text="Description")

    treeview.column("invoice", width=80)
    treeview.column("name", width=200)
    treeview.column("contact", width=150)
    treeview.column("description", width=300)

    # Load existing data into treeview
    treeview_data(treeview)

    # To highlight selected row and populate form fields
    treeview.bind("<ButtonRelease-1>", lambda event: select_data(event, invoice_entry, name_entry, contact_entry, description_text, treeview))
    return supplier_frame



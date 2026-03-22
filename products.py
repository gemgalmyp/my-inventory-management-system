import decimal
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from employees import connect_database

def show_all(treeview, search_combobox, search_entry):
    treeview_data(treeview)
    search_combobox.set("Search By")
    search_entry.delete(0, END)
    

def search_product(search_combobox, search_entry, treeview):
    if search_combobox.get() == "Search By":
        messagebox.showwarning("Warning", "Please select a search criteria!")
    elif search_entry.get() == "":
        messagebox.showwarning("Warning", "Please enter a search term!")
    else:
        column_mapping = {"Category": "category", "Supplier": "supplier", "Product Name": "name", "Status": "status"}
        search_column = column_mapping.get(search_combobox.get(), None)
        if not search_column:
            messagebox.showerror("Error", "Invalid search criteria!")
            return
        cursor, conn = None, None
        try:
            cursor, conn = connect_database()
            if not cursor or not conn:
                return
            cursor.execute("USE IMS")
            cursor.execute(f"SELECT * FROM product_data WHERE {search_column} LIKE ?", ('%' + search_entry.get() + '%',))
            records = cursor.fetchall()
            if len(records)==0:
                messagebox.showerror("Error", "No matching products found!")
                return
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
            messagebox.showerror("Error", f"Error due to {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        
    

def clear_fields(category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox, treeview):
    treeview.selection_remove(treeview.selection())
    category_combobox.set("Select")
    supplier_combobox.set("Select")
    name_entry.delete(0, END)
    price_entry.delete(0, END)
    quantity_entry.delete(0, END)
    status_combobox.set("Select Status")

def delete_product(treeview, category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox):
    selected = treeview.selection()
    
    if not selected:
        messagebox.showerror('Error', 'Please select a product to delete!')
        return
    
    if not messagebox.askyesno('Confirm Delete', 'Are you sure you want to delete this product?'):
        return
    
    item = selected[0]
    product_id = treeview.item(item)['values'][0]
    
    cursor, conn = None, None
    try: 
        cursor, conn = connect_database()
        if not cursor or not conn:
            return
        cursor.execute('USE IMS')
        cursor.execute('DELETE FROM product_data WHERE id=?', (product_id,))
        conn.commit()
        treeview_data(treeview)
        messagebox.showinfo('Success', 'Product deleted successfully!')
        clear_fields(category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox, treeview)
    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_product(category, supplier, name, price, quantity, status, treeview):
    selected = treeview.selection()
    if not selected:
        messagebox.showerror("Error", "Please select a product to update!")
        return
    item = selected[0]
    id = treeview.item(item)['values'][0]
    current = treeview.item(item)['values']
    if current[1] == category and current[2] == supplier and current[3] == name and str(current[4]) == price and str(current[5]) == quantity and current[6] == status:
        messagebox.showinfo('Information', 'No changes detected to update!')
        return
    
    try:
        price_val = decimal.Decimal(price)
        quantity_val = int(quantity)
    except ValueError:
        messagebox.showerror("Error", "Invalid price or quantity format!")
        return
    
    cursor, conn = None, None
    try:
        cursor, conn = connect_database()
        if not cursor or not conn:
            return
        cursor.execute('USE IMS')
        cursor.execute(
            'UPDATE product_data SET category=?, supplier=?, name=?, price=?, quantity=?, status=? WHERE id=?',
            (category, supplier, name, price_val, quantity_val, status, id)
        )
        conn.commit()
        messagebox.showinfo('Success', 'Product updated successfully!')
        treeview_data(treeview)
    except Exception as e:
        messagebox.showerror('Error', f'Error due to {e}')
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def select_data(event, treeview, category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox):
    selected = treeview.selection()
    if selected:
        item = selected[0]
        values = treeview.item(item)['values']
        category_combobox.set(values[1])
        supplier_combobox.set(values[2])
        name_entry.delete(0, END)
        name_entry.insert(0, values[3])
        price_entry.delete(0, END)
        price_entry.insert(0, values[4])
        quantity_entry.delete(0, END)
        quantity_entry.insert(0, values[5])
        status_combobox.set(values[6])

def treeview_data(treeview):
    cursor, conn = connect_database()
    if not cursor or not conn:
        return
    try:
        cursor.execute('USE IMS')
        cursor.execute('SELECT * FROM product_data')
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
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def fetch_supplier_category(category_combobox, supplier_combobox):
    category_option=[]
    supplier_option=[]
    cursor, conn = None, None
    try:
        cursor, conn = connect_database()
        if not cursor or not conn:
            return
        cursor.execute("USE IMS")
        cursor.execute("SELECT category_name FROM category_data")
        names=cursor.fetchall()
        if len(names)>0:
            category_combobox.set("Select")
            for name in names:
                category_option.append(name[0])
            category_combobox.config(values=category_option)

        cursor.execute("SELECT name FROM supplier_data")
        names=cursor.fetchall()
        if len(names)>0:
            supplier_combobox.set("Select")
            for name in names:
                supplier_option.append(name[0])
            supplier_combobox.config(values=supplier_option)
    except Exception as e:
        messagebox.showerror("Error", f"Error due to {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def add_product(category, supplier, name, price, quantity, status, treeview):
    if category == "Empty":
        messagebox.showerror("Error", "Please add categories")
    elif supplier == "Empty":
        messagebox.showerror("Error", "Please add suppliers")
    elif category == "Select" or supplier == "Select" or name == "" or price == "" or quantity == "" or status == "Select Status":
        messagebox.showerror("Error", "All fields are required!")
    else:
        try:
            price_val = decimal.Decimal(price)
            quantity_val = int(quantity)
        except ValueError:
            messagebox.showerror("Error", "Invalid price or quantity format!")
            return
        
        cursor, conn = None, None
        try:
            cursor, conn = connect_database()
            if not cursor or not conn:
                return
            cursor.execute("USE IMS")
            # create table if missing
            cursor.execute("""
            IF OBJECT_ID('dbo.product_data', 'U') IS NULL
            CREATE TABLE dbo.product_data (
                id INT IDENTITY(1,1) PRIMARY KEY,
                category VARCHAR(250),
                supplier VARCHAR(250),
                name VARCHAR(100),
                price DECIMAL(10, 2),
                quantity INT,
                status VARCHAR(50)
            )
            """)
            cursor.execute("SELECT * FROM product_data WHERE category=? AND supplier=? AND name=?", (category, supplier, name))
            if cursor.fetchone():
                messagebox.showerror("Error", "Product already exists!")
                return
            
            cursor.execute(
                "INSERT INTO product_data (category, supplier, name, price, quantity, status) VALUES (?,?,?,?,?,?)",
                (category, supplier, name, price_val, quantity_val, status)
            )
            conn.commit()
            messagebox.showinfo("Success", "Product added successfully!")
            try:
                treeview_data(treeview)
            except NameError:
                pass

        except Exception as e:
            messagebox.showerror("Error", f"Error due to {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


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
    left_frame.place(x=15, y=55, width=485, height=600)

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
    category_label.grid(row=1, column=0, padx=20, pady=25, sticky="w")
    category_combobox = ttk.Combobox(left_frame,
                                     font=("Franklin Gothic Book (Headings)", 13, "bold"),
                                     state="readonly",                                 
                                     width=28
    )
    category_combobox.grid(row=1, column=1, padx=20, pady=25)
    category_combobox.set("Empty")

    supplier_label = Label(left_frame, 
                          text="Supplier:", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    supplier_label.grid(row=2, column=0, padx=20, pady=25, sticky="w")
    supplier_combobox = ttk.Combobox(left_frame,
                                     font=("Franklin Gothic Book (Headings)", 13, "bold"),
                                     state="readonly",                                 
                                     width=28
    )
    supplier_combobox.grid(row=2, column=1, padx=20, pady=25)
    supplier_combobox.set("Empty")

    name_label = Label(left_frame, 
                          text="Name:", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    name_label.grid(row=3, column=0, padx=20, pady=25, sticky="w")
    name_entry = Entry(left_frame, 
                     font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                     width=30, 
                     bg="lightyellow"
    )
    name_entry.grid(row=3, column=1, padx=10, pady=25)

    price_label = Label(left_frame, 
                          text="Price:", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    price_label.grid(row=4, column=0, padx=20, pady=25, sticky="w")
    price_entry = Entry(left_frame, 
                     font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                     width=30, 
                     bg="lightyellow"
    )
    price_entry.grid(row=4, column=1, padx=10, pady=25)

    quantity_label = Label(left_frame, 
                          text="Quantity:", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    quantity_label.grid(row=5, column=0, padx=20, pady=25, sticky="w")
    quantity_entry = Entry(left_frame, 
                     font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                     width=30, 
                     bg="lightyellow"
    )
    quantity_entry.grid(row=5, column=1, padx=10, pady=25)

    status_label = Label(left_frame, 
                          text="Status:", 
                          font=("Franklin Gothic Book (Headings)", 13, "bold"), 
                          bg="white", 
                          fg="#045517"
    )
    status_label.grid(row=6, column=0, padx=20, pady=25, sticky="w")
    status_combobox = ttk.Combobox(left_frame,
                                   values=("Active", "Inactive"),
                                   font=("Franklin Gothic Book (Headings)", 13, "bold"),
                                   state="readonly",                                 
                                   width=28
    )
    status_combobox.grid(row=6, column=1, padx=20, pady=25)
    status_combobox.set("Select Status")

    button_frame = Frame(left_frame, bg="white")
    button_frame.grid(row=7, columnspan=2, pady=(30, 0))

    add_button = Button(
        button_frame, 
        text="Add", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="white", 
        command=lambda: add_product(category_combobox.get(), supplier_combobox.get(), name_entry.get(), price_entry.get(), quantity_entry.get(), status_combobox.get(), treeview)
        
    )
    add_button.grid(row=0, column=0, padx=10, pady=20)

    update_button = Button(
        button_frame, 
        text="Update", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="white", 
        fg="#045517",
        command=lambda: update_product(category_combobox.get(), supplier_combobox.get(), name_entry.get(), price_entry.get(), quantity_entry.get(), status_combobox.get(), treeview)
        
    )
    update_button.grid(row=0, column=1, padx=10, pady=20)

    delete_button = Button(
        button_frame, 
        text="Delete", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="white", 
        fg="#045517",
        command=lambda: delete_product(treeview, category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox)
        
    )
    delete_button.grid(row=0, column=2, padx=10, pady=20)

    clear_button = Button(
        button_frame, 
        text="Clear", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=10,
        cursor="hand2", 
        bg="white", 
        fg="#045517",
        command=lambda: clear_fields(category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox, treeview)
        
    )
    clear_button.grid(row=0, column=3, padx=10, pady=20)

    search_frame = LabelFrame(product_frame, text="Search Product", font=("Franklin Gothic Book (Headings)", 15, "bold"), bg="white")
    search_frame.place(x=520, y=50, width=570, height=120)
    search_combobox = ttk.Combobox(search_frame,
                                   values=("Category", "Supplier", "Product Name", "Status"),
                                   font=("Franklin Gothic Book (Headings)", 11, "bold"),
                                   state="readonly",                                 
                                   width=20
    )
    search_combobox.grid(row=0, column=0, padx=10, pady=15)
    search_combobox.set("Search By")
    search_entry = Entry(search_frame, 
                     font=("Franklin Gothic Book (Headings)", 11, "bold"), 
                     width=20, 
                     bg="lightyellow"
    )
    search_entry.grid(row=0, column=1, padx=8, pady=15)
    search_button = Button(
        search_frame, 
        text="Search", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=7,
        cursor="hand2", 
        bg="white", 
        fg="#045517",
        command=lambda: search_product(search_combobox, search_entry, treeview)      
    )
    search_button.grid(row=0, column=2, padx=7, pady=9)
    show_all_button = Button(
        search_frame, 
        text="Show All", 
        font=("Franklin Gothic Book (Headings)", 11, "bold"), width=7,
        cursor="hand2", 
        bg="white", 
        fg="#045517",
        command=lambda: show_all(treeview, search_combobox, search_entry)      
    )
    show_all_button.grid(row=0, column=3, padx=7, pady=9)

    treeview_frame = Frame(product_frame)
    treeview_frame.place(x=520, y=140, width=570, height=515)
    scrolly = Scrollbar(treeview_frame, orient=VERTICAL)
    scrollx = Scrollbar(treeview_frame, orient=HORIZONTAL)
    treeview = ttk.Treeview(treeview_frame, column=("id", "category", "supplier", "name", "price", "quantity", "status"), show='headings', yscrollcommand=scrolly.set, xscrollcommand=scrollx.set) 
    scrolly.pack(side=RIGHT, fill=Y)
    scrollx.pack(side=BOTTOM, fill=X)
    scrollx.config(command=treeview.xview)
    scrolly.config(command=treeview.yview)
    treeview.pack(fill=BOTH, expand=True)

    treeview.heading("id", text="ID")
    treeview.heading("category", text="Category")
    treeview.heading("supplier", text="Supplier")
    treeview.heading("name", text="Product Name")
    treeview.heading("price", text="Price")
    treeview.heading("quantity", text="Quantity")
    treeview.heading("status", text="Status")
    treeview.column("id", width=50)
    treeview.column("category", width=100)
    treeview.column("supplier", width=200)
    treeview.column("name", width=200)
    treeview.column("price", width=80)
    treeview.column("quantity", width=80)
    treeview.column("status", width=70)
    fetch_supplier_category(category_combobox, supplier_combobox)
    treeview_data(treeview)
    treeview.bind("<ButtonRelease-1>", lambda event: select_data(event, treeview, category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox))
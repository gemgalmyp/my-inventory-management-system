import os
from tkinter import *
# from PIL import Image, ImageTk

window = Tk()
window.title("ARSE ELECTRONICS IMS")
window.geometry("1420x800+0+0")
window.resizable(0,0)
window.config(bg="#bdbdbd")

base_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_dir, "icon.png")   # put icon.png next to dashboard.py

icon = PhotoImage(file=icon_path)
window.iconphoto(True, icon)
window._icon = icon   # keep reference to avoid GC
window.iconphoto(True, icon)
titleLabel = Label(
    window, 
    image=icon,
    compound=LEFT,
    text="ARSE Inventory Management System",
    font=("Franklin Gothic Book (Headings)", 40, "bold"), 
    bg="#045517", 
    fg="#d2db70",
    padx=10,
    anchor="w"
)

titleLabel.image = icon
titleLabel.place(x=0, y=0, relwidth=1)

logoutButton = Button(
    window, 
    text="Logout", 
    font=("Franklin Gothic Book (Headings)", 16, "bold"), 
    bg="#054b2e", 
    fg="white", 
    padx=5, 
    pady=5
)

logoutButton.place(x=1280, y=20)

subtitleLabel = Label(
    window, 
    text = "Welcome Admin\t\t\t\t\t Date: 12/27/2025\t\t\t\t\t Time: 5:11:05 AM",
    font=("Franklin Gothic Book (Headings)", 12, "bold"),
    bg="#7a7979",
    fg="white"
)
subtitleLabel.place(x=0, y=100, relwidth=1)

leftFrame = Frame(window)
leftFrame.place(x=0, y=130, width=300, height=680)

logoImage = PhotoImage(file="label.png")
imageLabel = Label(leftFrame, image=logoImage)
# imageLabel.grid(row=0, column=0)
imageLabel.place(x=0, y=5, width=300, height=200)
# imageLabel.pack(fill=BOTH)

# DESIGN OF THE DASHBOARD LEFT FRAME
menuLabel = Label(
    leftFrame,
    text="Menu",
    font=("Franklin Gothic Book (Headings)", 20),
    bg="#054b2e",
    fg="white"
)
menuLabel.place(x=0, y=210, width=300, height=70)


employee_icon = PhotoImage(file="employees.png")
EmployeeButton = Button(
    leftFrame,
    text=" Employees",
    image=employee_icon,
    compound=LEFT,
    font=("Franklin Gothic Book (Headings)", 16, "bold"),
    anchor="w",
    padx=40
)
EmployeeButton.place(x=0, y=295, width=300, height=60)


supplier_icon = PhotoImage(file="supplier.png")
SupplierButton = Button(
    leftFrame,
    text=" Supplier",
    image=supplier_icon,
    compound=LEFT,
    font=("Franklin Gothic Book (Headings)", 16, "bold"),
    anchor="w",
    padx=40
)
SupplierButton.place(x=0, y=355, width=300, height=60)


category_icon = PhotoImage(file="category.png")
CategoryButton = Button(
    leftFrame,
    text=" Categories",
    image=category_icon,
    compound=LEFT,
    font=("Franklin Gothic Book (Headings)", 16, "bold"),
    anchor="w",
    padx=40
)
CategoryButton.place(x=0, y=415, width=300, height=60)


product_icon = PhotoImage(file="product.png")
ProductButton = Button(
    leftFrame,
    text=" Products",
    image=product_icon,
    compound=LEFT,
    font=("Franklin Gothic Book (Headings)", 16, "bold"),
    anchor="w",
    padx=40
)
ProductButton.place(x=0, y=475, width=300, height=60)


sales_icon = PhotoImage(file="sales.png")
SalesButton = Button(
    leftFrame,
    text=" Sales",
    image=sales_icon,
    compound=LEFT,
    font=("Franklin Gothic Book (Headings)", 16, "bold"),
    anchor="w",
    padx=40
)
SalesButton.place(x=0, y=535, width=300, height=60)


exit_icon = PhotoImage(file="exit.png")
ExitButton = Button(
    leftFrame,
    text=" Exit",
    image=exit_icon,
    compound=LEFT,
    font=("Franklin Gothic Book (Headings)", 16, "bold"),
    anchor="w",
    padx=40
)
ExitButton.place(x=0, y=595, width=300, height=60)

# DASHBOARD CONTENTS
# Total Employees
emp_frame = Frame(
    window,
    bg="#1e8637",
    bd = 3,
    relief=RIDGE,
    highlightthickness=5,
    highlightbackground="#045517"
)
emp_frame.place(x=500, y=150, width=280, height=170)
total_emp_icon = PhotoImage(file="total_employees.png")
total_emp_icon_label = Label(emp_frame, image=total_emp_icon, bg="#1e8637")
total_emp_icon_label.pack()

total_emp_label = Label(
    emp_frame, 
    text="Total Employees", 
    bg="#1e8637", 
    fg="white", 
    font=("Franklin Gothic Book (Headings)", 16, "bold")
)
total_emp_label.pack()

total_emp_count_label = Label(
    emp_frame, 
    text="0", 
    bg="#1e8637", 
    fg="white", 
    font=("Franklin Gothic Book (Headings)", 30, "bold")
)
total_emp_count_label.pack()

# Total Suppliers
sup_frame = Frame(
    window,
    bg="#1e8637",
    bd = 3,
    relief=RIDGE,
    highlightthickness=5,
    highlightbackground="#045517"
)
sup_frame.place(x=950, y=150, width=280, height=170)
total_sup_icon = PhotoImage(file="total_suppliers.png")
total_sup_icon_label = Label(sup_frame, image=total_sup_icon, bg="#1e8637")
total_sup_icon_label.pack()

total_sup_label = Label(
    sup_frame, 
    text="Total Suppliers", 
    bg="#1e8637", 
    fg="white", 
    font=("Franklin Gothic Book (Headings)", 16, "bold")
)
total_sup_label.pack()

total_sup_count_label = Label(
    sup_frame, 
    text="0", 
    bg="#1e8637", 
    fg="white", 
    font=("Franklin Gothic Book (Headings)", 30, "bold")
)
total_sup_count_label.pack()

# Total Categories
cat_frame = Frame(
    window,
    bg="#1e8637",
    bd = 3,
    relief=RIDGE,
    highlightthickness=5,
    highlightbackground="#045517"
)
cat_frame.place(x=500, y=390, width=280, height=170)
total_cat_icon = PhotoImage(file="total_categories.png")
total_cat_icon_label = Label(cat_frame, image=total_cat_icon, bg="#1e8637")
total_cat_icon_label.pack()

total_cat_label = Label(
    cat_frame, 
    text="Total Categories", 
    bg="#1e8637", 
    fg="white", 
    font=("Franklin Gothic Book (Headings)", 16, "bold")
)
total_cat_label.pack()

total_cat_count_label = Label(
    cat_frame, 
    text="0", 
    bg="#1e8637", 
    fg="white", 
    font=("Franklin Gothic Book (Headings)", 30, "bold")
)
total_cat_count_label.pack()

# Total Products
prod_frame = Frame(
    window,
    bg="#1e8637",
    bd = 3,
    relief=RIDGE,
    highlightthickness=5,
    highlightbackground="#045517"
)
prod_frame.place(x=950, y=390, width=280, height=170)
total_prod_icon = PhotoImage(file="total_products.png")
total_prod_icon_label = Label(prod_frame, image=total_prod_icon, bg="#1e8637")
total_prod_icon_label.pack()

total_prod_label = Label(
    prod_frame, 
    text="Total Products", 
    bg="#1e8637", 
    fg="white", 
    font=("Franklin Gothic Book (Headings)", 16, "bold")
)
total_prod_label.pack()

total_prod_count_label = Label(
    prod_frame, 
    text="0", 
    bg="#1e8637", 
    fg="white", 
    font=("Franklin Gothic Book (Headings)", 30, "bold")
)
total_prod_count_label.pack()

# Total Sales
sales_frame = Frame(
    window,
    bg="#1e8637",
    bd = 3,
    relief=RIDGE,
    highlightthickness=5,
    highlightbackground="#045517"
)
sales_frame.place(x=720, y=610, width=280, height=170)
total_sales_icon = PhotoImage(file="total_sales.png")
total_sales_icon_label = Label(sales_frame, image=total_sales_icon, bg="#1e8637")
total_sales_icon_label.pack()

total_sales_label = Label(
    sales_frame, 
    text="Total Sales", 
    bg="#1e8637", 
    fg="white", 
    font=("Franklin Gothic Book (Headings)", 16, "bold")
)
total_sales_label.pack()

total_sales_count_label = Label(
    sales_frame, 
    text="0", 
    bg="#1e8637", 
    fg="white", 
    font=("Franklin Gothic Book (Headings)", 30, "bold")
)
total_sales_count_label.pack()




window.mainloop()

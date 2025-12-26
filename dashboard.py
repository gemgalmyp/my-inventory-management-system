import os
from tkinter import *
# from tkinter import PhotoImage

window = Tk()
window.title("ARSE ELECTRONICS IMS")
window.geometry("1420x810+0+0")
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
    bg="#045c19", 
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

window.mainloop()

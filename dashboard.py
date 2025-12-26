import os
from tkinter import *
from tkinter import PhotoImage

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
    padx=10
)

titleLabel.image = icon
titleLabel.place(x=0, y=0)
        

window.mainloop()

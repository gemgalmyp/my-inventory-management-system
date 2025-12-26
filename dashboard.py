from tkinter import * 


window = Tk()

window.title("ARSE ELECTRONICS IMS")
window.geometry("1420x810+0+0")
window.resizable(0,0)
window.config(bg="#bdbdbd")

# bg_image = PhotoImage(file="Inventory.jpg")
titleLabel = Label(window, text="ARSE Inventory Management System", font=("Arial", 40, "bold"), bg="#045c19", fg="#d2db70")

# titleLabel.image = bg_image         

window.mainloop()

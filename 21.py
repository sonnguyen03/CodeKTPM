from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x700")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 700,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background21.png")
background = canvas.create_image(
    257.0, 484.0,
    image=background_img)

img0 = PhotoImage(file = f"img021.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 54, y = 593,
    width = 194,
    height = 68)

img1 = PhotoImage(file = f"img121.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 776, y = 590,
    width = 194,
    height = 68)

img2 = PhotoImage(file = f"img221.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 403, y = 464,
    width = 194,
    height = 68)

entry0_img = PhotoImage(file = f"img_textBox021.png")
entry0_bg = canvas.create_image(
    512.0, 627.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 279.0, y = 600,
    width = 466.0,
    height = 52)

window.resizable(False, False)
window.mainloop()

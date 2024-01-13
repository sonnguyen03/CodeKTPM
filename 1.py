from tkinter import *
import subprocess

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

background_img = PhotoImage(file = f"background1.png")
background = canvas.create_image(
    720.0, 400.0,
    image=background_img)

img0 = PhotoImage(file = f"img01.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
#####
def btn_clicked():
    print("Button Clicked")

def open_third_file():
    subprocess.Popen(["python", "3.py"])



# Các phần khác của giao diện người dùng của bạn ở đây...

img0 = PhotoImage(file="img01.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=open_third_file,  # Sử dụng hàm mới để mở file 3.py
    relief="flat"
)

b0.place(
    x=273, y=560,
    width=181,
    height=37
)
#



b0.place(
    x = 273, y = 560,
    width = 181,
    height = 37)

img1 = PhotoImage(file = f"img11.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

def btn_clicked():
    print("Button Clicked")

def open_second_file():
    subprocess.Popen(["python", "2.py"])



# Các phần khác của giao diện người dùng của bạn ở đây...

img1 = PhotoImage(file="img11.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=open_second_file,  # Sử dụng hàm mới để mở file 2.py
    relief="flat"
)

b1.place(
    x=839, y=36,
    width=107,
    height=28
)
#
b1.place(
    x = 839, y = 36,
    width = 107,
    height = 28)

entry0_img = PhotoImage(file = f"img_textBox01.png")
entry0_bg = canvas.create_image(
    353.5, 363.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 120.5, y = 336,
    width = 466.0,
    height = 53)

entry1_img = PhotoImage(file = f"img_textBox01.png")
entry1_bg = canvas.create_image(
    357.0, 483.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 124.0, y = 456,
    width = 466.0,
    height = 52)

window.resizable(False, False)
window.mainloop()

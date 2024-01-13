from random import random
from tkinter import *
import subprocess
import random
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

background_img = PhotoImage(file = f"background3.png")
background = canvas.create_image(
    434.5, 390.5,
    image=background_img)

img0 = PhotoImage(file = f"img03.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 849, y = 47,
    width = 121,
    height = 40)

img1 = PhotoImage(file = f"img13.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 371, y = 490,
    width = 299,
    height = 70)
###
def btn_clicked():
    print("Button Clicked")

def open_random_file():
    chosen_file = random.randint(4, 5)
    subprocess.Popen(["python", f"{chosen_file}.py"])


# Phần giao diện người dùng của bạn ở đây...

img1 = PhotoImage(file="img13.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=open_random_file,  # Sử dụng hàm mới để chọn ngẫu nhiên giữa 4.py và 5.py
    relief="flat"
)

b1.place(
    x=371, y=490,
    width=299,
    height=70
)
###3
img2 = PhotoImage(file = f"img23.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 704, y = 610,
    width = 270,
    height = 50)
###
def btn_clicked():
    print("Button Clicked")

def open_random_file():
    chosen_file = random.randint(4, 5)
    subprocess.Popen(["python", f"{chosen_file}.py"])

def open_sixth_file():
    subprocess.Popen(["python", "6.py"])



# Code giao diện người dùng đã có

img2 = PhotoImage(file="img23.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=open_sixth_file,  # Liên kết button b2 với hàm mở file 6.py
    relief="flat"
)

b2.place(
    x=704, y=610,
    width=270,
    height=50
)
###
window.resizable(False, False)
window.mainloop()

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

background_img = PhotoImage(file = f"background2.png")
background = canvas.create_image(
    720.0, 402.5,
    image=background_img)

img0 = PhotoImage(file = f"img02.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 281, y = 611,
    width = 181,
    height = 37)

###
def btn_clicked():
    print("Button Clicked")

def open_third_file():
    subprocess.Popen(["python", "3.py"])



# Các phần khác của giao diện người dùng của bạn ở đây...

img0 = PhotoImage(file="img02.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=open_third_file,  # Sử dụng hàm mới để mở file 3.py
    relief="flat"
)

b0.place(
    x=281, y=611,
    width=181,
    height=37
)
###

img1 = PhotoImage(file = f"img12.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 839, y = 36,
    width = 107,
    height = 28)
### 
def btn_clicked():
    print("Button Clicked")

def open_first_file():
    subprocess.Popen(["python", "1.py"])



# Phần giao diện người dùng của bạn ở đây...

img1 = PhotoImage(file="img12.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=open_first_file,  # Sử dụng hàm mới để mở file 1.py
    relief="flat"
)

b1.place(
    x=839, y=36,
    width=107,
    height=28
)
#
entry0_img = PhotoImage(file = f"img_textBox02.png")
entry0_bg = canvas.create_image(
    355.5, 363.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 120.5, y = 336,
    width = 470.0,
    height = 53)

entry1_img = PhotoImage(file = f"img_textBox12.png")
entry1_bg = canvas.create_image(
    352.5, 467.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 117.5, y = 440,
    width = 470.0,
    height = 53)

entry2_img = PhotoImage(file = f"img_textBox22.png")
entry2_bg = canvas.create_image(
    352.5, 564.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 117.5, y = 537,
    width = 470.0,
    height = 53)

window.resizable(False, False)
window.mainloop()

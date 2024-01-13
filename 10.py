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

background_img = PhotoImage(file = f"background10.png")
background = canvas.create_image(
    501.0, 430.0,
    image=background_img)

img0 = PhotoImage(file = f"img010.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 657, y = 598,
    width = 315,
    height = 66)

img1 = PhotoImage(file = f"img110.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 75, y = 598,
    width = 315,
    height = 66)

###
def open_sixth_file():
    subprocess.Popen(["python", "6.py"])



# ... (Phần khai báo button và giao diện cửa sổ)

img1 = PhotoImage(file = f"img110.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = open_sixth_file,  # Thay đổi lệnh command ở đây
    relief = "flat")

b1.place(
    x = 75, y = 598,
    width = 315,
    height = 66)
###
img2 = PhotoImage(file = f"img210.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 327, y = 28,
    width = 365,
    height = 93)

window.resizable(False, False)
window.mainloop()

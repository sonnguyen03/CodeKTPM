from tkinter import *
import subprocess

def open_twelfth_file():
    subprocess.Popen(["python", "12.py"])

def open_eleventh_file():
    subprocess.Popen(["python", "11.py"])

def open_tenth_file():
    subprocess.Popen(["python", "10.py"])

def open_ninth_file():
    subprocess.Popen(["python", "9.py"])

def open_eighth_file():
    subprocess.Popen(["python", "8.py"])

def btn_clicked(action):
    actions = {
        "b0": open_twelfth_file,
        "b1": open_eleventh_file,
        "b2": open_tenth_file,
        "b3": open_ninth_file,
        "b4": open_eighth_file
    }
    if action in actions:
        actions[action]()

window = Tk()

window.geometry("1000x700")
window.configure(bg="#ffffff")

canvas = Canvas(
    window,
    bg="#ffffff",
    height=700,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

background_img = PhotoImage(file="background6.png")
background = canvas.create_image(
    434.5, 390.5,
    image=background_img
)

button_positions = [
    (588, 370),  # Nút 0
    (253, 375),  # Nút 1
    (719, 118),  # Nút 2
    (429, 118),  # Nút 3
    (138, 115),  # Nút 4
]

button_images = [
    "img06.png",
    "img16.png",
    "img26.png",
    "img36.png",
    "img46.png",
]

buttons = []
for i, (pos_x, pos_y) in enumerate(button_positions):
    img = PhotoImage(file=button_images[i])
    button = Button(
        image=img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda i=i: btn_clicked(f"b{i}"),
        relief="flat"
    )
    button.image = img  # Giữ tham chiếu để tránh bị hủy bởi garbage collection
    button.place(x=pos_x, y=pos_y, width=174, height=174)
    buttons.append(button)

window.resizable(False, False)
window.mainloop()

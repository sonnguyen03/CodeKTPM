from tkinter import *
from tkinter import ttk
import random

def btn_clicked():
    # Get the options from the combo box
    options = combo_box["values"]

    # Randomly select an option
    random_option = random.choice(options)

    # Set the selected option to the combo box
    combo_var.set(random_option)

    print("Button Clicked - Random Option:", random_option)

def on_combobox_select(event):
    selected_value = combo_var.get()
    print(f"Selected value: {selected_value}")

def clear_options():
    # Get the current options from the combo box
    options = list(combo_box["values"])

    # Get the selected option
    selected_option = combo_var.get()

    # Remove the selected option from the options list
    options.remove(selected_option)

    # Update the combo box with the modified options list
    combo_box["values"] = tuple(options)

    # Set the combo box value to an empty string
    combo_var.set("")

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
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file="background1.png")
background = canvas.create_image(
    500.0, 350.0,
    image=background_img)

img0 = PhotoImage(file="img01.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=75, y=598,
    width=315,
    height=66)

img1 = PhotoImage(file="img11.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,  # Change the command to btn_clicked
    relief="flat")

b1.place(
    x=657, y=598,
    width=315,
    height=66)

# Create a StringVar to store the selected value
combo_var = StringVar()

# Create Combobox widget
combo_box = ttk.Combobox(
    window,
    textvariable=combo_var,
    values=["Option 1", "Option 2", "Option 3"],
    state="readonly",
    background="#48ff07",
    font=("Times New Roman", 48, "bold"),  # Set font properties
    justify='center')  # Center-align the text within the combo box

combo_box.place(
    x=325, y=50,  # Maintain the original position
    width=350,
    height=100)

# Bind the event handler to the <<ComboboxSelected>> event
combo_box.bind("<<ComboboxSelected>>", on_combobox_select)

# Create a button to clear options
clear_button = Button(
    text="Clear Options",
    command=clear_options,
    font=("Times New Roman", 16, "bold"),
    bg="#ff0000",  # Red background color
    fg="#ffffff")  # White text color

clear_button.place(
    x=700, y=50,
    width=150,
    height=40)

window.resizable(False, False)
window.mainloop()

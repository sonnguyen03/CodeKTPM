import tkinter as tk

def main():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Ứng dụng Tkinter")

    # Tạo một nhãn (label)
    label_text = "Liên"
    label = tk.Label(root, text=label_text, font=("Arial", 14))

    # Đặt vị trí của nhãn trong cửa sổ
    label.pack(pady=20)

    # Chạy vòng lặp chính của ứng dụng
    root.mainloop()

if __name__ == "__main__":
    main()

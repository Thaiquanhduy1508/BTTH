import tkinter as tk  
window = tk.Tk()
window.title("Cửa sổ đồ họa Tkinter với Button tùy chỉnh")
window.geometry("400x300")
def on_button_click():
    print("Button đã được bấm!")  
button = tk.Button(window, text="Click Me!", command=on_button_click, bg="blue", fg="white")
button.pack(pady=20)
window.mainloop()
print('THÁI QUANG DUY ')

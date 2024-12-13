from tkinter import *
def NewFile():
    print("New File!")
def OpenFile():
    print("Open File!")
def Exit():
    print("Exiting...")
    root.quit()
def InsText():
    print("Inserting Text")
def InsPic():
    print("Inserting Picture")
def About():
    print("This is a simple example of a menu")
root = Tk()
root.title("Menu Example")  
root.geometry("300x200") 
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_command(label="Exit", command=Exit)  
# Tạo menu "Insert"
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)  
root.mainloop()
print('THÁI QUANG DUY ')
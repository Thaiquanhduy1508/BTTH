from tkinter import *
def NewFile():
    print("New File!")
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
filemenu.add_command(label="Open")
filemenu.add_command(label="Exit", command=root.quit)  
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text") 
insertmenu.add_command(label="Picture")  
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)oot.mainloop()
print('THÁI QUANG DUY ')

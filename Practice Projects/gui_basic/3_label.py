from tkinter import *
from PIL import ImageTk

root = Tk()
root.title("Nado GUI")
root.geometry("1000x900+700+300")


label1 = Label(root, text="안녕하세요", fg="white")
label1.pack()

photo = ImageTk.PhotoImage(file="/Users/kimminjae/BJOJ_KIM/Practice Projects/gui_basic/img.jpg")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
btn = Button(root, text="클릭", command=change)
btn.pack()
root.mainloop()
from tkinter import *
from req import requi
from PIL import Image, ImageTk

root = Tk()

def key(event):
    print ("pressed", repr(event.char))
    st.set(requi(1))

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

image = Image.open("img/image.png")
tkimg = ImageTk.PhotoImage(image)
lblimg = Label(root, image=tkimg)
lblimg.pack(side=RIGHT)

st = StringVar()
l = Label(root, textvariable=st)
l.pack(side=LEFT)

#Label(root, text="Ola mundo").pack(side=LEFT)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()

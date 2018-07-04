from tkinter import *
from pokedown import PokeDown
from PIL import Image, ImageTk

root = Tk()

def key(event):
    print ("pressed", repr(event.char))
    st.set(f"\nNome: {PokeDown(1).pokeselect()[1]} \n Habilidades: {PokeDown(1).pokeselect()[2]} - {PokeDown(1).pokeselect()[3]}")

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

image = Image.open("img/image.png")
image.thumbnail((128,128)) #Mudar o tamanho da imagem
tkimg = ImageTk.PhotoImage(image)
lblimg = Label(root, image=tkimg)
lblimg.grid(row=0, column=0, rowspan=2)

st = StringVar()
l = Label(root, textvariable=st)
l.grid(row=2,column=0, rowspan=10)

#Label(root, text="Ola mundo").pack(side=LEFT)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.grid()

root.mainloop()

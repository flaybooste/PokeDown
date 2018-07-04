from tkinter import *
from pokedown import PokeDown
from PIL import Image, ImageTk

root = Tk()

def key(event):
    print ("pressed", repr(event.char))
    st.set(f"\nNome: {PokeDown(2).pokeselect()[1]} \n Habilidades: {PokeDown(2).pokeselect()[2]} - {PokeDown(2).pokeselect()[3]}")

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

img1 = Image.open(f"img/{PokeDown(2).pokeselect()[0]}.png")
img1.thumbnail((128,128)) #Mudar o tamanho da imagem
tkimg = ImageTk.PhotoImage(img1)
lblimg = Label(root, image=tkimg)
lblimg.grid(row=1, column=0, rowspan=1)

img2 = Image.open(f"img/Poison.gif")
img2.thumbnail((50,19))
tkimg2 = ImageTk.PhotoImage(img2)
lblimg2 = Label(root, image=tkimg2)
lblimg2.grid(row=2, column=0, rowspan=2)

st = StringVar()
l = Label(root, textvariable=st)
l.grid(row=8,column=0, rowspan=14)

#Label(root, text="Ola mundo").pack(side=LEFT)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.grid()

root.mainloop()

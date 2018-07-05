from tkinter import *
from pokedown import PokeDown
from PIL import Image, ImageTk

class App:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        #self.widget1['width'] = 320
        #self.widget1['height'] = 320
        self.widget1.pack()
        self.msg = Label(self.widget1, text="ID:")
        self.msg['font'] = ("Ubuntu", "12")
        self.msg.grid(row=1, column=0)

        self.id1 = Entry(self.widget1)
        self.id1['width'] = 10
        self.id1['font'] = ("Ubuntu", "12")
        self.id1.grid(row=1, column=1)

        self.btn0 = Button(self.widget1, text="Get", command=self.btn0_action)
        self.btn0['font'] = ("Ubuntu")
        self.btn0.grid(row=2, column=1)

        self.lbl1 = Label(self.widget1, text=f"Nome: {PokeDown(1).pokeselect()[1]}\nHabilidade 1:{PokeDown(1).pokeselect()[2]}")
        self.lbl1['font']= ("Ubuntu")

        self.img0 = Image.open(f"img/{int(PokeDown(1).pokeselect()[0])}.png").resize((101,94))
        self.img0tk = ImageTk.PhotoImage(self.img0)
        self.lblimg0 = Label(self.widget1, image=self.img0tk)
    def btn0_action(self):
        #id1g = self.id1.get()
        #REMOVER
        self.msg.grid_remove()
        self.id1.grid_remove()
        self.btn0.grid_remove()
        #INSERIR
        self.lblimg0.grid(row=1)
        self.lbl1.grid(row=2)

        #return id1g
root = Tk()
App(root)
root.mainloop()

from tkinter import *
from pokedown import PokeDown
from PIL import Image, ImageTk
from selenium import webdriver

class App:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        #self.widget1['width'] = 320
        #self.widget1['height'] = 320
        self.widget1.pack()
        self.msg = Label(self.widget1, text="ID:")
        self.msg['font'] = ("Ubuntu", "12")
        self.msg.grid(row=1, column=0)

        self.msg1 = Label(self.widget1, text="ID:")
        self.msg1['font'] = ("Ubuntu", "12")
        self.msg1.grid(row=2, column=0)


        self.id1 = Entry(self.widget1)
        self.id1['width'] = 10
        self.id1['font'] = ("Ubuntu", "12")
        self.id1.grid(row=1, column=1)

        self.id2 = Entry(self.widget1)
        self.id2['width'] = 10
        self.id2['font'] = ("Ubuntu", "12")
        self.id2.grid(row=2, column=1)


        self.btn0 = Button(self.widget1, text="Get", command=self.btn0_action)
        self.btn0['font'] = ("Ubuntu")
        self.btn0.grid(row=3, column=1)

    def btn0_action(self):
        id1g = self.id1.get()
        id2g = self.id2.get()
        #REMOVER
        self.msg.grid_remove()
        self.msg1.grid_remove()
        self.id1.grid_remove()
        self.id2.grid_remove()
        self.btn0.grid_remove()
        #Labels
        try:
            self.lbl1 = Label(self.widget1, text=f"Nome: {PokeDown(id1g).pokeselect()[1]}\nHabilidade 1:{PokeDown(id1g).pokeselect()[2]}\t")
            self.lbl1['font']= ("Ubuntu", "12")
        except TypeError:
            PokeDown(id1g).pokedb()
            self.lbl1 = Label(self.widget1, text=f"Nome: {PokeDown(id2g).pokeselect()[1]}\nHabilidade 1:{PokeDown(id2g).pokeselect()[2]}\t")
            self.lbl1['font']= ("Ubuntu", "12")
        #----------------------------
        try:
            self.lbl2 = Label(self.widget1, text=f"Nome: {PokeDown(id2g).pokeselect()[1]}\nHabilidade 1:{PokeDown(id2g).pokeselect()[2]}")
            self.lbl2['font']= ("Ubuntu", "12")
        except TypeError:
            PokeDown(id2g).pokedb()
            self.lbl2 = Label(self.widget1, text=f"Nome: {PokeDown(id2g).pokeselect()[1]}\nHabilidade 1:{PokeDown(id2g).pokeselect()[2]}\t")
            self.lbl2['font']= ("Ubuntu", "12")
        #Button
        self.btn2 = Button(self.widget1, text="Voltar", command=self.btn2_action)
        #IMG
        try:
            self.img0 = Image.open(f"static/img/{int(PokeDown(id1g).pokeselect()[0])}.png").resize((101,94))
            self.img0type = Image.open(f"static/img/{PokeDown(id1g).pokeselect()[4]}.gif")
            self.img0typetk = ImageTk.PhotoImage(self.img0type)
            self.lblimg0type = Label(self.widget1, image=self.img0typetk)
            self.img0tk = ImageTk.PhotoImage(self.img0)
            self.lblimg0 = Label(self.widget1, image=self.img0tk)
        except FileNotFoundError:
            ff = webdriver.Firefox()
            ff.get(f"https://www.pokemon.com/br/pokedex/{PokeDown(id1g).pokeselect()[1]}")


        #-----------------------------------
        try:
            self.img1 = Image.open(f"static/img/{int(PokeDown(id2g).pokeselect()[0])}.png").resize((101,94))
            self.img1tk = ImageTk.PhotoImage(self.img1)
            self.lblimg1 = Label(self.widget1, image=self.img1tk)
            #type
            self.img1type = Image.open(f"static/img/{PokeDown(id2g).pokeselect()[4]}.gif")
            self.img1typetk = ImageTk.PhotoImage(self.img1type)
            self.lblimg1type = Label(self.widget1, image=self.img1typetk)
        except FileNotFoundError:
            ff = webdriver.Firefox()
            ff.get(f"https://www.pokemon.com/br/pokedex/{PokeDown(id2g).pokeselect()[1]}")
        #GRID
        self.lblimg0.grid(row=1, column=0)
        self.lblimg0type.grid(row=3, column=0)
        self.lblimg1.grid(row=1, column=2)
        self.lbl1.grid(row=2, column=0)
        self.lblimg1type.grid(row=3, column=2)
        self.lbl2.grid(row=2, column=2)
        self.btn2.grid(row=4, column=1)

    def btn2_action(self):
        #Remove
        self.lblimg0.grid_remove()
        self.lblimg0type.grid_remove()
        self.lblimg1.grid_remove()
        self.lblimg1type.grid_remove()
        self.lbl1.grid_remove()
        self.lbl2.grid_remove()
        self.btn2.grid_remove()
        #Inserir
        self.msg.grid(row=1, column=0)
        self.msg1.grid(row=2, column=0)
        self.id1.grid(row=1, column=1)
        self.id2.grid(row=2, column=1)
        self.btn0.grid(row=3, column=1)
root = Tk()
App(root)
root.mainloop()

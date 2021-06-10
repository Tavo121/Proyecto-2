from tkinter import *
from os import path
from random import *
v = Tk()
v.minsize(500, 700)

C = Canvas(v, width=500, height=700)
C.place(x = 0, y= 0)

def load_image(nombre):
    ruta = path.join('assets', nombre)
    img = PhotoImage(file=ruta)
    return img

Ast = load_image('Asteroide01.png')
Aste = C.create_image(100,100, image = Ast)

FLAG = True
def asteroides():
    def random1():
        global FLAG
        AX = randint(3,8)
        AY = randint(3,8)
        FLAG = True
        return move(AX, AY)

    def move(X,Y):
        global Aste, C, FLAG
        if FLAG:
            C.move(Aste, X, Y)
            C.after(50, move, X,Y)
            Coords = C.coords(Aste)
            if Coords[0] < 10: 
                FLAG = False
                return random1()
            elif Coords[1] < 20:
                FLAG = False
                return random1()
            elif  Coords[0] > 480:
                FLAG = False
                return random2()
            elif Coords[1] > 680:
                FLAG = False
                return random3()
            

    def random2():
        global FLAG
        FLAG = True
        AX = randint(-8,-3)
        AY = randint(-8,8)
        return move(AX, AY)
    
    def random3():
        global FLAG
        FLAG = True
        AX = randint(-8,8)
        AY = randint(-8,-3)
        return move(AX, AY)

    random1()
asteroides()

v.mainloop()
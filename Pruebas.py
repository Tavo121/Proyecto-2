from threading import Thread
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
print(C.bbox(Aste))
"""
FLAG = True
def asteroides():
    A = 0
    def random1():
        global FLAG
        AX = randint(1,2)
        AY = randint(1,2)
        FLAG = True
        Thread(target= move, args=(AX, AY, )).start()        

    def move(X,Y):
        global Aste, C, FLAG
        nonlocal A
        while FLAG == True:
            C.move(Aste, X, Y)            
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
        AX = randint(-2,-1)
        AY = randint(-2,2)
        Thread(target= move, args=(AX, AY, )).start()  
    
    def random3():
        global FLAG
        FLAG = True
        AX = randint(-2,2)
        AY = randint(-2,-1)
        Thread(target= move, args=(AX, AY, )).start()  
    


    random1()
asteroides()
"""
def close():
    global FLAG, v
    FLAG = False
    v.destroy()

v.protocol('WM_DELETE_WINDOW', close)
v.mainloop()

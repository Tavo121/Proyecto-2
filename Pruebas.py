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

Nombree = Entry(v, width = 10)
Nombree.pack()

score = 100
def save():
    global Nombree, score
    a = Nombree.get()
    b = "---" + str(score)+", "
    highscore = a + b
    Arch = open("Highscore.txt", 'r+')
    def callback():
        read = Arch.readline()
        if read == "":
            Arch.write(highscore)
        else:
            return callback()
    callback()
    Arch.close()


def save_higscore():
    global Nombree, score
    Nombre_usuario = Nombree.get()
    Score_Usuario = Nombre_usuario + "---" + str(score) + ","
    Arch = open("Highscore.txt", "r+")
    Nombres = Arch.readline()


    def compare_ptn(Puntos, Names, vueltas, Chars):
        nonlocal Score_Usuario

        def lenn(String, Result):
            if String == "":
                return Result
            else:
                return lenn(String[1:], Result +1)

        if vueltas == 10:
            print('Lower puntaje')
        elif Names[0] == "1" or Names[0] == '2' or Names[0] == '3' or Names[0] == "4" or Names[0] == '5':
            Comparacion = Names[:-2]
            if Comparacion <= Puntos:
                print('yes')
                #Punt = Arch.tell()
                #Arch.seek(Punt - Chars-1)
                #Arch.write(Score_Usuario + '\n')
                print(Chars)
                #Arch.writelines(Score_Usuario + "\n")
            else:
                Names = Arch.readline()
                Chars = lenn(Names, 0)
                return compare_ptn(Puntos, Names, vueltas +1, Chars)
        else:
            return compare_ptn(Puntos, Names[1:], vueltas, Chars)

    def compare(Puntaje, coma, Names):
        global score
        if coma == 10:
            Puntero = Arch.seek(0)
            Names = Arch.readline()
            print('a')
            return compare_ptn("100", Names, 0, 0)
        elif Names == "":
            Arch.write(Puntaje + "\n")
        elif Names[-2] == ",":
            Names = Arch.readline()
            return compare(Puntaje, coma+1, Names)

    compare(Score_Usuario, 0, Nombres)
    Arch.close()


def save_highscore2():
    global Nombree, score
    Nombre_usuario = Nombree.get()
    Score_Usuario = Nombre_usuario + "---" + str(score) + ","
    Arch = open("Highscore.txt", "r+")
    Nombres = Arch.read()


    def compare_ptn(Puntos, Names, vueltas, Chars):
        nonlocal Score_Usuario

        def lenn(String, Result):
            if String == "":
                return Result
            else:
                return lenn(String[1:], Result +1)

        if vueltas == 10:
            print('Lower puntaje')
        elif Names[0] == "1" or Names[0] == '2' or Names[0] == '3' or Names[0] == "4" or Names[0] == '5':
            Comparacion = Names[:-2]
            if Comparacion <= Puntos:
                print('yes')
                #Punt = Arch.tell()
                #Arch.seek(Punt - Chars-1)
                #Arch.write(Score_Usuario + '\n')
                print(Chars)
                #Arch.writelines(Score_Usuario + "\n")
            else:
                Names = Arch.readline()
                Chars = lenn(Names, 0)
                return compare_ptn(Puntos, Names, vueltas +1, Chars)
        else:
            return compare_ptn(Puntos, Names[1:], vueltas, Chars)

    def compare(Puntaje, coma, Names):
        global score
        if coma == 10:
            print('hola')
        elif Names == "":
            print('here')
            Names.append(Puntaje + "\n")
        elif Names[0] == ",":
            print('b')
            return compare(Puntaje, coma+1, Names[1:])

    compare(Score_Usuario, 0, Nombres)
    Arch.close()

Button(v, text = 'Save', command = save_highscore2).place(x=250, y=400)









"""
def save_higscore():
    global e_jugador, pnts
    Nombre_usuario = e_jugador.get()
    Score_Usuario = Nombre_usuario + "---" + str(pnts) + ", "
    Arch = open("Highscore.txt", "r+")
    Nombres = Arch.readline()
    def compare(Puntaje, coma, Names):
        nonlocal Score_Usuario
        if coma == 10:
            print("no")
        elif coma != 10:
            Arch.write(Score_Usuario)
            return compare(Puntaje, coma+1, Names[1:])"""

# def compare_pts(Puntos, Puntajes):
# if Puntajes[0] == ",":
"""
def compare(Puntaje, coma, Names): #verifica que haya menos de 10 nombres registrados
    nonlocal Score_Usuario
    if coma == 10:
        print('a')
        #return compare_pts()
    elif Names == "":
        Arch.write(Score_Usuario)
    elif Names[0] == ",":
        return compare(Puntaje, coma+1, Names[1:])
    else:
        return compare(Puntaje, coma, Names[1:])
compare(Score_Usuario, 0, Nombres)
"""

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
asteroides()"""

def close():
    global FLAG, v
    FLAG = False
    v.destroy()

v.protocol('WM_DELETE_WINDOW', close)
v.mainloop()




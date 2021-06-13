Creditos = """
Costa Rica
Instituto Tecnológico de Costa Rica
Ingeniería en Computadores
Taller de programación
1º año
Grupo 02
Profesor: Milton Villegas Lemus
Programa: Versión 1.0
Autores: Byron Mata Fuentes
         Gustavo Alvarado Aburto

Autores auxiliares:
-José Fernando Morales
-Ignacio Mora


Instrucciones:
-Para el movimiento de la nave se
utilizan las teclas direccionales:
[←],[↑],[→],[↓]

"""

#-----------------------------------------------------------------
from tkinter import *
import os
from os import path
from threading import Thread
import vlc
import glob
import random
from time import sleep

#-----------------------------------------------------------------
def load_image(nombre):
    """
    ***************************************************************************
                            Instituto Tecnológio de Costa Rica
                                Ingeniería en Computadores
                                
    Funciones: load_image, load_mp3, play_fx, play_songs & stop_song
    Lenguaje: Python 3.9.5
    Autores: Byron Mata F.
             Gustavo Alvarado A.

    Vesión: 1.0
    Fecha Última Edición: junio 4/2021
    Entradas: N/D
    Restricciones: N/D
    Salidas: N/D

    Autores auxiliares: Jose Fernando Morales

    ***************************************************************************"""
    ruta = path.join('assets', nombre)
    img = PhotoImage(file=ruta)
    return img

mp3_player = vlc.MediaPlayer()

def load_mp3(nombre):
    return path.join('assets', nombre)

def play_fx(MP3):
    vlc.MediaPlayer(MP3).play()
    
def play_songs(MP3):
    global mp3_player
    stop_song()
    mp3_player = vlc.MediaPlayer(MP3)
    mp3_player.audio_set_volume(50)
    mp3_player.play()
    
def stop_song():
    global mp3_player
    if(isinstance(mp3_player, vlc.MediaPlayer)):
        mp3_player.stop()

#------------------------------------------------------------------------------------------------------
fuente = ('OCR A Extended', 12)
vida = 3
#------------------------------------------------------------------------------------------------------
FLAG = True

ventana = Tk()
ventana.title ("Menú principal")
ventana.minsize(500, 700)
ventana.resizable(width=NO, height=NO)

C_ventana = Canvas(ventana, bg='black', width=500, height=700, highlightthickness = 0)
C_ventana.place(x=0,y=0)
C_ventana.fondo = load_image('Pantalla_principal.png')
fondo = C_ventana.create_image(0,0, anchor=NW, image=C_ventana.fondo)

e_jugador = Entry(ventana, width=18, font=fuente)
e_jugador.place(x=162,y=280)

C_ventana.songPP = load_mp3('PPSong.mp3')
songPP = play_songs(C_ventana.songPP)
#------------------------------------------------------------------------------------------------------
def load_sprite(Nombre):
    """
    ***************************************************************************
                            Instituto Tecnológio de Costa Rica
                                Ingeniería en Computadores
                                
    Funciones: load_sprite & load_images
    Lenguaje: Python 3.9.5
    Autores: Byron Mata F.
             Gustavo Alvarado A.

    Vesión: 1.0
    Fecha Última Edición: junio 5/2021
    Entradas: N/D
    Restricciones: N/D
    Salidas: N/D

    Autores auxiliares: Jose Fernando Morales

    ***************************************************************************"""
    Frames = glob.glob('assets\\Nave\\' + Nombre)
    Frames.sort()
    return load_images(Frames, [])

def load_images(Lista_inical, ListaResultado):
    if Lista_inical == []:
        return ListaResultado
    else:
        ListaResultado.append(PhotoImage(file = Lista_inical[0]))
        return load_images(Lista_inical[1:], ListaResultado)

Imagenes = load_sprite('tile*.png')

#------------------------------------------------------------------------------------------------------
def validar():
    """
    ***************************************************************************
                Instituto Tecnológio de Costa Rica
                    Ingeniería en Computadores
                        
    Función: validar
    Lenguaje: Python 3.9.5
    Autores: Gustavo Alvarado A.
             Byron Mata F.

    Vesión: 1.1
    Fecha Última Edición: junio 5/2021
    Entradas: N/D
    Restricciones: N/D
    Salidas: N/D

    Autores auxiliares: Jose Fernando Morales

    ***************************************************************************"""
    global e_jugador
    username = e_jugador.get()
    if (username!=""):
        return nivel1()
    else:
        mensaje()

def mensaje():
    Vent_msg = Toplevel()
    Vent_msg.minsize(width=150, height=20)
    Vent_msg.resizable(width=NO, height=NO)
    Texto = Label(Vent_msg, text="Favor ingresar un nombre de usuario antes de inicar", font=fuente, fg='white', bg='black')
    Texto.pack()

    Callback = 0
    def tiempo(Seg):
        nonlocal Callback, Vent_msg
        if Seg <= 4:
            Callback = Vent_msg.after(1000, tiempo, (Seg +1))
        else:
            parar_tiempo()      
    
    def parar_tiempo():
        nonlocal Callback, Vent_msg
        Vent_msg.after_cancel(Callback)
        Vent_msg.destroy()

    tiempo(0)

B_validar = Button(ventana, text="Play", font=fuente, width=10, height=1, command=validar)
B_validar.place(x=200,y=325)

def cerrar_menu():
    ventana.destroy()
    stop_song()
ventana.protocol('WM_DELETE_WINDOW', cerrar_menu)

B_cerrarmenu = Button (ventana, text='Exit', font=fuente, width=5 ,height=1, command=cerrar_menu)
B_cerrarmenu.place(x=435,y=665)

#------------------------------------------------------------------------------------------------------
Asteroide_img = load_image("Asteroide01.png")
Asteroide_img2 = load_image("Asteroide02.png")
Asteroide_img3 = load_image("Asteroide03.png")
def nivel1():
    """
    ***************************************************************************
                Instituto Tecnológio de Costa Rica
                    Ingeniería en Computadores
                    
    Función: nivel1
    Lenguaje: Python 3.9.5
    Autores: Byron Mata F.
             Gustavo Alvarado A.

    Vesión: 2.0
    Fecha Última Edición: junio 12/2021
    Entradas: N/D
    Restricciones: N/D
    Salidas: N/D

    ***************************************************************************"""
    global vida, puntos, username, sgnds, pnts, FLAG
    FLAG = True
    vida = 3
    pnts = 0
    sgnds = 60
    contador = 0

    ventana.withdraw()

    vent_nivel1 = Toplevel()
    vent_nivel1.title('Nivel 1')
    vent_nivel1.minsize(500, 700)
    vent_nivel1.resizable(width=NO, height=NO)
    C_vent_nivel1 = Canvas(vent_nivel1, bg='black', width=500, height=700, highlightthickness=0)
    C_vent_nivel1.place(x=0, y=0)

    C_vent_nivel1.fondo = load_image('Nivel1.png')
    fondo_niveles = C_vent_nivel1.create_image(0, 0, anchor=NW, image = C_vent_nivel1.fondo)

    C_vent_nivel1.songPJ1 = load_mp3('Interplanetary Odyssey.mp3')
    songPJ1 = play_songs(C_vent_nivel1.songPJ1)

    Frame = Canvas(vent_nivel1, width=500, height=30, highlightthickness=0, bg='#10304a')
    Frame.place(x=0,y=0)

    Vida = Label(vent_nivel1, text="Life: "+str(vida), font=('OCR A Extended', 12), bg='#10304a', fg='white')
    Vida.place(x=130,y=3)
    Puntos = Label(vent_nivel1, text="Score: "+str(pnts), font=('OCR A Extended', 12), bg='#10304a', fg='white')
    Puntos.place(x=10,y=3)
    Temp = Label(vent_nivel1, font=('OCR A Extended', 12), bg='#10304a', fg='white')
    Temp.place(x=310,y=3)

    F_tiempo = Frame.create_text(284, 15, text="Time: ", font=('OCR A Extended', 13), fill='white')
    F_jugadador = Frame.create_text(420, 15, text=e_jugador.get(), font=('OCR A Extended', 13), fill='white')

    # -----------------------------------------------------------------------------------------------------
    def temporizador():
        global sgnds, contador, pnts
        sgnds = sgnds - 1
        pnts = pnts + 1
        contador=vent_nivel1.after(1000, temporizador)
        Temp.config(text=(sgnds))
        Puntos.config(text="Score: "+str(pnts))
        if sgnds == 0:
            cerrar_nivel1()
            return nivel2()
    temporizador()

    # -----------------------------------------------------------------------------------------------------
    sprite = C_vent_nivel1.create_image(250, 600, tags=('sprite'))
    def nave():
        """
        ***************************************************************************
                    Instituto Tecnológio de Costa Rica
                        Ingeniería en Computadores
                            
        Función: nave
        Función interna: player_animation
        Lenguaje: Python 3.9.5
        Autores: Gustavo Alvarado A.
                 Byron Mata F.

        Vesión: 1.1
        Fecha Última Edición: junio 6/2021
        Entradas: N/D
        Restricciones: N/D
        Salidas: N/D

        Autores auxiliares: Jose Fernando Morales

        ***************************************************************************"""
        nonlocal vent_nivel1, sprite       

        # Animación del jugador
        def player_animation(X):
            global Imagenes, FLAG
            nonlocal sprite
            try:
                if X == 3:
                    X = 0
                if FLAG:
                    C_vent_nivel1.itemconfig('sprite', image=Imagenes[X])

                    def callback():
                        player_animation(X + 1)

                    ventana.after(100, callback)
            except:
                'Cancel'

        Thread(target=player_animation, args=(0,)).start()

        #Movimiento del jugador
        def derecha(Evento):
            nonlocal C_vent_nivel1
            C_vent_nivel1.move(sprite, 10, 0)
            if C_vent_nivel1.coords(sprite)[0] > 460: #colision con el borde de ventana
                C_vent_nivel1.move(sprite, -10, 0)
        def izquierda(Evento):
            nonlocal C_vent_nivel1
            C_vent_nivel1.move(sprite, -10, 0)
            if C_vent_nivel1.coords(sprite)[0] < 40: #colision con el borde de ventana
                C_vent_nivel1.move(sprite, 10, 0)
        def arriba(Evento):
            nonlocal C_vent_nivel1
            C_vent_nivel1.move(sprite, 0, -10)
            if C_vent_nivel1.coords(sprite)[1] < 100: #colision con el borde de ventana
                C_vent_nivel1.move(sprite, 0, 10)
        def abajo(Evento):
            nonlocal C_vent_nivel1
            C_vent_nivel1.move(sprite, 0, 10)
            if C_vent_nivel1.coords(sprite)[1] > 650: #colision con el borde de ventana
                C_vent_nivel1.move(sprite, 0, -10)

        vent_nivel1.bind('<Right>', derecha)
        vent_nivel1.bind('<Left>', izquierda)
        vent_nivel1.bind('<Up>', arriba)
        vent_nivel1.bind('<Down>', abajo)

    nave()

    # ------------------------------------------------------------------------------------------------------
    def asteroides():
        """
        ***************************************************************************
                    Instituto Tecnológio de Costa Rica
                        Ingeniería en Computadores
                        
        Función: nave
        Funciones internas: condicion, asteroide_move, recursive_move, reverse_move
        Lenguaje: Python 3.9.5
        Autores: Gustavo Alvarado A.
                 Byron Mata F.

        Vesión: 3.0
        Fecha Última Edición: junio 12/2021
        Entradas: N/D
        Restricciones: N/D
        Salidas: N/D

        ***************************************************************************"""
        global Asteroide_img, Asteroide_img2, Asteroide_img3
        nonlocal C_vent_nivel1
        Asteroide = C_vent_nivel1.create_image(200,200, anchor=NW, image=Asteroide_img)
        Asteroide2 = C_vent_nivel1.create_image(480,200, anchor=NW, image=Asteroide_img2)
        Asteroide3 = C_vent_nivel1.create_image(50,100, anchor=NW, image=Asteroide_img3)
        After = 0
        After2 = 0
        After3 = 0

        def start():
            nonlocal C_vent_nivel1
            sleep(1)
            Ast_x = random.randint(3,6)
            Ast_y = random.randint(3,6)
            return recursive_move(Ast_x, Ast_y), recursive_move2(Ast_x, Ast_y), recursive_move3(Ast_x, Ast_y)

        def random_coords1(Ast):
            nonlocal C_vent_nivel1, After, After2, After3
            Ast_x = random.randint(3,6)
            Ast_y = random.randint(3,6)
            if Ast == 1:
                C_vent_nivel1.after_cancel(After)
                return recursive_move(Ast_x, Ast_y)
            elif Ast == 2:
                C_vent_nivel1.after_cancel(After2)
                return recursive_move2(Ast_x, Ast_y)   
            elif Ast == 3:
                C_vent_nivel1.after_cancel(After3)
                return recursive_move3(Ast_x, Ast_y)     
        # ------------------------------------------------------------------------------------------------------
        def recursive_move(X,Y):
            global vida
            nonlocal C_vent_nivel1, Asteroide, After, sprite, Vida       
            C_vent_nivel1.move(Asteroide, X, Y)                
            After = C_vent_nivel1.after(45, recursive_move, X,Y)
            Coords = C_vent_nivel1.coords(Asteroide)
            Asteroide_bx = C_vent_nivel1.bbox(Asteroide)
            Nave_bx = C_vent_nivel1.bbox(sprite)
            if Coords[0] < 7:
                return random_coords1(1)
            elif Coords[1] < 25:
                return random_coords1(1)
            elif  Coords[0] > 420:
                return random_coords2(1)
            elif Coords[1] > 665:
                return random_coords3(1)
            elif Nave_bx[2]+4 > Asteroide_bx[0]+10 > Nave_bx[0]+4 and Nave_bx[1]+30 < Asteroide_bx[3]+10 < Nave_bx[3]+30:
                C_vent_nivel1.after_cancel(After)
                C_vent_nivel1.delete(Asteroide)
                C_vent_nivel1.hit = load_mp3('hit.mp3')
                hit = play_fx(C_vent_nivel1.hit)
                vida -= 1
                Vida.config(text= "Life: "+str(vida))
        
        def recursive_move2(X,Y):
            global vida
            nonlocal C_vent_nivel1, Asteroide2, After2, sprite, Vida 
            C_vent_nivel1.move(Asteroide2, X, Y)
            After2 = C_vent_nivel1.after(45, recursive_move2, X,Y)
            Coords = C_vent_nivel1.coords(Asteroide2)
            Asteroide_bx = C_vent_nivel1.bbox(Asteroide2)
            Nave_bx = C_vent_nivel1.bbox(sprite)
            if Coords[0] < 7:
                return random_coords1(2)
            elif Coords[1] < 25:
                return random_coords1(2)
            elif  Coords[0] > 420:
                return random_coords2(2)
            elif Coords[1] > 665:
                return random_coords3(2)
            elif Nave_bx[2]+4 > Asteroide_bx[0]+10 > Nave_bx[0]+4 and Nave_bx[1]+30 < Asteroide_bx[3]+10 < Nave_bx[3]+30:
                C_vent_nivel1.after_cancel(After2)
                C_vent_nivel1.delete(Asteroide2)
                C_vent_nivel1.hit = load_mp3('hit.mp3')
                hit = play_fx(C_vent_nivel1.hit)
                vida -= 1
                Vida.config(text= "Life: "+str(vida))
        
        def recursive_move3(X,Y):
            global vida
            nonlocal C_vent_nivel1, Asteroide3, After3, sprite, Vida 
            C_vent_nivel1.move(Asteroide3, X, Y)
            After3 = C_vent_nivel1.after(45, recursive_move3, X,Y)
            Coords = C_vent_nivel1.coords(Asteroide3)
            Asteroide_bx = C_vent_nivel1.bbox(Asteroide3)
            Nave_bx = C_vent_nivel1.bbox(sprite)
            if Coords[0] < 7: 
                return random_coords1(3)
            elif Coords[1] < 25:
                return random_coords1(3)
            elif  Coords[0] > 420:
                return random_coords2(3)
            elif Coords[1] > 665:
                return random_coords3(3)
            elif Nave_bx[2]+4 > Asteroide_bx[0]+10 > Nave_bx[0]+4 and Nave_bx[1]+30 < Asteroide_bx[3]+10 < Nave_bx[3]+30:
                C_vent_nivel1.after_cancel(After3)
                C_vent_nivel1.delete(Asteroide3)
                C_vent_nivel1.hit = load_mp3('hit.mp3')
                hit = play_fx(C_vent_nivel1.hit)
                vida -= 1
                Vida.config(text= "Life: "+str(vida))

        # ------------------------------------------------------------------------------------------------------
        def random_coords2(Ast):
            nonlocal After, C_vent_nivel1, After2, After3
            Ast_x = random.randint(-6,-3)
            Ast_y = random.randint(-6,6)            
            if Ast == 1:
                C_vent_nivel1.after_cancel(After)
                return recursive_move(Ast_x, Ast_y)
            elif Ast == 2:
                C_vent_nivel1.after_cancel(After2)
                return recursive_move2(Ast_x, Ast_y)
            elif Ast == 3:
                C_vent_nivel1.after_cancel(After3)
                return recursive_move3(Ast_x, Ast_y)  
            
        def random_coords3(Ast):
            nonlocal After, C_vent_nivel1, After2, After3
            Ast_x = random.randint(-6,6)
            Ast_y = random.randint(-6,-3)
            if Ast == 1:
                C_vent_nivel1.after_cancel(After)
                return recursive_move(Ast_x, Ast_y)
            elif Ast == 2:
                C_vent_nivel1.after_cancel(After2)
                return recursive_move2(Ast_x, Ast_y)
            elif Ast == 3:
                C_vent_nivel1.after_cancel(After3)
                return recursive_move3(Ast_x, Ast_y)  
        
        Thread(target = start).start()    

    asteroides()

    # ------------------------------------------------------------------------------------------------------
    def cerrar_nivel1():
        global FLAG
        FLAG = False        
        ventana.deiconify()
        vent_nivel1.destroy()
        stop_song()

    vent_nivel1.protocol('WM_DELETE_WINDOW', cerrar_nivel1)

    B_cerrar_nivel1 = Button(vent_nivel1, text='←', font=fuente, width=5, height=1, command=cerrar_nivel1)
    B_cerrar_nivel1.place(x=435, y=665)

# ------------------------------------------------------------------------------------------------------
def nivel2():
    """
    ***************************************************************************
                Instituto Tecnológio de Costa Rica
                    Ingeniería en Computadores
                    
    Función: nivel2
    Lenguaje: Python 3.9.5
    Autores: Byron Mata F.
             Gustavo Alvarado A.

    Vesión: 2.0
    Fecha Última Edición: junio 12/2021
    Entradas: N/D
    Restricciones: N/D
    Salidas: N/D

    ***************************************************************************"""
    global vida, puntos, username, sgnds, pnts, FLAG, vent_sala
    FLAG = True
    vida = 3
    pnts = 0
    sgnds = 60
    contador = 0

    ventana.withdraw()

    vent_nivel2 = Toplevel()
    vent_nivel2.title('Nivel 2')
    vent_nivel2.minsize(500, 700)
    vent_nivel2.resizable(width=NO, height=NO)
    C_vent_nivel2 = Canvas(vent_nivel2, bg='black', width=500, height=700, highlightthickness=0)
    C_vent_nivel2.place(x=0, y=0)

    C_vent_nivel2.fondo = load_image('Nivel2.png')
    fondo_niveles = C_vent_nivel2.create_image(0, 0, anchor=NW, image=C_vent_nivel2.fondo)

    C_vent_nivel2.songPJ2 = load_mp3('Interstellar Odyssey.mp3')
    songPJ2 = play_songs(C_vent_nivel2.songPJ2)

    Frame = Canvas(vent_nivel2, width=500, height=30, highlightthickness=0, bg='#10304a')
    Frame.place(x=0,y=0)

    Vida = Label(vent_nivel2, text="Life: "+str(vida), font=('OCR A Extended', 12), bg='#10304a', fg='white')
    Vida.place(x=130,y=3)
    Puntos = Label(vent_nivel2, text="Score: "+str(pnts), font=('OCR A Extended', 12), bg='#10304a', fg='white')
    Puntos.place(x=10,y=3)
    Temp = Label(vent_nivel2, font=('OCR A Extended', 12), bg='#10304a', fg='white')
    Temp.place(x=310,y=3)

    F_tiempo = Frame.create_text(284, 15, text="Time: ", font=('OCR A Extended', 13), fill='white')
    F_jugadador = Frame.create_text(420, 15, text=e_jugador.get(), font=('OCR A Extended', 13), fill='white')

    # -----------------------------------------------------------------------------------------------------
    def temporizador():
        global sgnds, contador, pnts
        sgnds = sgnds - 1
        pnts = pnts + 1
        contador=vent_nivel2.after(1000, temporizador)
        Temp.config(text=(sgnds))
        Puntos.config(text="Score: "+str(pnts))
    
    temporizador()
    
    # -----------------------------------------------------------------------------------------------------
    sprite = C_vent_nivel2.create_image(250, 600, tags=('sprite'))
    def nave():
        """
        ***************************************************************************
                    Instituto Tecnológio de Costa Rica
                        Ingeniería en Computadores
                        
        Función: nave
        Función interna: player_animation
        Lenguaje: Python 3.9.5
        Autores: Gustavo Alvarado A.
                 Byron Mata F.

        Vesión: 1.1
        Fecha Última Edición: junio 6/2021
        Entradas: N/D
        Restricciones: N/D
        Salidas: N/D

        Autores auxiliares: Jose Fernando Morales

        ***************************************************************************"""    

        def player_animation(X):
            global Imagenes, FLAG
            nonlocal sprite
            if X == 3:
                X = 0
            if FLAG:
                C_vent_nivel2.itemconfig('sprite', image=Imagenes[X])

                def callback():
                    player_animation(X + 1)

                ventana.after(100, callback)

        Thread(target=player_animation, args=(0,)).start()

        # Movimiento del jugador
        def derecha(Evento):
            nonlocal C_vent_nivel2
            C_vent_nivel2.move(sprite, 10, 0)
            if C_vent_nivel2.coords(sprite)[0] > 460:  # colision con el borde de ventana
                C_vent_nivel2.move(sprite, -10, 0)

        def izquierda(Evento):
            nonlocal C_vent_nivel2
            C_vent_nivel2.move(sprite, -10, 0)
            if C_vent_nivel2.coords(sprite)[0] < 40:  # colision con el borde de ventana
                C_vent_nivel2.move(sprite, 10, 0)

        def arriba(Evento):
            nonlocal C_vent_nivel2
            C_vent_nivel2.move(sprite, 0, -10)
            if C_vent_nivel2.coords(sprite)[1] < 100:  # colision con el borde de ventana
                C_vent_nivel2.move(sprite, 0, 10)

        def abajo(Evento):
            nonlocal C_vent_nivel2
            C_vent_nivel2.move(sprite, 0, 10)
            if C_vent_nivel2.coords(sprite)[1] > 650:  # colision con el borde de ventana
                C_vent_nivel2.move(sprite, 0, -10)

        vent_nivel2.bind('<Right>', derecha)
        vent_nivel2.bind('<Left>', izquierda)
        vent_nivel2.bind('<Up>', arriba)
        vent_nivel2.bind('<Down>', abajo)

    nave()
    # ------------------------------------------------------------------------------------------------------
    def asteroides():
        """
        ***************************************************************************
                    Instituto Tecnológio de Costa Rica
                        Ingeniería en Computadores
                        
        Función: asteroides
        Funciones internas: condicion, asteroide_move, recursive_move, reverse_move
        Lenguaje: Python 3.9.5
        Autores: Gustavo Alvarado A.
                 Byron Mata F.

        Vesión: 3.0
        Fecha Última Edición: junio 12/2021
        Entradas: N/D
        Restricciones: N/D
        Salidas: N/D

        ***************************************************************************"""
        global Asteroide_img, Asteroide_img2, Asteroide_img3
        nonlocal C_vent_nivel2
        Asteroide = C_vent_nivel2.create_image(200,200, anchor=NW, image=Asteroide_img)
        Asteroide2 = C_vent_nivel2.create_image(480,200, anchor=NW, image=Asteroide_img2)
        Asteroide3 = C_vent_nivel2.create_image(50,100, anchor=NW, image=Asteroide_img3)
        Asteroide4 = C_vent_nivel2.create_image(50,620, anchor=NW, image=Asteroide_img2)
        After = 0
        After2 = 0
        After3 = 0
        After4 = 0

        def start():
            nonlocal C_vent_nivel2
            sleep(1)
            Ast_x = random.randint(4,6)
            Ast_y = random.randint(4,6)
            return recursive_move(Ast_x, Ast_y), recursive_move2(Ast_x, Ast_y), recursive_move3(Ast_x, Ast_y), recursive_move4(Ast_x, Ast_y)

        def random_coords1(Ast):
            nonlocal C_vent_nivel2, After, After2, After3, After4
            Ast_x = random.randint(4,6)
            Ast_y = random.randint(4,6)
            if Ast == 1:
                C_vent_nivel2.after_cancel(After)
                return recursive_move(Ast_x, Ast_y)
            elif Ast == 2:
                C_vent_nivel2.after_cancel(After2)
                return recursive_move2(Ast_x, Ast_y)   
            elif Ast == 3:
                C_vent_nivel2.after_cancel(After3)
                return recursive_move3(Ast_x, Ast_y)
            elif Ast == 4:
                C_vent_nivel2.after_cancel(After4)
                return recursive_move4(Ast_x, Ast_y)      
        # ------------------------------------------------------------------------------------------------------
        def recursive_move(X,Y):
            global vida
            nonlocal C_vent_nivel2, Asteroide, After, sprite, Vida       
            C_vent_nivel2.move(Asteroide, X, Y)                
            After = C_vent_nivel2.after(45, recursive_move, X,Y)
            Coords = C_vent_nivel2.coords(Asteroide)
            Asteroide_bx = C_vent_nivel2.bbox(Asteroide)
            Nave_bx = C_vent_nivel2.bbox(sprite)
            if Coords[0] < 7:
                return random_coords1(1)
            elif Coords[1] < 25:
                return random_coords1(1)
            elif  Coords[0] > 420:
                return random_coords2(1)
            elif Coords[1] > 665:
                return random_coords3(1)
            elif Nave_bx[2]+4 > Asteroide_bx[0]+10 > Nave_bx[0]+4 and Nave_bx[1]+30 < Asteroide_bx[3]+10 < Nave_bx[3]+30:
                C_vent_nivel2.after_cancel(After)
                C_vent_nivel2.delete(Asteroide)
                C_vent_nivel2.hit = load_mp3('hit.mp3')
                hit = play_fx(C_vent_nivel2.hit)
                vida -= 1
                Vida.config(text= "Life: "+str(vida))
        
        def recursive_move2(X,Y):
            global vida
            nonlocal C_vent_nivel2, Asteroide2, After2, sprite, Vida 
            C_vent_nivel2.move(Asteroide2, X, Y)
            After2 = C_vent_nivel2.after(45, recursive_move2, X,Y)
            Coords = C_vent_nivel2.coords(Asteroide2)
            Asteroide_bx = C_vent_nivel2.bbox(Asteroide2)
            Nave_bx = C_vent_nivel2.bbox(sprite)
            if Coords[0] < 7:
                return random_coords1(2)
            elif Coords[1] < 25:
                return random_coords1(2)
            elif  Coords[0] > 420:
                return random_coords2(2)
            elif Coords[1] > 665:
                return random_coords3(2)
            elif Nave_bx[2]+4 > Asteroide_bx[0]+10 > Nave_bx[0]+4 and Nave_bx[1]+30 < Asteroide_bx[3]+10 < Nave_bx[3]+30:
                C_vent_nivel2.after_cancel(After2)
                C_vent_nivel2.delete(Asteroide2)
                C_vent_nivel2.hit = load_mp3('hit.mp3')
                hit = play_fx(C_vent_nivel2.hit)
                vida -= 1
                Vida.config(text= "Life: "+str(vida))
        
        def recursive_move3(X,Y):
            global vida
            nonlocal C_vent_nivel2, Asteroide3, After3, sprite, Vida 
            C_vent_nivel2.move(Asteroide3, X, Y)
            After3 = C_vent_nivel2.after(45, recursive_move3, X,Y)
            Coords = C_vent_nivel2.coords(Asteroide3)
            Asteroide_bx = C_vent_nivel2.bbox(Asteroide3)
            Nave_bx = C_vent_nivel2.bbox(sprite)
            if Coords[0] < 7: 
                return random_coords1(3)
            elif Coords[1] < 25:
                return random_coords1(3)
            elif  Coords[0] > 420:
                return random_coords2(3)
            elif Coords[1] > 665:
                return random_coords3(3)
            elif Nave_bx[2]+4 > Asteroide_bx[0]+10 > Nave_bx[0]+4 and Nave_bx[1]+30 < Asteroide_bx[3]+10 < Nave_bx[3]+30:
                C_vent_nivel2.after_cancel(After3)
                C_vent_nivel2.delete(Asteroide3)
                C_vent_nivel2.hit = load_mp3('hit.mp3')
                hit = play_fx(C_vent_nivel2.hit)
                vida -= 1
                Vida.config(text= "Life: "+str(vida))
        
        def recursive_move4(X,Y):
            global vida
            nonlocal C_vent_nivel2, Asteroide4, After4, sprite, Vida 
            C_vent_nivel2.move(Asteroide4, X, Y)
            After4 = C_vent_nivel2.after(45, recursive_move4, X,Y)
            Coords = C_vent_nivel2.coords(Asteroide4)
            Asteroide_bx = C_vent_nivel2.bbox(Asteroide4)
            Nave_bx = C_vent_nivel2.bbox(sprite)
            if Coords[0] < 7: 
                return random_coords1(4)
            elif Coords[1] < 25:
                return random_coords1(4)
            elif  Coords[0] > 420:
                return random_coords2(4)
            elif Coords[1] > 665:
                return random_coords3(4)
            elif Nave_bx[2]+4 > Asteroide_bx[0]+10 > Nave_bx[0]+4 and Nave_bx[1]+30 < Asteroide_bx[3]+10 < Nave_bx[3]+30:
                C_vent_nivel2.after_cancel(After4)
                C_vent_nivel2.delete(Asteroide4)
                C_vent_nivel2.hit = load_mp3('hit.mp3')
                hit = play_fx(C_vent_nivel2.hit)
                vida -= 1
                Vida.config(text= "Life: "+str(vida))

        # ------------------------------------------------------------------------------------------------------
        def random_coords2(Ast):
            nonlocal After, C_vent_nivel2, After2, After3, After4
            Ast_x = random.randint(-6,-4)
            Ast_y = random.randint(-6,6)            
            if Ast == 1:
                C_vent_nivel2.after_cancel(After)
                return recursive_move(Ast_x, Ast_y)
            elif Ast == 2:
                C_vent_nivel2.after_cancel(After2)
                return recursive_move2(Ast_x, Ast_y)
            elif Ast == 3:
                C_vent_nivel2.after_cancel(After3)
                return recursive_move3(Ast_x, Ast_y)
            elif Ast == 4:
                C_vent_nivel2.after_cancel(After4)
                return recursive_move4(Ast_x, Ast_y)   
            
        def random_coords3(Ast):
            nonlocal After, C_vent_nivel2, After2, After3, After4
            Ast_x = random.randint(-6,6)
            Ast_y = random.randint(-6,-4)
            if Ast == 1:
                C_vent_nivel2.after_cancel(After)
                return recursive_move(Ast_x, Ast_y)
            elif Ast == 2:
                C_vent_nivel2.after_cancel(After2)
                return recursive_move2(Ast_x, Ast_y)
            elif Ast == 3:
                C_vent_nivel2.after_cancel(After3)
                return recursive_move3(Ast_x, Ast_y)
            elif Ast == 4:
                C_vent_nivel2.after_cancel(After4)
                return recursive_move4(Ast_x, Ast_y)   
        
        Thread(target = start).start()    

    asteroides()

    # ------------------------------------------------------------------------------------------------------
    def cerrar_nivel2():
        global FLAG
        FLAG = False
        ventana.deiconify()
        vent_nivel2.destroy()
        stop_song()

    vent_nivel2.protocol('WM_DELETE_WINDOW', cerrar_nivel2)

    B_cerrar_nivel2 = Button(vent_nivel2, text='←', font=fuente, width=5, height=1, command=cerrar_nivel2)
    B_cerrar_nivel2.place(x=435, y=665)

# ------------------------------------------------------------------------------------------------------
def nivel3():
    """
    ***************************************************************************
                Instituto Tecnológio de Costa Rica
                    Ingeniería en Computadores
                    
    Función: nivel3
    Lenguaje: Python 3.9.5
    Autores: Byron Mata F.
             Gustavo Alvarado A.

    Vesión: 2.0
    Fecha Última Edición: junio 12/2021
    Entradas: N/D
    Restricciones: N/D
    Salidas: N/D

    ***************************************************************************"""
    global vida, puntos, username, sgnds, pnts, FLAG, vent_sala
    FLAG = True
    vida = 3
    pnts = 0
    sgnds = 60
    contador = 0

    ventana.withdraw()

    vent_nivel3 = Toplevel()
    vent_nivel3.title('Nivel 3')
    vent_nivel3.minsize(500, 700)
    vent_nivel3.resizable(width=NO, height=NO)

    C_vent_nivel3 = Canvas(vent_nivel3, bg='black', width=500, height=700, highlightthickness=0)
    C_vent_nivel3.place(x=0, y=0)

    C_vent_nivel3.fondo = load_image('Nivel3.png')
    fondo_niveles = C_vent_nivel3.create_image(0, 0, anchor=NW, image=C_vent_nivel3.fondo)

    C_vent_nivel3.songPJ3 = load_mp3('Intergalactic Odyssey.mp3')
    songPJ3 = play_songs(C_vent_nivel3.songPJ3)

    Frame = Canvas(vent_nivel3, width=500, height=30, highlightthickness=0, bg='#10304a')
    Frame.place(x=0,y=0)

    Vida = Label(vent_nivel3, text="Life: "+str(vida), font=('OCR A Extended', 12), bg='#10304a', fg='white')
    Vida.place(x=130,y=3)
    Puntos = Label(vent_nivel3, text="Score: "+str(pnts), font=('OCR A Extended', 12), bg='#10304a', fg='white')
    Puntos.place(x=10,y=3)
    Temp = Label(vent_nivel3, font=('OCR A Extended', 12), bg='#10304a', fg='white')
    Temp.place(x=310,y=3)

    F_tiempo = Frame.create_text(284, 15, text="Time: ", font=('OCR A Extended', 13), fill='white')
    F_jugadador = Frame.create_text(420, 15, text=e_jugador.get(), font=('OCR A Extended', 13), fill='white')

    # -----------------------------------------------------------------------------------------------------
    def temporizador():
        global sgnds, contador, pnts
        sgnds = sgnds - 1
        pnts = pnts + 1
        contador=vent_nivel3.after(1000, temporizador)
        Temp.config(text=(sgnds))
        Puntos.config(text="Score: "+str(pnts))
    
    temporizador()

    # -----------------------------------------------------------------------------------------------------
    def nave():
        """
        ***************************************************************************
                    Instituto Tecnológio de Costa Rica
                        Ingeniería en Computadores
                        
        Función: nave
        Función interna: player_animation
        Lenguaje: Python 3.9.5
        Autores: Gustavo Alvarado A.
                 Byron Mata F.

        Vesión: 1.1
        Fecha Última Edición: junio 6/2021
        Entradas: N/D
        Restricciones: N/D
        Salidas: N/D

        Autores auxiliares: Jose Fernando Morales

        ***************************************************************************"""
        sprite = C_vent_nivel3.create_image(250, 340, tags=('sprite'))

        def player_animation(X):
            global Imagenes, FLAG
            nonlocal sprite
            if X == 3:
                X = 0
            if FLAG:
                C_vent_nivel3.itemconfig('sprite', image=Imagenes[X])

                def callback():
                    player_animation(X + 1)

                ventana.after(100, callback)

        Thread(target=player_animation, args=(0,)).start()

        # Movimiento del jugador
        def derecha(Evento):
            nonlocal C_vent_nivel3
            C_vent_nivel3.move(sprite, 10, 0)
            if C_vent_nivel3.coords(sprite)[0] > 460:  # colision con el borde de ventana
                C_vent_nivel3.move(sprite, -10, 0)

        def izquierda(Evento):
            nonlocal C_vent_nivel3
            C_vent_nivel3.move(sprite, -10, 0)
            if C_vent_nivel3.coords(sprite)[0] < 40:  # colision con el borde de ventana
                C_vent_nivel3.move(sprite, 10, 0)

        def arriba(Evento):
            nonlocal C_vent_nivel3
            C_vent_nivel3.move(sprite, 0, -10)
            if C_vent_nivel3.coords(sprite)[1] < 100:  # colision con el borde de ventana
                C_vent_nivel3.move(sprite, 0, 10)

        def abajo(Evento):
            nonlocal C_vent_nivel3
            C_vent_nivel3.move(sprite, 0, 10)
            if C_vent_nivel3.coords(sprite)[1] > 650:  # colision con el borde de ventana
                C_vent_nivel3.move(sprite, 0, -10)

        vent_nivel3.bind('<Right>', derecha)
        vent_nivel3.bind('<Left>', izquierda)
        vent_nivel3.bind('<Up>', arriba)
        vent_nivel3.bind('<Down>', abajo)

    nave()

    # -----------------------------------------------------------------------------------------------------
    def cerrar_nivel3():
        global FLAG
        FLAG = False
        ventana.deiconify()
        vent_nivel3.destroy()
        stop_song()
    
    vent_nivel3.protocol('WM_DELETE_WINDOW', cerrar_nivel3)

    B_cerrar_nivel3 = Button(vent_nivel3, text='←', font=fuente, width=5, height=1, command=cerrar_nivel3)
    B_cerrar_nivel3.place(x=435, y=665)

#------------------------------------------------------------------------------------------------------
def sala():
    """
    ***************************************************************************
                Instituto Tecnológio de Costa Rica
                    Ingeniería en Computadores
                    
    Función: sala
    Lenguaje: Python 3.9.5
    Autores: Byron Mata F.
             Gustavo Alvarado A.

    Vesión: 1.2
    Fecha Última Edición: junio 11/2021
    Entradas: N/D
    Restricciones: N/D
    Salidas: N/D

    ***************************************************************************"""
    ventana.withdraw()

    vent_sala = Toplevel()
    vent_sala.title('Sala de Niveles')
    vent_sala.minsize(500, 700)
    vent_sala.resizable(width=NO, height=NO)

    C_vent_sala = Canvas(vent_sala, bg='black', width=500, height=700, highlightthickness=0)
    C_vent_sala.place(x=0, y=0)

    C_vent_sala.fondo = load_image('Creditos.png')
    fondo_sala = C_vent_sala.create_image(0, 0, anchor=NW, image=C_vent_sala.fondo)

    def selec_niv1():
        nonlocal vent_sala
        vent_sala.destroy()
        nivel1()
    
    B_nivel1 = Button(vent_sala, text='Easy', font=fuente, width=10, height=1, command=selec_niv1)
    B_nivel1.place(x=200, y=150)

    def selec_niv2():
        nonlocal vent_sala
        vent_sala.destroy()
        nivel2()

    B_nivel2 = Button(vent_sala, text='Easy +', font=fuente, width=10, height=1, command=selec_niv2)
    B_nivel2.place(x=200, y=350)

    def selec_niv3():
        nonlocal vent_sala
        vent_sala.destroy()
        nivel3()

    B_nivel3 = Button(vent_sala, text='Easy ++', font=fuente, width=10, height=1, command=selec_niv3)
    B_nivel3.place(x=200, y=550)    

    def cerrar_sala():
        ventana.deiconify()
        vent_sala.destroy()
    vent_sala.protocol('WM_DELETE_WINDOW', cerrar_sala)

    B_cerrar_cerrar = Button(vent_sala, text='←', font=fuente, width=5 ,height=1, command=cerrar_sala)
    B_cerrar_cerrar.place(x=435,y=665)

B_sala = Button(ventana, text='Level Room', font=fuente, width=10, height=1, command=sala)
B_sala.place(x=200,y=400)

#------------------------------------------------------------------------------------------------------
def puntaje():
    """
    ***************************************************************************
                Instituto Tecnológio de Costa Rica
                    Ingeniería en Computadores
                    
    Función: puntaje
    Lenguaje: Python 3.9.5
    Autores: Byron Mata F.
             Gustavo Alvarado A.

    Vesión: 2.0
    Fecha Última Edición: junio 14/2021
    Entradas: N/D
    Restricciones: N/D
    Salidas: N/D

    ***************************************************************************"""
    ventana.withdraw()

    vent_puntajes = Toplevel()
    vent_puntajes.title('Puntajes')
    vent_puntajes.minsize(500, 700)
    vent_puntajes.resizable(width=NO, height=NO)
    C_vent_puntajes = Canvas(vent_puntajes, bg='black', width=500, height=700, highlightthickness = 0)
    C_vent_puntajes.place(x=0,y=0)

    C_vent_puntajes.fondo = load_image('Creditos.png')
    fondo_puntaje = C_vent_puntajes.create_image(0,0, anchor=NW, image = C_vent_puntajes.fondo)

    def cerrar_puntajes():
        ventana.deiconify()
        vent_puntajes.destroy()
    vent_puntajes.protocol('WM_DELETE_WINDOW', cerrar_puntajes)

    B_cerrar_puntajes = Button(vent_puntajes, text='←', font=fuente, width=5 ,height=1, command=cerrar_puntajes)
    B_cerrar_puntajes.place(x=435,y=665)

B_sala = Button(ventana, text='Scores', font=fuente, width=10, height=1, command=puntaje)
B_sala.place(x=200,y=480)

#------------------------------------------------------------------------------------------------------
def creditos():
    """
    ***************************************************************************
                Instituto Tecnológio de Costa Rica
                    Ingeniería en Computadores
                    
    Función: creditos
    Lenguaje: Python 3.9.5
    Autores: Byron Mata F.
             Gustavo Alvarado A.

    Vesión: 1.0
    Fecha Última Edición: junio 6/2021
    Entradas: N/D
    Restricciones: N/D
    Salidas: N/D

    ***************************************************************************"""
    ventana.withdraw()

    vent_creditos = Toplevel()
    vent_creditos.title('Créditos')
    vent_creditos.minsize(500, 700)
    vent_creditos.resizable(width=NO, height=NO)
    C_vent_creditos = Canvas(vent_creditos, width=500, height=700, highlightthickness = 0)
    C_vent_creditos.place(x=0,y=0)

    C_vent_creditos.fondo = load_image('Creditos.png')
    fondo_puntaje = C_vent_creditos.create_image(0,0, anchor=NW, image = C_vent_creditos.fondo)

    Text_creditos = C_vent_creditos.create_text(185, 200, fill='#00eaff', font=fuente, text=Creditos)
    
    def cerrar_creditos():
        ventana.deiconify()
        vent_creditos.destroy()
    vent_creditos.protocol('WM_DELETE_WINDOW', cerrar_creditos)

    B_cerrar_creditos = Button(vent_creditos, text='←', font=fuente, width=5 ,height=1, command=cerrar_creditos)
    B_cerrar_creditos.place(x=435,y=665)

B_creditos = Button(ventana, text='Credits', font=fuente, width=8, height=1, command=creditos)
B_creditos.place(x=5,y=665)

#------------------------------------------------------------------------------------------------------
ventana.mainloop()

#------------------------------------------------------------------------------------------------------
def doc():
    print(load_image.__doc__)
    print(load_sprite.__doc__)
    print(validar.__doc__)
    print(nivel1.__doc__)
    #print(nave.__doc__)
    #print(asteroides.__doc__)
    print(nivel2.__doc__)
    print(nivel3.__doc__)
    print(sala.__doc__)
    print(puntaje.__doc__)
    print(creditos.__doc__)

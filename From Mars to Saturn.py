creditos = """
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
import pygame

#-----------------------------------------------------------------
def load_image(nombre):
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

#------------------------------------------------------------------------------------------------------
def load_sprite(Nombre):
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

Asteroide_img = load_image("Asteroide01.png")
#------------------------------------------------------------------------------------------------------
def nivel1():
    global vida, puntos, username, FLAG
    FLAG = True
    vida = 3
    puntos = 0

    ventana.withdraw()

    vent_nivel1 = Toplevel()
    vent_nivel1.title('Nivel 1')
    vent_nivel1.minsize(500, 700)
    vent_nivel1.resizable(width=NO, height=NO)
    C_vent_nivel1 = Canvas(vent_nivel1, bg='black', width=500, height=700, highlightthickness=0)
    C_vent_nivel1.place(x=0, y=0)

    C_vent_nivel1.fondo = load_image('Nivel1.png')
    fondo_niveles = C_vent_nivel1.create_image(0, 0, anchor=NW, image = C_vent_nivel1.fondo)

    Frame = Canvas(vent_nivel1, width=500, height=30, highlightthickness=0, bg='#10304a')
    Frame.place(x=0,y=0)

    F_puntos = Frame.create_text(40, 15, text="Score: ", font=('OCR A Extended', 13), fill='white')
    F_vida = Frame.create_text(170, 15, text="Lifes: ", font=('OCR A Extended', 13), fill='white')
    F_tiempo = Frame.create_text(290, 15, text="Time: ", font=('OCR A Extended', 13), fill='white')
    F_jugadador = Frame.create_text(420, 15, text=e_jugador.get(), font=('OCR A Extended', 13), fill='white')

     # -----------------------------------------------------------------------------------------------------
    def nave():
        nonlocal vent_nivel1
        sprite = C_vent_nivel1.create_image(250, 600, tags=('sprite'))

        # Animación del jugador
        def player_animation(X):
            global Imagenes, FLAG
            nonlocal sprite
            if X == 3:
                X = 0;
            if FLAG:
                C_vent_nivel1.itemconfig('sprite', image=Imagenes[X])

                def callback():
                    player_animation(X + 1)

                ventana.after(100, callback)

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
    FLAG_AST = True
    def asteroides():
        global Asteroide_img
        nonlocal C_vent_nivel1
        Asteroide = C_vent_nivel1.create_image(200,200, anchor=NW, image=Asteroide_img)
        Contador = 1
        A = 0

        def condicion():
            nonlocal Contador
            if Contador%2 == 0:
                return reverse_move()
            else:
                return asteroide_move()

        def asteroide_move():
            nonlocal FLAG_AST, Contador, C_vent_nivel1, A
            Ast_x = random.randint(1,10)
            Ast_y = random.randint(1,10)
            FLAG_AST = True
            Contador += 1
            return recursive_move(Ast_x, Ast_y)

        def recursive_move(X,Y):
            nonlocal FLAG_AST, vent_nivel1, C_vent_nivel1, Contador, A
            if FLAG_AST == True:
                C_vent_nivel1.move(Asteroide, X, Y)
                Ast_coords = C_vent_nivel1.coords(Asteroide)
                def callback(AX,AY):
                    recursive_move(AX,AY)
                A = C_vent_nivel1.after(50, callback, X,Y)
                if Ast_coords[0] < 30 or Ast_coords[0] > 480 or Ast_coords[1] < 20 or Ast_coords[1] > 680:
                    FLAG_AST = False
                    C_vent_nivel1.after_cancel(A)
                    return condicion()

        def reverse_move():
            nonlocal FLAG_AST, Contador, A, C_vent_nivel1
            Ast_x = random.randint(-10,-1)
            Ast_y = random.randint(-10,-1)
            FLAG_AST = True
            Contador += 1
            C_vent_nivel1.after_cancel(A)
            return recursive_move(Ast_x, Ast_y)

        condicion()

    asteroides()
    # ------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------
    def cerrar_nivel1():
        global FLAG
        nonlocal FLAG_AST
        FLAG = False
        FLAG_AST = False
        ventana.deiconify()
        vent_nivel1.destroy()
        stop_song()

    vent_nivel1.protocol('WM_DELETE_WINDOW', cerrar_nivel1)

    B_cerrar_nivel1 = Button(vent_nivel1, text='←', font=fuente, width=5, height=1, command=cerrar_nivel1)
    B_cerrar_nivel1.place(x=435, y=665)

B_nivel1 = Button(ventana, text='Level Room', font=fuente, width=10, height=1, command=validar)
B_nivel1.place(x=200, y=400)

# ------------------------------------------------------------------------------------------------------
def nivel2():
    global vida, puntos, username, FLAG
    FLAG = True
    vida = 3
    puntos = 0

    ventana.withdraw()

    vent_nivel2 = Toplevel()
    vent_nivel2.title('Nivel 2')
    vent_nivel2.minsize(500, 700)
    vent_nivel2.resizable(width=NO, height=NO)
    C_vent_nivel2 = Canvas(vent_nivel2, bg='black', width=500, height=700, highlightthickness=0)
    C_vent_nivel2.place(x=0, y=0)

    C_vent_nivel2.fondo = load_image('Nivel2.png')
    fondo_niveles = C_vent_nivel2.create_image(0, 0, anchor=NW, image=C_vent_nivel2.fondo)

    Frame = Canvas(vent_nivel2, width=500, height=30, highlightthickness=0, bg='#10304a')
    Frame.place(x=0,y=0)

    Frame.create_text(40, 15, text="Score: ", font=('OCR A Extended', 13), fill='white')
    Frame.create_text(170, 15, text="Lifes: ", font=('OCR A Extended', 13), fill='white')
    Frame.create_text(290, 15, text="Time: ", font=('OCR A Extended', 13), fill='white')
    Frame.create_text(420, 15, text=e_jugador.get(), font=('OCR A Extended', 13), fill='white')

    # ------------------------------------------------------------------------------------------------------
    def nave():
        sprite = C_vent_nivel2.create_image(250, 340, tags=('sprite'))

        def player_animation(X):
            global Imagenes, FLAG
            nonlocal sprite
            if X == 3:
                X = 0;
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
    def cerrar_nivel2():
        global FLAG
        FLAG = False
        ventana.deiconify()
        vent_nivel2.destroy()
        stop_song()

    vent_nivel2.protocol('WM_DELETE_WINDOW', cerrar_nivel2)

    B_cerrar_nivel2 = Button(vent_nivel2, text='←', font=fuente, width=5, height=1, command=cerrar_nivel2)
    B_cerrar_nivel2.place(x=435, y=665)

B_nivel2 = Button(ventana, text='Level Room', font=fuente, width=10, height=1, command=validar)
B_nivel2.place(x=200, y=400)

# ------------------------------------------------------------------------------------------------------
def nivel3():
    global vida, puntos, username, FLAG
    FLAG = True
    vida = 3
    puntos = 0

    ventana.withdraw()

    vent_nivel3 = Toplevel()
    vent_nivel3.title('Nivel 3')
    vent_nivel3.minsize(500, 700)
    vent_nivel3.resizable(width=NO, height=NO)

    C_vent_nivel3 = Canvas(vent_nivel3, bg='black', width=500, height=700, highlightthickness=0)
    C_vent_nivel3.place(x=0, y=0)

    C_vent_nivel3.fondo = load_image('Nivel3.png')
    fondo_niveles = C_vent_nivel3.create_image(0, 0, anchor=NW, image=C_vent_nivel3.fondo)

    Frame = Canvas(vent_nivel3, width=500, height=30, highlightthickness=0, bg='#10304a')
    Frame.place(x=0,y=0)

    Frame.create_text(40, 15, text="Score: ", font=('OCR A Extended', 13), fill='white')
    Frame.create_text(170, 15, text="Lifes: ", font=('OCR A Extended', 13), fill='white')
    Frame.create_text(290, 15, text="Time: ", font=('OCR A Extended', 13), fill='white')
    Frame.create_text(420, 15, text=e_jugador.get(), font=('OCR A Extended', 13), fill='white')

    # ------------------------------------------------------------------------------------------------------
    def nave():
        sprite = C_vent_nivel3.create_image(250, 340, tags=('sprite'))

        def player_animation(X):
            global Imagenes, FLAG
            nonlocal sprite
            if X == 3:
                X = 0;
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

#------------------------------------------------------------------------------------------------------
def puntaje():
    ventana.withdraw()

    vent_puntajes = Toplevel()
    vent_puntajes.title('Puntajes')
    vent_puntajes.minsize(500, 700)
    vent_puntajes.resizable(width=NO, height=NO)
    C_vent_puntajes = Canvas(vent_puntajes, bg='black', width=500, height=700, highlightthickness = 0)
    C_vent_puntajes.place(x=0,y=0)

    C_vent_puntajes.fondo = load_image('Pantalla_niveles.png')
    fondo_puntaje = C_vent_puntajes.create_image(0,0, anchor=NW, image = C_vent_puntajes.fondo)

    def cerrar_puntajes():
        ventana.deiconify()
        vent_puntajes.destroy()
        stop_song()
    vent_puntajes.protocol('WM_DELETE_WINDOW', cerrar_puntajes)

    B_cerrar_puntajes = Button(vent_puntajes, text='←', font=fuente, width=5 ,height=1, command=cerrar_puntajes)
    B_cerrar_puntajes.place(x=435,y=665)

B_sala = Button(ventana, text='Scores', font=fuente, width=10, height=1, command=puntaje)
B_sala.place(x=200,y=480)

#------------------------------------------------------------------------------------------------------

def credits():
    ventana.withdraw()

    vent_creditos = Toplevel()
    vent_creditos.title('Créditos')
    vent_creditos.minsize(500, 700)
    vent_creditos.resizable(width=NO, height=NO)
    C_vent_creditos = Canvas(vent_creditos, width=500, height=700, highlightthickness = 0)
    C_vent_creditos.place(x=0,y=0)

    C_vent_creditos.fondo = load_image('Creditos.png')
    fondo_puntaje = C_vent_creditos.create_image(0,0, anchor=NW, image = C_vent_creditos.fondo)

    Text_creditos = C_vent_creditos.create_text(185, 200, fill='#00eaff', font=fuente, text=creditos)
    
    def cerrar_creditos():
        ventana.deiconify()
        vent_creditos.destroy()
        stop_song()
    vent_creditos.protocol('WM_DELETE_WINDOW', cerrar_creditos)

    B_cerrar_creditos = Button(vent_creditos, text='←', font=fuente, width=5 ,height=1, command=cerrar_creditos)
    B_cerrar_creditos.place(x=435,y=665)

B_creditos = Button(ventana, text='Credits', font=fuente, width=8, height=1, command=credits)
B_creditos.place(x=5,y=665)

#------------------------------------------------------------------------------------------------------

ventana.mainloop()

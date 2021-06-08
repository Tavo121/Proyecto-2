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

-Para el disparo se utiliza
la tecla de barra espacidora:
[espacio]
"""
#-----------------------------------------------------------------

from tkinter import *
import os
from os import path
from threading import Thread
import vlc
import glob

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

FLAG = True
#------------------------------------------------------------------------------------------------------

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

def validar():
    global e_jugador
    username = e_jugador.get()
    if (username!=""):
        return sala()
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
Nave = load_image('tile00.png')

def sala():
    global Nave
    ventana.withdraw()

    vent_sala = Toplevel()
    vent_sala.title('Selección de niveles')
    vent_sala.minsize(500, 700)
    vent_sala.resizable(width=NO, height=NO)
    C_vent_sala = Canvas(vent_sala, bg='black', width=500, height=700, highlightthickness = 0)
    C_vent_sala.place(x=0,y=0)

    C_vent_sala.fondo = load_image('Nivel1.png')
    fondo_niveles = C_vent_sala.create_image(0,0, anchor=NW, image = C_vent_sala.fondo)

    C_vent_sala.create_image(100,100, anchor = NW, image = Nave)

    def cerrar_sala():
        ventana.deiconify()
        vent_sala.destroy()
        stop_song()
    vent_sala.protocol('WM_DELETE_WINDOW', cerrar_sala)

    B_cerrar_sala = Button(vent_sala, text='←', font=fuente, width=5 ,height=1, command=cerrar_sala)
    B_cerrar_sala.place(x=435,y=665)

B_sala = Button(ventana, text='Level Room', font=fuente, width=10, height=1, command=validar)
B_sala.place(x=200,y=400)

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

    Text_creditos = C_vent_creditos.create_text(185, 215, fill='#00eaff', font=fuente, text=creditos)
    
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

#------------------------------------------------------------------------------------------------------

ventana.mainloop()

Nombree = 'Juan'
score = 100
Total_score = Nombree +'---' + str(score) + '\n'
def save_highscore2():
    global Nombree, score
    Nombre_usuario = Nombree
    Score_Usuario = Nombre_usuario + "---" + str(score) + ","
    Arch = open("Highscore.txt", "r+")
    Nombres = Arch.readline()

    def rewrite(Names):
        if Names == []:
            print('saved succesfully')
        else:
            Arch.write(Names[0])
            return rewrite(Names[1:])

    def compare_ptn2(Puntos, Names, vueltas, i,j):
        nonlocal Score_Usuario
        if vueltas == 10:
            print('Lower puntaje')
        elif Names[i][j] == "1" or Names[i][j] == '2' or Names[i][j] == '3' or Names[i][j] == "4" or Names[i][j] == '5':
            Comparacion = Names[i][j:-2]
            if Comparacion <= str(Puntos):
                print('yes')
                Names[i] = Score_Usuario + '\n'
                Arch.seek(0)
                return rewrite(Names)
            else:
                return compare_ptn2(Puntos, Names, vueltas +1, i+1, 0)
        else:
            return compare_ptn2(Puntos, Names, vueltas, i, j+1)


    def compare2(Puntaje, Registros, Names, Names2):
        global score
        if Registros == 10:
            compare_ptn2(score, Names2, 0, 0, 0)
        elif Names[0] == "":
            Names.append(Puntaje + "\n")
        else:
            compare2(Puntaje, Registros +1, Names[1:], Names2)

    def create_list(Names, Result):
        nonlocal Score_Usuario
        if Names == "":
            return compare2(Score_Usuario, 0, Result, Result)
        else:
            Result.append(Names)
            Names = Arch.readline()
            return create_list(Names, Result)
    create_list(Nombres, [])
    Arch.close()

#save_highscore2()
#=====================================================================

def num_finder(Nombre, i, Result):
    if Nombre[i] == "1" or Nombre[i] == '2' or Nombre[i] == '3' or Nombre[i] == "4" or Nombre[i] == '5' or Nombre[i] == '6' or Nombre[i] == '7' or Nombre[i] == '8' or Nombre[i] == '9':
        Result = Nombre[i:-2]
        return Result
    else:
        return num_finder(Nombre, i+1, Result)

def quickS_list_maker():
    Arch = open('a.txt', 'r')
    def create_list(Names, Result):
        if Names == "":
            return Result
        else:
            Result.append(Names)
            Names = Arch.readline()
            return create_list(Names, Result)

    Lista_nombres = create_list(Arch.readline(), [])
    Arch.close()
    return quicksort_pnts(Lista_nombres)

def rewrite(Names):
    Arch = open('a.txt', 'w')
    while Names != []:
        Arch.write(Names[0])
        Names = Names[1:]
    Arch.close()

def quicksort_pnts(Lista):
    Menores = []
    Iguales = []
    Mayores = []
    if len(Lista) <= 1:
        return rewrite(Lista)


    Pivote = num_finder(Lista[-1], 0, '')
    dividir_lista(Lista, 0, len(Lista), Pivote, Menores, Iguales, Mayores)
    Result = quicksort_pnts(Menores)
    Result.extend(Iguales)
    Result.extend(quicksort_pnts(Mayores))
    return rewrite(Result)

def dividir_lista(Nombres, i, Cant_list, Pivote, Menores, Iguales, Mayores):
    if i == Cant_list:
        return Menores, Iguales, Mayores
    if num_finder(Nombres[i], 0, '') < Pivote:
        Menores.append(Nombres[i])
    elif num_finder(Nombres[i], 0, '') > Pivote:
        Mayores.append(Nombres[i])
    elif num_finder(Nombres[i], 0, '') == Pivote:
        Iguales.append(Nombres[i])
    return dividir_lista(Nombres,i+1,Cant_list,Pivote,Menores,Iguales,Mayores)

#quickS_list_maker()

def position():
    global e_jugador, pnts
    Arch = open('Highscore.txt', 'r')
    Nombre = 'Gustavo' + '---' + '65' + ',' + '\n'
    Pos = 1
    Comp = Arch.readline()
    while Comp != "":
        print(Comp)
        if Comp == Nombre:
            Arch.close()
            print('Su posicion es: ' + str(Pos))
            return 0
        Comp = Arch.readline()
        Pos += 1
    print('No sea manco')
    Arch.close()



def num_finder(Nombre, i, Result): #toma los numeros del string ingresado
    if Nombre[i] == "1" or Nombre[i] == '2' or Nombre[i] == '3' or Nombre[i] == "4" or Nombre[i] == '5' or Nombre[i] == '6' or Nombre[i] == '7' or Nombre[i] == '8' or Nombre[i] == '9':
        Result = Nombre[i:-2]
        return Result
    else:
        return num_finder(Nombre, i+1, Result)

def quickS_list_maker(): #crea una lista con los nombres y sus puntajes y luego llama a la funcion quicksort_names con la lista creada
    Arch = open('Highscore.txt', 'r')
    def create_list(Names, Result): #crea la lista con nombres y sus puntajes
        if Names == "": #condicion de finalizacion
            return Result
        else:
            Result.append(Names)
            Names = Arch.readline()
            return create_list(Names, Result)

    Lista_nombres = create_list(Arch.readline(), [])
    Arch.close()
    print(Lista_nombres)
    #return quicksort_pnts(Lista_nombres)

def rewrite(Names): #reescribe los puntajes en el archivo txt
    Arch = open('Highscore.txt', 'w')
    while Names != []:
        Arch.write(Names[0])
        Names = Names[1:]
    Arch.close()

def quicksort_pnts(Lista):
    """
    ***************************************************************************
                Instituto Tecnol??gio de Costa Rica
                    Ingenier??a en Computadores

    Funci??n: quicksort_pnts
    Lenguaje: Python 3.9.5
    Autores: Byron Mata F.
             Gustavo Alvarado A.

    Vesi??n: 1.0
    Fecha ??ltima Edici??n: junio 6/2021
    Entradas: Lista de puntajes
    Restricciones: Nombres deben ser tipo string y seguir el formato de guardado de puntajes
    Salidas: Puntajes ordenados por puntos de manera descendiente

    ***************************************************************************"""
    Menores = []
    Iguales = []
    Mayores = []
    if len(Lista) <= 1:
        return Lista

    Pivote = num_finder(Lista[-1], 0, '') #variable para realizar las comparaciones
    dividir_lista(Lista, 0, len(Lista), Pivote, Menores, Iguales, Mayores)
    Result = quicksort_pnts(Menores)
    Result.extend(Iguales) #agrega los puntajes menores al pivote
    Result.extend(quicksort_pnts(Mayores)) #agrega los puntajes mayores al pivote
    return Result

def dividir_lista(Nombres, i, Cant_list, Pivote, Menores, Iguales, Mayores): #divide en diferentes listas y clasifica los puntajes
    if i == Cant_list:
        return Menores, Iguales, Mayores
    if int(num_finder(Nombres[i], 0, '')) < int(Pivote):
        Menores.append(Nombres[i]) #lista de menores al pivote
    elif int(num_finder(Nombres[i], 0, '')) > int(Pivote):
        Mayores.append(Nombres[i])#lista de mayores al pivote
    elif int(num_finder(Nombres[i], 0, '')) == int(Pivote):
        Iguales.append(Nombres[i]) #lista de iguales al pivote
    return dividir_lista(Nombres,i+1,Cant_list,Pivote,Menores,Iguales,Mayores)

quickS_list_maker()
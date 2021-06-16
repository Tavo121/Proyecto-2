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

save_highscore2()
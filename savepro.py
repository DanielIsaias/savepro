#import subprocess as sub
import os 
import functions as fun 
import sys

#En este archivo lo usare para crear todas la opciones y parametros
#que tendra el programa 

#Esta divido en 2 codicionales
#si los argumentos son 4, contando el nombre del script y
#si los argumentos son 3, contando el nombre del script
#-s --save y -r --repo <-- para aguardar el programa 
#-d --del y -r --repo  <-- para borrarlo 
#para listar los programas aguardados solo se usara 3 parametros
#especificando el origen del programa, si viene de los repositorios si vienede los paquetes snap. 


#Guardar las opciones en una lista, hace que escriba menos codigo
arguments = [ ["-s","--save"], ["-d", "--del"], ["-r","--repo"],["-l", "--list" ] ]




if len(sys.argv) == 4: #cantidad de argumentos de terminal
    op1 = sys.argv[1]  #option
    op2 = sys.argv[2]  #option
    pr  = sys.argv[3]  #program 

    if (op1 in arguments[0]) and (op2 in arguments[2]): #add a program to the selected list-------
        if not fun.is_installed(pr):
            print("The program in not installed.")
            exit() 
        elif fun.in_the_file("repo_programs.txt", pr):
            print("The program is in the file.")
            exit()
        else:
            #si no se cumple ninguna de las condiciones anteriores, el programa se guardara
            fun.add_to_file("repo_programs.txt", pr, True)
            print("The program is saved.") 
            exit()
    elif (op1 in arguments[1]) and (op2 in arguments[2]): #delete a program from the list---------
        if (not fun.in_the_file("repo_programs.txt", pr) ):
            print("The program you want to remove is not in the file.")
            exit()
        else:
            fun.del_from_file("repo_programs.txt", pr) 
            print("The program is removed from your list.")
            exit()

elif len(sys.argv) == 3: 
    op1 = sys.argv[1] #option
    pr  = sys.argv[2] #name of the origin of the program
    
    if (op1 in arguments[3]) and (pr == "repo"): #list the programs in the specified archive--------
        fun.list_programms("repo_programs.txt") 
        exit() 
    else:
        print("Error: parametros no reconocidos.") 

else:
    print("-Error: parametros incorrectos.") 
    exit() 


    

























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





if len(sys.argv) == 4: #cantidad de argumentos de terminal
    op1,op2  = sys.argv[1],sys.argv[2] #options
    pr = sys.argv[3] #program 

    if (op1 == "-s" or op1 == "--save") and (op2 == "-r" or op2 == "--repo"):
        if fun.add_program("repo_programs.txt", pr) == True:
            print("Program save.")
            exit()
        else:
            print("Lo siento, El programa no existe.") 
            exit()
    elif (op1 == "-d" or op1 == "--del") and (op2 == "-r" or op2 == "--repo"):
        fun.del_from_file("repo_programs.txt",pr)
        print("Program removed.") 
        exit() 
    else:
        print("-Error: parametros no reconocidos.") 
        exit()

elif len(sys.argv) == 3: 
    op1 = sys.argv[1] #option
    pr  = sys.argv[2] #name of the origin of the program
    
    if (op1 == "-l" or op1 == "--list") and  pr == "repo":
        fun.list_programms("repo_programs.txt") 
        exit() 
    else:
        print("Error: parametros no reconocidos.") 

else:
    print("-Error: parametros incorrectos.") 
    exit() 


    

























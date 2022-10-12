#import subprocess as sub
import os 
import functions as fun 
import sys

#En este archivo lo usare para crear todas la opciones y parametros
#que tendra el programa 



if not len(sys.argv) == 3: 
    print("Error: se requiren 3 parametros")
    exit()


op = sys.argv[1] #op
pr = sys.argv[2] #program


if op == "-s":
    if not fun.add_program(pr): 
        print("Error:El programa no esta instalado") 
        exit()
    else:
        print("El programa se aguardo con exito.")
        exit() 
elif op == "-l" or op == "--list": 
    if pr != "repo": 
        print("Error: parametro desconocido.") 
        exit() 
    else: 
        fun.list_programms("list_of_programms.txt") 
        exit()
elif op == "-dr" or op == "--delrepo":
    fun.del_from_file("list_of_programms.txt", pr)
    exit() 
else:
    print("Parametros no reconocidos.") 
























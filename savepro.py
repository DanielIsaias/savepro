import subprocess as sub
import os

#With this file we store the record of installed Programs
import list_of_programms




#The list can be replaced by a file to store permanently the programs we have
repo_programs = [] 



def record_install(repo, nameOfApp):
    #The type of instalation is from where we install the program 
    #Using dictionaris we can avoid use ifElse 
    type_of_installation = {'-repo': "sudo apt install "} 

    install = type_of_installation[repo] + nameOfApp 

    os.system(install) 
    #la mejor practica es obtener la salida del comando para poder manejar los errores que surgan
    

    #If every thing is ok, we can store the program
     
    infoCommand = 'whatis {} | cut -c 24-'.format(nameOfApp) 
    appInfo = sub.run(infoCommand, capture_output=True, text=True, shell=True) 


    repo_programs.append([nameOfApp,appInfo.stdout]) 



#Nos falta agregar aque lista se aguardara
#mejor usaremos una funcion para guardar el programa junto con su descripsion
def add_program(name): 
    
    #infoCommand = 

    list_of_programms.repo_programs.append(name)




#Nos muestra una lista de los progrmas instalados 
#La idea es que nos lo muestre en un tabla de manera ordenada
def list_terminal_apps():
    for i in range(len(repo_programs)):
        print(repo_programs[i]) 



answer = input("Enter program name:")
repo = input("repo:") 
record_install(repo, answer)


list_terminal_apps() 

















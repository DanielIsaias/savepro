import subprocess as sub
import os

#With this file we store the record of installed Programs
#import list_of_programms







def record_install(repo, nameOfApp):
    #The type of instalation is from where we install the program 
    #Using dictionaris we can avoid use ifElse 
    type_of_installation = {'-repo': "sudo apt install "} 

    install = type_of_installation[repo] + nameOfApp 

    os.system(install) 
    #la mejor practica es obtener la salida del comando para poder manejar los errores que surgan
    

    #If every thing is ok, we can store the program
   





#mejor usaremos una funcion para guardar el programa junto con su descripsion
def add_program(name): 
    infoCommand = f"whatis {name} | cut -c 20-"

    #Esta variable almacena la salida del comando
    appInfo = sub.run(infoCommand, capture_output=True, text=True, shell=True)
    
    #La string que agregaremos al archivo 
    lineToAppend = name + appInfo.stdout

    add_to_file('list_of_programms.txt',lineToAppend) 




#vamos a usar la palabra "with" para trabajar con nuestro archivo de python
#crearemos una funcion donde se hace todo el proceso de abrir y almacenar info en el archivo
#tenemos que poner el texto de agregaremos y el archivo .txt
def add_to_file(nameFile, text):
    with open(nameFile, 'a') as file:
        file.write(f"{text}")




#Esta funcion nos permite verifcar si el programa que queremos guardar esta instalado correctamente
#en caso  de que no, nos muestra un mensaje y se sale de la ejecucion.
def is_installed(name):
    command = f"dpkg -s {name}"

    appInfo = sub.run(command, capture_output=True, text=True, shell=True)

    appInfo_text = appInfo.stdout.split("\n")

    if "Status: install ok installed" in appInfo_text:
        return True
    else:
        return "This program is not installed."

    return False



#Esta funcion nos muestra el contenido de un archivo
def list_programs(nameFile):
    with open(nameFile, 'r', encoding = 'utf-8') as file:
        for i in file:
            print(i, end = '')


#Esta funcion se usara para eliminar la linea de texto que contenga
#el nombre del programa que queremos eliminar
def del_from_file(nameFile, text):
    with open(nameFile, 'r') as oldFile:
        with open("temp.txt", 'w') as newFile:
            for line in oldFile:
                if text not in line.strip('\n'):
                    newFile.write(f"{line}")
    #Creamos un nuevo archivo y luego cambiamos el nombre 
    os.replace("temp.txt", nameFile)






#line for test the functions
















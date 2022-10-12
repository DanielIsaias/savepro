import subprocess as sub
import os


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
    #Check if the program is installed.
    if not is_installed(name):
        return False

    add_to_file('list_of_programms.txt', name, True) 






#vamos a usar la palabra "with" para trabajar con nuestro archivo de python
#crearemos una funcion donde se hace todo el proceso de abrir y almacenar info en el archivo
#tenemos que poner el texto de agregaremos y el archivo .txt
def add_to_file(nameFile, text, lineBreak=False):
    with open(nameFile, 'a') as file:
        file.write(f"{text}")
        if lineBreak == True:
            file.write('\n') 







#Esta funcion nos permite verifcar si el programa que queremos guardar esta instalado correctamente
#en caso  de que no, nos muestra un mensaje y se sale de la ejecucion.
def is_installed(name):
    command = f"dpkg -s {name}"

    appInfo = sub.run(command, capture_output=True, text=True, shell=True)

    appInfo_text = appInfo.stdout.split("\n")

    if "Status: install ok installed" in appInfo_text:
        return True

    return False








#Esta funcion nos muestra el contenido de un archivo
def list_programms(nameFile):
    with open(nameFile, 'r', encoding = 'utf-8') as file:
        num = 0 #variable que sirve para contar
        for i in file:
            num += 1
            print(f"{num}.-{i}", end = '')







#Esta funcion se usara para eliminar la linea de texto que contenga
#el nombre del programa que queremos eliminar
def del_from_file(nameFile, text):
    with open(nameFile, 'r') as oldFile:
        with open("temp.txt", 'w') as newFile:
            for line in oldFile:
                if text != line.strip('\n'):
                    newFile.write(f"{line}")
    #Creamos un nuevo archivo y luego cambiamos el nombre
    os.replace("temp.txt", nameFile)













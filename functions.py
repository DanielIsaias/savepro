import subprocess as sub
import os





def add_program(nameFile, name):
#El programa que querramos aguardar tiene que cumplir con las siguientes condiciones
#para poder ser guardado en el archivo correspondiente.
    if is_installed(name) and (not in_the_file(nameFile, name)): 
        add_to_file(nameFile, name, True)
        return True
    else:
        return False

        





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
    else:
        return False


#La funcion verificara que el programa que querramos agregar NO exista en el archivo y
#de esta menera evitamos que se duplique el nombre.
def in_the_file(nameFile, name): 
    with open(nameFile, 'r') as file_txt:
        lines = file_txt.readlines() 
        lines = [i.strip('\n') for i in lines]

        if name in lines:
            return True
        else:
            return False





#Esta funcion nos muestra el contenido de un archivo
def list_programms(nameFile):
    with open(nameFile, "r") as file_txt:
        num = 0 #variable que sirve para contar
        for i in file_txt:
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




#add_program("repo_programs.txt", "inxi")
#list_programms("repo_programs.txt")
#del_from_file("repo_programs.txt", "inxi")







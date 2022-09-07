
import os




#The list can be replaced by a file to store permanently the programs we have
terminal_programs = [] 

#The type of installation or the type of repo 
#this way can avoid use (if and else) 
type_of_installation = {'-repo': "sudo apt install " } 




def record_install(repo, nameOfApp):
    command = type_of_installation[repo] + nameOfApp 
    os.system(command) #la mejor practica es obtener la salida del comando para poder manejar los errores que surgan
    terminal_programs.append(nameOfApp) 




#nos muestra una lista de los progrmas instalados 
def list_terminal_apps():
    for i in range(len(terminal_programs)):
        print(str(i) + terminal_programs ) 







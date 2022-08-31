
import os




#The list can be replaced by a file to store permanently the programs we have
terminal_programs = [] 

#The type of installation or the type of repo 
#this way can avoid use (if and else) 
type_of_installation = {'-r': "sudo apt install " } 




def recapp(repo, nameOfApp):
    command = type_of_installation[repo] + nameOfApp 
    os.system(command) 
    terminal_programs.append(nameOfApp) 





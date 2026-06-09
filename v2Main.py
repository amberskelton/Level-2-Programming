"""Version 2 Menu Program
   ----------------------
   Menu program with a login, displays the cafe menu,
   allows users to add multiple items to the cart, and ability to pay"""
#imports different modules and their functions
import sys#sys.exit() to exit program
from easygui import buttonbox, msgbox, enterbox#user interface
import v2UI#functions containing input/output
import v2Auth#functions containing authentication processes

def menuProgram():
    while True:
        ask_acc=v2UI.login_register("Do you have an existing account or would you like to register?")
        if ask_acc=="Login":#if existing account
            password=v2Auth.login()
            if password==None:#if cancelled, loop and run the login/register choice again
                continue
            break
        elif ask_acc=="Register":#if registering account
            password=v2Auth.register()
            break
        elif ask_acc=="Exit":#if user wants to quit the program
            sys.exit()
        
menuProgram()#runs the program

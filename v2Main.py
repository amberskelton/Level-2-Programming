"""Version 2 Menu Program
   ----------------------
   Menu program with a login, displays the cafe menu,
   allows users to add multiple items to the cart, and ability to pay"""
#imports different modules and their functions
import sys#sys.exit() to exit program
from easygui import buttonbox, msgbox, enterbox#user interface
import v2UI#functions containing input/output
import v2Auth#functions containing authentication processes
import v2Menu#functions containing the menu, ordering and payment processes

def menuProgram():#function that operates the whole menu using imported functions from other modules
    while True:
        ask_acc=v2UI.login_register("Do you have an existing account or would you like to register?")
        if ask_acc=="Login":#if existing account
            result=v2Auth.login()
            if result==None:#if cancelled, loop and run the login/register choice again
                continue
            student_id,password=result#v2Auth.login() returns the student ID and its password, this line just splits the two variables up
            v2Menu.cafeMenu(student_id,password)
            break
        elif ask_acc=="Register":#if registering account
            result=v2Auth.register()
            if result==None:#if cancelled, loop and run the login/register choice again
                continue
            student_id,password=result#v2Auth.register() returns the student ID and its password, this line just splits the two variables up
            v2Menu.cafeMenu(student_id,password)
            break
        elif ask_acc=="Exit":#if user wants to quit the program
            sys.exit()
        
menuProgram()#runs the program

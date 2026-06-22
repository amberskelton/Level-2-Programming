"""Version 3 Menu Program
   ----------------------
   Menu program with a login, displays the cafe menu,
   allows users to add multiple items to the cart, and ability to pay"""
#imports different modules and their functions
import sys#sys.exit() to exit program
from easygui import buttonbox, msgbox, enterbox#user interface
'''import v3Auth#functions containing authentication processes'''
'''import v3Menu#functions containing the menu, ordering and payment processes'''
import tkinter as tk#user interface using frames
import v3Auth#functions containing authorisation

root=tk.Tk()
root.title("BDSC Café Menu")
root.geometry("600x800")

#create frames
fr_welcome=tk.Frame(root)
fr_login=tk.Frame(root)
fr_register=tk.Frame(root)
fr_menu=tk.Frame(root)

#use for loop to bring forward frames
for frame in (fr_welcome,fr_login,fr_register):
    frame.place(relwidth=1,relheight=1)

#function to show frame
def show_frame(frame):
    frame.tkraise()

#function for if login chosen
def login_chosen():
    student_id=verify_id.get()
    pswd=verify_pswd.get()
    print(student_id)
    print(pswd)

#function for if register chosen
def register_chosen():
    student_id=verify_id.get()
    pswd=verify_pswd.get()
    print(student_id)
    print(pswd)

#welcome page
tk.Label(fr_welcome,padx=20,pady=5,text="BDSC Café",font=("Arial",30,"bold")).pack()
tk.Label(fr_welcome,padx=20,pady=5,text="Do you have an existing account or would you like to register?").pack()
tk.Button(fr_welcome,text="Login",command=lambda:show_frame(fr_login)).pack()
tk.Button(fr_welcome,text="Register",command=lambda:show_frame(fr_register)).pack()

#login page
tk.Label(fr_login,padx=20,pady=5,text="Please enter your ID:",font=("Arial",12)).pack()
verify_id=tk.Entry(fr_login,font=("Arial",12))
verify_id.pack()
tk.Label(fr_login,padx=20,pady=5,text="Please enter your password:",font=("Arial",12)).pack()
verify_pswd=tk.Entry(fr_login,font=("Arial",12))
verify_pswd.pack()

tk.Button(fr_login,text="Login",command=login_chosen).pack()
tk.Button(fr_login,text="Back",command=lambda:show_frame(fr_welcome)).pack()

#register page
tk.Label(fr_register,padx=20,pady=5,text="Please enter your ID:",font=("Arial",12)).pack()
verify_id=tk.Entry(fr_register,font=("Arial",12))
verify_id.pack()
tk.Label(fr_register,padx=20,pady=5,text="Please create a password:",font=("Arial",12)).pack()
verify_pswd=tk.Entry(fr_register,font=("Arial",12))
verify_pswd.pack()

tk.Button(fr_register,text="Register",command=register_chosen).pack()
tk.Button(fr_register,text="Back",command=lambda:show_frame(fr_welcome)).pack()


'''def menuProgram():#function that operates the whole menu using imported functions from other modules
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
            sys.exit()'''

show_frame(fr_welcome)
root.mainloop()

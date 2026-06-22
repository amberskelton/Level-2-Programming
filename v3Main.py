"""Version 3 Menu Program
   ----------------------
   Menu program with a login, displays the cafe menu,
   allows users to add multiple items to the cart, and ability to pay"""
#imports different modules and their functions
import sys#sys.exit() to exit program
import v3Auth#functions containing authentication processes
'''import v3Menu#functions containing the menu, ordering and payment processes'''
import tkinter as tk#user interface using frames
from tkinter import messagebox

root=tk.Tk()
root.title("BDSC Café Menu")
root.geometry("600x800")

#create frames
fr_welcome=tk.Frame(root)
fr_login=tk.Frame(root)
fr_register=tk.Frame(root)
fr_menu=tk.Frame(root)

#use for loop to bring forward frames
for frame in (fr_welcome,fr_login,fr_register,fr_menu):
    frame.place(relwidth=1,relheight=1)

#function to show frame
def show_frame(frame):
    frame.tkraise()

#function for if login chosen
def login_chosen():
    student_id=login_id.get().strip()
    pswd=login_pswd.get().strip()
    if not student_id.isdigit() or len(student_id)!=5:
        messagebox.showerror(title="Error",message="Please enter your 5-number student ID.")
        return
    if pswd=="":
        messagebox.showerror(title="Error",message="Please enter your password.")
        return
    if v3Auth.user_login(student_id,pswd):
        messagebox.showinfo(title="Success",message="Login success!")
        login_id.delete(0, tk.END)#clears the entry box after button pressed
        login_pswd.delete(0, tk.END)
        show_frame(fr_menu)
    else:
        if v3Auth.find_acc(student_id):
            messagebox.showerror(title="Error",message="Incorrect password. Please try again.")
        else:
            messagebox.showerror(title="Error",message="This ID has not been registered.")

#function for if register chosen
def register_chosen():
    student_id=register_id.get().strip()
    pswd=register_pswd.get().strip()
    if not student_id.isdigit() or len(student_id)!=5:
        messagebox.showerror(title="Error",message="Please enter your 5-number student ID.")
        return
    if not pswd=="" or not pswd.isalnum():
        messagebox.showerror(title="Error",message="Please create your password containing only letters and numbers.")
        return
    if v3Auth.user_register(student_id,pswd):
        messagebox.showinfo(title="Success",message=f'You have been registered.\nYour password is "{pswd}".')
        register_id.delete(0, tk.END)#clears the entry box after button pressed
        register_pswd.delete(0, tk.END)
        show_frame(fr_menu)
    else:
        messagebox.showerror(title="Error",message="This ID has already been registered.\n\nPlease register with another ID, or go back and log in.")
    
#welcome page
tk.Label(fr_welcome,padx=20,pady=5,text="BDSC Café",font=("Arial",30,"bold")).pack()
tk.Label(fr_welcome,padx=20,pady=5,text="Do you have an existing account or would you like to register?").pack()
tk.Button(fr_welcome,text="Login",command=lambda:show_frame(fr_login)).pack()
tk.Button(fr_welcome,text="Register",command=lambda:show_frame(fr_register)).pack()

#login page
tk.Label(fr_login,padx=20,pady=5,text="Logging into BDSC Café menu",font=("Arial",20,"bold")).pack()
tk.Label(fr_login,padx=20,pady=5,text="Student ID:",font=("Arial",12)).pack()
login_id=tk.Entry(fr_login,font=("Arial",12))
login_id.pack()
tk.Label(fr_login,padx=20,pady=5,text="Password:",font=("Arial",12)).pack()
login_pswd=tk.Entry(fr_login,font=("Arial",12),show="*")
login_pswd.pack()

tk.Button(fr_login,text="Login",command=login_chosen).pack()
tk.Button(fr_login,text="Back",command=lambda:show_frame(fr_welcome)).pack()

#register page
tk.Label(fr_register,padx=20,pady=5,text="Registering into the BDSC Café menu",font=("Arial",20,"bold")).pack()
tk.Label(fr_register,padx=20,pady=5,text="Student ID:",font=("Arial",12)).pack()
register_id=tk.Entry(fr_register,font=("Arial",12))
register_id.pack()
tk.Label(fr_register,padx=20,pady=5,text="Create your password:",font=("Arial",12)).pack()
register_pswd=tk.Entry(fr_register,font=("Arial",12),show="*")
register_pswd.pack()

tk.Button(fr_register,text="Register",command=register_chosen).pack()
tk.Button(fr_register,text="Back",command=lambda:show_frame(fr_welcome)).pack()

#menu page
tk.Label(fr_menu,text="menu time!!",font=("Arial", 12)).pack()

tk.Button(fr_menu,text="Log out",command=lambda:show_frame(fr_welcome)).pack()

show_frame(fr_welcome)
root.mainloop()

#imports different modules and their functions
import sys#sys.exit() to exit program
import tkinter as tk#user interface using frames

def find_acc(student_id):#function that finds the user's inputted account in the external file, returns the password if found, returns false if not
    with open('studentID.txt', 'r') as file:#opens the studentID.txt external file, 'r' means it reads the text in the external file
        getid=file.read().splitlines()
        for line in getid:
            obtainedid,obtainedpswd=line.strip().split(';')
            if str(student_id)==obtainedid:
                return obtainedpswd
        return False

def write_pswd(student_id,pswd):
    with open ('studentID.txt', 'a')as file:#opens the studentID.txt external file, 'a' means it adds new text to the external file
        file.write(f'{student_id};{pswd}\n')

def user_login(ask_id,password):#function that user enters ID and password to login into the cafe menu
    obtainedpswd=find_acc(ask_id)
    if str(password)==obtainedpswd:
        return True
    return False

def user_register(register_id,password):
    existing_acc=find_acc(register_id)
    if existing_acc:#if ID found on the external file
        return False
    write_pswd(register_id,password)
    return True

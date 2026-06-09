#imports different modules and their functions
import sys#sys.exit() to exit program
from easygui import buttonbox, msgbox, enterbox#user interface
import v2UI#functions containing input/output

def find_acc(student_id):#function that finds the user's inputted account in the external file, returns the password if found, returns false if not
    with open('studentID.txt', 'r') as file:
        getid=file.read().splitlines()
        for line in getid:
            obtainedid,obtainedpswd=line.strip().split(';')
            if str(student_id)==obtainedid:
                return obtainedpswd
        return False

def write_pswd(student_id,pswd):
    with open ('studentID.txt', 'a')as file:#opens the studentID.txt external file, 'a' means it adds new text to the external file
        file.write(f'{student_id};{pswd}\n')
        v2UI.msg(f'\nYou have been registered.\nYour password is "{pswd}".')

def login():#function that user enters ID and password to login into the cafe menu
    while True:#loop where user enters their ID and checks if the user's ID is on the external file
        try:
            ask_id=v2UI.user_int('Please enter your student ID to login: ')
            if ask_id==None:
                return None
            elif len(str(ask_id))!=5:#checks if the input has 5 digits, the length of the BDSC student ID, by converting input into string
                v2UI.err_msg('Please enter your 5-number student ID.')
            else: 
                obtainedpswd=find_acc(ask_id)
                if obtainedpswd:#if ID found on the external file
                    while True:#loop where user enters their password and checks if password is in the external file under their ID and reprompts if not
                        password=v2UI.user_str('Please enter your password: ')
                        if password==None:
                            return None
                        elif password.isalnum():#checks if password contains any characters other than letters or numbers and proceeds if not
                            if str(password)==obtainedpswd:#if password equals the password on the file proceed, str() because IDs in the external file are strings and not integers
                                return obtainedpswd
                            else:#if password is incorrect
                                v2UI.err_msg('Incorrect password. Please try again.')
                        else:
                            v2UI.err_msg('Incorrect password. Please try again.')
                else:#if ID is not found on the external file
                    v2UI.err_msg('This ID has not been registered, please login with another ID or register.')
        except ValueError:#catches error when input contains characters that are not numbers
            v2UI.err_msg('Please enter your 5-number student ID.')

def register():
    while True:#loop where user enters their ID and checks if the user's ID is on the external file
        try:
            register_id=v2UI.user_int('Please enter your student ID to register: ')
            if register_id==None:
                return None
            elif len(str(register_id))!=5:#checks if the input has 5 digits, the length of the BDSC student ID, by converting input into string
                v2UI.err_msg('Please enter your 5-number student ID.')
            else:
                existing_acc=find_acc(register_id)
                if existing_acc:#if ID found on the external file
                    v2UI.err_msg('This ID has already been registered.\n\nPlease register with another ID, or press "Cancel" after the "OK" to choose login.')
                else:#if ID not found on external file
                    while True:#loop where user creates their password and reprompts if invalid input
                        password=v2UI.user_str('Please create a password: ')
                        if password==None:
                            return None
                        elif password.isalnum():#checks if password contains any characters other than letters or numbers and proceeds if not
                            write_pswd(register_id,password)
                            return password
                        else:
                            v2UI.err_msg('Please create your password containing only letters and numbers.')
        except ValueError:#catches error when input contains characters that are not numbers
            v2UI.err_msg('Please enter your 5-number student ID.')

#imports different modules and their functions
import sys#sys.exit() to end programs
from easygui import buttonbox, msgbox, enterbox#user interface

def msg(msg):#function for message
    msgbox(msg)

def err_msg(msg):#function for error message
    msgbox(msg)

def login_register(prompt):#function for buttons login, register and exit
    return buttonbox(prompt,choices=["Login","Register","Exit"])

def user_str(prompt):#function for user input (string)
    return enterbox(prompt)

def user_int(prompt):#function for user input (number)
    num=enterbox(prompt)
    if num==None:#if cancelled, user input is None
        return None
    return int(num)#num integer if not None

def yes_no(prompt):#function for buttons yes and no
    return buttonbox(prompt,choices=["Yes","No"])

def menu_choices(prompt):#function for buttons of menu items
    return buttonbox(prompt,choices=["Nachos",
                                     "Bottled Water",
                                     "Steamed Buns",
                                     "Noodles",
                                     "Hot Chocolate",
                                     "Brownie",
                                     "Pizza Bread",
                                     "Hash Brown",
                                     "Aloe Vera",
                                     "Garlic Bread"])

def remove(prompt,choices):#function for buttons of items in cart
    return buttonbox(prompt,choices=choices)

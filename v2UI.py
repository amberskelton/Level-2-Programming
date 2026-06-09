#imports different modules and their functions
import sys
from easygui import buttonbox, msgbox, enterbox#user interface

def msg(msg):
    msgbox(msg)

def err_msg(msg):
    msgbox(msg)

def login_register(prompt):
    return buttonbox(prompt,choices=["Login","Register","Exit"])

def user_str(prompt):
    return enterbox(prompt)

def user_int(prompt):
    num=enterbox(prompt)
    if num==None:
        return None
    return int(num)

def yes_no(prompt):
    return buttonbox(prompt,choices=["Yes","No"])

def menu_choices(prompt):
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

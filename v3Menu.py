#imports different modules and their functions
from datetime import datetime#gets the date

def dict_menu():#function containing a dictionary of the menu items as the keys and its price as the values
    return {
        'Food':{
            'Nachos':5.00,
            'Steamed Buns':4.00,
            'Noodles':4.00,
            'Brownie':3.80,
            'Pizza Bread':3.50,
            'Hash Brown':1.50,
            'Garlic Bread':2.50
            },
        'Drinks':{
            'Bottled Water':3.00,
            'Hot Chocolate':2.00,
            'Aloe Vera':5.00
            }
        }

def calculate_total(cart):#function that calculates the total price of all items in the cart
    total=0
    for item in cart:
        total+=(item[1]*item[2])
    return total

def write_invoice(cart):#function that specifically handles the ordered items part of the whole invoice
    total=calculate_total(cart)
    invoice=""#empty invoice
    for item in cart:
        invoice+=(f'{item[0]} ~ ${item[1]:.2f} x{item[2]}\n')
    return invoice,total

def save_order(student_id,invoice,total):#function that saves the user's invoice to ext file orderhistory along with the ID
    with open ('orderhistory.txt', 'a')as file:#opens the orderhistory.txt external file, 'a' means it adds new text to the external file
        invoice=invoice.replace('\n',', ')#replaces the '\n' in invoice to ', ' so \n doesn't break the lines in the external file
        date_time=datetime.now().strftime("%d/%m/%Y %H:%M")
        file.write(f'{student_id} ; {date_time} ; {invoice} ; ${total:.2f}\n')

def get_order_hist(student_id):#function that gets the order history of the user from the external file
    history=""
    with open ('orderhistory.txt', 'r')as file:#opens the orderhistory.txt external file, 'r' means it reads the text and does not edit it
        for line in file:#filters through every line in the order history file
            if f"{student_id} ;" in line:#if the current student id is in the file
                hist_parts=line.strip().split(";")#removes spaces and splits each part at the semicolon ;
                student_id=hist_parts[0].strip()
                date_time=hist_parts[1].strip()
                order=hist_parts[2].strip()
                total=hist_parts[3].strip()
                history+=(f"Date: {date_time}\nOrder: {order}\nTotal: {total}\n\n")
    return history

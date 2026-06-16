#imports different modules and their functions
import sys#sys.exit() to exit program
from easygui import buttonbox, msgbox, enterbox#user interface
import v2UI#functions containing input/output
import v2Auth#functions containing authentication (password)

def dict_menu():#function containing a dictionary of the menu items as the keys and its price as the values
    return {
        'Nachos':5.00,
        'Bottled Water':3.00,
        'Steamed Buns':4.00,
        'Noodles':4.00,
        'Hot Chocolate':2.00,
        'Brownie':3.80,
        'Pizza Bread':3.50,
        'Hash Brown':1.50,
        'Aloe Vera':5.00,
        'Garlic Bread':2.50
        }

def add_cart(cart,menu,chosen,quantity):#function that adds the user's selected item into the cart
    selected=menu[chosen]
    cart.append([chosen,menu[chosen],quantity])#adds a list of the menu item, its price and the quantity set by user into the cart
    return selected

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

def remove_cart(cart):#function that removes an item from the cart
    if len(cart)==0:#if there is nothing in the cart
        v2UI.msg('Your cart is empty.')
        return
    choices=[]
    for item in cart:
        choices.append(item[0])#adds the cart to the list choices=[] to remove
    remove_item=v2UI.remove('Select the item you would like to remove.',choices)
    for item in cart:
        if item[0]==remove_item:#if the item in the cart is the same as the user's selected
            try:
                qty_remove=v2UI.user_int(f'How many of this item ({remove_item}) would you like to remove?\nThere is currently {item[2]} in the cart.')
                if qty_remove==None:#if cancelled, user input is None
                    return None
                elif qty_remove<0:
                    v2UI.err_msg('Please enter a positive number.')
                elif qty_remove<item[2]:#if the quantity they want to remove is less than the quantity of that item
                    item[2]-=qty_remove#removes from the quantity
                elif qty_remove==item[2]:#if the quantity they want to remove is the same as the quantity of that item
                    cart.remove(item)#removes that item altogether from cart
                else:
                    v2UI.err_msg('You cannot remove more than what is in the cart.')
                break
            except ValueError:
                v2UI.err_msg('Please add a valid number.')

def save_order(student_id,invoice,total):#function that saves the user's invoice to ext file orderhistory along with the ID
    with open ('orderhistory.txt', 'a')as file:#opens the orderhistory.txt external file, 'a' means it adds new text to the external file
        invoice=invoice.replace('\n',', ')#replaces the '\n' in invoice to ', ' so \n doesn't break the lines in the external file
        file.write(f'{student_id} ; {invoice} ; ${total:.2f}\n')
        
def payment(cart,student_id,obtainedpswd):#function containing payment process
    invoice,total=write_invoice(cart)
    v2UI.msg('Invoice\n\n'f'ID: {student_id}\n\n'
             f'Order:\n{invoice}\n'
             f'Total: ${total:.2f}')
    while True:#loop that asks user if they want to remove from cart
        remove=v2UI.yes_no('Would you like to remove something from the cart?')
        if remove=='Yes':
            remove_cart(cart)
            invoice,total=write_invoice(cart)
            v2UI.msg('Invoice\n\n'f'ID: {student_id}\n\n'
             f'Order:\n{invoice}\n'
             f'Total: ${total:.2f}')
        elif remove=='No':
            while True:#loop that asks the user if they want confirm their order
                confirm=v2UI.yes_no('Confirm order?')
                if confirm=='Yes':
                    while True:#loop that ensures the user enters the correct password to pay
                        pay=v2UI.user_str('Please enter your password to make the payment:')
                        if pay==None:#if cancelled, user input is None
                            break
                        elif pay!=obtainedpswd:#if the input does not equal the user's stored password
                            v2UI.msg('Incorrect password. Please try again.')
                        elif pay==obtainedpswd:#if the input equals the user's stored password
                            save_order(student_id,invoice,total)
                            v2UI.msg('Payment complete! Please pick up your order at the cafe.')
                            sys.exit()
                elif confirm=='No':
                    return#ends function

def cafeMenu(student_id,obtainedpswd):#function containing the menu process
    cart=[]#empty list as cart is currently empty
    menu=dict_menu()
    while True:#loop that asks the user what they want to add to the cart from menu
        menu_text=('-----------------\nBDSC Cafe Menu:\n-----------------\nItem ~ Price\n-----------------\n')
        for item,price in menu.items():#displays the menu
            menu_text+=(f'{item} ~ ${price:.2f}\n')
        menu_text+=('\nWhat would you like to order from the menu?')
        chosen=v2UI.menu_choices(menu_text)
        while True:#loop that asks the user the quantity of the item they want to add to the cart
            try:
                quantity=v2UI.user_int(f'How many of this item ({chosen}) would you like to order?')
                if quantity==None:#if cancelled, user input is None
                    return None
                elif quantity<=0 or quantity>10:#if input is 0 or lower or 10 or higher (daily cafe stock)
                    v2UI.err_msg('Please enter a quantity greater than 0 and below 10.')
                else:
                    selected=add_cart(cart,menu,chosen,quantity)
                    v2UI.msg(f'{quantity} {chosen} for ${selected*quantity:.2f} was added to the cart!')
                    order_text=('Would you like to add another item to the cart?')
                    while True:#loop that asks the user if they want to order again
                        again=v2UI.yes_no(order_text)
                        if again=='Yes':
                            break
                        elif again=='No':
                            payment(cart,student_id,obtainedpswd)
                    break#if they want to order again this breaks out of the quantity loop and brings user to the menu loop
            except ValueError:#catches invalid input
                v2UI.err_msg('Please enter a number for the quantity of the item you want to order.')

#imports different modules and their functions
import sys#sys.exit() to exit program
from easygui import buttonbox, msgbox, enterbox#user interface
import v2UI#functions containing input/output
import v2Auth#functions containing authentication (password)

def dict_menu():
    #dictionary containing id numbers of the menu items as the key and its value is a list containing the menu item and its corresponding price
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

def add_cart(cart,menu,chosen):
    selected=menu[chosen]#stores the chosen menu item under the selected variable
    cart.append([chosen,menu[chosen]])#adds a list of the menu item and its price into the cart
    return selected

def calculate_total(cart):
    total=0
    for item in cart:
        total+=item[1]
    return total

def cafeMenu(student_id,obtainedpswd):
    cart=[]#empty list as cart is currently empty
    menu=dict_menu()
    while True:#loop that asks the user what they want to add to the cart
        menu_text=('-----------------\nBDSC Cafe Menu:\n-----------------\nItem ~ Price\n-----------------\n')
        for item,price in menu.items():#displays the menu
            menu_text+=(f'{item} ~ ${price:.2f}\n')
        menu_text+=('\nWhat would you like to order from the menu?')
        chosen=v2UI.menu_choices(menu_text)
        selected=add_cart(cart,menu,chosen)
        order_text=(f'{chosen} for ${selected:.2f} was added to the cart!\n'
                    '\nWould you like to add another item to the cart?')
        while True:
            again=v2UI.yes_no(order_text)
            if again=='Yes':
                break
            elif again=='No':
                total=calculate_total(cart)
                invoice=""
                for item in cart:
                    invoice+=(f'{item[0]} ~ ${item[1]:.2f}\n')
                v2UI.msg('Invoice\n\n'f'ID: {student_id}\n\n'
                         f'Order:\n{invoice}\n'
                         f'Total: ${total:.2f}')
                while True:#loop that asks the user if they want confirm their order
                    confirm=v2UI.yes_no('Confirm order?')
                    if confirm=='Yes':
                        while True:#loop that ensures the user enters the correct password to pay
                            pay=v2UI.user_str('Please enter your password to make the payment:')
                            if pay==None:
                                break
                            elif pay!=obtainedpswd:#if the input does not equal the user's stored password
                                v2UI.msg('Incorrect password. Please try again.')
                            elif pay==obtainedpswd:#if the input equals the user's stored password
                                v2UI.msg('Payment complete! Please pick up your order at the cafe.')
                                sys.exit()
                    elif confirm=='No':
                        break

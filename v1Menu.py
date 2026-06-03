import sys#sys.exit() to exit the program

def cafeMenu(obtainedpswd):#function to display menu, add items to cart and pay using password
    cart=[]#empty list as cart is currently empty
    #dictionary containing id numbers of the menu items as the key and its value is a list containing the menu item and its corresponding price
    menu={
        1:['Nachos',5.00],
        2:['Bottled Water',3.00],
        3:['Steamed Buns',4.00],
        4:['Noodles',4.00],
        5:['Hot Chocolate',2.00],
        6:['Brownie',3.80],
        7:['Pizza Bread',3.50],
        8:['Hash Brown',1.50],
        9:['Aloe Vera',5.00],
        10:['Garlic Bread',2.50]
        }
    print('-----------------------')
    print('BDSC Cafe Menu:')
    print('-----------------------')
    print('ID Number. Item ~ Price')
    print('-----------------------')
    for number,item in menu.items():#displays the menu
        print(f'{number}. {item[0]} ~ ${item[1]:.2f}')#item[0] is the food item, item[1] is the price of the corresponding food item, ':.2f'sets the decimal place of the prices to 2d.p.
    while True:#loop that asks the user what they want to add to the cart
        try:
            print('------------------------------------------------------------------------')
            chosen=int(input('What would you like to add to cart?\nPlease enter the ID number of the item you would like to order: '))
            if chosen not in menu:#if the input from the user is not on the menu, e.g. a non-existent id number, reprompts user
                print('------------------------------------------------------------------------')
                print('Please enter the ID number of the item you would like to order from the menu.')
            else:
                selected=menu[chosen]#stores the chosen menu item under the selected variable
                cart.append(menu[chosen])#adds the chosen menu item to the cart
                print(f'{selected[0]} for ${selected[1]:.2f} added to cart!')
                while True:#loop that asks the user if they want to add another item to the cart once they add an item to cart
                    print('------------------------------------------------------------------------')
                    again=input('Would you like to add another item to the cart?\nPlease enter "yes" or "no": ')
                    if again.lower()=='yes':
                        break
                    elif again.lower()=='no':
                        print('------------------------------------------------------------------------')
                        print('Invoice:')
                        total=0
                        for item in cart:#each item in the cart is a list containing the food item and its price
                            total+=item[1]#item[1] is the price in each list as the index number of the price is 1, so this adds all the prices in the cart to the total
                            print(f'{item[0]} ~ ${item[1]:.2f}')
                        print(f'Total: ${total:.2f}')
                        while True:#loop that asks the user if they want confirm their order
                            print('------------------------------------------------------------------------')
                            confirm=input('Confirm order?\nPlease enter "yes" or "no": ')
                            if confirm.lower()=='yes':
                                while True:#loop that ensures the user enters the correct password to pay
                                    print('------------------------------------------------------------------------')
                                    pay=input('Please enter your password to make the payment: ')
                                    if pay!=obtainedpswd:#if the input does not equal the user's stored password
                                        print('------------------------------------------------------------------------')
                                        print('Incorrect password. Please try again.')
                                    elif pay==obtainedpswd:#if the input equals the user's stored password
                                        print('------------------------------------------------------------------------')
                                        print('Payment complete! Please pick up your order at the cafe.')
                                        sys.exit()#exits the program
                            elif confirm.lower()=='no':#breaks out of the confirm order loop and returns to the loop that asks the user if they want to add to cart
                                break
                            else:
                                print('------------------------------------------------------------------------')
                                print('Please enter either "yes" or "no".')
                    else:
                        print('------------------------------------------------------------------------')
                        print('Please enter either "yes" or "no".')
                if again.lower()=='no':
                    break
        except ValueError:#handles invalid input from user (str,floats,None)
            print('------------------------------------------------------------------------')
            print('Please enter the ID number of the item you would like to order.')

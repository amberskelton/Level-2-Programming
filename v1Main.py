import sys

def menuProgram():
    while True:
        try:
            print('------------------------------------------------------------------------')
            ask_acc=int(input("Do you have an existing account or would you like to register?\nEnter '1' if you have an existing account\nEnter '2' if you would like to register\nEnter: "))
            if ask_acc==1:
                while True:
                    try:
                        print('------------------------------------------------------------------------')
                        ask_id=int(input("Please enter your student ID to login: "))
                        if len(str(ask_id))!=5:#checks if the input has 5 digits, the length of the BDSC student ID, by converting input into string
                            print('------------------------------------------------------------------------')
                            print('Please enter your student ID in 5 digits.')
                        else:
                            with open('studentID.txt', 'r') as file:
                                getid=file.read().splitlines()#separates each line in the external file
                                existing=False
                                for line in getid:
                                    obtainedid,obtainedpswd=line.strip().split(';')#splits the line e.g."33333;password", into '33333' and 'password'
                                    if str(ask_id)==obtainedid:#str() because IDs in the external file are strings and not integers
                                        existing=True
                                        break
                                if existing==True:
                                    while True:
                                        print('------------------------------------------------------------------------')
                                        password=input("Please enter your password: ")
                                        if password.isalnum():#checks if password contains any characters other than letters or numbers and proceeds if not
                                            if str(password)==obtainedpswd:#str() because IDs in the external file are strings and not integers
                                                existing=True
                                                print('menu')
                                                break
                                            else:
                                                print('------------------------------------------------------------------------')
                                                print('Incorrect password. Please try again.')
                                        else:
                                            print('------------------------------------------------------------------------')
                                            print('Please enter your password containing only letters and numbers.')
                                elif existing==False:
                                    print('------------------------------------------------------------------------')
                                    print('This ID has not been registered, please login with another ID or register.')
                                    break
                            break
                    except ValueError:#catches error when input contains characters that are not numbers
                        print('------------------------------------------------------------------------')
                        print('Please enter your student ID in 5 numbers.')
            elif ask_acc==2:
                while True:  
                    try:
                        print('------------------------------------------------------------------------')
                        register=int(input("Please enter your student ID to register: "))
                        if len(str(register))!=5:#checks if the input has 5 digits, the length of the BDSC student ID, by converting input into string
                            print('------------------------------------------------------------------------')
                            print('Please enter your student ID in 5 digits.')
                        else:
                            with open('studentID.txt', 'r') as file:
                                getid=file.read().splitlines()#separates each line in the external file
                                existing=False
                                for line in getid:
                                    obtainedid,obtainedpswd=line.strip().split(';')#splits the line e.g."33333;password", into '33333' and 'password'
                                    if str(register)==obtainedid:#str() because IDs in the external file are strings and not integers
                                        existing=True
                                        break
                                if existing==True:
                                    print('------------------------------------------------------------------------')
                                    print('This ID has already been registered.\nPlease login with this ID.')
                                    break
                                elif existing==False:
                                    while True:
                                        password=input("Please create a password: ")
                                        if password.isalnum():#checks if password contains any characters other than letters or numbers and proceeds if not
                                            with open ('studentID.txt', 'a')as file:
                                                file.write(f'{register};{password}\n')
                                            print(f'\nYou have been registered.\nYour password is "{password}".')
                                            print('------------------------------------------------------------------------')
                                            print('menu')
                                            break
                                        else:
                                            print('------------------------------------------------------------------------')
                                            print('Please create a password containing only letters and numbers.')
                                    break
                    except ValueError:#catches error when input contains characters that are not numbers
                        print('------------------------------------------------------------------------')
                        print('Please enter your student ID in 5 numbers.')
            else:
                print('------------------------------------------------------------------------')
                print('Please enter either "1" to login or "2" to register.')
        except ValueError:
            print('------------------------------------------------------------------------')
            print('Please enter either "1" to login or "2" to register.')
        
menuProgram()

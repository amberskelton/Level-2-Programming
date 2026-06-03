import sys#sys.exit() 
import v1Menu#imports the menu function from the other module

def menuProgram():#function to display the program, which contains the login/register and then calls the menu function from v1Menu
    while True:#loop that ensures the user goes under an existing account or registers their student ID
        try:
            print('------------------------------------------------------------------------')
            ask_acc=int(input("Do you have an existing account or would you like to register?\nEnter '1' if you have an existing account\nEnter '2' if you would like to register\nEnter: "))
            if ask_acc==1:#if existing account
                while True:#loop where user enters their ID and checks if the user's ID is on the external file
                    try:
                        print('------------------------------------------------------------------------')
                        ask_id=int(input("Please enter your student ID to login: "))
                        if len(str(ask_id))!=5:#checks if the input has 5 digits, the length of the BDSC student ID, by converting input into string
                            print('------------------------------------------------------------------------')
                            print('Please enter your student ID in 5 digits.')
                        else:
                            with open('studentID.txt', 'r') as file:#opens the studentID.txt external file, 'r' reads the file and does not edit it
                                getid=file.read().splitlines()#separates each line in the external file
                                existing=False#default sets the variable to false as in ID not in file
                                for line in getid:#for each line in the amount of lines in the external file
                                    obtainedid,obtainedpswd=line.strip().split(';')#splits the line e.g."33333;password", into '33333' and 'password'
                                    if str(ask_id)==obtainedid:#str() because IDs in the external file are strings and not integers
                                        existing=True#sets the variable to true meaning the ID is in the file
                                        break
                                if existing==True:#if ID found on the external file
                                    while True:#loop where user enters their password and checks if password is in the external file under their ID and reprompts if not
                                        print('------------------------------------------------------------------------')
                                        password=input("Please enter your password: ")
                                        if password.isalnum():#checks if password contains any characters other than letters or numbers and proceeds if not
                                            if str(password)==obtainedpswd:#if password equals the password on the file proceed, str() because IDs in the external file are strings and not integers
                                                existing=True#sets the variable to true meaning the password is in the file
                                                v1Menu.cafeMenu(obtainedpswd)#runs the cafeMenu function imported from v1Menu
                                                break
                                            else:#if password is incorrect
                                                print('------------------------------------------------------------------------')
                                                print('Incorrect password. Please try again.')
                                        else:
                                            print('------------------------------------------------------------------------')
                                            print('Please enter your password containing only letters and numbers.')
                                elif existing==False:#if ID is not found on the external file
                                    print('------------------------------------------------------------------------')
                                    print('This ID has not been registered, please login with another ID or register.')
                                    break
                            break
                    except ValueError:#catches error when input contains characters that are not numbers
                        print('------------------------------------------------------------------------')
                        print('Please enter your student ID in 5 numbers.')
            elif ask_acc==2:#if registering
                while True:#loop where user enters their ID and checks if the user's ID is on the external file, if so, redirects them back to login, if not, prompts them to create password and writes ID and password to the studentID.txt external file
                    try:
                        print('------------------------------------------------------------------------')
                        register=int(input("Please enter your student ID to register: "))
                        if len(str(register))!=5:#checks if the input has 5 digits, the length of the BDSC student ID, by converting input into string
                            print('------------------------------------------------------------------------')
                            print('Please enter your student ID in 5 digits.')
                        else:
                            with open('studentID.txt', 'r') as file:#opens the studentID.txt external file, 'r' reads the file and does not edit it
                                getid=file.read().splitlines()#separates each line in the external file
                                existing=False#default sets the variable to false as in ID not in file
                                for line in getid:#for each line in the amount of lines in the external file
                                    obtainedid,obtainedpswd=line.strip().split(';')#splits the line e.g."33333;password", into '33333' and 'password'
                                    if str(register)==obtainedid:#str() because IDs in the external file are strings and not integers
                                        existing=True#sets the variable to true meaning the ID is in the file
                                        break
                                if existing==True:#if ID found on external file
                                    print('------------------------------------------------------------------------')
                                    print('This ID has already been registered.\nPlease login with this ID.')
                                    break
                                elif existing==False:#if ID not found on external file
                                    while True:#loop that asks the user to create a password with only letters and numbers and writes it to the external file along with the ID
                                        password=input("Please create a password: ")
                                        if password.isalnum():#checks if password contains any characters other than letters or numbers and proceeds if not
                                            with open ('studentID.txt', 'a')as file:#opens the studentID.txt external file, 'a' means it adds new text to the external file
                                                file.write(f'{register};{password}\n')
                                            print(f'\nYou have been registered.\nYour password is "{password}".')
                                            v1Menu.cafeMenu(password)#runs the cafeMenu function imported from v1Menu
                                            break
                                        else:#catches error when input is invalid
                                            print('------------------------------------------------------------------------')
                                            print('Please create a password containing only letters and numbers.')
                                    break
                    except ValueError:#catches error when input contains characters that are not numbers
                        print('------------------------------------------------------------------------')
                        print('Please enter your student ID in 5 numbers.')
            else:#catches error when input is not 1 or 2
                print('------------------------------------------------------------------------')
                print('Please enter either "1" to login or "2" to register.')
        except ValueError:#catches error when input is not 1 or 2
            print('------------------------------------------------------------------------')
            print('Please enter either "1" to login or "2" to register.')
        
menuProgram()#runs the program

import sys
from Menu import *
from database import Database as db


def login_option():
    print('''
           Choose a option:
           
           1 - New User
           2 - Login
           3 - Forget Password
           4 - Exit App''')

    option = int(input('>: '))

    if option not in (1, 2, 3, 4):
        print('Invalid Option.')
        option = int(input('Try again >: '))

    # Register new user
    if option == 1:
        name = input('Enter a Name: ')
        username = input('Enter a Username: ')
        email = input('Enter a Email: ')
        cpf = int(input('Enter a CPF (Only numbers): '))
        password = getpass.getpass(prompt='Enter a Password: ')
        confirm_password = getpass.getpass(prompt='Confirm Password: ')

        if password != confirm_password:
            while True:
                print('Passwords do not match. Try again.')
                password = getpass.getpass(prompt='Enter a Password: ')
                confirm_password = getpass.getpass(prompt='Confirm Password: ')
                if password == confirm_password:
                    break

        # Consult if username already exist in Users table
        consult = db.consult_user(username)

        if consult == 0:
            insert_user = db.insert_table(name, username, email, cpf, password)

            if insert_user == 0:
                print('Successfully registered user')
                login_option()
            elif insert_user == 1:
                print('Error inserting record --> def insert_Table')

        else:
            print('Username already registered. ')
            login_option()

    # Logon System
    if option == 2:
        username = input('Enter Username: ')
        password = getpass.getpass(prompt='Enter a Password: ')

        consult_user_login, id_user = db.consult_login(username, password)

        if consult_user_login == 0:
            print('Login Successful')
            main_menu(id_user)

        else:
            print('*** Username or password incorrect ***')
            login_option()

    # Forget password
    if option == 3:
        email = input('Enter you email: ')
        consul_email = db.consult_email(email)

        if consul_email == 0:
            consul_password = db.consult_password(email)
            send_password = db.forget_password(email, consul_password)
            print(send_password)
        else:
            print('Email not exist.')

        login_option()

    # Exit program
    if option == 4:
        print('Goodbye. See you...')
        sys.exit()


login_option()



# Add, list or remove ingredients of recipe
def menu_ingrediente(id_receita, id_usuario):
    while True:
        print('''
            Choose a option:

            1 - List ingredient
            2 - Add ingredient
            3 - Remove ingredient
            4 - Start the recipe
            5 - Main menu
            6 - Exit app ''')

        option = int(input('>: '))
        print(' ')

        if option not in (1, 2, 3, 4, 5, 6):
            print('Invalid Option.')
            option = int(input('Try again >: '))

        # List Ingredients
        if option == 1:
            list = list_ingredient(recipeid)

            for ingredient in list:
                print(f'Ingredient: {ingredient[1]} - Qtd: {ingredient[2]}')

            print(' ')
            menu = input('Press Enter to back Menu..')

        # Add Ingredients
        if option == 2:
            add = add_ingredient(recipeid, userid)

            if add == 0:
                print('ingredient successfully inserted')
            else:
                print('error inserting ingredient')

        # Remove Ingredients
        if option == 3:
            ingred = list_ingredient(recipeid)

            for line in ingred:
                print(line)

            ingredid = input('Enter ID the ingredient: ')
            remove = remove_ingredient(ingredid)

            if remove == 0:
                print('Ingredient successfully deleted')
            else:
                print('Error deleting ingredient')

        # Start Recipe
        if option == 4:
            start_recipe(userid, recipeid)

        # Call Main Menu
        if option == 5:
            main_menu(userid)

        # Exit app
        if option == 6:
            print('Thaks for use our app. Goodbye..')
            sys.exit()
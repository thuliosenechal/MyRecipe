import sqlite3
import sys
from defRecipe import *
from defIngredient import *


conn = sqlite3.connect('MinhaReceita.db')
cursor = conn.cursor()

# Add, list or remove ingredients of recipe
def menu_ingredients(recipeid, userid):
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


def main_menu(userid):
    while True:
        print('''
            Choose a option:

            1 - List Recipe 
            2 - Add Recipe
            3 - Remove Recipe
            4 - Select Recipe
            5 - Supermarket List
            6 - Exit app ''')

        option = int(input('>: '))
        print(' ')

        if option not in (1, 2, 3, 4, 5, 6):
            print('Invalid Option.')
            option = int(input('Try again >: '))

        # List Recipes
        if option == 1:
            list = list_recipe(userid)
            for recipe in list:
                print(f'\t - {recipe[1]}')

            print(' ')
            menu = input('Press Enter to back Menu..')

        # Add Recipes
        if option == 2:
            add = add_recipe(userid)

            if add == 0:
                    print('successfully added recipe')
            else:
                print('error added recipe')

        # Remove Recipes
        if option == 3:
            list = list_recipe(userid)

            for line in list:
                print(line)

            recipeid = input('Enter ID the recipe: ')
            remove = remove_recipe(recipeid)

            if remove == 0:
                print('recipe successfully deleted')
            else:
                print('error deleting recipe')

        # List recipes and call ingredients
        if option == 4:
            recipes = list_recipe(userid)
            for recipe in recipes:
                print(f'ID: {recipe[0]} - {recipe[1]}')
            print(' ')

            recipeid = input('Enter ID the recipe: ')
            menu_ingredients(recipeid, userid)

        # Supermarket List
        if option == 5:
            list = list_supermarket(userid)

            for ingredient in list:
                print(f'Ingredient: {ingredient[1]} / Qtd: {ingredient[2]}')

            print(' ')
            input('Press Enter to back Menu..')

        # Exit app
        if option == 6:
            print('Thanks for use our app. Goodbye..')
            sys.exit()

if __name__ == '__main__':
    userid = 7
    main_menu(userid)



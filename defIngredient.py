import sqlite3


conn = sqlite3.connect('MinhaReceita.db')
cursor = conn.cursor()


def list_supermarket(userid):
    cursor.execute('SELECT ID, NAME, QTD FROM SupermarketList WHERE UserID = ?', (userid,))

    list = cursor.fetchall()

    return list

def list_ingredient(recipeid):
    cursor.execute('SELECT ID, NAME, QTD FROM Ingredient WHERE RecipeID = ?', (recipeid,))

    list = cursor.fetchall()

    return list

def add_supermarket(userid, ingredid, name, qtd):
    msgcode = 0

    try:
        cursor.execute("""
                        INSERT INTO SupermarketList (IngredientID, UserID, Name, Qtd, ItemPurchased)
                        VALUES (?, ?, ?, ?, ?)""", (ingredid, userid, name, qtd, 1))

        conn.commit()

    except sqlite3.Error as e:
        print('An error occurred: ', e.args[0])
        msgcode = 1

    return msgcode


def add_ingredient(recipeid, userid):
    name = input('Enter an ingredient to add in your recipe: ').lower().title()
    qtd = int(input(f'Enter a quantity of {name}: '))
    msgcode = 0

    try:
        cursor.execute("""
                                     INSERT INTO Ingredient (Name, RecipeID, UserID, Qtd) 
                                     VALUES (?, ?, ?, ?)""", (name, recipeid, userid, qtd))

        conn.commit()

    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        msgcode = 1

    return msgcode


def remove_ingredient(ingredid):
    msgcode = 0
    try:
        cursor.execute("""
                                         DELETE FROM Ingredient WHERE ID = ? 
                                         """, (ingredid,))

        conn.commit()

    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        msgcode = 1

    return msgcode


def start_recipe(userid, recipeid):
    count = 0

    list = list_ingredient(recipeid)

    for ingredient in list:
        ingred = input(f'Do you have {ingredient[1]}? Y or N? ').lower()

        if ingred not in ('n', 'y'):
            while True:
                print('\nInvalid Option')
                ingred = input('\nAnswer Only "(Y)es" or "(N)o": ')
                if ingred in ('n', 'y'):
                    break

        if ingred == 'n':
            count = count + 1

            print(f"\nDo you want to add {ingredient[1]} in your supermarket list? (Y)es or (N)o ")
            resp = input().lower()

            if resp == 'y':
                add = add_supermarket(userid, ingredient[0], ingredient[1], ingredient[2])

                if add == 0:
                    print(f'{ingredient[1]} added in Supermarket List successfuly')
                else:
                    print(f'Error added {ingredient[1]} in supermarket list')
            else:
                continue
        else:
            print(f'\nAdding {ingredient[1]} in your basket.')
            add = input('\nPress ENTER if added ingredient.')

            if add == '':
                pass

    if count > 0:
        print(f'\n{count} ingredients left to complete the recipe. Would you like to see them? (Y)es or (N)o: ')
        resp = input().lower()

        if resp == 'y':
            list = list_supermarket(userid)

            for ingred in list:
                print(f'Ingredient: {ingred[1]} / Qtd {ingred[2]}')

            print(' ')
            print('\nBuy the all ingredients and return to app. See you soon!!!')
        else:
            print('\nbye bye!!!')

    else:
        print(f'\nCongratulations. Can you start your recipe now.')



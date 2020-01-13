import sqlite3

conn = sqlite3.connect('MinhaReceita.db')
cursor = conn.cursor()


def list_recipe(userid):
    cursor.execute('SELECT ID, NAME FROM Recipe WHERE UserID = ?', (userid,))

    list = cursor.fetchall()

    return list


def add_recipe(userid):
    name = input('Enter a name for your recipe: ').title()
    msgcode = 0
    try:
        cursor.execute("""
                                 INSERT INTO Recipe (Name, UserID) 
                                 VALUES (?, ?)""", (name, userid))

        conn.commit()

    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        msgcode = 1

    return msgcode


def remove_recipe(recipeid):
    msgcode = 0
    try:
        cursor.execute("""
                                     DELETE FROM Recipe WHERE ID = ? 
                                     """, (recipeid,))

        conn.commit()

    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        msgcode = 1

    return msgcode


def list_supermarket(userid):
    cursor.execute('SELECT ID, NAME FROM SupermarketList WHERE UserID = ? and ItemPurchased = 0', (userid,))

    ingred = cursor.fetchall()

    return ingred


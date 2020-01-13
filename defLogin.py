import sqlite3
import getpass
import smtplib

from email.mime.text import MIMEText

conn = sqlite3.connect('MinhaReceita.db')
cursor = conn.cursor()

# Consult if username and password are correct
def consult_login(username, password):
    msgcode = 0
    cursor.execute('SELECT count(1), ID FROM Users WHERE username = ? and password = ?', (username, password,))

    record = cursor.fetchone()
    count = record[0]
    iduser = record[1]

    if count == 0:
        msgcode = 1
        iduser = 0
        return msgcode, iduser
    return msgcode, iduser


# Consult if email exist
def consult_email(email):
    msgcode = 0
    cursor.execute('SELECT count(1) FROM Users WHERE Email = ?', (email,))

    count = cursor.fetchone()[0]

    if count == 0:
        msgcode = 1
        return msgcode
    return msgcode


# Consult password to send an email to user
def consult_password(email):
    cursor.execute('SELECT Password FROM Users WHERE Email = ? ', (email,))

    pwd = cursor.fetchone()[0]
    return pwd


# Send email to user with password
def forget_password(email, pwd):
    # connection with servers google
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465

    # Username and email to login in mail server
    username = 'email' # insert your gmail email
    password = 'password' # insert your password mail

    from_addr = 'email' # insert your gmail email
    to_addrs = email

    # Only text
    message = MIMEText(f'Your password is {pwd}')
    message['subject'] = 'Password forget MinhaReceita app'
    message['from'] = from_addr
    message['to'] = to_addrs

    # Secure connection using SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # To interage with an external server we need login him
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()

    msg = 'We sent you an email with your password'

    return msg

# Consult if username already exist in table Users
def consult_user(username):
    msgcode = 0
    cursor.execute('SELECT count(1) FROM Users WHERE username = ?', (username,))

    count = cursor.fetchone()[0]

    if count > 0:
        msgcode = 1

    return msgcode


# Register user data in Users table
def insert_table(name, username, email, cpf, password):
    msgcode = 0
    try:
        cursor.execute("""
                             INSERT INTO Users (name, username, email, cpf, password) 
                             VALUES (?, ?, ?, ?, ?)""", (name, username, email, cpf, password))

        conn.commit()

    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        msgcode = 1

    return msgcode
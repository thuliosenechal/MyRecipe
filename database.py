import sqlite3
import smtplib
import os.path
from time import sleep
from email.mime.text import MIMEText
import query_banco as query


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "MinhaReceita.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

class Database():
    
    def consulta_login(self, usuario, senha):
        # Verifica se usuario e senha estao corretos
        cursor.execute(query.consulta_usuario_senha, (usuario, senha,))

        record = cursor.fetchone()
        count = record[0]
        id_usuario = record[1]

        if count == 0:
            print('\n*** Usuário e/ou senha incorretos ***')
            from menu_login import login_option
            login_option()
        
        menu_receita(id_usuario)

    def consulta_email(self, email):
        # Consult if email exist
        msgcode = 0
        cursor.execute(query.consulta_email, (email,))

        count = cursor.fetchone()[0]

        if count == 0:
            print('\n***Email não cadastrado***')
            sleep(1.5)
            from menu_login import login_option
            login_option()
        
        pega_senha = consulta_senha(email)
        recupera_senha(email, pega_senha)
        
    def consulta_senha(self, email):
        # Consult password to send an email to user
        cursor.execute(query.recupera_senha, (email,))

        senha = cursor.fetchone()[0]
        return senha

    def recupera_senha(self, email, senha_usuario):

        smtp_ssl_host = 'smtp.gmail.com'
        smtp_ssl_port = 465

        # Username and email to login in mail server
        usuario_email = 'email' # insert your gmail email
        senha = 'password' # insert your password mail

        from_addr = 'email' # insert your gmail email
        to_addrs = email

        # Only text
        message = MIMEText(f'Sua senha é: {senha_usuario}')
        message['subject'] = 'Recuperação de senha do app MinhaReceita'
        message['from'] = from_addr
        message['to'] = to_addrs

        # Secure connection using SSL
        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        # To interage with an external server we need login him
        server.login(usuario_email, senha)
        server.sendmail(from_addr, to_addrs, message.as_string())
        server.quit()

        print('\nEnviamos a sua senha para o email cadastrado')

    def consulta_usuario(self, usuario):
        # Consulta se o usuário já existe na base de dados
        cursor.execute(query.consulta_usuario, (usuario,))
        count = cursor.fetchone()[0]

        if count > 0:
            return 1
        return 0

    def insere_usuario(self, nome, usuario, email, cpf, senha):
        
        try:
            cursor.execute(query.insere_usuario_banco, 
            (nome, usuario, email, cpf, senha))

            conn.commit()
        except sqlite3.Error as e:
            print('Ocorreu um erro:', e.args[0])
            print('Por favor, contactar o administrador do sistema')
            from menu_login import login_option
            login_option()

        print('\nUsuário cadastrado com sucesso.')
        from menu_login import login_option
        login_option()

    def listar_receita(self, id_usuario):
        cursor.execute(query.listar_receitas, (id_usuario,))

        receitas = cursor.fetchall()
        return receitas

    def adicionar_receita(self, nome, id_usuario):
        try:
            cursor.execute(query.adicionar_receita, (nome, id_usuario))
            conn.commit()

        except sqlite3.Error as e:
            msg = ("Ocorreu um erro ao adicionar a receita: ", e.args[0])
            return msg

        msg = 'Receita adicionada com sucesso.'    
        return msg

    def deletar_receita(self, id_receita):
        try:
            cursor.execute(query.deletar_receita, (id_receita,))
            conn.commit()

        except sqlite3.Error as e:
            msg = ("Ocorreu um erro ao deletar a receita: ", e.args[0])
            return msg

        msg = 'Receita deletada com sucesso'
        return msg
        
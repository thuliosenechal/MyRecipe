import sys
from time import sleep
import getpass
import database
import menu_receita


db = database.Database()

class Usuario():
    
    def cadastrar_novo_usuario(self):

        usuario = input('\nEntre com um usuário: ')
        valida_usuario = self.valida_se_usuario_existe(usuario)
        
        if valida_usuario == 0:
            nome = input('Nome completo: ')
            email = input('Email: ')
            cpf = int(input('CPF (Somente números): '))
            senha = getpass.getpass(prompt='Entre com a Senha: ')
            confirma_senha = getpass.getpass(prompt='Confirme a senha: ')

            while senha != confirma_senha:
                print('\nSenha e confirmação de senha diferentes.\n')
                senha = getpass.getpass(prompt='Entre com a senha: ')
                confirma_senha = getpass.getpass(prompt='Confirme a senha: ')
        
            insere_usuario_banco = db.insere_usuario(nome, usuario, email, cpf, senha)

    def valida_se_usuario_existe(self, usuario):
        consulta_usuario = db.consulta_usuario(usuario)

        if consulta_usuario == 0:
            return 0
        print('\nUsuário já cadastrado.')
        sleep(1.5)
        from menu_login import login_option
        login_option()

    def logar_sistema(self):
        usuario = input('\nUsuário: ')
        senha = getpass.getpass(prompt='Senha: ')
        #senha = input('Senha: ')
        db.consulta_login(usuario, senha)

    def recuperar_senha_esquecida(self):
        email = input('\nInsira seu email: ')
        consulta_email = db.consulta_email(email)

    def sair_programa(self):
        print('\nSaindo do programa...')
        time.sleep(1.5)
        sys.exit()

        
        
from time import sleep
from database import Database as db
from menu_receita import *
from menu_ingrediente import *


class Receita():

    def __init__(self, id_usuario):
        self.id_usuario = id_usuario

    def listar_receita(self):
        receitas = db.listar_receita(self.id_usuario)

        for receita in receitas:
            print(f'\t - {receita[1]}')
            print(' ')

        opcao_usuario = int(input('''1 - Retornar ao menu de receitas 
                                     2 - Selecionar uma receita
                                     
                                     >: '''))
        if opcao_usuario == 2:
            id_receita = int(input('Informe o ID da receita: '))
            menu_ingrediente(id_receita, self.id_usuario)
        menu_receita()
         
    def adicionar_receita(self):
        nome_receita = input('Entre com o nome da receita: ').title()
        print(db.adicionar_receita(nome_receita, self.id_usuario))
        sleep(1.5)
        menu_receita()
        
    def deletar_receita(self):
        listar_receita()
        id_receita = int(input('Informe o ID da receita a ser deletada: '))
        print(db.deletar_receita(id_receita))
        sleep(1.5)
        menu_receita()

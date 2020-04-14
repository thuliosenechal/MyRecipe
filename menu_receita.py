from receita import Receita


def menu_receita(id_usuario):
    while True:
        print('''
            Escolha uma opção:

            1 - Listar receita 
            2 - Adicionar receita
            3 - Deletar receita
            4 - Sair do programa ''')

        option = int(input('>: '))
        print(' ')

        if option not in (1, 2, 3, 4, 5):
            print('Opção inválida.')
            option = int(input('Tente novamente >: '))

        receita = Receita(id_usuario)            

        if option == 1:
            receita.listar_receita()
       
        if option == 2:
            receita.adicionar_receita()

        if option == 3:
            receita.deletar_receita()

        if option == 4:
            from usuario import Usuario
            Usuario.sair_programa()

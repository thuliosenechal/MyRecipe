import usuario


usuario = usuario.Usuario()

def login_option():    
    print('''
           Escolha uma opção:
           
           1 - Novo usuário
           2 - Entrar no Sistema
           3 - Esqueci a senha
           4 - Sair''')

    opcao_usuario = int(input('>: '))

    if opcao_usuario not in (1, 2, 3, 4):
        print('Opção inválida.')
        option = int(input('Tente novamente >: '))

    if opcao_usuario == 1:
        usuario.cadastrar_novo_usuario()
        
    if opcao_usuario == 2:
        usuario.logar_sistema()

    if opcao_usuario == 3:
        usuario.recuperar_senha_esquecida()

    if opcao_usuario == 4:
        usuario.sair_programa()

login_option()


if __name__ == "__main__":
        login_option()
import os
#os = sistema operacional
 
restaurantes = [{"nome":"Spolleto", "categoria":"Italiana", "ativo": True},
                {"nome":"Starbucks", "categoria":"cafeteria", "ativo": False},
                {"nome":"Hino", "categoria":"Japonesa", "ativo": True},
                {"nome":"KFC", "categoria":"americana", "ativo": False},
                {"nome":"Popeye's", "categoria":"americana", "ativo": True},
                {"nome":"Gendai", "categoria":"Japonesa", "ativo": False}
                ]

def exibir_nome_do_programa():
   print("""
         ᕙ(`▿´)ᕗ🍔🍱🍦 ✿✨ 𝓡𝓲𝓼𝓽𝓸𝓻𝓪𝓷𝓽𝓮✨✿ ( ◑‿◑)ɔ┏🍟--🍔┑٩(^◡^ )
         """)

def exibir_opcao():
    print("🌹 1. Cadastrar Restaurante")
    print("🌻 2. Listar Restaurantes")
    print("🌷 3. Ativar Restaurante")
    print("🌼 4. Sair")

def finalizar_app():
#def = definir função
    os.system("cls")
    #limpar o menu e retornar apenas:
    print("💥Finalizando o app!💥")

def opção_invalida():
    print("Opção invali"da!\n")
    input("🏡Digite uma tecla para voltar ao menu principal")
    main()          

def voltar_ao_menu_principal():
    input("🌌precione o botão enter para voltar ao menu:")
    main()
    
def exibir_subtitulo(texto):  
    os.system("cls")
    print(texto)

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes\n")

    nome_do_restaurante = input("🍀 - Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input("🌺 - Digite a categoria do restaurante que deseja cadastrar: ")
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante) #append = colocar, (onde?) exemplo restaurantes
    print(f"🌠 O restaurante {nome_do_restaurante}, da categoria {categoria}, foi cadastrado com sucesso!")
    input("🏡 Digite uma tecla para voltar ao menu principal")

def listar_restaurantes():
    os.system("cls")
    print(f"Listando os restaurantes de Osasco ✨💸✨ \n")

    for restaurante in restaurantes: #for = laço de repetição
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f"🌟 - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}")
    input('Digite uma tecla para voltar ao menu principal')
    main()

for restaurante in restaurantes: #for = laço de repetição
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'--{nome_restaurante} | {categoria} | {ativo}')


def alternar_estado_restaurante():
    print('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
        
    input('Digite uma tecla para voltar ao menu principal')
    main()



def escolher_opcao():
    try:
        opção_escolhida = int(input("Escolha a sua opção: "))
        if opção_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            listar_restaurantes()
        elif opção_escolhida == 3:
            alternar_estado_restaurante()
        elif opção_escolhida == 4:
            finalizar_app()
        else:
            opção_invalida()
    except:
        opção_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcao()
    escolher_opcao()

if __name__ == "__main__":
    main()
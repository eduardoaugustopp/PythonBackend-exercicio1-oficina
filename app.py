import os
import json

veiculos = []


# Função para carregar a lista de veículos de um arquivo JSON
def carregar_veiculos():
    ''' Carrega a lista de veículos de um arquivo JSON, se existir '''
    global veiculos
    if os.path.exists('veiculos.json'):
        with open('veiculos.json', 'r') as file:
            veiculos = json.load(file)


# Função para salvar a lista de veículos em um arquivo JSON
def salvar_veiculos():
    ''' Salva a lista de veículos em um arquivo JSON '''
    with open('veiculos.json', 'w') as file:
        json.dump(veiculos, file, indent=4)


def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print("""          
░█████╗░███████╗██╗░█████╗░██╗███╗░░██╗░█████╗░
██╔══██╗██╔════╝██║██╔══██╗██║████╗░██║██╔══██╗
██║░░██║█████╗░░██║██║░░╚═╝██║██╔██╗██║███████║
██║░░██║██╔══╝░░██║██║░░██╗██║██║╚████║██╔══██║
╚█████╔╝██║░░░░░██║╚█████╔╝██║██║░╚███║██║░░██║
░╚════╝░╚═╝░░░░░╚═╝░╚════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝

███╗░░░███╗███████╗░█████╗░░█████╗░███╗░░██╗██╗░█████╗░░█████╗░
████╗░████║██╔════╝██╔══██╗██╔══██╗████╗░██║██║██╔══██╗██╔══██╗
██╔████╔██║█████╗░░██║░░╚═╝███████║██╔██╗██║██║██║░░╚═╝███████║
██║╚██╔╝██║██╔══╝░░██║░░██╗██╔══██║██║╚████║██║██║░░██╗██╔══██║
██║░╚═╝░██║███████╗╚█████╔╝██║░░██║██║░╚███║██║╚█████╔╝██║░░██║
╚═╝░░░░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚════╝░╚═╝░░╚═╝
   """)


def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar veículo')
    print('2. Listar veículos')
    print('3. Alternar estado do veículo')
    print('4. Excluir veículo')
    print('5. Editar veículo')  # Nova opção
    print('6. Sair\n')


def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('Finalizar app')
    print('Aplicativo finalizado. Até logo!')
    exit()


def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal '''
    input('\nDigite uma tecla para voltar ao menu...')
    main()


def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela '''
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_veiculo():
    ''' Cadastra um novo veículo na lista '''
    exibir_subtitulo('Cadastro de novos veículos')
    nome_do_veiculo = input('Digite o nome do veículo que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do veículo {nome_do_veiculo}: ')
    dados_do_veiculo = {'nome': nome_do_veiculo, 'categoria': categoria, 'ativo': False}
    veiculos.append(dados_do_veiculo)
    print(f'O veículo {nome_do_veiculo} foi cadastrado com sucesso!')

    salvar_veiculos()
    voltar_ao_menu_principal()


def listar_veiculos():
    ''' Lista os veículos presentes na lista '''
    exibir_subtitulo('Listando veículos')

    if not veiculos:
        print('Nenhum veículo cadastrado.')
    else:
        print(f"{'Nome do veículo'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
        for veiculo in veiculos:
            nome_veiculo = veiculo['nome']
            categoria = veiculo['categoria']
            ativo = 'ativado' if veiculo['ativo'] else 'desativado'
            print(f'- {nome_veiculo.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_veiculo():
    ''' Altera o estado ativo/desativado de um veículo '''
    exibir_subtitulo('Alterando estado do veículo')
    nome_veiculo = input('Digite o nome do veículo que deseja alterar o estado: ')
    veiculo_encontrado = False

    for veiculo in veiculos:
        if nome_veiculo.lower() == veiculo['nome'].lower():
            veiculo_encontrado = True
            veiculo['ativo'] = not veiculo['ativo']
            mensagem = f'O veículo {nome_veiculo} foi {"ativado" if veiculo["ativo"] else "desativado"} com sucesso'
            print(mensagem)
            salvar_veiculos()
            break

    if not veiculo_encontrado:
        print('O veículo não foi encontrado')

    voltar_ao_menu_principal()


def excluir_veiculo():
    ''' Exclui um veículo da lista '''
    exibir_subtitulo('Exclusão de veículos')
    nome_veiculo = input('Digite o nome do veículo que deseja excluir: ')
    veiculo_encontrado = False

    for veiculo in veiculos:
        if nome_veiculo.lower() == veiculo['nome'].lower():
            veiculo_encontrado = True
            veiculos.remove(veiculo)
            print(f'O veículo {nome_veiculo} foi excluído com sucesso.')
            salvar_veiculos()
            break

    if not veiculo_encontrado:
        print('O veículo não foi encontrado.')

    voltar_ao_menu_principal()


def editar_veiculo():
    ''' Edita os detalhes de um veículo existente '''
    exibir_subtitulo('Edição de veículos')
    nome_veiculo = input('Digite o nome do veículo que deseja editar: ')
    veiculo_encontrado = False

    for veiculo in veiculos:
        if nome_veiculo.lower() == veiculo['nome'].lower():
            veiculo_encontrado = True
            novo_nome = input(f'Novo nome do veículo (deixe em branco para manter "{veiculo["nome"]}"): ')
            nova_categoria = input(f'Nova categoria (deixe em branco para manter "{veiculo["categoria"]}"): ')

            if novo_nome:
                veiculo['nome'] = novo_nome
            if nova_categoria:
                veiculo['categoria'] = nova_categoria

            print(f'O veículo foi atualizado com sucesso!')
            salvar_veiculos()
            break

    if not veiculo_encontrado:
        print('O veículo não foi encontrado.')

    voltar_ao_menu_principal()


def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_veiculo()
        elif opcao_escolhida == 2:
            listar_veiculos()
        elif opcao_escolhida == 3:
            alternar_estado_veiculo()
        elif opcao_escolhida == 4:
            excluir_veiculo()
        elif opcao_escolhida == 5:
            editar_veiculo()  # Nova opção
        elif opcao_escolhida == 6:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    ''' Função principal que inicia o programa '''
    carregar_veiculos()
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()

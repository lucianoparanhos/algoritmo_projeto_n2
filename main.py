# GUILHERME TEODORO DE OLIVEIRA (42303893) 
# LUCIANO PARANHOS (42324882)

import os
from sys import platform

# variavel que armazena o comando usado para limpar a tela.
# considera linux ou macOS como sistema padrao. Somente se for windows
# o comando será trocado para cls
clear_cmd = "clear"
if platform == "win32":
    clear_cmd = "cls"

# funcao que imprime o menu principal
def menu_principal():
    os.system(clear_cmd)
    print('MACK BANK – ESCOLHA UMA OPÇÃO\n')
    print('   (1) CADASTRAR CONTA CORRENTE')
    print('   (2) DEPOSITAR')
    print('   (3) SACAR')
    print('   (4) CONSULTAR SALDO')
    print('   (5) CONSULTAR EXTRATO')
    print('   (6) FINALIZAR')

# funcao que exibe uma mensagem de opcao invalida
# e retorna ao menu principal
def exibe_opcao_invalida():
    os.system(clear_cmd)
    print('Opção inválida!')
    input('Pressione ENTER para continuar...')
    main()

# funcao que valida a opcao selecionada pelo usuario
# se a opcao nao for valida, o programa retorna ao menu principal
def valida_opcao_selecionada(entrada_menu):
    if entrada_menu.isdigit():
        opcao_selecionada = int(entrada_menu)
        if 1 <= opcao_selecionada <= 6:
            return True
        else:
            exibe_opcao_invalida()
    else:
        exibe_opcao_invalida()

def cadastrar_conta_corrente():
    os.system(clear_cmd)
    print('cadastrar_conta_corrente')
    input('Pressione ENTER para continuar...')
    main()

def depositar():
    os.system(clear_cmd)
    print('depositar')
    input('Pressione ENTER para continuar...')
    main()

def sacar():
    os.system(clear_cmd)
    print('sacar')
    input('Pressione ENTER para continuar...')
    main()

def consultar_saldo():
    os.system(clear_cmd)
    print('consultar_saldo')
    input('Pressione ENTER para continuar...')
    main()

def consultar_extrato():
    os.system(clear_cmd)
    print('consultar_extrato')
    input('Pressione ENTER para continuar...')
    main()

# funcao que exibe o nome dos autores em finaliza o programa
def exibe_sair():
    os.system(clear_cmd)
    print("MACK BANK – SOBRE")
    print("Este programa foi desenvolvido por")
    print("GUILHERME TEODORO DE OLIVEIRA (42303893)")
    print("LUCIANO PARANHOS (42324882)")

menu_opcoes = {
    1: cadastrar_conta_corrente,
    2: depositar,
    3: sacar,
    4: consultar_saldo,
    5: consultar_extrato
}

def main():
    menu_principal()

    entrada_menu = input('SUA OPÇÃO: ')
    if valida_opcao_selecionada(entrada_menu):
        opcao_selecionada = int(entrada_menu)

        menu = menu_opcoes.get(opcao_selecionada, exibe_sair)
        menu()

main()

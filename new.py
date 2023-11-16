import os
import random
from sys import platform

# variavel que armazena o comando usado para limpar a tela.
# considera linux ou macOS como sistema padrao. Somente se for windows
# o comando será trocado para cls
clear_cmd = "clear"
if platform == "win32":
    clear_cmd = "cls"

fim_execucao = False

entrada_menu = ""
opcao_selecionada = 0

def exibir_opcao_invalida():
    limpar_tela()
    print('Opção inválida!')
    input('Pressione ENTER para continuar...')

# funcao que exibe o nome dos autores em finaliza o programa
def exibir_opcao_6_sair():
    fim_execucao = True
    limpar_tela()
    print("MACK BANK – SOBRE")
    print("Este programa foi desenvolvido por")
    print("GUILHERME TEODORO DE OLIVEIRA (42303893)")
    print("LUCIANO PARANHOS (42324882)")

# funcao que valida a opcao selecionada pelo usuario
# se a opcao nao for valida, o programa retorna ao menu principal
def validar_opcao_selecionada():
    if entrada_menu.isdigit() and 1 <= int(entrada_menu) <= 6:
        return int(entrada_menu)
    else:
        exibir_opcao_invalida()        

# variável que controla o fim da execução do programa


# dicionario que armazena as funcoes de cada opcao do menu principal
menu_opcoes = {
    1: cadastrar_conta_corrente,
    2: depositar,
    3: sacar,
    4: consultar_saldo,
    5: consultar_extrato,
    6: exibir_opcao_6_sair
}

# funcao que limpa a tela do terminal
def limpar_tela():
    os.system(clear_cmd)

# funcao que imprime o menu principal
def menu_principal():
    limpar_tela()
    print('MACK BANK – ESCOLHA UMA OPÇÃO\n')
    print('   (1) CADASTRAR CONTA CORRENTE')
    print('   (2) DEPOSITAR')
    print('   (3) SACAR')
    print('   (4) CONSULTAR SALDO')
    print('   (5) CONSULTAR EXTRATO')
    print('   (6) FINALIZAR')

# funcao principal do programa
def main():
    while not fim_execucao:
        menu_principal()
        entrada_menu = input('SUA OPÇÃO: ')
        
        opcao_selecionada = validar_opcao_selecionada()

        if opcao_selecionada:
            menu_opcoes[opcao_selecionada]()

# executa a funcao principal
main()

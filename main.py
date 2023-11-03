import os
import random
from sys import platform

# variavel que armazena o comando usado para limpar a tela.
# considera linux ou macOS como sistema padrao. Somente se for windows
# o comando será trocado para cls
clear_cmd = "clear"
if platform == "win32":
    clear_cmd = "cls"

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

# funcao que exibe uma mensagem de opcao invalida
# e retorna ao menu principal
def exibe_opcao_invalida():
    limpar_tela()
    print('Opção inválida!')
    input('Pressione ENTER para continuar...')

# funcao que valida a opcao selecionada pelo usuario
# se a opcao nao for valida, o programa retorna ao menu principal
def valida_opcao_selecionada(entrada_menu):
    if entrada_menu.isdigit() and 1 <= int(entrada_menu) <= 6:
        return int(entrada_menu)
    else:
        exibe_opcao_invalida()
        return None

# funcao que valida a entrada de texto para os campos do cadastro de conta corrente
def validar_entrada_texto_cadastro_conta_corrente(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada:
            return entrada
        print("Dado digitado inválido. Não pode estar em branco")

def validar_entrada_numerica_cadastro_conta_corrente(mensagem, minimo, maximo=float('inf')):
    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        
        if entrada.replace('.', '', 1).isdigit() and entrada.count('.') <= 1:
            valor = float(entrada)
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f'Erro: o valor deve estar entre {minimo} e {maximo}.')
        else:
            print('Entrada inválida. Por favor, insira um número.')

# funcao que exibe o menu de cadastro de conta corrente
def cadastrar_conta_corrente():
    limpar_tela()
    print('MACK BANK – CADASTRO DE CONTA')

    numero_conta = random.randint(1000, 9999)
    print(f'NÚMERO DA CONTA: {numero_conta}')

    # Utilização da função validar_entrada para cada campo
    nome_cliente = validar_entrada_texto_cadastro_conta_corrente('NOME DO CLIENTE: ')
    telefone = validar_entrada_texto_cadastro_conta_corrente('TELEFONE: ')
    email = validar_entrada_texto_cadastro_conta_corrente('EMAIL: ')
    saldo_inicial = validar_entrada_numerica_cadastro_conta_corrente('SALDO INICIAL: ', 1000)
    limite_credito = validar_entrada_numerica_cadastro_conta_corrente('LIMITE DE CRÉDITO: ', 0)

    input('CADASTRO REALIZADO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...')

# funcao que exibe o menu de deposito
def depositar():
    limpar_tela()
    print('depositar')
    input('Pressione ENTER para continuar...')

# funcao que exibe o menu de saque
def sacar():
    limpar_tela()
    print('sacar')
    input('Pressione ENTER para continuar...')

# funcao que exibe o menu de consulta de saldo
def consultar_saldo():
    limpar_tela()
    print('consultar_saldo')
    input('Pressione ENTER para continuar...')

# funcao que exibe o menu de consulta de extrato
def consultar_extrato():
    limpar_tela()
    print('consultar_extrato')
    input('Pressione ENTER para continuar...')

# funcao que exibe o nome dos autores em finaliza o programa
def exibe_sair():
    limpar_tela()
    print("MACK BANK – SOBRE")
    print("Este programa foi desenvolvido por")
    print("GUILHERME TEODORO DE OLIVEIRA (42303893)")
    print("LUCIANO PARANHOS (42324882)")
    exit()

# dicionario que armazena as funcoes de cada opcao do menu principal
menu_opcoes = {
    1: cadastrar_conta_corrente,
    2: depositar,
    3: sacar,
    4: consultar_saldo,
    5: consultar_extrato,
    6: exibe_sair
}

# funcao principal do programa
def main():
    while True:
        menu_principal()
        entrada_menu = input('SUA OPÇÃO: ')
        
        opcao_selecionada = valida_opcao_selecionada(entrada_menu)

        if opcao_selecionada:
            menu_opcoes[opcao_selecionada]()

# executa a funcao principal
main()

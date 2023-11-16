import os
import random
from sys import platform

# funcao que limpa a tela do terminal
def limpar_tela():
    # variavel que armazena o comando usado para limpar a tela.
    # considera linux ou macOS como sistema padrao. Se for windows
    # o comando será trocado para cls
    clear_cmd = "clear"
    if platform == "win32":
        clear_cmd = "cls"

    os.system(clear_cmd)

# funcao que exibe o menu principal
def exibir_menu_principal():
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
def exibir_opcao_invalida():
    limpar_tela()
    print('Opção inválida!')
    input('Pressione ENTER para continuar...')

# funcao que valida a opcao selecionada pelo usuario
def validar_opcao_selecionada(entrada_menu):
    if entrada_menu.isdigit() and int(entrada_menu) >= 1 and int(entrada_menu) <= 6:
        return True
    else:        
        return False

# funcao que valida a entrada de texto para os campos do cadastro de conta corrente
def obter_entrada_texto(campo):
    texto_valido = False
    while not texto_valido:

        # strip remove os espaços em branco no inicio e no final da string
        entrada = input(campo).strip()

        # explicar pra o Guilherme este trecho
        if len(entrada) > 0:
            texto_valido = True # não é necessário essa linha por conta do return
            return entrada
        else:
            print("Dado digitado inválido. Não pode estar em branco")

def obter_entrada_numerica(mensagem, minimo, maximo=float('inf')):
    while True:
        # remove os espaços em branco e troca "," por "."
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
def cadastrar():
    limpar_tela()
    print('MACK BANK – CADASTRO DE CONTA')

    # Gera um número aleatório entre 1000 e 9999
    numero_conta = random.randint(1000, 9999)
    print(f'NÚMERO DA CONTA: {numero_conta}')

    # Utilização da função validar_entrada para cada campo
    nome_cliente = obter_entrada_texto('NOME DO CLIENTE: ')
    telefone = obter_entrada_texto('TELEFONE: ')
    email = obter_entrada_texto('EMAIL: ')
    saldo_inicial = obter_entrada_numerica('SALDO INICIAL: ', 1000)
    limite_credito = obter_entrada_numerica('LIMITE DE CRÉDITO: ', 0)

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
def sair():
    limpar_tela()
    print("MACK BANK – SOBRE")
    print("Este programa foi desenvolvido por")
    print("GUILHERME TEODORO DE OLIVEIRA (42303893)")
    print("LUCIANO PARANHOS (42324882)")

# dicionario que armazena as funcoes de cada opcao do menu principal
menu_opcoes = {
    1: cadastrar,
    2: depositar,
    3: sacar,
    4: consultar_saldo,
    5: consultar_extrato,
    6: sair
}

# funcao principal do programa
def main():
    fim_execucao = False

    while not fim_execucao:
        exibir_menu_principal()

        entrada_menu = input('\nSUA OPÇÃO: ')
        opcao_selecionada_esta_validada = validar_opcao_selecionada(entrada_menu)
        
        if opcao_selecionada_esta_validada:

            opcao_selecionada = int(entrada_menu)

            if opcao_selecionada == 6:
                sair()
                fim_execucao = True
            else:
                menu_opcoes[opcao_selecionada]()
        else:
            exibir_opcao_invalida()

# executa a funcao principal
main()

import os
import random
from sys import platform

# funcao que limpa a tela do terminal
def limpar_tela():
    # variavel que armazena o comando usado para limpar a tela.
    # considera linux ou macOS como sistema padrao. se for windows
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
def exibir_opcao_invalida():
    limpar_tela()
    print('Opção inválida!')
    input('Pressione ENTER para continuar...')


# funcao que valida a opcao selecionada pelo usuario
def validar_opcao_selecionada(entrada_menu):        
    return entrada_menu.isdigit() and int(entrada_menu) >= 1 and int(entrada_menu) <= 6


# funcao que valida a entrada de texto para os campos do cadastro de conta corrente
def obter_entrada_texto(entrada_texto):
    texto_valido = False
    while not texto_valido:
        # strip remove os espaços em branco no inicio e no final da string
        entrada = input(entrada_texto).strip()

        # se a quantidade de caracteres for maior que 0 o texto é considerado válido
        if len(entrada) > 0:
            texto_valido = True  # não é necessário essa linha por conta do return
            return entrada
        else:
            print("Dado digitado inválido. Não pode estar em branco")


# funcao que valida a entrada de numeros para os campos do cadastro de conta corrente
# texto_exibicao exibe a label para o usuário
# valor_minimo é o valor que será usado para aplicar validação de valor mínimo
# valor_maximo é opcional e por padrão é zero. É usado 
def obter_entrada_numerica(texto_exibicao, valor_minimo, valor_maximo = 0):
    while True:
        # remove os espaços em branco e troca "," por "."
        entrada = input(texto_exibicao).strip().replace(',', '.')        

        if entrada.replace('.', '', 1).isdigit() and entrada.count('.') <= 1:
            valor = float(entrada)
            if valor_minimo <= valor:
                return valor
            else:
                if valor_maximo > 0:
                    print(f'O VALOR DEVE SER ENTRE {valor_minimo} E {valor_maximo}')
                else:
                    print(f'O VALOR DEVE SER NO MINÍMO {valor_minimo}')
        else:
            print('ENTRADA INVÁLIDA. POR FAVOR, INSIRA UM NÚMERO')


# funcao que faz a validacao do comprimento da senha
def validar_entrada_senha(senha):
    return len(senha) == 6


def obter_entrada_senha(campo):
    senha = obter_entrada_texto(campo)

    while not validar_entrada_senha(senha):
        print("A senha deve conter 6 caracteres")
        senha = obter_entrada_texto(campo)

    return senha


# funcao para validar a senha e a repeticao da senha. Ambas devem ser iguais
def validar_senha(senha, repetir_senha):
    return senha == repetir_senha


# funcao que realiza o cadastro da conta corrente
def cadastrar():
    limpar_tela()
    print("MACK BANK – CADASTRO DE CONTA\n")

    # Gera um número aleatório entre 1000 e 9999
    numero_conta = random.randint(1000, 9999)
    print(f"NÚMERO DA CONTA: {numero_conta}")

    # Utilização da função obter_entrada_texto para cada campo
    nome_cliente = obter_entrada_texto("NOME DO CLIENTE: ")
    telefone = obter_entrada_texto("TELEFONE: ")
    email = obter_entrada_texto("EMAIL: ")

    # Utilização da função obter_entrada_numerica para cada campo
    saldo = obter_entrada_numerica("SALDO INICIAL: R$ ", 1000)
    limite_credito = obter_entrada_numerica("LIMITE DE CRÉDITO: R$ ", 0)

    # Utilização da função obter_entrada_senha para cada campo
    senha = obter_entrada_senha("SENHA: ")
    repetir_senha = obter_entrada_senha("REPITA A SENHA: ")

    while not validar_senha(senha, repetir_senha):
        print("As senhas não estão iguais")
        senha = obter_entrada_senha("SENHA: ")
        repetir_senha = obter_entrada_senha("REPITA A SENHA: ")

    cadastro = {
        "numero_conta": numero_conta,
        "nome_cliente": nome_cliente,
        "telefone": telefone,
        "email": email,
        "saldo": saldo,
        "limite_credito": limite_credito,
        "senha": senha,
    }

    input('\nCADASTRO REALIZADO! PRESSIONE ENTER PARA VOLTAR AO MENU...')    
    return cadastro


# funcao que realiza o deposico na conta corrente
def depositar(dados_cadastro):
    limpar_tela()
    print(dados_cadastro)
    print("MACK BANK – DEPÓSITO EM CONTA")
    
    numero_conta = obter_entrada_numerica("INFORME O NÚMERO DA CONTA: ", 1000, 9999)

    # Se encontrar o númer da conta no dicionário, solicita o valor de depósito
    if int(dados_cadastro["numero_conta"]) == numero_conta:
        print(f"NOME DO CLIENTE: {dados_cadastro["nome_cliente"]}")
        
        # O valor de depósito deve ser maior que zero
        valor_deposito = obter_entrada_numerica("VALOR DO DEPÓSITO: R$ ", 1)

        # Soma o valor depositado ao saldo
        dados_cadastro["saldo"] = dados_cadastro["saldo"] + valor_deposito

        limpar_tela()
        print("DEPÓSITO REALIZADO COM SUCESSO!")

    else:
        print("CONTA NÃO LOCALIZADA")

    input('Pressione ENTER para continuar...')

# funcao que exibe o menu de saque


def sacar(dados_cadastro):
    limpar_tela()
    print('sacar')
    input('Pressione ENTER para continuar...')

# funcao que exibe o menu de consulta de saldo


def consultar_saldo(dados_cadastro):
    limpar_tela()
    print('consultar_saldo')
    input('Pressione ENTER para continuar...')

# funcao que exibe o menu de consulta de extrato


def consultar_extrato(dados_cadastro):
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


def exibir_cadastro_primeira_opcao():
    limpar_tela()
    print("CONTA CORRENTE não cadastrada!")
    input('Pressione ENTER para continuar...')


# funcao principal do programa
def main():
    fim_execucao = False

    dados_cadastro = {}
    cadastro_realizado = False

    while not fim_execucao:
        exibir_menu_principal()

        # obtem a opcao que o usuário digitou
        entrada_menu = input("\nSUA OPÇÃO: ")

        # faz a validacao da opcao do menu digitada
        opcao_selecionada_esta_validada = validar_opcao_selecionada(entrada_menu)

        if opcao_selecionada_esta_validada:
            # converte para int a opcao do menu
            opcao_selecionada = int(entrada_menu)

            if opcao_selecionada == 1:
                if cadastro_realizado == True:
                    limpar_tela()
                    print("CONTA CORRENTE já cadastrada!")
                    input('Pressione ENTER para continuar...')
                else:
                    dados_cadastro = cadastrar()
                    cadastro_realizado = True


            elif opcao_selecionada == 2:
                if cadastro_realizado == False:
                    exibir_cadastro_primeira_opcao()
                else:
                    depositar(dados_cadastro)


            elif opcao_selecionada == 3:
                if cadastro_realizado == False:
                    exibir_cadastro_primeira_opcao()
                else:
                    sacar(dados_cadastro)


            elif opcao_selecionada == 4:
                if cadastro_realizado == False:
                    exibir_cadastro_primeira_opcao()
                else:
                    consultar_saldo(dados_cadastro)


            elif opcao_selecionada == 5:
                if cadastro_realizado == False:
                    exibir_cadastro_primeira_opcao()

                else:
                    consultar_extrato(dados_cadastro)


            elif opcao_selecionada == 6:
                sair()
                fim_execucao = True


        else:
            exibir_opcao_invalida()


# executa a funcao principal
main()

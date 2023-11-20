# GUILHERME TEODORO DE OLIVEIRA (42303893)
# LUCIANO PARANHOS (42324882)
# MIGUEL HONORIO BOREL CUTIS DOS SANTOS (42320003)

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
# texto_exibicao exibe o texto para o usuário
# valor_minimo é o valor que será usado para aplicar validação de valor mínimo
# valor_maximo é opcional e por padrão é zero
def obter_entrada_numerica(texto_exibicao, valor_minimo, valor_maximo = 0):
    numero_valido = False
    while not numero_valido:
        # remove os espaços em branco e troca "," por "."
        # necessário para fazer a conversão para float
        entrada = input(texto_exibicao).strip().replace(',', '.')        

        # verifica se a entrada é um número válido
        # removendo todos os . "pontos" a entrada tem que ser um número
        # e só pode ter um ou nenhum . "ponto" 

        # é possível usar o split e verificar se o array é apenas de números
        # apenas como exemplo comentado...
        # banana_split = entrada.split(".")
        # if banana_split[0].isdigit() and banana_split[1].isdigit() and len(banana_split) <= 2:
        #     print("número válido")
        # else:
        #     print("número inválido")

        if entrada.replace('.', '').isdigit() and entrada.count('.') <= 1:
            valor = float(entrada)

            if valor_minimo <= valor:
                numero_valido = True
                return valor
            
            else:
                if valor_maximo > 0:
                    print(f'O VALOR DEVE SER ENTRE {valor_minimo} E {valor_maximo}')
                else:
                    print(f'O VALOR DEVE SER NO MINÍMO {valor_minimo}')
        else:
            print('ENTRADA INVÁLIDA. POR FAVOR, INSIRA UM NÚMERO')


# funcao que faz a validacao do comprimento da senha
def validar_comprimento_senha(senha):
    return len(senha) == 6


# funcao que solicita ao usuário para digitar a senha
def obter_entrada_senha(campo):
    senha = obter_entrada_texto(campo)

    while not validar_comprimento_senha(senha):
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

    # Utilização da função obter_entrada_senha para cada campo de senha
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
        "historico": [],
        "conta_bloqueada": False
    }

    input('\nCADASTRO REALIZADO! PRESSIONE ENTER PARA VOLTAR AO MENU...')    
    return cadastro


# funcao que realiza o deposico na conta corrente
def depositar(dados_cadastro):
    limpar_tela()
    print("MACK BANK – DEPÓSITO EM CONTA")
    
    numero_conta = obter_entrada_numerica("INFORME O NÚMERO DA CONTA: ", 1000, 9999)

    # Se encontrar o númer da conta no dicionário, solicita o valor de depósito
    if int(dados_cadastro["numero_conta"]) == numero_conta:
        print("NOME DO CLIENTE: ", dados_cadastro["nome_cliente"])
        
        # O valor de depósito deve ser maior que zero
        valor_deposito = obter_entrada_numerica("VALOR DO DEPÓSITO: R$ ", 1)

        # Soma o valor depositado ao saldo
        #
        # Pode ser simplificado 
        # dados_cadastro["saldo"] += valor_deposito
        dados_cadastro["saldo"] = dados_cadastro["saldo"] + valor_deposito
        
        # Incrementa no histórico o depósito realizado
        dados_cadastro["historico"].append(f"DEPÓSITO R$ {valor_deposito:.2f}")

        limpar_tela()
        print("DEPÓSITO REALIZADO COM SUCESSO!")

    else:
        print("CONTA NÃO LOCALIZADA")

    input('Pressione ENTER para continuar...')


# funcao que exibe uma mensagem para conta bloqueada
def exibir_mensagem_conta_bloqueada():
    print("CONTA BLOQUEADA! ENTRE EM CONTATO COM UM FUNCIONÁRIO")
    input('Pressione ENTER para continuar...')


# funcao que exibe o menu de saque
def sacar(dados_cadastro):
    limpar_tela()
    print("MACK BANK – SAQUE DA CONTA")

    if dados_cadastro["conta_bloqueada"]:
        exibir_mensagem_conta_bloqueada()

    else: 
        numero_conta = obter_entrada_numerica("INFORME O NÚMERO DA CONTA: ", 1000, 9999)
        senha_validada = False

        # Se encontrar o númer da conta no dicionário, solicita o valor de depósito
        if int(dados_cadastro["numero_conta"]) == numero_conta:
            print("NOME DO CLIENTE: ", dados_cadastro["nome_cliente"])

            for tentativa in range(1, 4):
                if senha_validada:
                    continue

                # Utilização da função obter_entrada_senha para cada campo de senha
                senha = obter_entrada_senha("INFORME A SENHA: ")            
                senha_validada = validar_senha(senha, dados_cadastro["senha"])

                if not senha_validada:
                    print(f"SENHA INVÁLIDA: TENTATIVA {tentativa} de 3")
                    if tentativa == 3:
                        dados_cadastro["conta_bloqueada"] = True
                        exibir_mensagem_conta_bloqueada()

                if senha_validada:
                    # O valor do saque deve ser maior que zero
                    valor_saque = obter_entrada_numerica("VALOR DO SAQUE: R$ ", 1)
                    saldo_mais_limite = dados_cadastro["saldo"] + dados_cadastro["limite_credito"]

                    # o saque não pode ser maior que saldo_mais_limite
                    if valor_saque <= saldo_mais_limite:
                        limpar_tela()
                        dados_cadastro["historico"].append(f"SAQUE R$ {valor_saque:.2f}")

                        if valor_saque <= dados_cadastro["saldo"]:
                            dados_cadastro["saldo"] = dados_cadastro["saldo"] - valor_saque
                            
                            print("SAQUE REALIZADO COM SUCESSO!")
                        else:                            
                            valor_saque = valor_saque - dados_cadastro["saldo"]
                            dados_cadastro["saldo"] = 0
                            
                            dados_cadastro["limite_credito"] = dados_cadastro["limite_credito"] - valor_saque
                            print("VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO")                        
                        
                    else:
                        limpar_tela()                      
                        print("NÃO POSSUI SALDO SUFICIENTE")

                    input('Pressione ENTER para continuar...')                
            
        else:
            print("CONTA NÃO LOCALIZADA")
            input('Pressione ENTER para continuar...')


# funcao que exibe o menu de consulta de saldo
def consultar_saldo(dados_cadastro):
    limpar_tela()
    print("MACK BANK – CONSULTA SALDO")
    
    if dados_cadastro["conta_bloqueada"]:
        exibir_mensagem_conta_bloqueada()

    else:
        numero_conta = obter_entrada_numerica("INFORME O NÚMERO DA CONTA: ", 1000, 9999)
        senha_validada = False

        if int(dados_cadastro["numero_conta"]) == numero_conta:
            print("NOME DO CLIENTE: ", dados_cadastro["nome_cliente"])

            for tentativa in range(1, 4):
                if senha_validada:
                    continue

                # Utilização da função obter_entrada_senha para cada campo de senha
                senha = obter_entrada_senha("INFORME A SENHA: ")
                senha_validada = validar_senha(senha, dados_cadastro["senha"])

                if not senha_validada:
                    print(f"SENHA INVÁLIDA: TENTATIVA {tentativa} de 3")
                    if tentativa == 3:
                        dados_cadastro["conta_bloqueada"] = True
                        exibir_mensagem_conta_bloqueada()
            
            if senha_validada:
                # O valor do saque deve ser maior que zero
                saldo_em_conta = dados_cadastro["saldo"]
                limite_credito = dados_cadastro["limite_credito"]
                # Foi necessário duas novas variáveis o print com aspas duplas
                # gera problema quando vai acessar o valor de um dicionario                
                print(f"SALDO EM CONTA: R$ {saldo_em_conta:.2f}")
                print(f"LIMITE DE CRÉDITO: R$ {limite_credito:.2f}")

                input('Pressione ENTER para continuar...')

        else:
            print("CONTA NÃO LOCALIZADA")
            input('Pressione ENTER para continuar...')


# funcao que exibe o menu de consulta de extrato
def consultar_extrato(dados_cadastro):
    limpar_tela()
    print("MACK BANK – EXTRATO DA CONTA")
    
    if dados_cadastro["conta_bloqueada"]:
        exibir_mensagem_conta_bloqueada()

    else:
        numero_conta = obter_entrada_numerica("INFORME O NÚMERO DA CONTA: ", 1000, 9999)
        senha_validada = False

        if int(dados_cadastro["numero_conta"]) == numero_conta:
            print("NOME DO CLIENTE: ", dados_cadastro["nome_cliente"])

            for tentativa in range(1, 4):
                if senha_validada:
                    continue

                # Utilização da função obter_entrada_senha para cada campo de senha
                senha = obter_entrada_senha("INFORME A SENHA: ")

                senha_validada = validar_senha(senha, dados_cadastro["senha"])

                if not senha_validada:
                    print(f"SENHA INVÁLIDA: TENTATIVA {tentativa} de 3")
                    if tentativa == 3:
                        dados_cadastro["conta_bloqueada"] = True
                        exibir_mensagem_conta_bloqueada()
            
            if senha_validada:
                saldo_em_conta = dados_cadastro["saldo"]
                limite_credito = dados_cadastro["limite_credito"]

                # O valor do saque deve ser maior que zero
                print(f"LIMITE DE CRÉDITO: R$ {limite_credito:.2f}")

                for historico in dados_cadastro["historico"]:
                    print(f"{historico}")

                print(f"SALDO EM CONTA: R$ {saldo_em_conta:.2f}")

                input('Pressione ENTER para continuar...')

        else:
            print("CONTA NÃO LOCALIZADA")
            input('Pressione ENTER para continuar...')

# funcao que exibe o nome dos autores em finaliza o programa
def sair():
    limpar_tela()
    print("MACK BANK – SOBRE")
    print("Este programa foi desenvolvido por\n")
    print("42303893 - GUILHERME TEODORO DE OLIVEIRA")
    print("42324882 - LUCIANO PARANHOS")
    print("42320003 - MIGUEL HONORIO BOREL CUTIS DOS SANTOS\n")


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
                if cadastro_realizado:
                    limpar_tela()
                    print("CONTA CORRENTE já cadastrada! - ", dados_cadastro["numero_conta"])
                    input('Pressione ENTER para continuar...')
                else:
                    dados_cadastro = cadastrar()
                    cadastro_realizado = True


            elif opcao_selecionada == 2:
                if not cadastro_realizado:
                    exibir_cadastro_primeira_opcao()
                else:
                    depositar(dados_cadastro)


            elif opcao_selecionada == 3:
                if not cadastro_realizado:
                    exibir_cadastro_primeira_opcao()
                else:
                    sacar(dados_cadastro)


            elif opcao_selecionada == 4:
                if not cadastro_realizado:
                    exibir_cadastro_primeira_opcao()
                else:
                    consultar_saldo(dados_cadastro)


            elif opcao_selecionada == 5:
                if not cadastro_realizado:
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

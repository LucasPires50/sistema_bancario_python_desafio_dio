from conta_bancaria import criar_conta, listar_contas, selecionar_conta
from operacoes import deposito, formatar_float_para_real, gerar_extrato, saque
from usuario import criar_usuario, realizar_login

banco = "Banco Python"

login = f"""
{banco}

    [1] Fazer login
    [2] Criar conta

Escolha um opção:

"""
conta = f"""
{banco}

    [1] Criar conta
    [2] Listar contas

Escolha um opção:
"""

operacoes = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [x] Sair
    
Qual operação deseja realizar:    
"""

saldo = {}
valor_total_sacado = {}
limite_diario_de_saque = 500
extrato = {}
numeros_de_saques = 0
limete_de_saques_diario = 3
banco_de_usuario = []
banco_de_contas = []
logado = ""
conta_selecinada = ""

while True:
    if not logado:
        opcao = input(login)
        if opcao == '1':
            logado = realizar_login(banco_de_usuario)
        elif opcao == '2':
            logado = criar_usuario(banco_de_usuario)
    else:
        if not conta_selecinada:
            opcao = input(conta)
            if opcao == '1':
                conta_selecinada, extrato, saldo, valor_total_sacado = criar_conta(logado, banco_de_contas, extrato, saldo, valor_total_sacado)
            elif opcao == '2':
                if listar_contas(banco_de_contas):
                    conta_selecinada = selecionar_conta(banco_de_contas)
        else:
            opcao = input(operacoes)

            if opcao == '1':
                deposito(conta_selecinada, saldo, extrato)
            elif opcao == '2':
                saque(saldo, conta_selecinada, limete_de_saques_diario, valor_total_sacado, limite_diario_de_saque, numeros_de_saques, extrato)
            elif opcao == '3':
                gerar_extrato(conta_selecinada, saldo, extrato)
            elif opcao == 'x':
                conta_selecinada = ""
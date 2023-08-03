from operacoes import formatar_float_para_real

operacoes = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [x] Sair
    
Qual operação deseja realizar:    
"""

saldo = 0
valor_total_sacado = 0
limite_diario_de_saque = 500
extrato = []
numeros_de_saques = 0
limete_de_saques_diario = 3

while True:
    opcao = input(operacoes)
    
    if opcao == '1':
        print("Depósito\n")
        valor_deposito = input("Informe o valor do depósito:")
        
        if valor_deposito.replace(".", "", 1).isdigit():
            valor_deposito = float(valor_deposito)
            saldo += valor_deposito
            extrato.append({"tipo": "depósito", "valor": valor_deposito})
            
        else:
            print("Valor Inválido!")
            
    elif opcao == '2':
        print("Saque\n")
        valor_saque = input("Informe o valor a ser sacado:")
        
        if valor_saque.replace(".", "", 1).isdigit():
            valor_saque = float(valor_saque)
            if valor_saque > saldo:
                print("Saldo Insuficiente!")
            elif numeros_de_saques == limete_de_saques_diario:
                print("Limite de saque diário atingido!")
            else:
                valor_total_sacado += valor_saque
                if valor_total_sacado > limite_diario_de_saque:
                    print("Limite de valor de saque diário atingido!")
                saldo -= valor_saque
                numeros_de_saques += 1
                extrato.append({"tipo": "saque", "valor": valor_saque})
        else:
            print("Valor Inválido!")
        
    elif opcao == '3':
        print("Extrato\n")
        for trasacao in extrato:
            print(f'{trasacao["tipo"]} : R$ {formatar_float_para_real(trasacao["valor"])}')
            
        print(f"\nSaldo: R$ {formatar_float_para_real(saldo)}")
    elif opcao == 'x':
        break
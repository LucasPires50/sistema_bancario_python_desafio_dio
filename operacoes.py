def formatar_float_para_real(valor):
    valor_formatado = f"{valor:.2f}".replace(".", ",")
    return valor_formatado

def deposito(conta_selecinada, saldo, extrato):
    print("Depósito\n")
    valor_deposito = input("Informe o valor do depósito:")
    
    if valor_deposito.replace(".", "", 1).isdigit():
        valor_deposito = float(valor_deposito)
        saldo_conta = saldo.get(conta_selecinada, 0)
        saldo.update({conta_selecinada : (saldo_conta + valor_deposito)})
        extrato[conta_selecinada].append({"tipo": "depósito", "valor": valor_deposito})
    else:
        print("Valor Inválido!")
    
def saque(saldo, conta_selecinada, limete_de_saques_diario, valor_total_sacado, limite_diario_de_saque, numeros_de_saques, extrato):
    print("Saque\n")
    valor_saque = input("Informe o valor a ser sacado:")
    
    if valor_saque.replace(".", "", 1).isdigit():
        valor_saque = float(valor_saque)
        if valor_saque > saldo[conta_selecinada]:
            print("Saldo Insuficiente!")
        elif numeros_de_saques == limete_de_saques_diario:
            print("Limite de saque diário atingido!")
        else:
            valor_sacado = valor_total_sacado.get(conta_selecinada, 0)
            valor_total_sacado.update({conta_selecinada : (valor_sacado + valor_saque)})

            if valor_total_sacado[conta_selecinada] > limite_diario_de_saque:
                print("Limite de valor de saque diário atingido!")
            saldo_conta = saldo.get(conta_selecinada, 0)
            saldo.update({conta_selecinada : (saldo_conta - valor_saque)})
            numeros_de_saques += 1
            extrato[conta_selecinada].append({"tipo": "saque", "valor": valor_saque})
    else:
        print("Valor Inválido!")
    
def gerar_extrato(conta_selecinada, saldo, extrato):
    titulo = " Extrato "
    print(len(titulo))
    print(titulo.center(20, "#"))
    print(extrato.get(conta_selecinada, None))
    if extrato:
        for trasacao in extrato[conta_selecinada]:
            print(f'{trasacao["tipo"]} : R$ {formatar_float_para_real(trasacao["valor"])}')
        
        print(f"\nSaldo: R$ {formatar_float_para_real(saldo[conta_selecinada])}")
    else:
        print("Não foram realizadas movimentações.")
    print("".center(10+len(titulo), "#"))
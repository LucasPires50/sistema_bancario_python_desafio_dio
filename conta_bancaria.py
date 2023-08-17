
def criar_conta(logado, banco_de_contas, extrato, saldo, valor_total_sacado):
    conta = 0
    if banco_de_contas:
        ultima_conta = banco_de_contas[::-1][0].get("conta", None)
        conta = ultima_conta
        conta += 1
    else:
        conta = 1
        
    banco_de_contas.append(
        {
            "cpf" : logado,
            "conta" : conta,
            "agencia": "0001"
        }
    )
    
    extrato.update({conta : []})
    saldo.update({conta : 0})
    valor_total_sacado.update({conta : 0})
    return conta, extrato, saldo, valor_total_sacado

def listar_contas(banco_de_contas):
    titulo = " Contas "
    print(len(titulo))
    print(titulo.center(20, "#"))
    resultado = ""
    if banco_de_contas:
        for conta in banco_de_contas:
            print(f'conta : {conta["conta"]}')
        resultado = True
    else:
        print("Nenhuma conta cadastrada.")
        resultado = False
    print("".center(10+len(titulo), "#"))
    return resultado
    

def selecionar_conta(banco_de_contas):
    numero = input("Informe o numero da sua conta: ")
    for conta in banco_de_contas:
        numero_conta = conta.get("conta", None)
        if int(numero) == int(numero_conta):
            return numero_conta
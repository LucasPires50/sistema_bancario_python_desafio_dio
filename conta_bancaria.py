
def criar_conta(logado, banco_de_contas):
    
    if banco_de_contas:
        ultima_conta = banco_de_contas[::-1][0].get("conta", None)
        print(ultima_conta)
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
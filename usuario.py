
def criar_usuario(banco_de_usuario):
    
    print(f"\nPreencha as informações abaixo: \n")
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    cpf = input("cpf: ").replace(".", "").replace("-", "")
    logadouro = input("logadouro: ")
    numero = input("numero: ")
    bairro = input("bairro: ")
    cidade = input("cidade: ")
    estado = input("estado: ")
    
    validar_estado(estado)
    verifica_cpf_utilizado(banco_de_usuario, cpf)
    
    banco_de_usuario.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": f"{logadouro} - {numero} - {bairro} - {cidade}/{estado}",
    })
    
    return cpf
    
def validar_estado(estado):
    if not len(estado) == 2:
        print("Preencha somente com a sigla do estado.")

def verifica_cpf_utilizado(banco_de_usuario, cpf):
    for usuario in banco_de_usuario:
        usuario_cpf = usuario.get("cpf", None)
        print(usuario_cpf)
        if cpf == usuario_cpf:
            print("O cpf já foi utilizado.")
            
def realizar_login(banco_de_usuario):
    cpf = input("Informe seu cpf: ")
    for usuario in banco_de_usuario:
        usuario_cpf = usuario.get("cpf", None)
        if cpf == usuario_cpf:
            return cpf
    
    
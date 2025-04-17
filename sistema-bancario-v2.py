import textwrap

def menu():

    menu = """\n
    ================ MENU ================

    [0]\tDepósito
    [1]\tSaque
    [2]\tExtrato
    [3]\tNova Conta
    [4]\tListar Contas
    [5]\tNovo usuário
    [6]\tSair
    => """
    return input(textwrap.dedent(menu))

def deposito (valor_deposito, saldo, extrato, /):

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato = extrato + f'\nDepósito:\tR$ {valor_deposito:.2f}'
        print("\nOperação realizada com sucesso!")
    else:
        print("\nA operação falhou! Informe um valor válido.")
    
    return saldo, extrato

def saque (*, valor_saque, saldo, extrato, limite_por_saque, numero_de_saques, limite_saques):
     
    if saldo < valor_saque:
        print("\nOperação falhou! Você não tem saldo suficiente.") 
    elif valor_saque > limite_por_saque:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif numero_de_saques >= limite_saques:
        print("\nOperação falhou! Limite de saques diários excedidos") 
    elif valor_saque > 0:
        saldo -= valor_saque
        numero_de_saques += 1
        extrato = extrato + f'\nSaque\t\tR${valor_saque:.2f}'
        print("Operação realizada com sucesso!") 
    else:
        print("A operação falhou! Informe um valor válido.")   
    
    return saldo, extrato

def exibir_extrato (saldo, /, *, extrato):
    print("\n================Extrato================")
    print("Nao foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo final:\t\tR$ {saldo:.2f}\n")
    print("=========================================")
    return saldo, extrato

def criar_usuario (usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário cadastrado com este CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    
    print("\nUsuário cadastrado com sucesso!")
   
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta (agencia, numero_conta, usuarios):
    cpf = input('\nInforme o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado! Fluxo de criação de conta encerrado!")
    
def listar_contas (contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
   
    saldo = 1200
    limite_por_saque = 500
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []
   
    while True:

        opcao = menu()

        if opcao == "0":
            valor_deposito = float(input("Informe o valor de depósito: "))

            saldo, extrato = deposito(valor_deposito, saldo, extrato)

        elif opcao == "1":
            valor_saque = float(input("Informe o valor de saque: "))

            saldo, extrato = saque(
                 valor_saque=valor_saque,
                 saldo=saldo,
                 extrato=extrato,
                 limite_por_saque=limite_por_saque,
                 numero_de_saques=numero_de_saques,
                 limite_saques=LIMITE_SAQUES, 
            )
              
        elif opcao == "2":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "5":
            criar_usuario(usuarios)  

        elif opcao == "3":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
       
        elif opcao == "4":
            contas = listar_contas(contas)

        elif opcao == "6":
            break
    
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada")
        
main()

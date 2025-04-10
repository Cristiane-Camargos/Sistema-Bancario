menu = """

[0] Depósito
[1] Saque
[2] Extrato
[3] Sair

=> """

saldo = 1200
limite_por_saque = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "0":
        valor_deposito = float(input("Informe o valor de depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato = extrato + f'\nDepósito: R$ {valor_deposito:.2f}'
            print("Operação realizada com sucesso!")
        else:
            print("A operação falhou! Informe um valor válido.")
    
    elif opcao == "1":
        valor_saque = float(input("Informe o valor de saque: "))
        if saldo < valor_saque:
            print("Operação falhou! Você não tem saldo suficiente.") 
        elif valor_saque > limite_por_saque:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_de_saques >= LIMITE_SAQUES:
            print("Operação falhou! Limite de saques diários excedidos") 
        elif valor_saque > 0:
            saldo -= valor_saque
            numero_de_saques += 1
            extrato = extrato + f'\nSaque R${valor_saque:.2f}'
            print("Operação realizada com sucesso!") 
        else:
            print("A operação falhou! Informe um valor válido.")      
        
    elif opcao == "2":
        print("\n================Extrato================")
        print("Nao foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo final R$ {saldo:.2f}\n")
        print("=========================================")
    
    elif opcao == "3":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada")
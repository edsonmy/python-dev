def isNumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """
saldo = 0 
limite = 500
extrato = ""
numeroSaques = 0
limiteSaques = 3
while True:
    opcao = input(menu).upper()
    if opcao == "D":
        v = input("Informe o valor do depósito: ")
        if isNumber(v):
            valor = float(v)
        else:
            print("** Operação falhou! O valor informado é inválido.")
            continue
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("** Operação falhou! O valor informado é inválido.")
    elif opcao == "S":
        excedeu_saques = numeroSaques >= limiteSaques
        if excedeu_saques:
            print("** Operação falhou! Número máximo de saques excedido.")
            continue
        v = input("Informe o valor do saque: ")
        if isNumber(v):
            valor = float(v)
        else:
            print("** Operação falhou! O valor informado é inválido.")
            continue
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        if excedeu_saldo:
            print("** Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("** Operação falhou! O valor do saque excede o limite.")
        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeroSaques += 1
        else:
            print("** Operação falhou! O valor informado é inválido.")
    elif opcao == "E":
        print("\n")
        print("================Extrato=================")
        if extrato != "":
            print(extrato)
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================")
    elif opcao == "Q":
        break
    else:
        print("** Operação inválida, por favor selecione novamente a operação desejada.")
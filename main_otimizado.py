def isNumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

menu = """
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair
=> """
saldo = 0 
limite = 500
extrato = ""
linha = ""
numeroSaques = 0
limiteSaques = 3
usuarios = []
agencia = "0001"
contas = []

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
        print("=" * 40)

    elif opcao == "Q":
        break

    elif opcao == "NU":
        cpf = input("Informe o CPF (somente número): ")
        usuario = filtrar_usuario(cpf, usuarios)
        if usuario:
            print("** Já existe usuário com esse CPF!")
            continue

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("=== Usuário criado com sucesso! ===")

    elif opcao == "NC":
        cpf = input("Informe o CPF (somente número): ")
        usuario = filtrar_usuario(cpf, usuarios)
        if usuario:
            contas.append({"agencia": agencia, "numero_conta": len(contas)+1, "usuario": usuario})
        else:
            print("** Usuário não encontrado, fluxo de criação de conta encerrado!")

    elif opcao == "LC":
        for conta in contas:
            linha = f"Agência:\t{conta['agencia']}\tC/C:\t{conta['numero_conta']}\tTitular:\t{conta['usuario']['nome']}"
            print("=" * 50)
            print(linha)
    else:
        print("** Operação inválida, por favor selecione novamente a operação desejada.")
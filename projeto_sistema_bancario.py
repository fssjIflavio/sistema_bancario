menu = """
[S] Sacar
[D] Depositar
[E] Extrato
[Q] Sair

=> """

saldo = 0
# saldo começa zerado
limite_saque = 500
# limite por saque
extrato = ""
# extrato sem valor, precisa existir pra ter função lá embaixo
numero_saques = 0
# número de saques zerado e vai enchendo com o tempo
LIMITE_SAQUES = 3
# limite de saques é 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            # esse f"Depósito: R$ {valor:.2f}\n" vai aparecer lá no extrato.
        else:
            print("A operação falhou!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_saque

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")
        
        elif excedeu_limite:
            print("Operação falhou! Você excedeu o limite do valor de saques")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            # esse código também aparecerá no extrato
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================= EXTRATO =================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("==============================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione a operação desejada novamente.")
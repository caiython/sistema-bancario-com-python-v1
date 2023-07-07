menu = """********** SISTEMA BANCÁRIO V1.0 - CAIYTHON **********

Digite a letra correspondente a ação desejada

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 # Saldo da conta bancária
limite = 500 # Limite do valor do saque
extrato = "" # Variável que armazena as movimentações
numero_saques = 0 # Contador de saques
n_operacao = 0 # Contador de operações

LIMITE_SAQUES = 3 # Limite de Saques

while True:

    opcao = input(menu) # Usuário entra com a operação desejada

    # Depósito
    if opcao == "d":
        valor_deposito = float(input("\nDigite o valor do depósito\n\n=> "))
        if valor_deposito <= 0:
            print("\nO valor do depósito deve ser superior a R$ 0.\n")
        else:
            saldo += valor_deposito
            n_operacao += 1
            extrato += f"Operação {n_operacao}\n- Saldo anterior: R$ {saldo-valor_deposito:.2f}\n- Depósito realizado: R$ {valor_deposito:.2f}\n- Novo saldo: R$ {saldo:.2f}\n\n"
            print(f"\nO valor de R$ {valor_deposito:.2f} foi depositado em sua conta.\n")
    
    # Saque
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("\nVocê já atingiu o número máximo de 3 saques ao dia.\n")
        else:
            valor_saque = float(input("\nDigite o valor do saque\n\n=> "))
            if valor_saque <= 0:
                print("\nO valor do saque deve ser superior a R$ 0.\n")
            elif valor_saque > limite:
                print("\nO valor do saque é limitado a R$ 500.\n")
            elif valor_saque > saldo:
                print("\nSaldo insuficiente para realizar o saque.\n")
            else:
                saldo -= valor_saque
                n_operacao += 1
                numero_saques += 1
                extrato += f"Operação {n_operacao}\n- Saldo anterior: R$ {(saldo+valor_saque):.2f}\n- Saque realizado: R$ {valor_saque:.2f}\n- Novo saldo: R$ {saldo:.2f}\n\n"
                print(f"\nO valor de R$ {valor_saque:.2f} foi sacado da sua conta.\n")

    # Extrato
    elif opcao == "e":
        if extrato == "":
            print("\nAinda não foi feita nenhuma movimentação na conta.\n")
        else:
            print(f"\nExtrato: \n\n{extrato}")
    
    # Sair
    elif opcao == "q":
        break

    # Operação inválida
    else:
        print("\nOperação inválida, por favor selecione novamente a opção desejada.\n\n")

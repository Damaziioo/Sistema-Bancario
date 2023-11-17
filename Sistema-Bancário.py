menu = f""" 

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=>"""

LIMITE_SAQUE_DIARIO = 3
saque_diario= 0
LIMITE_POR_SAQUE= 500.00
saque = 0.00
deposito = 0.00
saldo = 0.00
extrato= ""

while True:
    opcao = input(menu).lower()

    if opcao=="d": #Deposito
        
        deposito=float(input("Insira o valor a ser depositado: "))
        if deposito > 0:
            saldo+=deposito
            extrato += f"Deposito: R$ {deposito:.2f} \n"
            print(f"\n Valor de R$ {deposito:.2f} depositado com sucesso!")
        else:
            print("Não é permitido depositar valores nulos ou negativos!")
                
    elif opcao == "s": #Saque
        if( saque_diario>=LIMITE_SAQUE_DIARIO):
            print("Você atingiu o limite de saques diários!")

        saque = float(input("Insira o valor a ser sacado: "))

        if saque <= 0:
            print("Operação falhou. Não é permitido sacar valores nulos ou negativos!")
            
        elif saque > LIMITE_POR_SAQUE:
            print(f"Operação falhou. Você ultrapassou o limite por saque, insira um valor abaxo de R$ {LIMITE_POR_SAQUE}!")
            
        elif saque > saldo:
            print("Operação falhou. Você não tem saldo suficiente.")
        else:
            print("Operação falou. Valor informado é inválido.")

        print(f"\nValor de R$ {saque:.2f} sacado com sucesso!")
        saldo -= saque
        saque_diario += 1
        extrato += f"Saque: R$ {saque:.2f} \n"

    elif opcao == "e": #Extrato
        print(" EXTRATO ".center(35,"="))
        print("Não foram realizadas movimentações!" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print('='*35)
    elif opcao == "q":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")




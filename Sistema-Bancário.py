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

def sacar(saldo = 0 ,saque_diario = 0,LIMITE_SAQUE_DIARIO=0, extrato = " " ,LIMITE_POR_SAQUE=" "):

    if( saque_diario>=LIMITE_SAQUE_DIARIO):
        return print("Você atingiu o limite de saques diários!")
    else:

        valor_saque = float(input("Insira o valor a ser sacado: "))

        if valor_saque <= 0:
            return print("Operação falhou. Não é permitido sacar valores nulos ou negativos!")
            
        elif valor_saque > LIMITE_POR_SAQUE:
            return print(f"Operação falhou. Você ultrapassou o limite por saque, insira um valor abaixo de R$ {LIMITE_POR_SAQUE}!")
            
        elif valor_saque > saldo:
          return  print("Operação falhou. Você não tem saldo suficiente.")
        else:
            print(f"\nValor de R$ {valor_saque:.2f} sacado com sucesso!")
            saldo -= valor_saque
            saque_diario += 1
            extrato.join(f"Saque: R$ {valor_saque:.2f} \n")
            return print(f"\nValor de R$ {valor_saque:.2f} sacado com sucesso!"), saldo, saque_diario, extrato


def depositar(saldo, lista_extrato):

    deposito=float(input("Insira o valor a ser depositado: "))

    if deposito > 0:
        saldo+=deposito
        lista_extrato.join(f"Deposito: R$ {deposito:.2f} \n")
        print(f"\n Valor de R$ {deposito:.2f} depositado com sucesso!")
    elif deposito<=0:
        print("Não é permitido depositar valores nulos ou negativos!")
    else:
        print("Operação falhou!")

def emitir_extrato(saldo,extrato=" "):
        print(" EXTRATO ".center(35,"="))
        print("Não foram realizadas movimentações!" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print('='*35)

while True:
    opcao = input(menu).lower()

    if opcao=="d": #Deposito
        
        depositar(saldo, extrato)
                
    elif opcao == "s": #Saque
        sacar(saldo,saque_diario, LIMITE_SAQUE_DIARIO, extrato )

    elif opcao == "e": #Extrato

        emitir_extrato(saldo,extrato=extrato)

    elif opcao == "q":

        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")




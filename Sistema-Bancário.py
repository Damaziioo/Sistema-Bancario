menu_interno = """ 
=======================================
    
                MENU

=======================================


[D] Depositar
[S] Sacar
[E] Extrato
[Q] Deslogar

=>"""

menu_externo = """ 
=======================================
    
    SEJA BEM VINDO AO BANCO DAMAZIO

=======================================


[L] Login
[N] Novo Usuario
[Q] Sair

=>"""

menu_interno_contas= """ 
=======================================
    
            MENU DE CONTAS

=======================================


[A] Acessar conta
[N] Nova conta
[L] Listar contas
[F] Fechar conta
[Q] Deslogar

=>"""


cpf_usuarios = ()
lista_usuarios=[]
lista_contas=[]
numero_conta = 1
agencia = "0001"


def nova_conta(agencia,numero_conta, CPF,lista_contas):
    conta={
        "agencia":agencia,
        "numero_conta":numero_conta,
        "usuario":"",
        "extrato":"",
        "LIMITE_POR_SAQUE":500.00,
        "LIMITE_SAQUE_DIARIO":3,
        "saldo":0.00,
        "limite_diario":0
    }

    for usuario in lista_usuarios:
        if usuario["cpf"] == CPF:
             conta["usuario"] = usuario
        
    numero_conta+=numero_conta

    return print("Conta criada com sucesso!"), numero_conta, lista_contas.add(conta)


def login(lista_usuarios):
    if not len(lista_usuarios) == 0:
        cpf = input("Insira seu CPF: ")
        senha = input("Insira sua senha: ")

    
        for usuario in lista_usuarios:
            if cpf == usuario["cpf"] and senha==usuario["senha"]:
                return  menu_interno(usuario)
            else:
                print("Usuario nao encontrado ou senha informada nao confere!")
    else:
        print("Não há usuários cadastrados!")
    
    return print("Operacao falhou!")

def novo_usuario(lista_usuarios, cpf_usuarios):
    usuario={
        "nome":"",
        "data_nascimento":"",
        "cpf":"",
        "endereço": {"logradouro":"", "bairro":"", "cidade":"", "estado":""},
        "senha":" ",
        "extrato":"",
        "LIMITE_POR_SAQUE":500.00,
        "LIMITE_SAQUE_DIARIO":3,
        "limite_diario":0,
        "saldo":0.00
    }

    usuario["nome"]=input("Insira seu Nome: ")
    usuario["cpf"]= input("Insira seu CPF: ")
    usuario["data_nascimento"]=input("Insira sua Data de Nascimento (DD/MM/YY): ")
    usuario["endereço"]["logradouro"] = input("Insira o seu Logradouro: ")
    usuario["endereço"]["bairro"] = input("Insira o seu Bairro: ")
    usuario["enereço"]["cidade"] = input("Insira sua Cidade: ")
    usuario["endereço"]["estado"] = input("Insira a sigla do seu Estado: ")
    usuario["senha"] = input("Insira uma senha: ")

    for cpf in cpf_usuarios:
        if cpf == usuario[cpf]:
            return print ("Já existe um usuário com esse cpf")
        
    return print("Usuario criado com sucesso!"), lista_usuarios.add(usuario),cpf_usuarios.add(usuario[cpf])


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


def menu_interno(usuario):
    LIMITE_SAQUE_DIARIO = usuario["LIMITE_SAQUE_DIARIO"]
    LIMITE_POR_SAQUE= usuario[""]
    limite_diario = usuario[""]
    saldo = 0.00
    extrato= ""
    
    
    while True:
        opcao = input(menu_interno).lower()

        if opcao=="d": #Deposito
            
            depositar(saldo, extrato)
                    
        elif opcao == "s": #Saque
            sacar(saldo,limite_diario, LIMITE_SAQUE_DIARIO, extrato,LIMITE_POR_SAQUE)

        elif opcao == "e": #Extrato

            emitir_extrato(saldo,extrato=extrato)

        elif opcao == "q":

            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

def menu_interno_contas(usuario):
    while True:
        opcao= input(menu_interno_contas).lower()

        if opcao == "a":
            login_conta()
        elif opcao =="l":
            listar_contas(usuario)
        elif opcao =="n":
            nova_conta(agencia,numero_conta, usuario["CPF"],lista_contas)
        elif opcao =="f":
            fechar_conta()
        elif opcao=="q":
            break
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

def menu_externo():
    while True:
        opcao= input(menu_externo).lower()

        if opcao == "l":
            login(lista_usuarios)
        elif opcao =="n":
            novo_usuario()
        elif opcao=="q":
            break
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

menu_externo()

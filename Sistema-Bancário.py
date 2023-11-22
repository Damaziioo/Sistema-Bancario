menu_interno_txt = """ 
=======================================
    
                MENU

=======================================

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Deslogar

=>"""

menu_externo_txt = """ 
=======================================
    
    SEJA BEM VINDO AO BANCO DAMAZIO

=======================================

[L] Login
[N] Novo Usuario
[Q] Sair

=>"""

menu_interno_contas_txt= """ 
=======================================
    
            MENU DE CONTAS

=======================================

[A] Acessar conta
[N] Nova conta
[L] Listar contas
[F] Fechar conta
[Q] Deslogar

=>"""

cpf_usuarios = set()
lista_usuarios=[]
numero_conta = 1
agencia = "0001"

def listar_contas(usuario):
    if len(usuario["contas"]) > 0:
        for conta in usuario["contas"]:
           print(f"Número da conta:{conta['numero_conta']}") 
    else:
        print("Operação falhou. Você não possui contas registratas.")

def nova_conta(usuario):
    global agencia, numero_conta
    conta={
        "agencia":agencia,
        "numero_conta":numero_conta,
        "usuario":usuario,
        "extrato":"",
        "limite_por_saque":500.00,
        "limite_saque_diario":3,
        "saldo":0.00,
        "limite_diario_conta":0
    }
    usuario["contas"].append(conta)
    numero_conta+=1
    return print("Conta criada com sucesso!")

def fechar_conta(usuario):
    if len(usuario["contas"]) > 0:
        fechar_conta = input("Insira a conta a ser fechada:")
        for conta in usuario["contas"]:
            if conta["numero_conta"] == fechar_conta:
                escolha = input("Cancelando a conta você perder todo o saldo, tem certeza? (s/n)").lower()
                if escolha == "s":
                    usuario["contas"].pop(conta)
                else: 
                    print("Operação cancelada")
            print("Conta cancelada com sucesso!")
    else:
        print("Você não possui contas registratas.")

def login():
    global lista_usuarios
    if not len(lista_usuarios) == 0:
        cpf = input("Insira seu CPF: ")
        senha = input("Insira sua senha: ")
        for usuario in lista_usuarios:
            if cpf == usuario["CPF"] and senha==usuario["senha"]:
                return  menu_interno_contas(usuario)
            else:
                print("Usuario nao encontrado ou senha informada nao confere!")
    else:
        print("\nNão há usuários cadastrados!")
    return print("Operacao falhou!")

def acessar_conta(usuario):
    if len(usuario["contas"]) > 0:
        acessar_conta= int(input("Insira a conta que deseja acessar: "))
        for conta in usuario["contas"]:
           if acessar_conta == conta["numero_conta"]:
               menu_interno(conta)
    else:
        print("Você não possui contas registratas.")
            
    return print("Operacao falhou!")

def novo_usuario():
    global lista_usuarios, cpf_usuarios
    usuario={
        "nome":"",
        "data_nascimento":"",
        "CPF":"",
        "endereço": {"logradouro":"", "bairro":"", "cidade":"", "estado":""},
        "senha":" ",
        "contas":[]
    }
    usuario["nome"]=input("Insira seu Nome: ") 
    if usuario["nome"] == '':
        return print("Operação falhou. Insira um valor não nulo")
    usuario["CPF"]= input("Insira seu CPF: ")
    if usuario["CPF"] == '':
        return print("Operação falhou. Insira um valor não nulo")
    else:
        for cpf in cpf_usuarios:
            if cpf == usuario["CPF"]:
                return print ("Operação falhou. Já existe um usuário com esse cpf")
        
    usuario["data_nascimento"]=input("Insira sua Data de Nascimento (DD/MM/YY): ")
    if usuario["data_nascimento"] == '':
        return print("Operação falhou. Insira um valor não nulo")
    
    usuario["endereço"]["logradouro"] = input("Insira o seu Logradouro: ")
    if usuario["endereço"]["logradouro"] == '':
        return print("Operação falhou. Insira um valor não nulo")
    
    usuario["endereço"]["bairro"] = input("Insira o seu Bairro: ")
    if usuario["endereço"]["bairro"] == '':
        return print("Operação falhou. Insira um valor não nulo")
    
    usuario["endereço"]["cidade"] = input("Insira sua Cidade: ")
    if usuario["endereço"]["cidade"] == '':
        return print("Operação falhou. Insira um valor não nulo")
    
    usuario["endereço"]["estado"] = input("Insira a sigla do seu Estado: ")
    if usuario["endereço"]["estado"] == '':
        return print("Operação falhou. Insira um valor não nulo")
    
    usuario["senha"] = input("Insira uma senha: ")
    if usuario["senha"] == '':
        return print("Operação falhou. Insira um valor não nulo")

    lista_usuarios.append(usuario)
    cpf_usuarios.add(usuario["CPF"])
        
    return print("Usuario criado com sucesso!")

def sacar(conta):
    if( conta["limite_diario_conta"]>=conta["limite_saque_diario"]):
        return print("Você atingiu o limite de saques diários!")
    else:
        valor_saque = float(input("Insira o valor a ser sacado: "))
        if valor_saque <= 0:
            return print("Operação falhou. Não é permitido sacar valores nulos ou negativos!")
        elif valor_saque > conta["limite_por_saque"]:
            return print(f"Operação falhou. Você ultrapassou o limite por saque, insira um valor abaixo de R$ {conta['limite_por_saque']}!")   
        elif valor_saque > conta["saldo"]:
          return  print("Operação falhou. Você não tem saldo suficiente.")
        else:
            conta["saldo"] -= valor_saque
            conta["limite_diario_conta"] += 1
            conta["extrato"]+=(f"Saque: R$ {valor_saque:.2f} \n")
            print(f"\nValor de R$ {valor_saque:.2f} sacado com sucesso!")
            return  conta
        
def depositar(conta):
    deposito=float(input("Insira o valor a ser depositado: "))
    if deposito > 0:
        conta["saldo"]+=deposito
        conta["extrato"]+=(f"Deposito: R$ {deposito:.2f} \n")
        print(f"\n Valor de R$ {deposito:.2f} depositado com sucesso!")
        return conta
    elif deposito<=0:
        return print("Não é permitido depositar valores nulos ou negativos!")
    else:
       return print("Operação falhou!")
    
def emitir_extrato(conta):
        print(" EXTRATO ".center(35,"="))
        print("Não foram realizadas movimentações!" if not conta["extrato"] else conta["extrato"])
        print(f"\nSaldo: R$ {conta['saldo']:.2f}\n")
        print('='*35)

        return conta
        
def menu_interno(conta):
    while True:
        opcao = input(menu_interno_txt).lower()
        if opcao=='d':
            depositar(conta)
        elif opcao == 's':
            sacar(conta)
        elif opcao == 'e':
            emitir_extrato(conta)
        elif opcao == 'q':
            break
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")
    return conta

def menu_interno_contas(usuario):
    while True:
        opcao= input(menu_interno_contas_txt).lower()
        if opcao == "a":
            acessar_conta(usuario)
        elif opcao =="l":
            listar_contas(usuario)
        elif opcao =="n":
            nova_conta(usuario)
        elif opcao =="f":
            fechar_conta(usuario)
        elif opcao=="q":
            break
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

def menu_externo():
    while True:
        opcao= input(menu_externo_txt).lower()
        if opcao == "l":
            login()
        elif opcao =="n":
            novo_usuario()
        elif opcao=="q":
            break
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

menu_externo()

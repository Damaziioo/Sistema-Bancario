# Sistema Bancário - Documentação do Programa Bancário Simples

Este programa em Python implementa um sistema bancário básico que permite aos usuários realizar operações como depósito, saque e visualização de extrato. O sistema é interativo e conta com funcionalidades de login, criação de usuários, acesso a contas, e operações bancárias.

## Funcionalidades Principais

### Menu Externo

Ao iniciar o programa, os usuários são recebidos com um menu externo, oferecendo as seguintes opções:

- [L] Login
- [N] Novo Usuário
- [Q] Sair

Os usuários podem selecionar as opções digitando a letra correspondente.

### Menu Interno - Contas

Após realizar o login ou criar um novo usuário, os usuários têm acesso a um menu interno de contas, incluindo as seguintes opções:

- [A] Acessar Conta
- [N] Nova Conta
- [L] Listar Contas
- [F] Fechar Conta
- [Q] Deslogar

### Operações Bancárias

1. **Depósito (Opção 'D'):**
   - Solicita ao usuário inserir o valor a ser depositado.
   - Verifica se o valor é maior que zero.
   - Atualiza o saldo e registra a transação no extrato.

2. **Saque (Opção 'S'):**
   - Verifica se o usuário atingiu o limite diário de saques.
   - Solicita ao usuário inserir o valor a ser sacado.
   - Realiza verificações para garantir que o saque seja válido.
   - Atualiza o saldo, incrementa o contador de saques diários e registra a transação no extrato.

3. **Extrato (Opção 'E'):**
   - Exibe um cabeçalho decorativo.
   - Apresenta o extrato, informando se não houve movimentações.
   - Exibe o saldo atual.

4. **Sair (Opção 'Q'):**
   - Encerra o programa.

## Contas e Usuários

- Cada usuário pode ter várias contas associadas.
- As informações do usuário incluem nome, CPF, data de nascimento, endereço e senha.
- Contas possuem informações como número da conta, agência, saldo, extrato e limites de saque.

## Observações

- O programa possui validações para garantir que o usuário insira valores válidos em depósitos e saques.
- Limites diários e máximos por saque são implementados para restringir certas operações.
- O extrato é mantido e exibido ao usuário, mostrando todas as transações realizadas.

## Instruções de Uso

1. Execute o programa.
2. Selecione a opção desejada no menu externo.
3. Siga as instruções para login, criação de usuário e operações bancárias.
4. Repita conforme necessário até escolher a opção 'Q' para sair.

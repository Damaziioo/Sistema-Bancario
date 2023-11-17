# Sistema Bancario
 
**Documentação do Programa Bancário Simples**

---

**Objetivo:**

O código a seguir implementa um programa bancário simples em Python, permitindo ao usuário realizar operações básicas como depósito, saque e visualização de extrato.

---

**Menu:**

O programa apresenta um menu interativo com as seguintes opções:

- [D] Depositar
- [S] Sacar
- [E] Extrato
- [Q] Sair

O usuário pode selecionar a operação desejada digitando a letra correspondente.

---

**Variáveis:**

- `LIMITE_SAQUE_DIARIO`: Define o número máximo de saques permitidos por dia.
- `saque_diario`: Contador de saques diários.
- `LIMITE_POR_SAQUE`: Define o limite máximo permitido por saque.
- `saque`: Armazena o valor do saque inserido pelo usuário.
- `deposito`: Armazena o valor do depósito inserido pelo usuário.
- `saldo`: Armazena o saldo da conta.
- `extrato`: Armazena o histórico de transações para exibição no extrato.

---

**Operações:**

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

---

**Loop Principal:**

O programa opera em um loop infinito (`while True`) que permite ao usuário realizar várias operações consecutivas sem a necessidade de reiniciar o programa.

---

**Observações:**

- O código possui validações para garantir que o usuário insira valores válidos em depósitos e saques.
- Limites diários e máximos por saque são implementados para restringir certas operações.
- O extrato é mantido e exibido ao usuário, mostrando todas as transações realizadas.

---

**Instruções de Uso:**

1. Execute o programa.
2. Selecione a operação desejada digitando a letra correspondente.
3. Siga as instruções para cada operação.
4. Repita conforme necessário até escolher a opção 'Q' para sair.

---

**Fim da Documentação**

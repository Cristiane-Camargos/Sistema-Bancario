# Sistema Bancário
Sistema bancário simples que permite ao usuário realizar as operações de saque, depósito, consultar o extrato da conta, cadastar usuário e criar nova conta.

## Ferramentas:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Desafio do projeto - v1:
A primeira versão do sistema bancário(v1) trabalha apenas com um usuário, não sendo necessário, portanto, identificar qual é o número da agência e conta bancária. Além disso, permite ao usuário realizar apenas operações de saque, depósito e consultar o extrato da conta.
### Depósito
A operação de depósito deve admitir apenas valores positivos, e todas operações devem ser armazenadas para possível conferência no extrato. 
### Saque
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta ou exceda o limite de saques, o sistema deve exibir uma mensagem informando ao usuário. Todos as operações de saque devem ser armazenadas para possível conferência em extrato.
### Extrato
Deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Todos os valores devem ser exibidos utilizando o formato R$ xxx.xx.

## Desafio do projeto - v2:
As operações da primeira versão do projeto devem ser separadas em funções. Duas novas operações devem ser adicionadas: cadastrar usuário e criar conta bancária. A função saque deve receber os argumentos apenas por nome (keyword only), a função depósito deve receber os argumentos apenas por posição (positional only) e, por fim, a função extrato deve receber os argumentos por posição e nome. O programa deve armazenar os usuários em lista e as contas bancárias também. Não é permitido cadastrar dois usuários com o mesmo CPF. O número da conta bancária é sequencial, iniciando em 1 e o número da agência é fixo (0001).

## Instruções de como contribuir:

### 1) Faça um **Fork** deste Repositório

### 2) Clone localmente

```bash
git clone https://github.com/Cristiane-Camargos/Sistema-Bancario.git
```
### 3) Crie uma nova **branch** 
```
git checkout -b feature/nome-da-feature
```
### 4) Faça suas alterações e commit
```
git commit -m 'feat:descrição da nova feat'
```
### 5) Envie as alterações para seu repositório remoto
```
git push origin feature/nome-da-feature
```
### 6) Solicite um pull request

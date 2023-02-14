import os
os.system('clear')

class Usuario():
    def __init__(self, nome, idade, cpf):
        self.cadastro = {}
        self.__saldo = float(0)
        self.nome = str(nome).title()
        self.idade = idade
        self.cpf = cpf
        self.cadastro['NOME'] = self.nome
        self.cadastro['IDADE'] = self.idade
        self.cadastro['CPF'] = self.cpf
        self.cadastro['SALDO R$'] = self.__saldo

        print('-'*75)
        print('|\t         **** CADASTRO REALIZADO COM SUCESSO ****                 |')
        print('|                                                                         |')
        print('|\t\t            | DADOS DO CLIENTE |                          |')
        print('-'*75)
        print(f"{self.cadastro}")
        print('-'*75)

    def Deposito(self, valor):
        self.__saldo += valor
        print(f"\nSeu saldo é: R${self.__saldo:.2f}\n")
    
    def Saque(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            print(f"\nSeu saldo é: R${self.__saldo:.2f}\n")
        else:
            print('\nSALDO INSUFICIENTE')

    def Extrato(self):
        self.cadastro['SALDO R$'] = self.__saldo
        print(f'\n[EXTRATO]CLIENTE: \n\n{self.cadastro}\n')

    def Update(self):
        print('-'*75)
        print('|\t\t         R BANK - ATUALIZAR CADASTRO                      |')
        print('-'*75)
        print('|\t\t\t          1 - NOME                                |'
            '\n|\t\t\t          2 - IDADE                               |'
            '\n|\t\t\t          3 - CPF                                 |'
            '\n|\t\t\t          0 - SAIR                                |')
        print('-'*75)

        op = int(input('\nO que voce deseja atualizar?:'))

        if op == 1:
            self.cadastro['NOME'] = input('\nDIGITE NOVO NOME: ').title()
            print('-'*75)
            print(f'{self.cadastro}')
            print('-'*75)
            print('\t\t       **** CADASTRO ATUALIZADO ****')
            print('-'*75)
            print()
        
        if op == 2:
            self.cadastro['IDADE'] = input('\nDIGITE NOVA IDADE: ')
            print('-'*75)
            print(f'{self.cadastro}')
            print('-'*75)
            print('\t\t       **** CADASTRO ATUALIZADO ****')
            print('-'*75)
            print()
        
        if op == 3:
            self.cadastro['CPF'] = input('\nDIGITE NOVO CPF: ')
            print('-'*75)
            print(f'{self.cadastro}')
            print('-'*75)
            print('\t\t       **** CADASTRO ATUALIZADO ****')
            print('-'*75)
            print()

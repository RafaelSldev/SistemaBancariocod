from function import *


print('-'*75)
print('|\t\t\t          R BANK                                  |')
print('-'*75)
print('|\t           **** CADASTRE-SE PARA CONTINUAR ****                   |')
print('-'*75)

nome = str(input("\nDigite o seu nome: "))
idade = int(input("\nDigite a sua idade: "))
cpf = int(input("\nDigite o seu CPF: "))
print()
a = Usuario(nome, idade, cpf)

while True:
        print('-'*75)
        print('|\t\t\t          R BANK                                  |')
        print('-'*75)
        print('|\t\t\t      1 - DEPOSITO                                |'
                '\n|\t\t\t      2 - SAQUE                                   |'
                '\n|\t\t\t      3 - EXTRATO                                 |'
                '\n|\t\t\t      4 - ATUALIZAR                               |'
                '\n|\t\t\t      0 - SAIR                                    |')
        print('-'*75)

        op = int(input("\nDigite a opção desejada: "))


        match op:
                case 1:
                        valor = float(input("\n[DEPOSITO]Digite o valor: "))
                        a.Deposito(valor)
                case 2:
                        valor = float(input("\n[SAQUE]Digite o valor: "))
                        a.Saque(valor)
                case 3:
                        a.Extrato()
                
                case 4:
                        a.Update()

                case 0:
                        print("\nFinalizando...\n\n\n")
                        break

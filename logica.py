import os 
from datetime import datetime 

def escolher_arquivo():
    
    while True:
        print("\nDeseja salvar o histórico em qual formato?")
        print("1 - TXT")
        print("2 - CSV")
        print("3 - Ambos")
        try:    
            entrada_csv = int(input("Escolha: "))
            if entrada_csv == 1:
                salvar_arquivo()
                break

            elif entrada_csv == 2:
                salvar_csv()
                break

            elif entrada_csv == 3:
                salvar_arquivo()
                salvar_csv()
                break
            else:
                print("Escolha uma opção válida!")
        except ValueError:
            print("Digite um numero válido!")



def salvar_csv():
    with open("historico.csv", "w") as arquivo:
        for operacao in historico:
            arquivo.write(operacao + "\n")

def carregar_historico_csv():
    if os.path.exists("historico.csv"):
        with open("historico.csv", "r") as arquivo:
            return [linha.strip() for linha in arquivo.readlines()]
    return []

def salvar_arquivo():
    with open("historico.txt", "w") as arquivo:
        for operacao in historico:
            arquivo.write(operacao + "\n")

def carregar_historico():
    if os.path.exists("historico.txt"):
        with open("historico.txt", "r") as arquivo:
            return [linha.strip() for linha in arquivo.readlines()]
    return []

def data():
    return datetime.now().strftime(' %d/%m/%Y %H:%M:%S')
    
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def entradas():
    while True:
        try:
            num1 = int(input("Digite um numero que deseja efetuar uma conta: "))
            num2 = int(input("Digite um numero que deseja efetuar uma conta: ")) 
            return num1, num2 
        except ValueError:
            print("Digite um numero válido!")

def soma():
    num1, num2 = entradas()
    resultado = num1+num2
    operacao = f"{data()} | {num1} + {num2} = {resultado} "
    print(operacao)
    historico.append(operacao)
    escolher_arquivo()


def sub():
    num1, num2 = entradas()
    resultado = num1-num2
    operacao = f"{data()} | {num1} - {num2} = {resultado}"
    print(operacao)
    historico.append(operacao)
    escolher_arquivo()


def mult():
    num1, num2 = entradas()
    resultado = num1*num2
    operacao = f"{data()} | {num1} * {num2} = {resultado}"
    print(operacao)
    historico.append(operacao)
    escolher_arquivo()


def div():
    num1, num2 = entradas()
    resultado = num1 / num2
    operacao = f"{data()} | {num1} / {num2} = {resultado}"
    print(operacao)
    historico.append(operacao)
    escolher_arquivo()

def potencia():
    num1, num2 = entradas()
    resultado = num1^num2
    operacao = f"{data()} | {num1} ** {num2} = {resultado}"
    print(operacao)
    historico.append(operacao)
    escolher_arquivo()


def ver_historico():
    if not historico:
        print("Nenhuma operação realizada!")
    else:
     for i, operacao in enumerate(historico, 1):
        print(f"{i}. {operacao}")

def del_historico():
    while True:
        print("\nQual histórico você deseja deletar?")
        print("1 - TXT")
        print("2 - CSV")
        print("3 - Ambos")
        try:
            entrada = int(input("Escolha: "))
            if entrada == 1:
                open("historico.txt", "w").close()
                historico.clear()
                print("Histórico TXT apagado!")
                break
            elif entrada == 2:
                open("historico.csv", "w").close()
                historico.clear()
                print("Histórico CSV apagado!")
                break
            elif entrada == 3:
                open("historico.txt", "w").close()
                open("historico.csv", "w").close()
                historico.clear()
                print("Ambos os históricos foram apagados!")
                break
            else:
                print("Opção inválida, digite 1, 2 ou 3.")
        except ValueError:
            print("Por favor, digite um número válido.")


def apagar_historico():
    historico.clear()
    print("Historico apagado com sucesso!")
    salvar_arquivo()
    del_historico()

historico = []
historico = carregar_historico()
historico_csv = carregar_historico_csv()

while True:
    print(''' Digite o numero da operação que você deseja fazer:
        1 - soma
        2 - subtração
        3 - multiplicação
        4 - Dividir
        5 - Potência
        6 - Ver historico
        7 - Apagar historico
        8 - Finalizar o programa
    ''' )
    try:
        entrada = int(input("Digite o calculo que deseja ser executado: "))

        if entrada == 1:
            soma()

        elif entrada == 2:
            sub()
            
        elif entrada == 3:
            mult()
        
        elif entrada == 4:
            div()
        
        elif entrada == 5:
            potencia()
            
        elif entrada == 6:
            ver_historico()
        
        elif entrada == 7:
            apagar_historico()

        elif entrada == 8:
            print("Calculadora finalizada!!!")
            break

        else: 
            print("Opção Inválida!")

    except ValueError:
            print("Digite um numero válido!")
            

    input("\nPressione ENTER para continuar...")
    limpar_terminal()
            
    

saldo = 0
limite = 100
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

def depositar():
    global saldo, extrato
    print('DEPÓSITO')
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
    else:
        print('Operação falhou! O valor informado é inválido.')

def sacar():
    global saldo, extrato, numero_saque
    print('SAQUE')
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque >= LIMITE_SAQUE

    if excedeu_saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
    elif excedeu_limite:
        print('Operação falhou! O valor excede o limite de saque.')
    elif excedeu_saques:
        print('Operação falhou! Número máximo de saques excedido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saque += 1
    else:
        print('Operação falhou! O valor informado é inválido.')

def exibir_extrato():
    global saldo, extrato
    print('================ EXTRATO ================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo: R$ {saldo:.2f}')
    print('=========================================')

def sair():
    print('Saindo...')
    return False  # Indica que o loop deve parar

# Mapeia as opções para as funções correspondentes
operacoes = {
    'd': depositar,
    's': sacar,
    'e': exibir_extrato,
    'q': sair
}

while True:
    opcao = input('[d] = depósito; [s] = saque; [e] = extrato; [q] = sair\n').strip().lower()

    if opcao in operacoes:
        if opcao == 'q':  # Se for 'q', a função sair() retorna False e encerra o loop
            if not operacoes[opcao]():
                break
        else:
            operacoes[opcao]()  # Chama a função correspondente
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')

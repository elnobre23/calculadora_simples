condicao = True
operadores = ['+', '-', '*', '/']
resultado = 0.0

while condicao:
    try:
        numero_1 = float(input('Digite o primeiro número: '))
        numero_2 = float(input('Digite o segundo número: '))
        operador = input('Digite o operador (+, -, * ou /): ')

        if operador not in operadores:
            print('Você não digitou um operador válido!')
            continue

        if operador == '+':
            resultado = numero_1 + numero_2
        elif operador == '-':
            resultado = numero_1 - numero_2
        elif operador == '*':
            resultado = numero_1 * numero_2
        elif operador == '/':
            if numero_2 == 0:
                print(f'Não é possível dividir por {numero_2}')
                continue
            resultado = numero_1 / numero_2        
        print(f'O resultado foi {resultado}')
        
        sair = input('Deseja continuar utilizando a calculadora? (S/N)? ')
        if sair.lower() == 'n':
            break
    except:
        print('Você não digitou um número válido!')   

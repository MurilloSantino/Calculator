def Main():
    while True:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Escolha um Operador: (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        if operador == '+':
            resultado = num1 + num2

        elif operador == '-':
            resultado = num1 - num2

        elif operador == '*':
            resultado = num1 * num2

        elif operador == '/':
            if num2 == 0:
                print("Divisão por zero não é permitido")
            else:
                resultado = num1 / num2
                
        else:
            print("Operador inválido.")
            continue

        print("Resultado:", resultado)

        continuar = input("Deseja cotinuar? (y/n): ")
        if continuar.lower() != 'y':
            break
Main()

import re
def calcular(expressao):
    try:
        expressao = expressao.replace(' ', '')
        if not re.match(r'^[0-9+\-*/.]+$', expressao):
            return "Erro: A Expressão contém caracteres inválidos."
        resultado = eval(expressao)

        if isinstance(resultado, float):
            return f"{resultado}".replace('.', ',')
        return resultado
    except Exception as e:
        return f"Erro: {str(e)}"
    
def main():
    while True:
        expressao = input("Calcule: ")
        if expressao.lower() == 'sair':
            print("Fechando Calculadora...")
            break
        resultado = calcular(expressao)
        print(f"Resultado: {resultado}\n")

if __name__ == "__main__":
    main()
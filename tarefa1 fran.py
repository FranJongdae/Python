class Calculadora:
    def __init__(self):
        pass
 
    def calcular(self, num1, operador, num2):
        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            if num2 == 0:
                return "Erro: Divisão por zero."
            else:
                return num1 / num2
        else:
            return "Operador inválido."
 
calc = Calculadora()

while True:
    try:
        numero1 = float(input("Indique o primeiro número: "))
        operador = input("Indique a operação (+, -, *, /): ")
        numero2 = float(input("Indique o segundo número: "))
    except ValueError:
        print("Aviso -> Insira números válidos!")
        continue

    if operador not in ['+', '-', '*', '/']:
        print ("Aviso -> Operador inválido. Insira um operador válido!")
        continue

    resultado = calc.calcular (numero1, operador, numero2)
    print ("Resultado:", numero1, operador, numero2, "=", resultado)

    continuar = input("Quer realizar outro cáculo? (Digite 'Esc' para sair do programa, ou pressione Enter para continuar): ")
    if continuar.lower() == "esc":
        break
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

numero1 = int(input("Indique o primeiro número: "))
operador = input("Indique a operação (+, -, *, /): ")
numero2 = int(input("Indique o segundo número: "))
 
 
 
resultado = calc.calcular(numero1, operador, numero2)
print("Resultado:", numero1, operador, numero2, "=", resultado)
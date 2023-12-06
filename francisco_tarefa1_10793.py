import msvcrt

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

def get_key():          #   definição de uma nova função
    return msvcrt.getch().decode('utf-8')      

#   utilização da função (getch) e (decode) para intrepretar a intrudução do operador na calculadora

##################### INICIO DA CALCULADORA ################################################

calc = Calculadora() # Chamada da classe ao "programa"

while True: # inicio do loop do calculo
    numero1 = float(input("Indique o primeiro número: ")) #  Pedido para a Introdução do primeiro Valor

    while True: # inicio do loop para o operador 
        print("Qual o operador? (+, -, *, /)")
        # Mensagem para o utilizador a pedir a introdução do operador, que será aceite de imediato.
        operador = get_key()
        #  Antes tinhamos input() em que o utilizador teria de pressionar a tecla enter, e passamos a definir (def) uma função chamada (get_key) para que a introdução seja aceite automaticamente.

        if operador in ['+', '-', '*', '/']:
            break #se tiver certo break e continua com o proximo codigo
        else:
            print("Operador inválido. Tente novamente.")

   
    numero2 = float(input("Indique o segundo número: ")) #  Pedido para a Introdução do segundo Valor

    resultado = calc.calcular(numero1, operador, numero2) # Realiza o cálculo dos diferentes valores dependendo do operador introduzido
    print ("Resultado:", resultado) # Apresenta o resultado final da operação.

    print("Pressione 'Esc' para sair ou qualquer tecla para continuar.")
    tecla = get_key()
    
    if tecla == '\x1b':  # Se a tecla pressionada for 'Esc', o programa acaba.
        break
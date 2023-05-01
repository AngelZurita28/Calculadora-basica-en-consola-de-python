# Calculadora para probar en diferentes sistemas operativos


def calcular(a, b, operator):
    if (operator == '+'):
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return 'operador no valido'


if __name__ == '__main__':
    end = False

    while not end:
        a = int(input('ingrese un numero: '))
        b = int(input('ingrese el segundo numero: '))
        operator = input("Ingrese un operador \n ['+' para suma] \n ['-' para restar]" +
                         " \n ['*' para multiplicacion] \n ['/' para dividir] \n :... ")
        print('el resultado es: ' + str(calcular(a, b, operator)) )

        respuesta = False
        while not respuesta:
            p = input('Quiere seguir o terminar con el programa? [S/T]: ')
            if p.upper() == "T":
                end = True
                respuesta = True
            elif p.upper() == 'S':
                respuesta = True
        

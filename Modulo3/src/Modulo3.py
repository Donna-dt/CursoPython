# 1. importar librerias
import os
import pandas as pd


# 2. Declaro constantes




# 3. Funciones y/o clases

def validar_numero(num):
    try:
        return num = float(num)
    except:
        print('Dato ingresado no es un número')
        num = input('Ingrese el número:')
        return validar_numero(num) 

class operaciones:

    def __init__(self, num1, num2):
        # Atributos de clase
        self.num1 = num1
        self.num2 = num2

    #Creación de métodos de clase

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def potencia(self, n):
        return math.pow(self.num1,n) 


# 4. Programa incicial
if __name__ == "__main__":
# Solicitar el ingreso de 2 números
    n1 = validar_numero(input("Ingrese el primer numero"))
    n2 = validar_numero(input("Ingrese el segundo numero"))

    # creo el objeto de clase
    opp = operaciones(n1, n2)

    #Imprimo resultado
    s = opp.sumar()
    r = opp.restar()
    p = opp.potencia(2)


    print(f'La suma de los valores es : {s}')
    print(f'La resta de los valores es : {r}')
    print(f'La potencia de {opp.num1} elevado a la 2 es : {p}')

    pass
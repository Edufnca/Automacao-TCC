import math

def soma(x,y,z=0):
    resultado = x+y+z
    return resultado
def subtracao(x,y,z=0):
    resultado = x-y-z
    return resultado
def divisao(x,y):
    resultado = x/y
    return resultado
def fatorial(x):
    while x>0:
        x*(x-1)
    return x
def segundo_grau(a, b, c):
    D = (b**2 - 4*a*c)
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)
    return x1, x2, D


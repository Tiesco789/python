"""
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
"""

VALOR = tuple(map(float, input("").split()))

A = VALOR[0]
B = VALOR[1]
C = VALOR[2]
PI = 3.14159

TRIANGULO = A * C / 2
CIRCULO = PI * C ** 2
TRAPEZIO = (A + B) * C / 2
QUADRADO = B * B
RETANGULO = A * B

print(f"TRIANGULO: {TRIANGULO:.3f}")
print(f"CIRCULO: {CIRCULO:.3f}")
print(f"TRAPEZIO: {TRAPEZIO:.3f}")
print(f"QUADRADO: {QUADRADO:.3f}")
print(f"RETANGULO: {RETANGULO:.3f}")

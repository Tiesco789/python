"""
1. Soma de dois números: Crie um programa que solicite ao usuário dois números e exiba a soma deles
2. Calculadora de idade: Peça ao usuário o ano de nascimento e calcule a idade.
3. Verificador de número par ou ímpar: Solicite um número e determine se ele é par ou ímpar.
4. Conversor de temperatura: Crie um programa que converta uma temperatura em graus Celsius para Fahrenheit.
5. Calculadora de fatorial: Solicite um número inteiro e calcule seu fatorial.
6. Jogo de adivinhação: Crie um jogo simples em que o programa gera um número aleatório e o jogador tenta adivinhar o número.

print("Primeiro exercicio: ")
print("Somar 2 numeros que o usuário digitar")

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
soma = a + b

print(f"A soma de {a} e {b} é {soma}")

print("Segundo exercicio: ")
print("calculadora de idade")

born_year = int(input("Me diga o ano em que você nasceu: "))
age = 2023 - born_year

print(f"voce tem {age} anos")

print("terceiro exercicio: ")
print("Verificar se o numero é par ou impar")

num = int(input("Digite um número: "))

if num % 2 == 0:
    print("Número par")
else:
    print("Numero impar")


print("quarto exercicio")
print("Conversor de temperatura de Celsiu para Fahrenheit")

celsius = float(input("Digite uma temperatura em celsius: "))
ftemp = (1.8 * celsius) + 32

print(f"a temperatura em Fahrenheit é {ftemp}")

print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')
"""

nome = "Luiz"
idade = 23
formato = f'{nome} tem {idade:.2f} anos'
print(formato)

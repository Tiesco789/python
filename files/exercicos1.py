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
nome = "Luiz"
idade = 23
formato = f'{nome} tem {idade:.2f} anos'
print(formato)

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

nome = 'Franccesco Bordon'
altura = 1.83
peso = 86.60
imc = peso / (altura ** 2)
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é de {imc:.2f}'
print(linha_1)
print(linha_2)

a = 'AAAAA'
b = 'BBBBB'
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f} '
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)

idade = input("Qual a sua idade: ")
print(f'o seu nome é {idade}')
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == "entrar":
    print('Você entrou no sistema')
elif entrada == "sair":
    print('Você saiu do sistema')
else:
    print('Você não digitou nem "entrar" e nem "sair"')


print('Fora dos blocos')

condicao = True
if condicao:
    print('Este é o código do if')
else:
    print('')

print(1)


primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(f'o {primeiro_valor=} é maior ou igual ao {segundo_valor=}')
else:
    print(f'o {segundo_valor=} é maior ou igual ao {primeiro_valor=}')


entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# If condição
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
"""
if 1 and 1:
    print(True and 1 and False)

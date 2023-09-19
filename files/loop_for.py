"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java:
    for(int i = 0; i < 10; i++) {
        // Execução
    }

Python:
    for item in interavel:
        // Execução

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de Iteráveis:
    - String
        nome = 'Geek University'
    - Lista
        lista = [1, 2, 3, 4, 5]
    - Range
        numeros = (1, 10)


    # 1. Exemplo de for (iterando em um string)
    print("-----")
    print("Exemplo 1")
    for letra in nome:
        print(letra)

    # 2. Exemplo de for (iterando sobre uma lista)
    print("-----")
    print("Exemplo 2")
    for numeros in lista:
        print(numeros)


    # 3. Exemplo de for (iterando sobre o range)
    print("-----")
    print("Exemplo 3")
    for numeros in range(1, 10):
        print(numeros)

    # 4. Exemplo de for (iterando usando enumerate)
    print("-----")
    for _, letra in enumerate(nome):
        print(letra)

    OBS: Quando não pr3ecisamos de um valor, podemos descartá-lo usando um underline (_)
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor: '))
    soma = soma + num

print(f'A soma é {soma}')

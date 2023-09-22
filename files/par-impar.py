while True:
    try:
        num = int(input("Digite um número: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

if num % 2 == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")


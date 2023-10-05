valor = tuple(map(int, input("").split()))

A = valor[0]
B = valor[1]
C = valor[2]

if A > B and A > C:
    print(f"{A} eh o maior")
elif B > C:
    print(f"{B} eh o maior")
else:
    print(f"{C} eh o maior")

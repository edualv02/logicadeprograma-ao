a = 0
b = 1

print(a, end=" ")  # Imprime o primeiro termo da sequência
print(b, end=" ")  # Imprime o segundo termo da sequência

while b <= 500:
    c = a + b
    print(c, end=" ")
    a = b
    b = c

print()  # Imprime uma quebra de linha após a sequência
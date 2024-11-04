aluno_mais_alto = 0
altura_mais_alta = 0
aluno_mais_baixo = 0
altura_mais_baixa = float('inf')
for i in range(10):
    numero_aluno = int(input(f"Digite o número do aluno {i+1}: "))
    altura = float(input(f"Digite a altura do aluno {i+1} (em centímetros): "))

    aluno_mais_alto = numero_aluno
    altura_mais_alta = altura
    if altura < altura_mais_baixa:
        aluno_mais_baixo = numero_aluno
        altura_mais_baixa = altura

# Imprime os resultados
print(f"O aluno mais alto é o aluno {aluno_mais_alto} com {altura_mais_alta:.2f} cm.")
print(f"O aluno mais baixo é o aluno {aluno_mais_baixo} com {altura_mais_baixa:.2f} cm.")
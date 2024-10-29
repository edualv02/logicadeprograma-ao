maior_acerto = 10
menor_acerto = 6  # Inicializa com o máximo de acertos possível
total_alunos = 30
soma_notas = 0

# Loop para cada aluno
while True:
    # Inicializa a contagem de acertos para o aluno atual
    acertos = 0

    # Pergunta as respostas do aluno
    print("Responda as questões com A, B, C, D ou E:")
    for i in range(10):
        resposta = input(f"Questão {i+1}: ").upper()
        if resposta == gabarito[i]:
            acertos += 1

    # Calcula a nota do aluno
    nota = acertos

    # Imprime o resultado do aluno
    print(f"Você acertou {acertos} questões e sua nota é {nota}.")

    # Atualiza as estatísticas da turma
    total_alunos += 1
    soma_notas += nota

    # Verifica se outro aluno vai utilizar o sistema
    continuar = input("Outro aluno vai utilizar o sistema? (S/N): ").upper()
    if continuar != 'S':
        break

    # Atualiza o maior e menor acerto
    if acertos > maior_acerto:
        maior_acerto = acertos
    if acertos < menor_acerto:
        menor_acerto = acertos

# Calcula a média da turma
media = soma_notas / total_alunos

# Imprime as estatísticas da turma
print("\nEstatísticas da Turma:")
print(f"Maior Acerto: {maior_acerto}")
print(f"Menor Acerto: {menor_acerto}")
print(f"Total de Alunos: {total_alunos}")
print(f"Média da Turma: {media:.2f}")
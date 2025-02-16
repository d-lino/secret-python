# Missão 1: Restaurando as Regras Escolares 📝

nota = float(input("Digite a nota do aluno: "))

if nota >= 6:
    print("O aluno está aprovado")
elif nota <= 5:
    print("O Aluno foi reprovado!")
else:
    print("Nota inválida!")

# Missão 2: O Sistema Eleitoral Secreto 📝 

dianna = 17

if dianna >= 16:
    print("pode votar")
else:
    print("não pode votar")

# Missão 3: Recuperando o Sistema de Notas 📊

nota_aluno = int(input("Digite a nota do aluno: "))

if nota_aluno >= 90:
    print("parabéns você tirou A!")
elif nota_aluno >= 80:
    print("Muito bem, você tirou B")
elif nota_aluno >= 70:
    print("Bom trabalho, você tirou C")
elif nota_aluno >= 60:
    print("Fique atento! você tirou D")
elif nota_aluno < 60:
    print("Estude mais! você tirou F")
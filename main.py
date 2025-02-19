# Missão 1: Restaurando as Regras Escolares 

nota = float(input("Digite a nota do aluno: "))

if nota >= 6:
    print("O aluno está aprovado")
elif nota <= 5:
    print("O Aluno foi reprovado!")
else:
    print("Nota inválida!")

# Missão 2: O Sistema Eleitoral Secreto 

dianna = 17

if dianna >= 16:
    print("pode votar")
else:
    print("não pode votar")

# Missão 3: Recuperando o Sistema de Notas 

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

# Missão 4: Restaurando a Identificação de Números

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2

print("A soma de", numero1, "e", numero2, "é:", soma)

# Missão 5: Recuperando o Cofre de Segurança

senha = input("digite a senha: ")

if senha == "Python123":
    print("Acesso liberado!")
else:
    print("Senha incorreta!")

# Missão 6: Reforçando a Segurança e a Contagem do Sistema

contador = 0

while contador < 10:
    contador += 1
    print(contador)

# Missão 7: Organizando a Lista

numeros = [ 8, 3, 10, 1, 5]
numeros.sort()
print(numeros)


# Missão 8: Acessando os Registros de Alunos 

alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
print(alunos[0], alunos[-1])


# Missão 9: Calculando Dobro de um Número 

valor = int(input("Digite um número: "))
print(f"O dobro de {valor} é:",valor * 2)

# Missão 10: Contando Letras 

nome = input("Digite o nome: ")
quantidade = len(nome)
print(f"O nome {nome} tem {quantidade} letras")

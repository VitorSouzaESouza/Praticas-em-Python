#Exercício do slide 88
# prova1 = float(input("Digite a nota da prova 1: "))
# prova2 = float(input("Digite a nota da prova 2: "))
# trabalho = float(input("Digite a nota do trabalho: "))
# media = ((prova1 + prova2)*0.7+trabalho*0.3)/3
# print("A média é", media)

#Exercício do slide 94
# angulo = float(input("Digite um ângulo: "))
# quadrante = ''
# if angulo<0:
#     angulo += 360
# if angulo%360 >= 0 and angulo%360 < 90:
#     quadrante = 'primeiro'
# elif angulo%360 >= 90 and angulo%360 < 180:
#     quadrante = 'segundo'
# elif angulo%360 >= 180 and angulo%360 < 270:
#     quadrante = 'terceiro'
# else:
#     quadrante = 'quarto'
# print("Está no", quadrante, "quadrante.")

#Exercício do slide 102
# a1 = 2
# razao = 3
# soma = 0
# an = a1
# while an<=100:
#     soma += an
#     an += razao
# print("A soma da PA é", soma)

#Exercício do slide 105
# notas = []
# soma = 0
# media = 0
# numAlunos = int(input("Número de alunos: "))
# for i in range(numAlunos):
#     nota = float(input("Nota do aluno: "))
#     notas.append(nota)
#     soma += nota
# media = soma/numAlunos
# print("A média da turma é", media)

#Exercício do slide 109
# matriz = [[0,0,0],[0,0,0],[0,0,0]]
# soma = 0
# for i in range(3):
#     for j in range(3):
#         num = int(input("Digite um número inteiro: "))
#         matriz[i][j] = num
#         if i==j:
#             soma += num
# print("A soma dos elementos da diagonal principal é", soma)
import pandas as pd
import os

aluno, nota1, nota2 = [], [], []

while True:
  a = input("Digite o nome ou enter para sair: ")
  if a == "":
    break
  aluno.append(a)
  n1 = float(input('Digite a nota 1: '))
  nota1.append(n1)
  n2 = float(input('Digite a nota 2: '))
  nota2.append(n2)

tabela = pd.DataFrame(data=zip(aluno, nota1, nota2), columns=['Aluno', 'Nota_1', 'Nota_2'])
tabela["Média"] = tabela[['Nota_1', 'Nota_2']].mean(axis=1)
os.system('clear')
print(tabela)

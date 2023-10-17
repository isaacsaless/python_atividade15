# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR

print("Descubra se um triângulo é real")
l1 = float(input("Digite o 1° lado do triângulo: "))
l2 = float(input("Digite o 2° lado do triângulo: "))
l3 = float(input("Digite o 3° lado do triângulo: "))

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    print("Você pode formar um triângulo com essas medidas.")
else:
    print("Você não pode formar um triângulo com essas medidas.")
print("Algoritmo do voto obrigatótio")

idade = int(input("Digite a sua idade: "))

if (idade >= 18 and idade < 65):
    print("Voto Obrigatório!")
elif (16 <= idade < 18 or idade >= 65):
    print("Voto opcional!")
else:
    print("Voto não permitido!")

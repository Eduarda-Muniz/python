# Definindo os preços dos ingressos
inteira = 20.00
meia = 10.00

# Entrada de dados do usuário
idade = int(input("Escreva a sua idade: "))

# Determinando o preço com base na idade
if idade < 18 or idade >= 60:
    preco = meia
else:
    estudante = input("A pessoa é estudante? (sim/não): ")
    preco = meia if estudante == "sim" else inteira

# Exibindo o preço do ingresso
print(f"Preço do ingresso: R$ {preco:.2f}")
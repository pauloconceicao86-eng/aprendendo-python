produto = input("qual produto deseja comprar? ")
preco = float(input("qual o preço do produto? "))
quantidade = int(input("quantas unidades deseja comprar? "))
total = preco * quantidade

if total > 100:
    desconto = total * 0.10
else:
    desconto = 0

total_com_desconto = total - desconto
print(f"Você comprou {quantidade} unidades de {produto} por R${total:.2f}.")
print(f"Você recebeu um desconto de R${desconto:.2f}.")
print(f"O total a pagar com desconto é R${total_com_desconto:.2f}.")
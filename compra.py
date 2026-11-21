produto = input("qual produto deseja comprar? ")
preco = float(input("qual o preço do produto? "))
quantidade = int(input("quantas unidades deseja comprar? "))
total = preco * quantidade
print(f"Você comprou {quantidade} unidades de {produto} por R${total:.2f}.")
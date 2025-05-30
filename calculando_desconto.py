# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço=float(input('Digite o preço do produto: R$ '))
novo_preço = preço - (preço * 5/100)
print('o preço do produto que custava R$ {:.2f} na promoção com desconto de 5% vai custar R${}'.format(preço,novo_preço))
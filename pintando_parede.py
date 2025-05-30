# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg=float(input('Largura da parede:'))
alt=float(input('Altura da parede:'))
area=larg*alt
print (f'A área da parede é {area} m²')
tinta=area/2      
print (f'Você precisará de {tinta} litros de tinta para pintar a parede.')
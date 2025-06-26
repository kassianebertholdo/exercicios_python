#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid=str(input('Em que cidade voce nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

# Verifica se a cidade começa com "SANTO"
# A função strip() deve ser chamada com parênteses para funcionar corretamente
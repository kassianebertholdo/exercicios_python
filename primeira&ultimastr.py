# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()
print ( 'A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print ('A letra "A" aoarece pela primeira vez na posiçaõ{} e pela ultima vez na posiçaõ {}'.format(frase.find('A')+1,frase.rfind('A')+1))
# A função strip() remove os espaços no início e no final da string.   
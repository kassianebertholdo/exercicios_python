# Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome =input('Digite seu nome completo:')
print('Seu nome em maiúscula é :', nome.upper())
print('seu nome tem',len(nome.replace("","")),'letras ao todo sem considerar espaços.')
print('Seu primeiro nome tem',len(nome.split()[0]),'letras.')



nome=str(input('Digite seu nome completo:'))
print("Analisando seu nome........")
print ('seu nome com letras maiscula é {}' .format(nome.upper()))
print('E com minusculas é  :{}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras sem considerar os espaços.' .format(len(nome)))
print('Seu primeiro nome tem {} letras.' .format(len(nome.split()[0])))
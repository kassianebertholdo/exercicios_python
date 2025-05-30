#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario =float (input('Informe o salário do funcionario: '))
novo_salario = (salario * 15/100)
print('o novo salario do funcionario é R$ {:.2f}' .format(salario + novo_salario   ))
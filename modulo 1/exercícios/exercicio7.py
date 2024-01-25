'''Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente,
adulto ou idoso.'''

idade = int(input('Por favor, insira sua idade: '));

if idade<=13:
    print('De acordo com a classificação você se enquadra como criança');
elif idade<=21:
    print('De acordo com a classificação você se enquadra como adolescente');
elif idade<=65:
    print ('De acordo com a classificação você se enquadra como adulto');
else:
    print ('De acordo com a classificação você se enquadra como idoso');
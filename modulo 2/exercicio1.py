'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"",
entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"".
Caso contrário,ele será classificado como""Inocente"".'''

positivo = 0
resposta = input('Telefonou para a vítima? (sim ou não) ');
if resposta == "sim":
    positivo += 1

resposta = input('Esteve no local do crime? (sim ou não) ');
if resposta == "sim":
    positivo += 1

resposta = input('Mora perto da vítima? (sim ou não) ');
if resposta == "sim":
    positivo += 1

resposta = input('Devia para a vítima? (sim ou não) ');
if resposta == "sim":
    positivo += 1

resposta = input('Já trabalhou com a vítima? (sim ou não) ');
if resposta == "sim":
    positivo += 1

if positivo < 2:
    print('Inocente');
elif positivo == 2:
    print('Suspeito');
elif positivo < 5:
    print('Cúmplice');
else:
    print('Culpado');
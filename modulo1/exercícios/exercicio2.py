'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou
N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = input('Você estuda em qual turno? M-Matutino, V-Vespertino ou N-Noturno? ');

if turno == 'M-Matutino':
    print('Bom dia!');
elif turno == 'V-Vespertino':
    print('Boa tarde!');
elif turno == 'N-Noturno':
    print('Boa noite!');
else:
    print('Valor Inválido');

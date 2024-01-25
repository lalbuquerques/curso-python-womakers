'''Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas se
o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.'''

login = input('Insira seu nome de usuário: ');
senha = input('Insira sua senha: ');

if login == 'admin'and senha =='admin123':
    print('Acesso liberado');
else:
    print('Erro, verifique sua senha e seu usuário');
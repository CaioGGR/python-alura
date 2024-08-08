# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

n = int(input('Digite um numero: '))

if n % 2 != 0:
  print('impar')
else:
  print('par')
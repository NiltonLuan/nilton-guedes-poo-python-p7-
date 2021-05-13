def verificacao(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    else:
        if a < b + c and b < a + c and c < a + b:
            return True
        return False

print('Esse programa foi feito para conferir se três comprimentos conseguem \
formar um triângulo\n')
a = int(input('Digite o Primeiro Lado do Triângulo: '))
b = int(input('Digite o Segundo Lado do Triângulo: '))
c = int(input('Digite o Terceiro Lado do Triângulo: '))

verificar = verificacao(a, b, c)

if verificar:
  print('\nTriângulo possível!')
else:
  print('\nNão é possível fazer um triângulo!')

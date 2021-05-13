"""Questão: O triângulo pode ser classificado com base no comprimento de
seus lados em equilátero, isósceles ou escaleno. Todos os três lados de um
triângulo equilátero têm o mesmo comprimento. Um triângulo isósceles tem dois
lados que são do mesmo comprimento e um terceiro lado que é diferente comprimento.
Se todos os lados tiverem comprimentos diferentes, o triângulo é escaleno.  
Escreva um programa que leia os comprimentos dos três lados de um triângulo do usuário. Em seguida, exiba uma mensagem que declara o tipo do triângulo."""

print('Bem-vindo ao confere triângulo"\n')


#Primeira checagem, ver se os valores são float!
try:
	#Aqui pedimos para o usuário entrar com os valores do triangulo
	a = float(input('Digite o Primeiro Lado do Triângulo: '))
	b = float(input('Digite o Segundo Lado do Triângulo: '))
	c = float(input('Digite o Terceiro Lado do Triângulo: '))

#Exibir essa mensagem de erro caso o usuário entre com valores diferentes de float!
except:
	print ('\nDigite números válidos!')

#Segunda checagem, ver se o triângulo tem valores maiores que zero
if a == 0 or b == 0 or c == 0:
	print('\nEsse triângulo não existe')
else:
	if a == b and b == c:
		print('\nO Triângulo é Equilátero')
	elif a == b or a == c or b == c:
		print('\nO Triângulo é Isósceles')
	else:
		print('\nO Triângulo é Escaleno')

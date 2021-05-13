"""
Questão: 3) Lista Encadeada (A retirada e a inserção de elementos se faz em qualquer posição da Lista). Usar os métodos da Lista Python que fazem menção nos seus parâmetros a índices.
"""
import random

#Vamos imaginar uma lista inicial de exercícios
lista_encadeada = []
i = 0
while (i != 5):
	a = input ('Adicione um exercício a lista:')
	lista_encadeada.insert(i, a)
	print (f'Adicionei o exercício [{a}] na lista!\n')
	i = i + 1

#Vamos printar o nosso resultado inicial
print (lista_encadeada)

# Adicionando mais itens
lista_encadeada.insert(0, 'polichinelo')
lista_encadeada.insert(4, 'agachamento')


# Mostrando a lista
print(f'\nA lista de exercícios contém: {len(lista_encadeada)}')
print(f'Esses são os exercícios: {lista_encadeada}\n')

#Deletando exercícios
posicao = list(range(1,5))
random.shuffle(posicao)

for i in posicao:
  print('Concluindo exercício: %s' % lista_encadeada[i])
  lista_encadeada.pop(i)
		

# Mostrando a lista atual
print(f'\nA lista contém {len(lista_encadeada)} exercícios a serem feitos')
print(f'Exercícios: {lista_encadeada}\n')

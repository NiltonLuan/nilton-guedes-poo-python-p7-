"""Questão: Para ganhar o prêmio máximo na Mega Sena, é necessário acertar todos os 6 números em seu bilhete com os 6 números entre 1 e 60 sorteados.
Escreva um programa que gere uma seleção aleatória de 6 números para uma aposta. Certifique-se de que os 6 números selecionados não contenham duplicatas. Exibir os números em ordem crescente."""

from random import randint

numeros = []

while len(numeros) < 6:
  sorteio = randint(1, 60)
  if sorteio not in numeros:
    numeros.append(sorteio)

numeros.sort()

print('Os números ideais são:', numeros)

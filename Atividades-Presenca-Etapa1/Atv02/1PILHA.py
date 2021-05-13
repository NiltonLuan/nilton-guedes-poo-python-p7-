"""
Questão: 1) Pilha (inserir e retirar pelo topo da Pilha). Considerar o topo como sendo o índice 0 da Lista.
"""

#Declarando nossa pilha
#de maneira didática usarei um exemplo: Uma pilha de papéis
pilha = [5,4,3,2,1]

#Colocando mais papéis na nossa pilha
for x in range(6, 10):
    print(f'O papel [{x}] foi colocado em cima da pilha')
    pilha.insert(0, x)

# Mostrando nossa pilha de papéis
print('\nTotal de papéis na pilha: %s' % len(pilha))
print('Papéis: %s\n' % pilha)

#Agora vamos arrumar nossa pilha!
for x in range(len(pilha),0,-1):
    print(f'Papel [{x}] foi retirado da pilha')
    pilha.pop(0)

#Resultado final
print('\nNúmero de papéis restantes: %s' % len(pilha))
print('Papeis:', pilha)

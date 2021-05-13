"""Questão 
2) Fila (Inserir no final da Fila. Considerar o final da fila o elementode maior índice positivo.
Retirar da Fila pelo elemento do inicio da Lista que tem o índice 0.)""" 

#Lista com alguns elementos que representarão a nossa fila
fila = [1,2,3,4,5,6,7,8]

#Loop para adicionar mais elementos a lista
for x in range(9, 15)
    print(F'Elemento [{x}] foi adicionado no fim da fila')
    fila.append(x)

#Vamos printar nossa fila atual
print('nEsse é o tamanho da nossa fila %s' % len(fila))
print('Esse são os elementos da fila %sn' %fila)

#Removendo elementos
for i in range(1, 15)
    print(F'Elemento [{i}] foi removido da fila da fila')
    fila.pop(0)


#Printando a fila novamente
print('nEsse é o tamanho atual da fila %s' % len(fila))
print('Essa é a nossa fila agora', fila)

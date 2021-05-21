from Folha_Pagamento import FolhaPagamento
from colaborador import Colaborador
from Movimento_Folha import MovimentoFolha
from Tipo_Movimento import TipoMovimento

if __name__ == '__main__':

# QUESTÃO 1:
    FP = FolhaPagamento(9, 2019)

# QUESTÃO 2:
    CL01 = Colaborador(100, 'Manoel Claudino', 'Av 13 de Maio 2081', '88671020', 'Benfica', '60020-060', '124543556-89', 4500)
    CL02 = Colaborador(200, 'Carmelina da Silva', 'Avenida dos Expedicionários 1200', '3035-1280', 'Aeroporto', '60530-020', '301789435-54', 2500)
    CL03 = Colaborador(300, 'Gurmelina Castro Saraiva', 'Av João Pessoa 1020', '3235-1089', 'Damas', '60330-090', '350245632-76', 3000)

# QUESTÃO 3:
    MF1 = MovimentoFolha(CL01, 'Gratificação', 4500, TipoMovimento.P)
    MF2 = MovimentoFolha(CL01, 'Plano Saúde', 1000, TipoMovimento.P)
    MF3 = MovimentoFolha(CL01, 'Pensão', 600, TipoMovimento.D)
    MF4 = MovimentoFolha(CL02, 'Gratificação', 2500, TipoMovimento.P)
    MF5 = MovimentoFolha(CL02, 'Plano Saúde', 1000, TipoMovimento.P)
    MF6 = MovimentoFolha(CL02, 'Faltas', 600, TipoMovimento.D)
    MF7 = MovimentoFolha(CL03, 'Gratificação', 4500, TipoMovimento.P)
    MF8 = MovimentoFolha(CL03, 'Plano Saúde', 1000, TipoMovimento.P)
    MF9 = MovimentoFolha(CL03, 'Pensão', 600, TipoMovimento.D)


#Organizando todos os movimentos em uma lista para facilitar organização e loops:
    MF = [MF1, MF2, MF3, MF4, MF5, MF6, MF7, MF8, MF9]

#QUESTÃO 6:
    for x in MF:
        FP.inserirmovimentos(x)

#QUESTÃO 7:
    cont = int(len(MF)/3)
    for i in range(0, cont):
        CL01.inserirmovimentos(MF[i])
        cont = cont + 1
    for m in range(3, cont):
        CL02.inserirmovimentos(MF[m])
        cont = cont + 1
    for n in range(6, cont):
        CL03.inserirmovimentos(MF[n])
        cont = cont + 1

#Fim:
    FP.calcularfolha()

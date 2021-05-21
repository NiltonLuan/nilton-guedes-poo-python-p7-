from Tipo_Movimento import TipoMovimento
from Movimento_Folha import MovimentoFolha
from colaborador import Colaborador

class FolhaPagamento:
    def __init__(self, mes, ano):
        self._mes = mes
        self._ano = ano
        self._total_descontos = 0
        self._total_proventos = 0
        self._movimentos = []
        self._colaboradores = []

    def get_mes(self):
        return self._mes

    def set_mes(self, mes):
        self._mes = mes


    def get_ano(self):
        return self._ano

    def set_ano(self, ano):
        self._ano = ano


    def get_total_descontos(self):
        return self._total_descontos

    def get_total_proventos(self):
        return self._total_proventos

    def get_movimentos(self):
        return self._movimentos


# Questão 4:
    def inserirmovimentos(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self._movimentos.append(movimento)
            self._colaboradores.append(movimento.get_colaborador())
            return 'Movimento adicionado'
        else:
            return 'Error ao adicionar o movimento'


#Questão 8:
    def calcularfolha(self):

        for movimento in self._movimentos:
            if movimento.get_tipo_movimento() == TipoMovimento.P:
                self._total_proventos += movimento.get_valor()
            elif movimento.get_tipo_movimento() == TipoMovimento.D:
                self._total_descontos += movimento.get_valor()
            else:
                print('Error')

        #Como na função anterior acaba repetindo três vezes cada um, precisei de um método para ficar
        # com apenas uma das três repetições
        colab = []
        for x in range(0, len(self._colaboradores), 3):
            colab.append(self._colaboradores[x])

        total_salarios = 0
        for colaborador in colab:
            total_salarios += colaborador.get_salarioatual()

        total_pagar = (total_salarios + self._total_proventos) - self._total_descontos

        resultado = f'Folha de Pagamento({self._mes}/{self._ano}):\n\n'\
                    'Total de Salários = %10.2f    Total de Proventos = %10.2f    Total de Descontos = %10.2f\nTotal' \
                    ' a Pagar = %10.2f\n' % (total_salarios, self._total_proventos, self._total_descontos, total_pagar)


        for i, colaborador in enumerate(colab):
            resultado += f'\nColaborador {i + 1}:\n{colaborador.calcularsalario()}'

        return print(resultado)






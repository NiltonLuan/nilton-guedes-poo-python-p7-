from Tipo_Movimento import TipoMovimento
from Movimento_Folha import MovimentoFolha


class Colaborador:
    def __init__(self, codigo, nome, endereco, telefone, bairro, CEP, CPF, salarioatual):
        self._codigo = codigo
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._bairro = bairro
        self._CEP = CEP
        self.__CPF = CPF
        self._salarioatual = salarioatual
        self._movimentos = []
        self._colaboradores = []

    def get_codigo(self):
        return self._codigo

    def set_codigo(self, codigo):
        self._codigo = codigo


    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome


    def get_endereco(self):
        return self._endereco

    def set_endereco(self, endereco):
        self._endereco = endereco


    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone


    def get_bairro(self):
        return self._bairro

    def set_bairro(self, bairro):
        self._bairro = bairro


    def get_cep(self):
        return self._CEP

    def set_cep(self, CEP):
        self._CEP = CEP


    def get_cpf(self):
        return self.__CPF

    def set_cpf(self, CPF):
        self.__CPF = CPF


    def get_salarioatual(self):
        return self._salarioatual

    def set_salarioatual(self, salarioatual):
        self._salarioatual = salarioatual

#QUESTÃO 5:
    def inserirmovimentos(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self._movimentos.append(movimento)
            self._colaboradores.append(movimento.get_colaborador())
            return 'Movimento adicionado'
        else:
            return 'Error ao adicionar o movimento'

#QUESTÃO 9:
    def calcularsalario(self):
        total_proventos = 0
        total_descontos = 0

        for movimento in self._movimentos:
            if movimento.get_tipo_movimento() == TipoMovimento.P:
                total_proventos += movimento.get_valor()
            elif movimento.get_tipo_movimento() == TipoMovimento.D:
                total_descontos += movimento.get_valor()
            else:
                print('Error')

        valor_liquido = (self._salarioatual + total_proventos) - total_descontos
        return 'Codigo: %4d    Nome: %s\
                \nSalário: %10.2f    Total Proventos: %10.2f    Total Descontos: %10.2f\
                \nValor Líquido a Receber: %10.2f\n' % (self._codigo, self._nome, self._salarioatual, total_proventos,
                                                        total_descontos, valor_liquido)


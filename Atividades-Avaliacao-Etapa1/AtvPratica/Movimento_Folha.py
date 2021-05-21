class MovimentoFolha:

    def __init__(self, colaborador, descricao, valor, tipomovimento):
        self._colaborador = colaborador
        self._descricao = descricao
        self._valor = valor
        self._tipo_movimento = tipomovimento


    def get_colaborador(self):
        return self._colaborador

    def set_colaborador(self, colaborador):
        self._colaborador = colaborador


    def get_descricao(self):
        return self._descricao

    def set_descricao(self, descricao):
        self._descricao = descricao


    def get_valor(self):
        return self._valor

    def set_valor(self, valor):
        self._valor = valor


    def get_tipo_movimento(self):
        return self._tipo_movimento

    def set_tipo_movimento(self, tipomovimento):
        self._tipo_movimento = tipomovimento

class cliente:
    def __init__(self, nome: str, documento: str, cnh: str, telefone: str):
        self.nome = nome
        self.documento = documento
        self.cnh = cnh
        self.telefone = telefone

    def aluguel(self, dataInicio: str, dataTermino: str, valor: float, status: str):
        self.contrato = _contrato(dataInicio, dataTermino, valor, status)

class _contrato:
    def __init__(self, dataInicio: str, dataTermino: str, valor: float, status: str):
        self.dataInicio = dataInicio
        self.dataTermino = dataTermino
        self.valor = valor
        self.status = status
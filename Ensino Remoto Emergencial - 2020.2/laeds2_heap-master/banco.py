from functools import total_ordering
from datetime import datetime
from heap import MaxHeap

class Cliente:
    def __init__(self,nome:str, idade:int, necessidades_especiais:bool):
        self.nome = nome
        self.idade = idade
        self.necessidades_especiais = necessidades_especiais

    def __str__(self):
        return self.nome
    def __repr__(self):
        return str(self)

class PrioridadeCliente:
    def __init__(self, cliente:Cliente, prioridade:int):
        self.cliente = cliente
        self.prioridade = prioridade
        self.horario_entrada = datetime.now()

    def __eq__(self, outro:"PrioridadeCliente") ->bool:
        if self is None or outro is None:
            return False
        elif self.cliente == outro.cliente:
            return True

    def __lt__(self,  outro:"PrioridadeCliente") -> bool:
        if self.prioridade == outro.prioridade and self.horario_entrada > outro.horario_entrada:
            return True
        elif self.prioridade < outro.prioridade:
            return True
        else:
            return False

    def __str__(self):
        return f"Cliente: {self.cliente} - Prioridade: {self.prioridade}"

    def __repr__(self):
        return str(self)

class CaixaBanco:
    def __init__(self,nome_banco:str):
        self.fila_prioridade = MaxHeap()

        self.nome_banco = nome_banco

    def adiciona_cliente(self,cliente:Cliente):
        if cliente.idade >= 80: #se o cliente tiver mais que 80 anos a prioridade é 3
            prioridade = 3
        elif 60 < cliente.idade < 80 or cliente.necessidades_especiais: #se o cliente tiver entre 60 e 80 anos ou é portador de necessidades especiais a prioridade é 2
            prioridade = 2
        else:
            prioridade = 1

        nova_prioridade = PrioridadeCliente(cliente, prioridade) #estanciação do objeto da classe PrioridadeCliente enviando como parâmetro o cliente e a prioridade
        self.fila_prioridade.insere(nova_prioridade) #inserindo cliente na fila de prioridade

    def proximo_cliente(self) -> Cliente:
        return self.fila_prioridade.retira_max()

    def __str__(self):
        return f"Banco: {self.nome_banco} \nFila: {self.fila_prioridade}"

    def __repr__(self):
        return str(self)
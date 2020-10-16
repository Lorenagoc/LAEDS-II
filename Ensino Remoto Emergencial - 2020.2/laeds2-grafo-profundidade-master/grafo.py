from collections import defaultdict
from typing import List, Dict
class Vertice:
	def __init__(self, valor):
		self.valor = valor
		self.adjacencias = {}

	def insere(self, vizinho, peso:int):
		self.adjacencias[vizinho] = peso

	def obtem_valor(self):
		return self.valor

class Grafo:

	def __init__(self):
		self.vertices = {}
		self.grafo = defaultdict(list) #criamos esse atributo para fazer um dicionario de listas e facilitar a implementacao

	def adiciona_vertice(self, valor_vertice) -> Vertice:
		#importante pois podem haver vertices que não tem arestas
		novo_vertice = Vertice(valor_vertice)
		self.vertices[valor_vertice] = novo_vertice
		return novo_vertice

	def adiciona_aresta(self, valor_origem, valor_destino, peso:int=1):
		self.grafo[valor_origem].append(valor_destino) #cria uma aresta ligando um vertice u e um vertice v
		vertice_origem = self.obtem_vertice(valor_origem)
		vertice_destino = self.obtem_vertice(valor_destino)
		if not vertice_origem is None and not vertice_destino is None:
			vertice_origem.insere(vertice_destino, peso)

	def obtem_vertice(self, valor_vertice:str) -> Vertice:
		if valor_vertice in self.vertices:
			return self.vertices[valor_vertice]
		else:
			return None

	def vizinhos(self, nodo):
		return self.grafo[nodo] #retorna o vizinho desse nodo especifico

	def e_um_dag(self) -> bool:
		visitados = set() #cria um conjunto
		falta_visitar = [] #cria um array
		for vertice in self.grafo: #percorremos todos os vertices do grafo
			falta_visitar = [vertice] #adicionamos no array
		while falta_visitar: #enquanto ainda ouver vertives sem visitar
			vertice_atual = falta_visitar.pop() #capturamos o primeiro vertice que sera verificado
			visitados.add(vertice_atual) #adicionamos no conjunto de visitados
			for vizinho in self.vizinhos(vertice_atual): #percorremos os vizinhos do vertice
				if vizinho in visitados: #se o vizinho ja tiver sido visitado
					return False #entao houve um ciclo
				falta_visitar.append(vizinho) #adiciona o vizinho no array para que uma busca em profundidade seja feita nele tbm
		return True #nao houve um ciclo

	def ordenacao_topologica(self) -> List[Vertice]:
		ordem_topologica = [] #array que retornara a ordem topologica do grafo
		graus_entrada = [0] * (len(self.grafo) + 1)
		#percorremos cada vertice do grafo e atualizamos o grau de entrada
		for vertice_atual in self.grafo:
			for vizinho in self.vizinhos(vertice_atual):
				graus_entrada[vizinho] += 1

		#fila de vertices com grau de entrada 0 (vertice de origem)
		fila_vertices = []
		for v in range(len(self.grafo)):
				if graus_entrada[v] == 0:
					fila_vertices.append(v)

		#enquanto ainda houver vertices na fila
		while fila_vertices:
			vertice_atual = fila_vertices.pop() #remove o primeiro vertice da fila
			ordem_topologica.append(vertice_atual) #adiciona no array de ordem topologica

			for vizinho in self.vizinhos(vertice_atual): #percorre os vizinhos do vertice atual retirado da fila
				graus_entrada[vizinho] -= 1 #atualiza o grau de entrada dos vizinhos

				#se por acaso o grau de entrada de algum dos vizinhos do vertice atual se tornar zero, inserimos na fila
				if graus_entrada[vizinho] == 0:
					fila_vertices.append(vizinho)

		#retorna a ordem topologica
		return ordem_topologica

'''
if __name__ == "__main__":

	grafo0 = Grafo()

	grafo0.adiciona_vertice(0)
	grafo0.adiciona_vertice(1)
	grafo0.adiciona_vertice(2)
	grafo0.adiciona_vertice(3)
	grafo0.adiciona_vertice(4)
	grafo0.adiciona_vertice(5)
	grafo0.adiciona_vertice(6)

	grafo0.adiciona_aresta(0, 1)
	grafo0.adiciona_aresta(1, 2)
	grafo0.adiciona_aresta(1, 3)
	grafo0.adiciona_aresta(2, 5)
	grafo0.adiciona_aresta(3, 5)
	grafo0.adiciona_aresta(4, 5)

	grafo1 = Grafo()

	grafo1.adiciona_vertice(0)
	grafo1.adiciona_vertice(1)
	grafo1.adiciona_vertice(2)
	grafo1.adiciona_vertice(3)

	grafo1.adiciona_aresta(0, 1)
	grafo1.adiciona_aresta(1, 2)
	grafo1.adiciona_aresta(2, 3)
	grafo1.adiciona_aresta(3, 1)

	if grafo0.e_um_dag() is True:
		print('Nao encontrou um ciclo')
	else:
		print('Encontrou um ciclo')

	if grafo1.e_um_dag() is True:
		print('Nao encontrou um ciclo')
	else:
		print('Encontrou um ciclo')

	print(grafo0.ordenacao_topologica())
'''
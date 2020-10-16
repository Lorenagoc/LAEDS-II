from collections import defaultdict
from typing import List, Dict
class Vertice:
	def __init__(self, valor):
		self.valor = valor
		self.adjacencias = {}

	def insere(self, vizinho : "Vertice", peso:int):
		self.adjacencias[vizinho] = peso

	def obtem_valor(self):
		return self.valor

	#para imprimir

	def __str__(self):
		valor = self.valor
		return str(valor)

	def __repr__(self):
		return self.__str__()

class Grafo:
	def __init__(self):
		self.vertices = {}

	def adiciona_vertice(self, valor_vertice) -> Vertice:
		#importante pois podem haver vertices que não tem arestas
		novo_vertice = Vertice(valor_vertice)
		self.vertices[valor_vertice] = novo_vertice
		return novo_vertice

	def adiciona_aresta(self, valor_origem, valor_destino, peso:int=1):
		vertice_origem = self.obtem_vertice(valor_origem)
		vertice_destino = self.obtem_vertice(valor_destino)
		if not vertice_origem is None and not vertice_destino is None:
			vertice_origem.insere(vertice_destino, peso)

	def obtem_vertice(self, valor_vertice) -> Vertice:
		if valor_vertice in self.vertices:
			return self.vertices[valor_vertice]
		else:
			return None

	def grau_separacao(self, valor_vertice_origem) -> Dict[Vertice,int]:
		distancia = {}
		visitou = {}
		vertice_inicial = self.obtem_vertice(valor_vertice_origem)
		if not vertice_inicial:
			return None
		for vertice in self.vertices.values():
			distancia[vertice] = float("inf")
			visitou[vertice] = False


		fila = [vertice_inicial] #cria uma fila e o vertice_inicial e o primeiro adicionado

		visitou[vertice_inicial] = True #vertice inicial e marcado como visitado
		distancia[vertice_inicial] = 0 #distancia do vertice_inicial para ele mesmo e zero

		while fila: #enquanto ainda houver elementos na fila
			vertice_atual = fila.pop(0) #tira o proximo elemento da fila
			for vizinho in vertice_atual.adjacencias: #percorre os vizinhos do elemento
				if not visitou[vizinho]: #se o vizinho ainda nao foi visitado
					visitou[vizinho] = True #entao o vizinho e marcado como visitado
					distancia[vizinho] = distancia[vertice_atual] + 1 #a distancia do vizinho e a distancia que o vertice atual tem com o vertice anterior + 1
					fila.append(vizinho)  #adiciona o vizinho na fila para suas adjacencias serem analisadas posteriormente

		#agora, iremos percorrer os vertices novamente para encontrar alguem que nao conhece ninguem no grafo ou entao que ninguem no grafo conhece
		fila_para_vertices_nao_visitados = [] #criamos uma outra fila para armazenar esses vertices
		for vertice in self.vertices.values(): #percorre todo o grafo
			if not visitou[vertice]: #se o vertice nao foi visitado
				visitou[vertice] = True #marca como visitado
				fila_para_vertices_nao_visitados.append(vertice) #insere na fila
		while fila_para_vertices_nao_visitados: #enquanto ainda houver algum elemento na fila...
			vertice_atual = fila_para_vertices_nao_visitados.pop(0) #retira o primeiro elemento da fila
			for vizinho in vertice_atual.adjacencias: #percorre os vizinhos desse elemento
				if vizinho is not None: #se o vizinho existir, ou seja, se a pessoa conhece alguem do grafo
					distancia[vertice_atual] = distancia[vertice_atual] + distancia[vizinho] + 1 #entao atualiza a distancia desse vertice

		return distancia

if __name__ == "__main__":

	grafo = Grafo()
	grafo.adiciona_vertice("Alice")
	grafo.adiciona_vertice("Bob")
	grafo.adiciona_vertice("Carol")
	grafo.adiciona_vertice("Daniel")
	grafo.adiciona_vertice("Elisa")
	grafo.adiciona_vertice("Fabio")
	grafo.adiciona_vertice("Gabriel")
	grafo.adiciona_vertice("Igor")
	grafo.adiciona_vertice("Katia")

	grafo.adiciona_aresta("Alice", "Carol")
	grafo.adiciona_aresta("Alice", "Daniel")
	grafo.adiciona_aresta("Alice", "Igor")

	grafo.adiciona_aresta("Bob", "Alice")
	grafo.adiciona_aresta("Bob", "Carol")

	grafo.adiciona_aresta("Carol", "Alice")
	grafo.adiciona_aresta("Carol", "Daniel")

	grafo.adiciona_aresta("Daniel", "Carol")
	grafo.adiciona_aresta("Daniel", "Elisa")

	grafo.adiciona_aresta("Elisa", "Gabriel")

	grafo.adiciona_aresta("Igor", "Daniel")
	grafo.adiciona_aresta("Igor", "Gabriel")

	grafo.adiciona_aresta("Gabriel", "Katia")

	for pessoa, distancia in grafo.grau_separacao("Alice").items():
		print("{} {}".format(pessoa.valor,pessoa.adjacencias.__repr__()))
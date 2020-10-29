from typing import List, Dict
from functools import total_ordering
from heap import MinHeap
class Vertice:
	def __init__(self, valor):
		self.valor = valor
		self.adjacencias = {}

	def insere(self, vizinho:"Vertice", peso:int):
		self.adjacencias[vizinho] = peso

	def obtem_valor(self):
		return self.valor

@total_ordering
class PesoVertice:
	def __init__(self, vertice_destino:Vertice, peso:int):
		self.vertice_destino = vertice_destino 
		self.peso = peso

	def __eq__(self, outro:"PesoVertice") ->bool:
		return self.vertice_destino.valor == outro.vertice_destino.valor and self.peso == outro.peso
	
	def __lt__(self,  outro:"PesoVertice") -> bool:
		return self.peso < outro.peso

	def __str__(self):
		return f"Peso até {self.vertice_destino.valor}: {self.peso}"
	
	def __repr__(self):
		return str(self)


class Grafo:
	def __init__(self):
		self.vertices = {}

	def adiciona_vertice(self, valor_vertice) -> Vertice:
		#importante pois podem haver vertices que não tem arestas
		novo_vertice = Vertice(valor_vertice)
		self.vertices[valor_vertice] = novo_vertice
		return novo_vertice

	def adiciona_aresta(self, valor_origem, valor_destino, peso:int=1, bidirecional = False):
		vertice_origem = self.obtem_vertice(valor_origem)
		vertice_destino = self.obtem_vertice(valor_destino)
		if not vertice_origem is None and not vertice_destino is None:
			vertice_origem.insere(vertice_destino, peso)
			if bidirecional:
				vertice_destino.insere(vertice_origem,peso)	


	def obtem_vertice(self, valor_vertice) -> Vertice:
		if valor_vertice in self.vertices:
			return self.vertices[valor_vertice]
		else:
			return None

			
	def cria_arv_geradora_minima(self, valor_vertice_inicial) -> Dict[Vertice,Vertice]:
		pai = {}
		fila_min_heap = MinHeap()
		set_ja_explorado = set()
		peso = {}
		vertice_inicial = self.obtem_vertice(valor_vertice_inicial)

		if not vertice_inicial:
			return None

		#para cada u que pertence aos vertices do grafo faca:
		for vertice in self.vertices.values():
			#pai[u] <- NULL
			pai[vertice] = None
			#menor_peso[u] <- infinito
			peso[vertice] = PesoVertice(vertice, float("inf"))

		#menor_peso[raiz] <- 0
		peso[vertice_inicial].peso = 0
		#INSERE(Q,raiz)
		fila_min_heap.insere(peso[vertice_inicial])

		#enquanto a fila nao estiver vazia
		while len(fila_min_heap.arr_heap)>1:
			#u <- EXTRAI_MIN(Q)
			peso_vertice_u = fila_min_heap.retira_min()

			#acha o vertice correspondente ao peso extraido da fila
			for vertice, valor in peso.items():
				if valor == peso_vertice_u:
					vertice_u = vertice

			#A <- A U {u}
			set_ja_explorado.add(vertice_u)

			#para cada vertice v adjacente ao vertice u faca:
			for vertice_v in vertice_u.adjacencias.keys():
				peso_aresta_uv = vertice_u.adjacencias[vertice_v]

				#se o vertice v ainda nao foi visitado e se o peso da aresta uv for menor que o menor peso vinculado ao vertice v faca:
				if vertice_v not in set_ja_explorado and peso_aresta_uv < peso[vertice_v].peso:
					#pai[v] <- u
					pai[vertice_v] = vertice_u
					#menor_peso[v] <- w[u,v]
					peso[vertice_v].peso = peso_aresta_uv
					#INSERE(Q,v)
					fila_min_heap.insere(peso[vertice_v])

		#retorna o caminho da arvore criada
		return pai

class GrafoMatrizAdjacencia(Grafo):
	def __init__(self):
		super().__init__()
		self.vertice_to_idx = {}
		self.idx_to_vertice = {}
		self.matriz_adjacencia = []

	def adiciona_aresta(self, valor_origem, valor_destino, peso:int=1) :
		
		vertice_origem,vertice_destino = super().__init__(valor_origem,valor_destino, peso)
		
		vertice_origem = self.obtem_vertice(valor_origem)
		vertice_destino = self.obtem_vertice(valor_destino)

		idx_origem = self.vertice_to_idx[vertice_origem]
		idx_destino = self.vertice_to_idx[vertice_destino]
		
		self.matriz_adjacencia[idx_origem,idx_destino] = peso

	def adiciona_vertice(self, valor_vertice) -> Vertice:
		#importante pois podem haver vertices que não tem arestas
		novo_vertice = super().adiciona_vertice(valor_vertice)

		#posicao referente a este vertice na matriz de adjacencia
		pos_novo_vertice = len(self.matriz_adjacencia)
		self.vertice_to_idx[novo_vertice] = pos_novo_vertice
		self.idx_to_vertice[pos_novo_vertice] = novo_vertice

		#inicializa na matriz d adjacencia
		for i in range(len(self.matriz_adjacencia)):
			self.matriz_adjacencia[i].append(0)
		
		self.matriz_adjacencia.append([])
		for j in range(len(self.matriz_adjaccencia)):
			self.matriz_adjacencia[pos_novo_vertice,j] = 0
		
		return novo_vertice


	def cria_arv_geradora_minima(self, valor_vertice_inicial) -> Dict[Vertice,Vertice]:
		pai = {}
		vertice_inicial = self.obtem_vertice(valor_vertice_inicial)
		if not vertice_inicial:
			return None

		idx_vertice_inicial = self.vertice_to_idx[vertice_inicial]
		vertices_arvore = set()


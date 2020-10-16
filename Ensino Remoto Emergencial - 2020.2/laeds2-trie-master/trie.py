from typing import List
import collections
class NoTrie:
	def __init__(self, letra = "", fim_palavra : bool = False):

		self.filhos = dict()
		self.fim_palavra = fim_palavra
		self.letra = letra

	##@property
	def insere(self, letra:str, fim_palavra:bool):
		self.filhos[letra] = NoTrie(letra, fim_palavra)

	def existe_letra(self, letra:str) -> bool:
		return letra in self.filhos

	def obtem_no_filho(self,letra:str) -> "NoTrie":
		return self.filhos[letra]

	def nos_filhos(self) -> List[str]:
		return self.filhos.keys()

class Trie:
	def __init__(self, raiz=None):
		if not raiz:
			raiz = NoTrie()
		self.raiz = raiz

	def insere(self, palavra:str):
		no_atual = self.raiz

		for i,letra in enumerate(palavra):
			if not no_atual.existe_letra(letra):
				no_atual.insere(letra, i == len(palavra)-1)

			no_atual = no_atual.obtem_no_filho(letra)
		no_atual.fim_palavra = True

	def pesquisa(self, palavra:str) -> bool:

		current_node = self.raiz #o no atual recebe a raiz
		for letra in palavra: #percorremos a palavra para verificar letra por letra
			if letra not in current_node.filhos: #se a letra nao e um filho do no atual retornamos false
				return False
			current_node = current_node.obtem_no_filho(letra) #o no atual recebe o no filho do no que possui a letra que estamos verificando no momento
		return True #retorna true se a todas as letras da palavra foram achadas

	def preditor(self, prefixo_palavra:str) -> List[str]:
		#obtem a ultima letra do prefixo
		no_ult_letra_prefixo = self.raiz
		for letra in prefixo_palavra:
			if not no_ult_letra_prefixo.existe_letra(letra):
				return []
			no_ult_letra_prefixo = no_ult_letra_prefixo.obtem_no_filho(letra)

		#por meio da ultima letra do prefixo, faz a predição das possiveis palavras
		#Para isso, você poderá precisar de fazer um método recursivo

		### SEU Código aqui
		return self.busca_possiveis_palavras(no_ult_letra_prefixo, prefixo_palavra)  # retorna o vetor com as possiveis palavras

	def busca_possiveis_palavras(self, no_ult_letra_prefixo, prefixo_palavra):

		predicao = [] #vetor que ira armazenar as possiveis palavras derivadas do prefixo inserido

		#busca as continuacoes do prefixo que sao possiveis para formar palavras
		self.busca_sufixo(no_ult_letra_prefixo, predicao)

		#concatena ao prefixo o resto das palavras que seriam possiveis serem formadas e insere no vetor predicao
		predicao = [prefixo_palavra+sufixo_palavra for sufixo_palavra in predicao]

		return predicao

	def busca_sufixo(self, no_ult_letra_prefixo, predicao):

		#values ira retornar uma lista de objetos que exibi todos os valores do dicionario
		for filho in no_ult_letra_prefixo.filhos.values():
			#busca, para todos os nos filhos, um proximo filho
			self.busca_sufixo(filho, predicao)
		if not no_ult_letra_prefixo.fim_palavra:
			predicao = [no_ult_letra_prefixo.letra]
		else:
			for letra in [no_ult_letra_prefixo.letra]:
				predicao.append(letra)
def main():

	#palavras criadas
	palavras = ["teste", "a", "texto", "aresta", "ano",
			  "zebra", "trabalho",]

	#arvore Trie
	arvore = Trie()

	#insere palavras
	print("Insercao:")
	for palavra in palavras:
		arvore.insere(palavra)
		print(f"palavra -{palavra}- inserida")

	print("\n")
	#pesquisa
	print("Pesquisa:")
	print(f'-{"ano"}-: {arvore.pesquisa("ano")}')
	print(f'-{"ana"}-: {arvore.pesquisa("ana")}')
	print(f'-{"teste"}-: {arvore.pesquisa("teste")}')
	print(f'-{"testa"}-: {arvore.pesquisa("testa")}')
	print(f'-{"texto"}-: {arvore.pesquisa("texto")}')
	print(f'-{"trabalho"}-: {arvore.pesquisa("trabalho")}')

	chaves = ["compor", "comer", "prefacio", "presente", "prever", "praticar"]

	for palavra in chaves:
		arvore.insere(palavra)
		print(f"palavra -{palavra}- inserida")

	arr_palavras = ["co", "com", "pre", "pr"]
	for palavra in arr_palavras:
		print(len(arvore.preditor(palavra)))

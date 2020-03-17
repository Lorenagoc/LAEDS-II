from typing import List

count = 0

class Node:
    def __init__(self, key, left: "Node" = None, right: "Node" = None):
        self.key = key
        self.left = left
        self.right = right

    def print_tree(self):
        """
        Imprime a arvore a partir do nodo atual
        """
        if self.left:
            self.left.print_tree()
        print(self.key, end=" ")
        if self.right:
            self.right.print_tree()

    def insert(self, key) -> bool:
        """
        Insere um nodo na árvore que a chave "key"
        """
        if key < self.key:
            if self.left:
                return self.left.insert(key)
            else:
                self.left = Node(key)
                return True
        elif key > self.key:
            if self.right:
                return self.right.insert(key)
            else:
                self.right = Node(key)
                return True
        else:
            return False

    def search(self, key) -> bool:
        """
        Retorna verdadeiro caso a chave `key` exista na árvore

        Lorena Gomes de Oliveira Cabral
        """
        global count  # Variável global
        if key < self.key:  # Se a chave for menor do que a chave que já está na árvore e está sendo comparada
            if self.left:  # Se o nó esquerdo existir
                count += 1  # Soma +1 ao contador
                return self.left.search(key)  # Retorna a chave em questão
        elif key > self.key:  # Se a chave for maior do que a chave que já está na árvore e está sendo comparada
            if self.right:  # Se o nó direito existir
                count += 1  # Soma +1 ao contador
                return self.right.search(key)  # Retorna a chave em questão
        else:  # Se as comparações já foram realizadas
            print(count)  # Printamos o contador
            return True  # Retorna true
        return False  # Retorna false

    def to_sorted_array(self, arr_result: List = None) -> List:
        """
        Retorna um vetor das chaves ordenadas.
        arr_result: Parametro com os itens já adicionados.

        Lorena Gomes de Oliveira Cabral

        """
        if arr_result is None:  # Se o array ainda não tiver nada inserido
            arr_result = []  # Então criamos uma lista vazia
        if self.left:  # Se o nó na esquerda existir
            self.left.to_sorted_array(
                arr_result)  # Cria - se uma chamada recursiva da função enviando como parâmetro a lista, ou seja, estaremos descendo a árvore pela esquerda

        arr_result.append(self.key)  # Adiciona o valor na lista

        if self.right:  # Se o nó na direita existir
            self.right.to_sorted_array(
                arr_result)  # Cria - se uma chamada recursiva da função enviando como parâmetro a lista, ou seja, estaremos descendo a árvore pela direita

        # Nos nós da esquerda, primeiros percorremos toda a profundidade e em seguida começamos a adicionar na lista de baixo para cima
        # Nos nós da direita, conforme vamos percorrendo, vamos adicionando na lista
        # Dessa forma retornamos uma lista já ordenada

        return arr_result  # Retorna a lista

    def max_depth(self, current_max_depth: int = 0, arr_distancia: List = None) -> int:
        """
        Calcula a maior distancia entre o nodo raiz e a folha
        current_max_depth: Valor representando a maior distancia até então
                           ao chamar pela primeira vez, não é necessário usa-lo

        Lorena Gomes de Oliveira Cabral
        """

        if arr_distancia is None:  # Se o array ainda não tiver nada inserido
            arr_distancia = []  # Então criamos uma lista vazia

        arr_distancia.append(
            current_max_depth)  # Adiciona na lista TODOS os valores de current_max_depth durante a execução das chamadas recursivas

        if self.left:  # Se o nó à esquerda existir
            self.left.max_depth(current_max_depth=current_max_depth + 1,
                                arr_distancia=arr_distancia)  # Cria uma chamada recursiva com o método e passa como parâmetro current_max_depth + 1

        if self.right:  # Se o nó à direita existir
            self.right.max_depth(current_max_depth=current_max_depth + 1,
                                 arr_distancia=arr_distancia)  # Cria uma chamada recursiva com o método passa como parâmetro current_max_depth + 1

        current_max_depth = max(arr_distancia) + 1  # Current_max_depth recebe o maior valor que a lista recebeu
        # Foi necessário o +1 para correção do resultado. Na ultima verificação, quando não houver mais folhas, o método não faz a chamada recursiva,
        # logo não soma +1 em current_max_depth, deixando o resultado sempre uma unidade menor.

        return current_max_depth

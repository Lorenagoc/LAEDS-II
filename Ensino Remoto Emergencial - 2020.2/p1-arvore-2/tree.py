from typing import List

class Node:
    def __init__(self, key, left:"Node"=None, right:"Node"=None):
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
        """
        if key < self.key:
            if self.left:
                return self.left.search(key)
        elif key > self.key:
            if self.right:
                return self.right.search(key)
        else:
            return True
        return False


    def to_sorted_array(self, arr_result:List =None) -> List:
        """
        Retorna um vetor das chaves ordenadas.
        arr_result: Parametro com os itens já adicionados.
        """
        if(arr_result == None):
            arr_result = []

        if self.left:
            self.left.to_sorted_array(arr_result)

        arr_result.append(self.key)

        if self.right:
            self.right.to_sorted_array(arr_result)
        return arr_result

    def max_depth(self,current_max_depth:int=0) -> int:
        """
        Calcula a maior distancia entre o nodo raiz e a folha
        current_max_depth: Valor representando a maior distancia até então
                           ao chamar pela primeira vez, não é necessário usa-lo
        """
        current_max_depth = current_max_depth +1
        val_left,val_right = current_max_depth,current_max_depth

        if self.left:
            val_left = self.left.max_depth(current_max_depth)
        if self.right:
            val_right = self.right.max_depth(current_max_depth)

        if val_left>val_right:
            return val_left
        else:
            return val_right

    def position_node(self, key, current_position:int=1) -> int:
        """
            Retorna a posição do nodo desejado na árvore
            current_position: representa a posição da árvore naquele momento
                           ao chamar pela primeira vez, não é necessário usa-lo
        """
        # Qualquer nodo de posição i tem seu filho da esquerda com posição 2*i
        # Qualquer nodo de posição i tem seu filho da direita com posição 2*i + 1

        '''
            Árvore usada como exemplo para fazer o código:          7
                                                                  /   \
                                                                 5     9
                                                                / \   / \
                                                               4   6 8  10

            Supondo que queremos saber a posição da chave 4

            A chave 4 é menor que a chave 7? Sim
            Existe um nó à esquerda de 7? Sim
            Então currente_position = 2*current_position ==> currente_position = 2
            Chama a função novamente

            A chave 4 é menor que 5? Sim
            Existe um nó à esquerda de 5? Sim
            Então currente_position = 2*current_position ==> currente_position = 4
            Chama a funçao novamente

            A chave 4 é igual a 4 então já chegamos ao fim da árvore
            retorna a posição atual                                               

        '''

        if key < self.key:  # se a chave que temos interesse em saber a posição for menor do que a comparada em questão
            if self.left:  # se existe um nó à esquerda do nó atual que está sendo comparado com a chave de interesse
                return self.left.position_node(key, (2 * current_position))  # cria - se uma chamada recursiva da função especificando que estamos descendo a árvore  pela esquerda
        elif key > self.key:  # se a chave que temos interesse em saber a posição for maior do que a comparada em questão
            if self.right:  #se existe um nó à esquerda do nó atual que está sendo comparado com a chave de interesse
                return self.right.position_node(key, ((current_position * 2) + 1))  # cria - se uma chamada recursiva da função especificando que estamos descendo a árvore  pela direita
        elif key == self.key:  #se a chave que temos interesse em saber a posição for igual a comparada em questão
            return current_position

    def is_balanced(self) -> bool:
        """
            Retorna true caso a árvore seja balanceada, false caso não seja
        """
        dist_raiz_sub_arvore_direita = 0
        dist_raiz_sub_arvore_esquerda = 0

        if self.right and self.right.is_balanced() is True: #se existe nó à direita e é balanceado
            dist_raiz_sub_arvore_direita = self.right.max_depth() #calcula a maior distancia existente na sub árvore direita da raiz


        if self.left and self.left.is_balanced() is True: #se existe nó à esquerda e é balanceado
            dist_raiz_sub_arvore_esquerda = self.left.max_depth() #calcula a maior distância existente na sub árvore esquerda da raiz

        #abs retorna o valor absoluto da diferença de alturas
        dif = abs(dist_raiz_sub_arvore_esquerda - dist_raiz_sub_arvore_direita) #calcula a diferença entre as alturas das sub árvores

        if dif <= 1:
            return True
        else:
            return False

    def sorted_array_to_balanced_tree(self, array:List, start:"Node", end:"Node"):
        """

        Suponha que o array seja [1,2,3,4,5,6,7,8]
        A lógica é dividir esse array ao meio sucessivamente até que não possamos mais.
        Na primeira divisão, o elemento do meio é o 4
        Feito isso, teremos agora a sub-árvore esquerda e direita com o resto dos elementos
        O elemento do meio da esquerda será o 2
        O elemento do meio da direita será o 6
        O 1, 3, 5 e 7 não possuem arrays dependentes para que outras divisões sejam feitas, então chegamos ao fim

                                                          4
                                                        /   \
                                                    [1|2|3] [5|6|7]
                                                      / \     / \
                                                     1  3    5   7


        """

        if start > end:
            return None

        elemento_meio = (start + end)//2 #achamos o elemento que equivale ao meio do array
        node = Node(array[elemento_meio]) #definimos uma árvore com o elemento do meio como raiz
        node.left = self.sorted_array_to_balanced_tree(array, start, elemento_meio - 1) #refazemos esse processo de divisão pela esquerda
        node.right = self.sorted_array_to_balanced_tree(array, elemento_meio + 1, end) #refazemos esse processo de divisão pela direita
        return node #retorna o nodo que será a nova raiz

    def to_balanced_tree(self)->"Node":

        array = self.to_sorted_array() #capturamos um vetor das chaves ordenadas

        return self.sorted_array_to_balanced_tree(array, 0, len(array)-1) #chamamos a função que irá balancear


from functools import total_ordering
import math
class MaxHeap:

    def __init__(self):
        #inicia com o heap com um elemento sentinela (que nunca será acessado)
        self.arr_heap = [None]

    def __str__(self):
        return str(self.arr_heap[1:])

    def __repr__(self):
        return str(self)
    
    #Os metodos esquerda, direita e pai serão usados nos demais metodos do heap
    def esquerda(self, i:int) ->int:
        """
            Retorna a posição do filho a esquerda de i
            Qualquer nodo de posição i tem seu filho da esquerda com posição 2*i
        """
        return 2 * i

    def direita(self, i:int) ->int:
        """
            Retorna a posição do filho a direita de i
            Qualquer nodo de posição i tem seu filho da direita com posição 2*i+1
        """
        return 2*i+1

    def pai(self, i:int) ->int:
        """
        Retorna a posição do pai do i-ésimo nó
        Qualquer nodo de posição i tem seu pai com posição i/2
        """
        return i//2

    @property
    def pos_ultimo_item(self):
        return len(self.arr_heap)-1

    def refaz(self, pos_raiz_sub_arvore:int):

        #maior_filho é inicializado com o da esquerda de pos raiz subarvore
        pos_pai = pos_raiz_sub_arvore
        pos_maior_filho = self.esquerda(pos_pai)

        #obtem o item raiz da subarvore do heap
        val_raiz_sub_arvore = self.arr_heap[pos_raiz_sub_arvore]

        while pos_maior_filho<=self.pos_ultimo_item:
            #se a posição do filho a esquerda não for a ultima do vetor,
            #atualize, se necessario, o pos_maior_filho considerando o filho a direita
            if pos_maior_filho<self.pos_ultimo_item:
                
                pos_filho_direita = self.direita(pos_pai)
                filho_direita = self.arr_heap[pos_filho_direita]
                filho_esquerda = self.arr_heap[pos_maior_filho]

                if filho_esquerda < filho_direita: #se o filho da esquerda for menor que o filho da direita então:
                    pos_maior_filho = pos_filho_direita #a posição do maior filho passa a ser a posição do filho da direita

                valor_maior_filho = self.arr_heap[pos_maior_filho]

            #caso o valor da  raiz desta subarvore (val_raiz_sub_arvore)
            #possua um valor maior que o de seus filhos,
            # finaliza o while
            #### SEU CODIGO AQUI ###########
                if val_raiz_sub_arvore > valor_maior_filho:
                    break;

                # realize a troca conforme especificação
                #### SEU CODIGO AQUI ############
                else:
                    self.arr_heap[pos_pai] = valor_maior_filho

            #prepare as variáveis pos_pai e pos_maior_filho para a proxima iteração
            #substitua os "None" das duas linhas abaixo apropriadamente
            pos_pai = pos_maior_filho
            pos_maior_filho = self.esquerda(pos_pai)

        #atualize a posição pos_pai apropriadamente
        self.arr_heap[pos_pai] = val_raiz_sub_arvore

    def retira_max(self):
        if len(self.arr_heap)<=1:
            raise IndexError("Heap Vazio")
        # Faça a retirada do máximo conforme especificação/slides da aula teórica
        # Tiramos o elemento da raiz, pois é o maior. Tiramos o elemento da última posição e realocamos na raiz.
        # Chamamos o método refaz para reorganizar o heap.

        maior_elemento = max(self.arr_heap[1:]) #max retorna o maior elemento do vetor começando da pos 1 (raiz)
        indice_maior_elemento = self.arr_heap.index(maior_elemento)
        maximo = self.arr_heap.pop(indice_maior_elemento)
        indice_ultimo_elemento = self.arr_heap.index(self.arr_heap[-1])
        elemento_ultima_pos = self.arr_heap.pop(indice_ultimo_elemento)
        self.arr_heap.insert(1, elemento_ultima_pos)
        if len(self.arr_heap) > 3: #não refazer o heap se o vetor tiver apenas 2 elementos, pois a atualização feita a cima já é suficiente
            self.refaz(1)
        return maximo

    def insere(self, item):
        self.arr_heap.append(None)
        pos_inserir = self.pos_ultimo_item
        pai_pos_inserir = self.pai(pos_inserir)

        #substitua o "None" apropriadamente
        while pos_inserir>1 and item>self.arr_heap[pai_pos_inserir]: #o item que será inserido precisa ser maior que o elemento no nodo pai para acontecer as atalizações
            #realiza a atualização (substitua os "None")
            elemento_pai_pos_inserir = self.arr_heap[pai_pos_inserir]
            self.arr_heap[pos_inserir] = elemento_pai_pos_inserir

            #ajusta para a proxima iteração (substitua os None apropriadamente)
            pos_inserir = self.pai(pos_inserir)
            pai_pos_inserir = self.pai(pai_pos_inserir)

        #finalize o insere apropriadamente
        self.arr_heap[pos_inserir] = item

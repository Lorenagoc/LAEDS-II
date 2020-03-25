class No:
    def __init__(self, chave=None):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

    @property
    def altura_subarvore_esquerda(self):
        if self.esquerda is None:
            return 0
        return self.esquerda.altura

    @property
    def altura_subarvore_direita(self):
        if self.direita is None:
            return 0

        return self.direita.altura

    @property
    def equilibrio(self):
        return self.altura_subarvore_esquerda - self.altura_subarvore_direita

    def atualiza_altura(self):
        self.altura = 1 + max(self.altura_subarvore_esquerda,
                              self.altura_subarvore_direita)


class AVL:
    def __init__(self, raiz):
        self.raiz = raiz

    def imprime(self):
        self._imprime(self.raiz)

    def _imprime(self, raiz_sub_arvore):

        print(raiz_sub_arvore.chave, end="\n")
        if raiz_sub_arvore.esquerda:
            print(f"---------Esquerda de {raiz_sub_arvore.chave}-------")
            self._imprime(raiz_sub_arvore.esquerda)

        if raiz_sub_arvore.direita:
            print(f"---------Direita  de {raiz_sub_arvore.chave}-------")
            self._imprime(raiz_sub_arvore.direita)

    def rotacao_esquerda(self, raiz_sub_arvore):
        """
            Lorena Gomes de Oliveira Cabral
            Os valores usados para construir a lógica do código são os mesmos dados na árvore exemplo contida no "Atividade 1" no arquivo jupyter "AVL Tree.ipynb"
        """
        '''
            O filho à direita do nó raiz será a nova raiz: O nó 15, que é o filho à direita do nó 13, agora é o nó raiz
        '''
        # nova_raiz_sub_arvore = raiz_sub_arvore.direita

        '''
            O nó raiz da árvore agora será o filho à esquerda do nó raiz da nova árvore. Ou seja, o nó 13 agora será filho à esquerda do nó 15.
        '''
        # nova_raiz_sub_arvore.esquerda = raiz_sub_arvore

        '''
            O filho à esquerda do filho à direita do nó raiz, agora será filho à direita do filho à esquerda da nova raiz da árvore: O nó 14 agora será filho à direita do nó 13, que 
            agora é filho à esquerda do nó 15
        '''
        # nova_raiz_sub_arvore.esquerda.direita = raiz_sub_arvore.direita.esquerda

        # Por algum motivo, a atribuição simples não funcionou. Usando tuplas o teste foi concluído sem problemas
        # http://excript.com/python/atribuicao-multipla-python.html --> site que usei de referência para isso

        (nova_raiz_sub_arvore, nova_raiz_sub_arvore.esquerda, nova_raiz_sub_arvore.esquerda.direita) = (raiz_sub_arvore.direita, raiz_sub_arvore, raiz_sub_arvore.direita.esquerda)

        if nova_raiz_sub_arvore.esquerda:  # Se o filho à esquerda da raiz da nova árvore existir
            nova_raiz_sub_arvore.esquerda.atualiza_altura()  # Atualizamos a altura do filho à esquerda do nó raiz da nova árvore, ou seja, a altura do nó 13
        nova_raiz_sub_arvore.atualiza_altura()  # Atualizamos a altura do nó raiz da nova árvore

        # Retorna a nova árvore
        return nova_raiz_sub_arvore

    def rotacao_direita(self, raiz_sub_arvore):

        '''
            Lorena Gomes de Oliveira Cabral
            Seguindo a mesma lógica do método anterior temos que:

            O nó raiz da nova árvore será o filho à esquerda do nó raiz da árvore original. Ou seja, o nó 6 será o nó raiz
            O filho à direita do nó raiz da nova árvore será o nó raiz da árvore original. Ou seja, o nó 13 será o filho à direita do nó raiz
            O filho à direita do filho à esquerda do nó raiz da árvore original será o filho à esquerda do filho à direita do nó raiz da nova árvore
            Ou seja, o nó 14 será o filho à esquerda do nó 13.
        '''

        (nova_raiz_sub_arvore, nova_raiz_sub_arvore.direita, nova_raiz_sub_arvore.direita.esquerda) = (raiz_sub_arvore.esquerda, raiz_sub_arvore, raiz_sub_arvore.esquerda.direita)

        if nova_raiz_sub_arvore.direita: # Se o filho à direita da raiz da nova árvore existir
            nova_raiz_sub_arvore.direita.atualiza_altura() # Atualizamos a altura do filho à direita do nó raiz da nova árvore, ou seja, a altura do nó 13
        nova_raiz_sub_arvore.atualiza_altura() # Atualizamos a altura do nó raiz da nova árvore

        # Retorna a nova árvore
        return nova_raiz_sub_arvore

    def rotacao_dupla_esquerda(self, raiz_sub_arvore):

        '''
            Lorena Gomes de Oliveira Cabral

            Efetua-se uma rotação simples direita na sub árvore direita do nó desbalanceado
            Realiza-se uma rotação simples esquerda no nó desbalanceado

            Fonte: https://ava.cefetmg.br/pluginfile.php/45638/mod_resource/content/1/Aula%2003%20-%20%C3%81rvore%20AVL.pdf

            Utilizaremos aqui os métodos de rotação simples anteriormente feitos
        '''

        '''
            Separamos toda a sub árvore à direita do nó desbalanceado.
        '''
        sub_arvore_direita_no_desbalanceado = AVL(raiz_sub_arvore.direita)

        '''
            Fazemos uma rotação direita simples na raiz dessa sub àrvore que separamos. O filho à direita da árvore original será essa raiz rotacionada
        '''
        raiz_sub_arvore.direita = sub_arvore_direita_no_desbalanceado.rotacao_direita(sub_arvore_direita_no_desbalanceado.raiz)

        '''
            Agora, realizamos uma rotação simples esquerda no nó desbalanceado da árvore original já com a sub árvore direita rotacionada
        '''
        arvore_com_sub_arvore_direita_rotacionada = AVL(raiz_sub_arvore)
        nova_raiz_sub_arvore = arvore_com_sub_arvore_direita_rotacionada.rotacao_esquerda(arvore_com_sub_arvore_direita_rotacionada.raiz)

        # Retorna a árvore
        return nova_raiz_sub_arvore

    def rotacao_dupla_direita(self, raiz_sub_arvore):

        '''
            Lorena Gomes de Oliveira Cabral

            Efetuar uma rotação simples esquerda na sub árvore esquerda do nó desbalanceado
            Realizar uma rotação simples direita no nó desregulado

            Fonte: https://ava.cefetmg.br/pluginfile.php/45638/mod_resource/content/1/Aula%2003%20-%20%C3%81rvore%20AVL.pdf

            Seguindo a mesma lógica do método rotacao_dupla_esquerda temos que:
        '''

        '''
            Separamos toda a sub árvore à esquerda do nó desbalanceado.
        '''
        sub_arvore_esquerda_no_desbalanceado = AVL(raiz_sub_arvore.esquerda)

        '''
            Fazemos uma rotação esquerda simples na raiz dessa sub àrvore que separamos. O filho à esquerda da árvore original será essa raiz rotacionada
        '''
        raiz_sub_arvore.esquerda = sub_arvore_esquerda_no_desbalanceado.rotacao_esquerda(sub_arvore_esquerda_no_desbalanceado.raiz)

        '''
            Agora, realizamos uma rotação simples direita no nó desbalanceado da árvore original já com a sub árvore esquerda rotacionada
        '''
        arvore_com_sub_arvore_esquerda_rotacionada = AVL(raiz_sub_arvore)
        nova_raiz_sub_arvore = arvore_com_sub_arvore_esquerda_rotacionada.rotacao_direita(arvore_com_sub_arvore_esquerda_rotacionada.raiz)

        # Retorna a árvore
        return nova_raiz_sub_arvore

    def insere(self, chave):
        self.raiz = self._insere(chave, self.raiz)

    def _insere(self, chave, raiz_sub_arvore):
        # Inserção - alterando subarvores se necessario
        if not raiz_sub_arvore:
            return No(chave)
        elif chave < raiz_sub_arvore.chave:
            raiz_sub_arvore.esquerda = self._insere(chave, raiz_sub_arvore.esquerda)
        elif chave > raiz_sub_arvore.chave:
            raiz_sub_arvore.direita = self._insere(chave, raiz_sub_arvore.direita)
        else:
            # raiz desta subarvore não é modificada quando a chave é a mesma - e não realiza inserção
            return raiz_sub_arvore

        # altura atualizada
        raiz_sub_arvore.atualiza_altura()

        # Rebalanceia a árvore de tal forma que o equilibrio sempre fique entre -1 e 1
        # Caso 1 - Quando o nó desbalanceado possui a sub árvore à esquerda maior e o nó inserido é menor do que o filho à esquerda da raiz
        # Rotação simples direita
        if raiz_sub_arvore.equilibrio > 1 and chave < raiz_sub_arvore.esquerda.chave:
            raiz_sub_arvore = AVL(raiz_sub_arvore).rotacao_direita(raiz_sub_arvore)
            print("Passou por uma rotação simples direita\n") # print para determinar as rotações pedidas no último exercício
            return raiz_sub_arvore

        # Caso 2 - Quando o nó desbalanceado possui a sub árvore à direita maior e nó inserido é maior do que o filho à direita da raiz
        # Rotação simples esquerda
        if raiz_sub_arvore.equilibrio < -1 and chave > raiz_sub_arvore.direita.chave:
            raiz_sub_arvore = AVL(raiz_sub_arvore).rotacao_esquerda(raiz_sub_arvore)
            print("Passou por uma rotação simples esquerda\n") # print para determinar as rotações pedidas no último exercício
            return raiz_sub_arvore

        # Caso 3 - Quando o nó desequilibrado possui a sub árvore à esquerda maior e o nó inserido é maior do que o filho à esquerda da raiz
        # Rotação dupla direita
        if raiz_sub_arvore.equilibrio > 1 and chave > raiz_sub_arvore.esquerda.chave:
            raiz_sub_arvore = AVL(raiz_sub_arvore).rotacao_dupla_direita(raiz_sub_arvore)
            print("Passou por uma rotação dupla direita\n") # print para determinar as rotações pedidas no último exercício
            return raiz_sub_arvore

        # Caso 4 - Quando o nó desequelibrado possui a sub árvore à direita maior e o nó inserido é menor do que o filho à direita da raiz
        # Rotação dupla esquerda
        if raiz_sub_arvore.equilibrio < -1 and chave < raiz_sub_arvore.direita.chave:
            raiz_sub_arvore = AVL(raiz_sub_arvore).rotacao_dupla_esquerda(raiz_sub_arvore)
            print("Passou por uma rotação dupla esquerda\n") # print para determinar as rotações pedidas no último exercício
            return raiz_sub_arvore

        # caso já esteja equilibrado, a raiz subarvore não é modificada
        return raiz_sub_arvore
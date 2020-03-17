class Autor():

    def __init__(self, primeiro_nome, nome_meio, ultimo_nome, data_nascimento):

        self.primeiro_nome = primeiro_nome

        # O atributo >> nome_meio << é opcional

        if nome_meio == "":
            self.nome_meio = ''
        else:
            self.nome_meio = nome_meio
        self.ultimo_nome = ultimo_nome
        self.data_nascimento = data_nascimento

    @property
    def nome_como_citado(self):

        # O método >> upper() << é o responsável por deixar todas as letras da string maiúsculas
        # A posição 0 no atributo self.primeiro_nome[0] pega a primeira letra do primeiro nome do autor

        return "{ultimo_nome} {primeiro_nome}.".format(ultimo_nome=self.ultimo_nome.upper(),
                                                       primeiro_nome=self.primeiro_nome[0].upper())

    def atributos_autor(self):

        return "\n******** Atributos do autor ********\nAutor: {first} {second} {last}\nData de nascimento: {date}\n".format(first=self.primeiro_nome, second=self.nome_meio, last=self.ultimo_nome, date=self.data_nascimento)

    def __str__(self):
        return self.nome_como_citado

#*****************************************************************************************************************

class Livro():
    def __init__(self, titulo, ano):

        # O título não pode ser vazio, caso contrário, uma mensagem de erro é encaminhada ao usuário

        if titulo == "":
            return ValueError("Erro! O título do livro não pode ser vazio!")
        else:
            self.titulo = titulo

        self.ano = ano
        self.lista_autores = []

    @property
    def get_titulo(self):
        return self.titulo

    @property
    def get_ano(self):
        return self.ano

    @property
    def get_lista_autores(self):
        return self.lista_autores

    def adiciona_autores(self, autor):
        self.lista_autores.append(autor)

    # O método join pega todos os ítens em um iterador e os une em uma string.

    def __str__(self):
        str1 = ' '.join([str(elemento) for elemento in self.lista_autores])
        return "\nTítulo: {titulo}\nAno: {ano}\nAutores: {autores}\n".format(titulo=self.titulo, ano=self.ano,
                                                                             autores=str1)

#*****************************************************************************************************************

class Biblioteca():
    def __init__(self):
        self.lista_livros = []
        self.acervo = {}

    def adiciona_livros(self, livro):
        self.lista_livros.append(livro)

    def livros_por_autor(self, obj_autor):

        # A chave do acervo (dicionário) é definida como sendo o autor em questão
        self.acervo.update({obj_autor.nome_como_citado: []})

        # O conteúdo da lista de livros é convertido de objeto para string
        livro_converter_obj_str = ' '.join([str(elemento) for elemento in self.lista_livros])

        # Separamos o conteúdo da string anteriormente formada um em cada linha
        lista_livros_organizada = livro_converter_obj_str.split('\n')

        # Percorre o acervo de livros
        for autor in self.acervo:

            # Lista que armazenará os livros que o autor em questão participou/escreveu
            livros_escritos_autor = []

            # Esse será um iterador que usaremos para pegar na lista, através do índice da posição, o título do livro
            pegando_titulo_livro = 1

            # Percorre a lista de livros anteriormente organizada (com um parâmetro do livro em cada linha)
            for livro in lista_livros_organizada:

                # Se o autor tiver como autor do livro...
                if autor in livro:

                    #Pegamos dentro da lista o título do livro (na primeira rodada do for o titulo fica na posição 1)
                    titulo_livro = lista_livros_organizada[pegando_titulo_livro]

                    # Para fins estéticos do programa, deixamos apenas o nome do livro, sem 'Título:' antes
                    titulo_livro = titulo_livro[8:]

                    # Adicionamos, na lista de livros escritos pelo autor, o titulo do livro que acabamos de encontrar
                    livros_escritos_autor.append(titulo_livro)

                    # Passamos para a próxima posição onde terá o título do próximo livro
                    pegando_titulo_livro = pegando_titulo_livro + 4

            # Fazemos um update no acervo, adicionando na chave um novo valor
            self.acervo.update({autor: livros_escritos_autor})

        # Imprime os livros do autor pesquisado percorrendo o acervo
        print('\n*************** Livros do autor pesquisado ***************')

        for nome_autor, livros_autor in self.acervo.items():
            print(nome_autor, ':', livros_autor)

        return ''

    def __str__(self):

        str1 = ' '.join([str(elemento) for elemento in self.lista_livros])
        return "********* LIVROS CONTIDOS NO ACERVO *********\n{livros}".format(livros=str1)

#*****************************************************************************************************************

# Instanciação dos objetos

livro1 = Livro('Física Experimental', '2008')
livro2 = Livro('Livro Fictício Elmo', '2010')

agostinho = Autor('Agostinho', 'Aurélio', 'Campos', '12/12/1964')
elmo = Autor('Elmo', 'Salomão', 'Alves', '12/12/1960')
nivaldo = Autor('Nivaldo', 'Lúcio', 'Speziali', '12/12/1963')

# Imprime os atributos do autor
print(agostinho.atributos_autor())
print(elmo.atributos_autor())
print(nivaldo.atributos_autor())

livro1.adiciona_autores(agostinho)
livro1.adiciona_autores(elmo)
livro1.adiciona_autores(nivaldo)
livro2.adiciona_autores(elmo)

biblioteca = Biblioteca()
biblioteca.adiciona_livros(livro1)
biblioteca.adiciona_livros(livro2)

# Imprime tudo que tem na biblioteca
print(biblioteca)
# Pesquisamos um autor específico dentre os disponíveis
print(biblioteca.livros_por_autor(elmo))

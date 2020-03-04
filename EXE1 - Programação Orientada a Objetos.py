class Autor():
    def __init__(self, primeiro_nome, nome_meio, ultimo_nome, data_nascimento):

        self.primeiro_nome = primeiro_nome
        # o atributo >> nome_meio << é opcional
        if nome_meio == "":
            self.nome_meio = ''
        else:
            self.nome_meio = nome_meio
        self.ultimo_nome = ultimo_nome
        self.data_nascimento = data_nascimento

    def nome_como_citado(self):
        # o método >> upper() << é o responsável por deixar todas as letras da string maiúsculas
        return "{ultimo_nome} {primeiro_nome}.".format(ultimo_nome=self.ultimo_nome.upper(),
                                                       primeiro_nome=self.primeiro_nome[0].upper())

    def __str__(self):
        return self.nome_como_citado()


class Livro():
    def __init__(self, titulo, ano):

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

    def __str__(self):
        str1 = ' '.join([str(elemento) for elemento in self.lista_autores])
        return "\nTítulo: {titulo}\nAno: {ano}\nAutores: {autores}\n".format(titulo=self.titulo, ano=self.ano,
                                                                             autores=str1)

class Biblioteca():
    def __init__(self):
        self.lista_livros = []
        self.acervo = {}

    def adiciona_livros(self, livro):
        self.lista_livros.append(livro)

    def livros_por_autor(self, autor):

        #As chaves do acervo foram definidas na main. Aqui acessamos uma por uma e armazenamos em uma lista auxiliar
        aux_autores = []
        for item_autores in self.acervo:
            aux_autores.append(item_autores)
    
        aux_livros = []
        for item_livros in self.lista_livros:
            aux_livros.append(item_livros)
            
        #Falta terminar essa classe        

livro1 = Livro('Física Experimental', '2008')
livro2 = Livro('Livro Fictício Elmo', '2010')

agostinho = Autor('Agostinho', 'Aurélio', 'Campos', '12/12/1964')
elmo = Autor('Elmo', 'Salomão', 'Alves', '12/12/1960')
nivaldo = Autor('Nivaldo', 'Lúcio', 'Speziali', '12/12/1963')

livro1.adiciona_autores(agostinho)
livro1.adiciona_autores(elmo)
livro1.adiciona_autores(nivaldo)
livro2.adiciona_autores(elmo)

#print(livro1)
#print(livro2)

biblioteca = Biblioteca()
biblioteca.adiciona_livros(livro1)
biblioteca.adiciona_livros(livro2)

#Definimos as chaves e os valores de cada uma
biblioteca.acervo.update({agostinho.nome_como_citado: [], elmo.nome_como_citado: [], nivaldo.nome_como_citado: []})

print(biblioteca.livros_por_autor(elmo))

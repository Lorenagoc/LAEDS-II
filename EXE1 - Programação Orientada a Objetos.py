class Autor():
    def __init__(self, primeiro_nome, nome_meio, ultimo_nome, data_nascimento):
        self.primeiro_nome = primeiro_nome
        self.nome_meio = ""
        self.ultimo_nome = ultimo_nome
        self.data_nascimento = data_nascimento

    def nome_como_citado(self):
        return "{ultimo_nome} {primeiro_nome}.".format(ultimo_nome=self.ultimo_nome.upper(), primeiro_nome=self.primeiro_nome[0].upper())

class Livro():
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano
        self.lista_autores = []

    def adiciona_autores(self, autor):

        self.lista_autores.append(autor.nome_como_citado())

    def __str__(self):

        return "{titulo} - Ano: {ano} - Autores: {autores}".format(titulo=self.titulo, ano=self.ano, autores=self.lista_autores)

class Biblioteca():
    def __init__(self):
        self.lista_livros = []

    def adiciona_livros(self, livro):
        self.lista_livros.append(livro.titulo)

    def livros_por_autor(self, autor, livro):

        x = {}
        x[autor.nome_como_citado()] = livro.titulo
        return x[autor.nome_como_citado()]


agostinho = Autor("Agostinho", "Aurélio", "Campos", "12/12/1964")
elmo = Autor("Elmo", "Salomão", "Alves", "12/12/1960")
nivaldo = Autor("Nivaldo", "Lúcio", "Speziali", "12/12/1963")

print("{agostinho}; {elmo}; {nivaldo}".format(agostinho=agostinho.nome_como_citado(), elmo=elmo.nome_como_citado(), nivaldo=nivaldo.nome_como_citado()))

livro1 = Livro("Física Experimental", "2008")
livro1.adiciona_autores(agostinho)
livro1.adiciona_autores(elmo)
livro1.adiciona_autores(nivaldo)

print("{livro}".format(livro=livro1))

livro2 = Livro("Livro Fictício Elmo", "2010")
livro2.adiciona_autores(elmo)

print("{livro}".format(livro=livro2))

biblioteca = Biblioteca()
biblioteca.adiciona_livros(livro1)
biblioteca.adiciona_livros(livro2)

print(biblioteca.livros_por_autor(elmo, livro1))
print(biblioteca.livros_por_autor(elmo, livro2))

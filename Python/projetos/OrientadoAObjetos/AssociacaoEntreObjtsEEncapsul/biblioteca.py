



class Livro: # Classe Livro
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def isbn(self):
        return self.__isbn

class Biblioteca: # Associação entre objetos
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado à biblioteca "{self.nome}".')

    def remover_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(f'Livro "{livro.titulo}" removido da biblioteca "{self.nome}".')
                return
        print(f'Livro com ISBN {isbn} não encontrado na biblioteca "{self.nome}".')

    def listar_livros(self):
        if not self.livros:
            print(f'A biblioteca "{self.nome}" não possui livros.')
        else:
            print(f'Livros na biblioteca "{self.nome}":')
            for livro in self.livros:
                print(f'- {livro.titulo} por {livro.autor} (ISBN: {livro.isbn})')

# Testando as classes
biblioteca = Biblioteca("Biblioteca Central")


# Criando alguns livros
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "978-0-261-10325-2")
livro2 = Livro("1984", "George Orwell", "978-0-452-28423-4")
livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "978-0-15-601219-5")

# Criando uma biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando os livros na biblioteca
biblioteca.listar_livros()

# Removendo um livro da biblioteca
biblioteca.remover_livro("978-0-452-28423-4")

# Listando os livros novamente após a remoção
biblioteca.listar_livros()
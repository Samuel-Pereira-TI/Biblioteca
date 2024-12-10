class Livro():
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
        self.status = False
    
    def informacoes(self):
        status = 'Disponível' if self.status == False else 'Indisponível'
        print(f'Nome: {self.titulo}\nAno de publicação: {self.ano}\nAutor: {self.autor}\nStatus: {status}')

    def emprestar(self):
        self.status = True

    def devolver(self):
        self.status = False



class Cliente():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.lista_de_livros = []
    
    def informacoes_cliente(self):
        print(f'Nome: {self.nome} \nIdade: {self.idade}')
        for indice, livro in enumerate(self.lista_de_livros, start=1):
            print(f'{indice}. Titulo: {livro.titulo}')
            

    def pegar_livro(self, livro):
        self.lista_de_livros.append(livro)
        
    
    def devolver_livro(self, livro):
        self.lista_de_livros.remove(livro)



livro1 = Livro('Harry Potter', 2008, 'JK Rowling')
cliente1 = Cliente('Cleitinho', 25)

cliente1.pegar_livro(livro1)
cliente1.informacoes_cliente()
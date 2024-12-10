import os

livros = [{'Nome': 'Harry Potter', 'Autor': 'JK Rowling', 'Ano': '2008', 'Status': True}, {'Nome': 'A', 'Autor': 'JK Rowling', 'Ano': '1937', 'Status': True}]
clientes = ['Juninho Pernambucano', 'Flavin Do Pneu']
def voltar():
    volta = Biblioteca()
    volta.bibliotecario()

class Livro():
    def __init__(self):
        pass

    def cadastro_livro(self):
        self.nome_do_livro = input('Digite o nome do livro: ').title()
        self.autor = input('Digite o autor do livro: ')
        self.ano = int(input('Digite o ano de publicação do livro: '))
        self.status = True
        livros.append({'Nome': self.nome_do_livro, 'Autor': self.autor, 'Ano': self.ano, 'Status': self.status})
        print(f'O livro {self.nome_do_livro} cadastrado com sucesso!')
        input('Tecle ENTER para ir ao menu incial: ')
        voltar()

    def livros(self):
        print('''\n                       Biblioteca \n''')
        print(f'{'Nome do livro'.ljust(15)} | {'Autor'.ljust(10)} | {'Ano'.ljust(5)} | {'Disponibilidade'.ljust(10)}')
        for livro in livros:
            nome = livro['Nome']
            autor = livro['Autor']
            ano = str(livro['Ano'])
            ativo = 'Disponível' if livro['Status'] == True else 'Indisponível'
            print(f'{nome.ljust(15)} | {autor.ljust(10)} | {ano.ljust(5)} | {ativo.ljust(10)}')
        input('Tecle ENTER para ir ao menu incial: ')
        voltar()
            

    def remover_livro(self):
        escolha = input('Digite o nome do livro que você deseja remover: ').title()
        for livro in livros:
            if escolha == livro['Nome']:
                livros.remove(livro)
            print(f'O livro {escolha} foi removido com sucesso.')
        input('Tecle ENTER para ir ao menu incial: ')
        voltar()
 
class Cliente():
    def __init__(self):
        self.livros_emprestados = []

    def cadastro(self):
        self.nome_cliente = input('Digite o seu nome: ').title()
        clientes.append(self.nome_cliente)
        input('Tecle ENTER para ir ao menu incial: ')
        voltar()
    
    def remover_cliente(self):
        escolha = input('Digite o nome do cliente que você deseja remover: ').title()
        if escolha in clientes:
            for cliente in clientes:
                if cliente == escolha:
                    clientes.remove(cliente)
                    print(f'O cliente {cliente} foi removido com sucesso.')
                    input('Tecle ENTER para ir ao menu incial: ')
                    voltar()
        else:
            input('Cliente não encontrado!! Tecle ENTER para ir ao inicio.')
            voltar()

        
    def menu_cliente(self):
        os.system('cls')
        print('''
█ █▄░█ █ █▀▀ █ █▀█
█ █░▀█ █ █▄▄ █ █▄█ 
              
Opções disponíveis:
1 - Pegar livros emprestados.
2 - Devolver livros
3 - Lista de livros emprestados.
4 - Voltar ao menu incial.''')
        escolha = int(input('\nSegundo as opções numéricas, escolha que função você deseja acessar: '))
        
        match escolha:
            case 1:
                self.emprestar()
            case 2:
                self.devolver()
            case 3:
                self.lista_de_livros()
            case 4:
                self.voltar = Biblioteca()
                self.voltar.menu()

    def emprestar(self):
        print('''\n                       Biblioteca \n''')
        print(f'{'Nome do livro'.ljust(15)} | {'Autor'.ljust(10)} | {'Ano'.ljust(5)} | {'Disponibilidade'.ljust(10)}')
        for livro in livros:
            nome = livro['Nome']
            autor = livro['Autor']
            ano = str(livro['Ano'])
            ativo = 'Disponível' if livro['Status'] == True else 'Indisponível'
            print(f'{nome.ljust(15)} | {autor.ljust(10)} | {ano.ljust(5)} | {ativo.ljust(10)}')

        escolha_livro = input('\nDigite o nome do livro que você deseja pegar emprestado: ').title()
        for livro in livros:   
            if escolha_livro == livro['Nome']:
                if livro['Status'] == True:
                    print('Empréstimo realizado com sucesso.')
                    self.livros_emprestados.append(livro['Nome'])
                    livros.remove(livro)
                    livro['Status'] = not livro['Status']
                    livros.append(livro)
                    input('Tecle ENTER para voltar o menu inicial.')
                    self.menu_cliente()                       
                                
                else:
                    print('Livro não disponível.')
                    input('Tecle ENTER para voltar o menu inicial.')
                    self.menu_cliente()
            else:
                print('Livro não encontrado, siga as instruções novamente.')
                input('Tecle ENTER para voltar o menu inicial.')
                self.menu_cliente
        
    def devolver(self):
        devolver_livro = input('Digite o nome do livro que você quer devolver: ').title()
        for livro_e in self.livros_emprestados:   
            if devolver_livro == livro_e:
                self.livros_emprestados.remove(livro_e)
                print(f'O livro: {livro_e} foi devolvido com sucesso!')
                input('Tecle ENTER para ir ao menu inicial: ')
                for livro in livros:
                    if livro ['Nome'] == livro_e:
                        livros.remove(livro)
                        livro_e == livro['Nome']
                        livro['Status'] = not livro['Status']
                        livros.append(livro)
                        self.menu_cliente()
            else:
                print('Livro não encontrado, siga as instruções novamente.')
                self.devolver

    def lista_de_livros(self):
        for i in self.livros_emprestados:
            print(i)
        input('Tecle ENTER para voltar o menu inicial.')
        self.menu_cliente

class Biblioteca():
    def __init__(self):
        pass
    def menu(self):
        os.system('cls')
        print('''
██████╗░██╗██████╗░██╗░░░░░██╗░█████╗░████████╗███████╗░█████╗░░█████╗░
██╔══██╗██║██╔══██╗██║░░░░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
██████╦╝██║██████╦╝██║░░░░░██║██║░░██║░░░██║░░░█████╗░░██║░░╚═╝███████║
██╔══██╗██║██╔══██╗██║░░░░░██║██║░░██║░░░██║░░░██╔══╝░░██║░░██╗██╔══██║
██████╦╝██║██████╦╝███████╗██║╚█████╔╝░░░██║░░░███████╗╚█████╔╝██║░░██║
╚═════╝░╚═╝╚═════╝░╚══════╝╚═╝░╚════╝░░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝

░██████╗███████╗███╗░░██╗░█████╗░░█████╗░
██╔════╝██╔════╝████╗░██║██╔══██╗██╔══██╗
╚█████╗░█████╗░░██╔██╗██║███████║██║░░╚═╝
░╚═══██╗██╔══╝░░██║╚████║██╔══██║██║░░██╗
██████╔╝███████╗██║░╚███║██║░░██║╚█████╔╝
╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░''')
        escolha = int(input('''Qual função você deseja acessar: 
1 - Sou cliente
2 - Sou bibliotecário
                        
Segundo as opções numéricas, escolha que função você deseja acessar: '''))

        match escolha:
            case 1: 
                self.cliente = Cliente()
                self.cliente.menu_cliente()
            case 2: 
                self.bibliotecario()
            case _:
                input('Essa opção não está disponível, por favor, tecle ENTER para reiniciar o programa.')
                self.menu()

    def bibliotecario(self):
        os.system('cls')
        print('''
▄▀█ █▀█ █▀▀ ▄▀█   ▄▀█ █▀▄ █▀▄▀█ █ █▄░█ █ █▀ ▀█▀ █▀█ ▄▀█ ▀█▀ █ █░█ ▄▀█
█▀█ █▀▄ ██▄ █▀█   █▀█ █▄▀ █░▀░█ █ █░▀█ █ ▄█ ░█░ █▀▄ █▀█ ░█░ █ ▀▄▀ █▀█

Opções disponíveis:
1 - Registrar livro.
2 - Remover livro.
3 - Lista de livros registrados.
4 - Registrar clientes.
5 - Remover Clientes
6 - Voltar ao início''')
        escolha = int(input('\nSegundo as opções numéricas, escolha que função você deseja acessar: '))

        match escolha:
            case 1:
                c_livro = Livro()
                c_livro.cadastro_livro()
                
                
            case 2:
                r_livro = Livro()
                r_livro.remover_livro()
                
            case 3:
                self.l_livro = Livro()
                self.l_livro = self.l_livro.livros()
                
            case 4:
                c_cliente = Cliente()
                c_cliente.cadastro()
                
            case 5:
                r_cliente = Cliente()
                r_cliente.remover_cliente()
            case 6:
                voltar = Biblioteca()
                voltar.menu()

senac = Biblioteca()
senac.menu()


from model.autor import Autor
from model.livro import Livro

def cadastrar_autor(autores): # Cadastra o Autor
    nome = input('Nome do Autor: ').strip().upper()
    nacionalidade = input('Nacionalidade: ').strip().upper()
    if any(autor.get_nome() == nome for autor in autores):
        print("\nAutor já está cadastrado.\n")
    else:
        autores.append(Autor(nome, nacionalidade))

def cadastrar_livro(livros, autores): # Cadastra o Livro
        titulo = input('Título: ').strip().upper()
        if any(livro.get_titulo() == titulo for livro in livros): # Talvez criar outra função para verificar se o livro ja esta cadastrado
            print("\nLivro já está cadastrado.\n")
            return

        while True:
            try:
                ano = int(input('Ano: '))
                break
            except ValueError:
                print(f'Valor inválido!')
        nome_autor = input('Nome do Autor: ').strip().upper()
        for autor in autores:
            if autor.get_nome() == nome_autor:
                livros.append(Livro(titulo, ano, autor))
                print('\nLivro cadastrado com sucesso.\n')
                return
        else:
            print(f'\nAutor informado não está cadastrado no sistema. Por favor, cadastre o autor antes de cadastrar o livro!\n')

def remover_livro(livros): # Remove um livro existente 
    titulo_livro = input("Informe o título do livro que deseja remover: ").upper().strip()
    for livro in livros:
        if livro.get_titulo() == titulo_livro:
            livros.remove(livro)
            print(f"\nO livro '{titulo_livro}' foi removido com sucesso.\n")
            return
    else:
        print(f"\nO livro '{titulo_livro}' não existe em nosso banco de dados.\n")

def listar_livros(livros):
    print('=' * 50)
    if not livros:
        print("\nNenhum livro cadastrado no sistema.\n")
        return
    else:
        print(f'\nLivros:\n')
        for livro in livros:
            print('-' * 20)
            livro.exibir_info()  
    print('=' * 50)

def buscar_livro_titulo(livros): # Busca um Livro pelo Título
        titulo_livro = input('Informe o titulo do livro para a busca: ').upper().strip()
        busca_livro = [livro for livro in livros if titulo_livro in livro.get_titulo().upper()]
        if busca_livro:
            for livro in busca_livro:
                print('-' * 20)
                livro.exibir_info()
        else:
            print('\nLivro não encontrado!\n')
            

def buscar_autor(livros): # Buscar o Autor e seus livros pelo nome do Autor
    nome_autor = input('Informe o nome do autor para a busca: ').upper().strip()
    busca_autor = [livro for livro in livros if nome_autor in livro.get_autor().get_nome().upper()]
    if busca_autor:
        for livro in busca_autor:
            print('-' * 20)
            livro.exibir_info()
    else:
        print('\nAutor não encontrado!\n')
"""
✅** Funcionalidades obrigatórias **
*Cadastrar autores e livros:

    - Permitir ao usuário cadastrar múltiplos autores

    - Associar um livro a um autor no momento do cadastro do livro

*Listar todos os livros:

    - Exibir Título, Ano e o nome do Autor

*Buscar livros por nome do autor ou título:

    - Fazer busca (parcial ou completa) sem diferenciar maiúsculas e minúsculas

*Menu de opções com loop até o usuário decidir sair:
"""

import json

################################################################################################
# Class
class Autor:

    def __init__(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

    def get_nome(self):
        return self._nome
    
    def get_nacionalidade(self):
        return self._nacionalidade
    
    def __str__(self):
        return f'Autor: {self.get_nome()} ({self.get_nacionalidade()})'
    
    def to_dict(self):
        return {'nome': self._nome, 'nacionalidade': self._nacionalidade}
    
    @staticmethod
    def from_dict(d):
        return Autor(d['nome'], d['nacionalidade'])


class Livro:
    
    def __init__(self, titulo, ano, autor):
        self._titulo = titulo
        self._ano = ano
        self._autor = autor
    
    def get_titulo(self):
        return self._titulo
    
    def get_ano(self):
        return self._ano
    
    def get_autor(self):
        return self._autor
    
    def exibir_info(self):
        print(f'Título: {self.get_titulo()}\nAno: {self.get_ano()}\n{self.get_autor()}')
    
    def to_dict(self):
        return {'titulo': self._titulo, 'ano': self._ano, 'autor': self._autor.to_dict()}
    
    @staticmethod
    def from_dict(d):
        return Livro(d['titulo'], d['ano'], Autor.from_dict(d['autor']))

#####################################################################################################

# Functions
def option_input(msg, valid_options):
    while True:
        try:
            valor = int(input(msg))
            if valor in valid_options:
                return valor
            else:
                print(f"Opção inválida. Escolha entre: {valid_options}")
        except ValueError:
            print(f"Opção inválida. Escolha entre: {valid_options}")

def cadastrar_autor(): # Cadastra o Autor
    nome = input('Nome do Autor: ').strip().upper()
    nacionalidade = input('Nacionalidade: ').strip().upper()
    if any(autor.get_nome() == nome for autor in autores):
        print("Autor já está cadastrado.")
    else:
        autores.append(Autor(nome, nacionalidade))

def cadastrar_livro(): # Cadastra o Livro
        titulo = input('Título: ').strip().upper()
        if any(livro.get_titulo() == titulo for livro in livros): # Talvez criar outra função para verificar se o livro ja esta cadastrado
            print("Livro já está cadastrado.")
            return

        while True:
            try:
                ano = int(input('Ano: '))
                break
            except ValueError:
                print(f'Valor inválido!')
        nome_autor = input('Nome do Autor: ').strip().upper()
        for autor in autores:
            if autor.get_nome().lower() == nome_autor:
                livros.append(Livro(titulo, ano, autor))
                print('Livro cadastrado com sucesso.')
                return
        else:
            print(f'Autor informado não está cadastrado no sistema. Por favor, cadastre o autor antes de cadastrar o livro!')

def remover_livro(): # Remove um livro existente 
    titulo_livro = input("Informe o título do livro que deseja remover: ").upper().strip()
    for livro in livros:
        if livro.get_titulo() == titulo_livro:
            livros.remove(livro)
            print(f"O livro '{titulo_livro}' foi removido com sucesso.")
            return
    else:
        print(f"O livro '{titulo_livro}' não existe em nosso banco de dados.")

def listar_livros():
    print('=' * 50)
    if not livros:
        print("Nenhum livro cadastrado no sistema.")
        return
    else:
        print(f'\nLivros:\n')
        for livro in livros:
            print('-' * 20)
            livro.exibir_info()  
    print('=' * 50)

def buscar_livro_titulo(): # Busca um Livro pelo Título
        titulo_livro = input('Informe o titulo do livro para a busca: ').upper().strip()
        busca_livro = [livro for livro in livros if titulo_livro in livro.get_titulo().upper()]
        if busca_livro:
            for livro in busca_livro:
                print('-' * 20)
                livro.exibir_info()
        else:
            print('Livro não encontrado!')
            

def buscar_autor(): # Buscar o Autor e seus livros pelo nome do Autor
    nome_autor = input('Informe o nome do autor para a busca: ').upper().strip()
    busca_autor = [livro for livro in livros if nome_autor in livro.get_autor().get_nome().upper()]
    if busca_autor:
        for livro in busca_autor:
            print('-' * 20)
            livro.exibir_info()
    else:
        print('Autor não encontrado!')

def carregar_autores(): # carrega o arquivo autores.json. Caso não tenha retorna uma lista vazia
    autores = []
    try:
        with open('autores.json', 'r') as arq:
            autores.extend([Autor.from_dict(autor) for autor in json.load(arq)])
    except FileNotFoundError:
        return []
    return autores

def carregar_livros(): # carrega o arquivo livros.json. Caso não tenha retorna uma lista vazia
    livros = []
    try:
        with open('livros.json', 'r') as arq:
            livros.extend([Livro.from_dict(livro) for livro in json.load(arq)])
    except FileNotFoundError:
        return []
    return livros
    
def salvar_autor():
    autores_dict = [autor.to_dict() for autor in autores]
    try:
        with open('autores.json', 'w') as arq:
            json.dump(autores_dict, arq, indent=4)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o autor!")

def salvar_livro():
        livros_dict = [livro.to_dict() for livro in livros]
        try:
            with open('livros.json', 'w') as arq:
                json.dump(livros_dict, arq, indent=4)
        except Exception as e:
            print(f"Ocorreu um erro ao salvar o livro!")
        
#####################################################################################################
autores = carregar_autores() # Variável para armazenar os autores
livros = carregar_livros() # Variável para armazenar os livros

msg = "[1] Cadastrar Autor\n[2] Cadastrar Livro\n[3] Listar Livros\n[4] Buscar Livro por Título\n[5] Buscar Livro por Autor\n[6] Remover Livro\n[0] Sair\n"
options = [0, 1, 2, 3, 4, 5, 6]

while True:

    op = option_input(msg, options)

    if op == 1: # Cadastrar Autor
        cadastrar_autor()
        salvar_autor()
        
    elif op == 2: # Cadastrar Livro
        cadastrar_livro()
        salvar_livro()


    elif op == 3: # Listar Livros
        listar_livros()
  
    elif op == 4: # Buscar livro por título
        buscar_livro_titulo()

    elif op == 5: # Buscar livro por autor
        buscar_autor()
    
    elif op == 6: # Remove um livro
        remover_livro()
        salvar_livro()
          
    elif op == 0: # Sair
        print('Encerrando programa...')   
        break


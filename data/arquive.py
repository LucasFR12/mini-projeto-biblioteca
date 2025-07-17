import json
import os
from model.autor import Autor
from model.livro import Livro


# Caminhos para salvar os arquivos na pasta "data"
BASE_DIR = os.path.dirname(__file__)
CAMINHO_AUTORES = os.path.join(BASE_DIR, 'autores.json')
CAMINHO_LIVROS = os.path.join(BASE_DIR, 'livros.json')

def carregar_autores(): # carrega o arquivo autores.json. Caso não tenha retorna uma lista vazia
    autores = []
    try:
        with open(CAMINHO_AUTORES, 'r') as arq:
            autores.extend([Autor.from_dict(autor) for autor in json.load(arq)])
    except FileNotFoundError:
        return []
    return autores

def carregar_livros(): # carrega o arquivo livros.json. Caso não tenha retorna uma lista vazia
    livros = []
    try:
        with open(CAMINHO_LIVROS, 'r') as arq:
            livros.extend([Livro.from_dict(livro) for livro in json.load(arq)])
    except FileNotFoundError:
        return []
    return livros
    
def salvar_autor(autores): # Salva o Autor cadastrado
    autores_dict = [autor.to_dict() for autor in autores]
    try:
        with open(CAMINHO_AUTORES, 'w') as arq:
            json.dump(autores_dict, arq, indent=4)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o autor!")

def salvar_livro(livros): # Salva o Livro cadastrado
        livros_dict = [livro.to_dict() for livro in livros]
        try:
            with open(CAMINHO_LIVROS, 'w') as arq:
                json.dump(livros_dict, arq, indent=4)
        except Exception as e:
            print(f"Ocorreu um erro ao salvar o livro!")
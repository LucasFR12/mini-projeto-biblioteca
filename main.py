from data.arquive import carregar_autores, carregar_livros, salvar_autor, salvar_livro
from service.livro_service import cadastrar_autor, cadastrar_livro, remover_livro, listar_livros, buscar_autor, buscar_livro_titulo
from service.menu_service import option_input


autores = carregar_autores() # Variável para armazenar os autores
livros = carregar_livros() # Variável para armazenar os livros

msg = "\n[1] Cadastrar Autor\n[2] Cadastrar Livro\n[3] Listar Livros\n[4] Buscar Livro por Título\n[5] Buscar Livro por Autor\n[6] Remover Livro\n[0] Sair\n"
options = [0, 1, 2, 3, 4, 5, 6]

while True:

    op = option_input(msg, options)

    if op == 1: # Cadastrar Autor
        cadastrar_autor(autores)
        salvar_autor(autores)
        
    elif op == 2: # Cadastrar Livro
        cadastrar_livro(livros, autores)
        salvar_livro(livros)

    elif op == 3: # Listar Livros
        listar_livros(livros)
  
    elif op == 4: # Buscar livro por título
        buscar_livro_titulo(livros)

    elif op == 5: # Buscar livro por autor
        buscar_autor(livros)
    
    elif op == 6: # Remove um livro
        remover_livro(livros)
        salvar_livro(livros)
          
    elif op == 0: # Sair
        print('Encerrando programa...')   
        break

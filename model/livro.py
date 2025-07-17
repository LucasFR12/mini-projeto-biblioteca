from model.autor import Autor # importando a classe Autor para o metodo from_dict()

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
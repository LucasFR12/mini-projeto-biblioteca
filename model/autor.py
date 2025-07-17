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
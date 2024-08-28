class Programa:
    def __init__(self, nome, ano):
        self.nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def imprime(self):
        print(f'Nome: {self.nome} - Likes: {self.ano}')
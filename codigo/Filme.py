from codigo.Programa import Programa
from abc import ABC
from collections.abc import MutableSequence

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'Nome: {self.nome} - duracao: {self.duracao}')

    def __str__ (self):
        return f'Nome: {self.nome} - duracao: {self.duracao}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'Nome: {self.nome} - temporadas: {self.temporadas}')

    def __str__ (self):
        return f'Nome: {self.nome} - temporadas: {self.temporadas}'


class PlayList(list):
    def __init__(self, nome, programas):
        super().__init__(programas)
        self.nome = nome

class PlayList_GetItem():
    def __init__(self, nome, programas):
        self._programas = programas
        self.nome = nome

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(selfs):
        return selfs._programas

    @property
    def __len__(selfs):
        return len(selfs._programas)


class PlayList_Abstract(MutableSequence):
    pass


filesm = PlayList_Abstract();

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')

lista = [vingadores,atlanta ]

playlist = PlayList('teste', lista)
playlist_getimte = PlayList_GetItem('teste', lista)

for programa in lista:
   print(programa)

for programa in playlist:
       print(programa)
1
for programa in playlist_getimte:
    print(programa)

#pyhthon data model
#__init__
#__str__, __contains__
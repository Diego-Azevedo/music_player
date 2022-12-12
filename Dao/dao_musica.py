from Dao.dao import DAO
from entidade.musica import Musica

#cada entidade terá uma classe dessa, implementação bem simples.
class MusicaDAO(DAO):
    def __init__(self):
        super().__init__('musicas.pkl')

    def add(self, musica: Musica):
        if((musica is not None) and isinstance(musica, Musica)):
            super().add(musica.id, musica)
        else:
          print("ERRO AQUI")

    def update(self, musica: Musica):
        if((musica is not None) and isinstance(musica, Musica)):
            super().update(musica.id, musica)

    def get(self):
        return super().get_random()

    def remove(selfself, key: int):
        print("AQUI")
        return super().remove(key)
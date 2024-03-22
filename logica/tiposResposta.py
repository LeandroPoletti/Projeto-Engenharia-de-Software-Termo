from enum import Enum

class tipoResposta(Enum):
    existePosCorreta = 1
    existePosErrada = 2
    naoExiste = 3
    tentativaInvalida = 4
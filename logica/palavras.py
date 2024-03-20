from dataclasses import dataclass
from tiposResposta import tipoResposta

@dataclass
class Palavra():
    nome: str
    listaResposta: list = None
    solved: bool = False
    
    def __post_init__(self):
        if self.listaResposta is None:
            self.listaResposta = []
            for i in self.nome:
                self.listaResposta.append(i)
    
    def checkAnswer(self, entrada: str):
        returnList = []
        for i in range(len(entrada)):
            returnList.append(self.__check(entrada[i], i))
            
        resultado = set(returnList)
        
        if len(resultado) == 1 and resultado == tipoResposta.existePosCorreta:
            self.solved = True
        
        return returnList
    
    def __check(self, letra: str, index: int):
        if letra == self.listaResposta[index]:
            return tipoResposta.existePosCorreta
        elif letra in self.listaResposta:
            return tipoResposta.existePosErrada
        else:
            return tipoResposta.naoExiste
    
    def getSolved(self) -> bool:
        return self.solved
        
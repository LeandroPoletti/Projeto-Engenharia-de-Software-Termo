from dataclasses import dataclass
from tiposResposta import tipoResposta
from estadoJogo import estadoJogo
from typing import List
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
        if len(entrada) == len(self.nome):
            returnList = []
            for i in range(len(entrada)):
                returnList.append(self._check(entrada[i], i))
            
            self._trySolve(returnList)
            
            return returnList
        else:
            return tipoResposta.tentativaInvalida
    
    def _trySolve(self, resultado: list):
        resultado = set(resultado)
        self.copia = resultado    
        if len(resultado) == 1:
            if tipoResposta.existePosCorreta in resultado:
                correta = True
            else:
                correta = False
            
            if correta:
                self.solved = True

    def _check(self, letra: str, index: int):
        if letra == self.listaResposta[index]:
            return tipoResposta.existePosCorreta
        elif letra in self.listaResposta:
            return tipoResposta.existePosErrada
        else:
            return tipoResposta.naoExiste
    
    def getSolved(self) -> bool:
        return self.solved

class Jogo():
    
    def __init__(self, palavras: list, tentativas: int) -> None:
        self.state = estadoJogo.naoSolucionado
        self.listaPalavras = palavras
        self.tentativasRestantes = tentativas
    
    def enterAttempt(self, entrada):
        self.tentativasRestantes -= 1
        solved = []
        for p in self.listaPalavras:
            p.checkAnswer(entrada)
            solved.append(p.getSolved())
        
        resumo = set(solved)
        if len(resumo) == 1 and True in resumo:
            self.state = estadoJogo.vencido
        elif self.tentativasRestantes == 0:
            self.state = estadoJogo.perdido
        
    def getWordState(self) -> List[bool]:
        result = []
        for p in self.listaPalavras:
            result.append(p.getSolved())
        return result
    
    def getState(self) -> estadoJogo:
        return self.state
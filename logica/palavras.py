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
            
    

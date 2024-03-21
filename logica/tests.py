from unittest import TestCase
from palavras import Palavra
from tiposResposta import tipoResposta

class PalavraTest(TestCase):
    
    def test_init(self):
        p = Palavra('teste')
        self.assertIsInstance(p, Palavra)
    
    def test_return_state_list(self):
        p = Palavra('Teste')
        # p.checkAnswer('Teste')
        expectedReturn = [
            tipoResposta.existePosCorreta,
            tipoResposta.existePosCorreta,
            tipoResposta.existePosCorreta,
            tipoResposta.existePosCorreta,
            tipoResposta.existePosCorreta,
        ]
        self.assertEqual(p.checkAnswer('Teste'), expectedReturn)
        
    def test_notice_all_incorrect_value(self):
        p = Palavra('Teste')
        entrada = 'lavar'
        expectedReturn = [
            tipoResposta.naoExiste,
            tipoResposta.naoExiste,
            tipoResposta.naoExiste,
            tipoResposta.naoExiste,
            tipoResposta.naoExiste,
        ]
        
        self.assertEqual(p.checkAnswer(entrada), expectedReturn)
        
    def test_return_quantity(self):
        p = Palavra('teste')
        entrada = 'tetsa'
        expectedReturn = [
            tipoResposta.existePosCorreta,
            tipoResposta.existePosCorreta,
            tipoResposta.existePosErrada,
            tipoResposta.existePosErrada,
            tipoResposta.naoExiste,
        ]
        self.assertEqual(p.checkAnswer(entrada), expectedReturn)
        
    def test_char_quantity_validation(self):
        p = Palavra('balo')
        entrada = 'bobo'
        # expectedReturn = [
        #     tipoResposta.existePosCorreta,
        #     tipoResposta.naoExiste,
        #     tipoResposta.naoExiste,
        #     tipoResposta.existePosCorreta
        # ]
        
        ### Perguntar pro Étttore ###
        
        
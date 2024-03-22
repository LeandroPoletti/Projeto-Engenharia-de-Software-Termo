from unittest import TestCase
from palavras import Palavra, Jogo
from tiposResposta import tipoResposta
from estadoJogo import estadoJogo

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
        
    # def test_char_quantity_validation(self):
    #     p = Palavra('balo')
    #     #entrada = 'bobo'
    #     # expectedReturn = [
    #     #     tipoResposta.existePosCorreta,
    #     #     tipoResposta.naoExiste,
    #     #     tipoResposta.naoExiste,
    #     #     tipoResposta.existePosCorreta
    #     # ]
        
    #     ### Perguntar pro Étttore ###
    
    def test_word_lenght(self):
        p = Palavra('teste')
        entrada = 'amar'
        expectedReturn = tipoResposta.tentativaInvalida
        self.assertEqual(p.checkAnswer(entrada), expectedReturn)
        
    def test_run_out_attempts(self):
        p1 = Palavra('test')
        gameWords = [p1]
        numberAttempts = 3
        game = Jogo(gameWords, numberAttempts)

        entrada = 'tesl'
        
        game.enterAttempt(entrada)
        game.enterAttempt(entrada)
        game.enterAttempt(entrada)
        
        self.assertEqual(game.getState(), estadoJogo.perdido)
        
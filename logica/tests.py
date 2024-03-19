from unittest import TestCase
from palavras import Palavra

class PalavraTest(TestCase):
    
    def test_init(self):
        p = Palavra('teste')
        self.assertIsInstance(p, Palavra)
    
    def test_return_exist(self):
        
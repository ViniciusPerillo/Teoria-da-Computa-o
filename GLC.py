from exceptions import GramaticaLivreDeContextoInvalida
from random import randint
class GLC:

    def __init__(self, 
                 nao_terminais: set[str],
                 terminais: set[str],
                 regras: dict[dict[set]],
                 inicio: str):
        
        self.nao_terminais =  nao_terminais
        self.terminais = terminais
        self.regras = regras
        self.inicio = inicio


    def validar_gramatica(self):
        if self.inicio not in self.nao_terminais:
            raise GramaticaLivreDeContextoInvalida

        for regra in self.regras:
            for key, values_set in regra:
                
                if len(key) > 1:
                    raise GramaticaLivreDeContextoInvalida
                if key not in self.nao_terminais:
                    raise GramaticaLivreDeContextoInvalida
                
                for value in values_set:
                    for char in value:
                        if char not in self.nao_terminais or char not in self.terminais:
                            raise GramaticaLivreDeContextoInvalida

    def _get_regra_aleatoria(self, nao_terminal):
        return self.regras[nao_terminal][randint(0, len(self.regras[nao_terminal]) - 1)]

    def get_sentenca_aleatoria(self):
        sentenca = self.inicio
        
        while True:
            nova_sentenca = ''
            for char in sentenca:
                if char in self.nao_terminais:
                    regra = self._get_regra_aleatoria(char)
                    nova_sentenca += regra
                else:
                    nova_sentenca += char

            if nova_sentenca == sentenca:
                return sentenca
            else: 
                sentenca = nova_sentenca        
    



# E -> II | CD | EG
# S -> + | - | * | /
# I -> II | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 
# D -> EF
# G -> SE
# C -> (
# F -> )
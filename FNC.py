from GLC import GLC
from exceptions import FormaNormalChomskyInvalida, GramaticaLivreDeContextoInvalida

from itertools import product

class FNC(GLC):
    
    def _validar_gramatica(self):
        if self.inicio not in self.nao_terminais:
            raise GramaticaLivreDeContextoInvalida

        for regra in self.regras:
            for key, values_set in regra:
                
                if len(key) > 1:
                    raise GramaticaLivreDeContextoInvalida
                if key not in self.nao_terminais:
                    raise GramaticaLivreDeContextoInvalida
                
                for value in values_set:

                    if value.islower() and len(value) != 1:
                        raise FormaNormalChomskyInvalida
                    if value.isupper() and len(value) != 2:
                        raise FormaNormalChomskyInvalida

                    for char in value:
                        if char not in self.nao_terminais or char not in self.terminais:
                            raise GramaticaLivreDeContextoInvalida
                        
    def CYK(self, sentenca: str):
        piramide = [[]]

        for char in sentenca:
            regras = []
            for nao_terminal in self.nao_terminais:
                if char in self.regras[nao_terminal]:
                    regras.append(nao_terminal)
            
            piramide[0].append(regras)

        for i in range(1, len(sentenca)):
            piramide.append([])
            for j in range(len(sentenca) - i):
                regras = set()
                for k in range(i):
                    nt1 = piramide[i-(k+1)][j]
                    nt2 = piramide[k][(j+i)-k]
                    
                    combinacoes = [''.join(pair) for pair in product(nt1, nt2)]

                    
                    for combinacao in combinacoes:
                        for nao_terminal in self.nao_terminais:
                            if combinacao in self.regras[nao_terminal]:
                                regras.add(nao_terminal)
                    
                piramide[i].append(list(regras))

        return self.inicio in piramide[i][0] 
 
                

            

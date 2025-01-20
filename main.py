from FNC import FNC
from random import choices, randint

def main():
    fnc = FNC(
        regras= {
            'E': ['II', 'CD', 'EG', 'II', 'II', 'EG'], # as repetições das mesmas regras são apenas para manipular o algoritmo de geração aleatória
            'S': ['+', '-', '*', '/'],
            'I': ['II', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\r'],
            'D': ['EF'],
            'G': ['SE'],
            'C': ['('],
            'F': [')']
        },
        nao_terminais={'E', 'S', 'I', 'D', 'G', 'C', 'F'},
        terminais={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')', '\r'},
        inicio='E'
    )

    for i in range(10):
        sent = fnc.get_sentenca_aleatoria()
        print(sent.replace('\r', ''))
        print(fnc.CYK(sent))
        print()

    for i in range(10):
        random_string = ''.join(choices(list(fnc.terminais), k=randint(1,32)))
        print(random_string)
        print(fnc.CYK(random_string))
        print()

if __name__ == '__main__':
    main()
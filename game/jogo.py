import os
import random
arquivo = open('game/words.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
arquivo.close()
words = conteudo.split()
stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

def jogar():
    print('='*45)
    print('1 - Fáceis\n2 - Difíceis\n3 - Infantis\n4 - Inglês')
    print('='*45)
    dificuldade = int(input('Escolha uma dificuldade acima: '))
    if dificuldade == 1:
        os.system('cls')
        numero = random.randrange(0, 41)
        palavra_secreta = words[numero].upper()
        tabuleiro = ['_'] * len(palavra_secreta)
        print('='*45)
        print('Perfeito, então vamos lá...')
        print('='*45)
        chances = 6
        listaletras = [letra for letra in palavra_secreta]
        letras_tentadas = []
        while chances > 0:
            if chances == 0:
                print(stages[0])
            elif chances == 1:
                print(stages[1])
            elif chances == 2:
                print(stages[2])
            elif chances == 3:
                print(stages[3])
            elif chances == 4:
                print(stages[4])
            elif chances == 5:
                print(stages[5])
            elif chances == 6:
                print(stages[6])
            print('Palavra:',tabuleiro)
            print('\nLetras tentadas:',letras_tentadas)
            tentativa = input('\nEscolha uma letra: ')
            tentativa = tentativa.upper()
            if tentativa in letras_tentadas:
                print('Opa! Parece que você já tentou essa letra!')
                continue
            letras_tentadas.append(tentativa)
            if tentativa in listaletras:
                print('Você acertou a letra!')
                for indice in range(len(listaletras)):
                    if listaletras[indice] == tentativa:
                        tabuleiro[indice] = tentativa
                if '_' not in tabuleiro:
                    print('\nVocê venceu! A palavra era {}'.format(palavra_secreta))
                    break
            else: 
                print('Opa, essa letra não está na palavra!')
                chances -= 1
        if '_' in tabuleiro and chances == 0:
            print('Você perdeu, sinto muito! A palavra era {}'.format(palavra_secreta))
    elif dificuldade == 2:
        os.system('cls')
        numero = random.randrange(42, 82)
        palavra_secreta = words[numero].upper()
        tabuleiro = ['_'] * len(palavra_secreta)
        print('='*45)
        print('Difícil hum? então vamos lá...')
        print('='*45)
        chances = 6
        listaletras = [letra for letra in palavra_secreta]
        letras_tentadas = []
        while chances > 0:
            if chances == 0:
                print(stages[0])
            elif chances == 1:
                print(stages[1])
            elif chances == 2:
                print(stages[2])
            elif chances == 3:
                print(stages[3])
            elif chances == 4:
                print(stages[4])
            elif chances == 5:
                print(stages[5])
            elif chances == 6:
                print(stages[6])
            print('Palavra:',tabuleiro)
            print('\nLetras tentadas:',letras_tentadas)
            tentativa = input('\nEscolha uma letra: ')
            tentativa = tentativa.upper()
            if tentativa in letras_tentadas:
                print('Opa! Parece que você já tentou essa letra!')
                continue
            letras_tentadas.append(tentativa)
            if tentativa in listaletras:
                print('Você acertou a letra!')
                for indice in range(len(listaletras)):
                    if listaletras[indice] == tentativa:
                        tabuleiro[indice] = tentativa
                if '_' not in tabuleiro:
                    print('\nVocê venceu! A palavra era {}'.format(palavra_secreta))
                    break
            else: 
                print('Opa, essa letra não está na palavra!')
                chances -= 1
        if '_' in tabuleiro and chances == 0:
            print('Você perdeu, sinto muito! A palavra era {}'.format(palavra_secreta))
    elif dificuldade == 3:
        os.system('cls')
        numero = random.randrange(83, 101)
        palavra_secreta = words[numero].upper()
        tabuleiro = ['_'] * len(palavra_secreta)
        print('='*45)
        print('Perfeito, então vamos lá...')
        print('='*45)
        chances = 6
        listaletras = [letra for letra in palavra_secreta]
        letras_tentadas = []
        while chances > 0:
            if chances == 0:
                print(stages[0])
            elif chances == 1:
                print(stages[1])
            elif chances == 2:
                print(stages[2])
            elif chances == 3:
                print(stages[3])
            elif chances == 4:
                print(stages[4])
            elif chances == 5:
                print(stages[5])
            elif chances == 6:
                print(stages[6])
            print('Palavra:',tabuleiro)
            print('\nLetras tentadas:',letras_tentadas)
            tentativa = input('\nEscolha uma letra: ')
            tentativa = tentativa.upper()
            if tentativa in letras_tentadas:
                print('Opa! Parece que você já tentou essa letra!')
                continue
            letras_tentadas.append(tentativa)
            if tentativa in listaletras:
                print('Você acertou a letra!')
                for indice in range(len(listaletras)):
                    if listaletras[indice] == tentativa:
                        tabuleiro[indice] = tentativa
                if '_' not in tabuleiro:
                    print('\nVocê venceu! A palavra era {}'.format(palavra_secreta))
                    break
                if '_' in tabuleiro and chances == 0:
                    print('Você perdeu, sinto muito! A palavra era {}'.format(palavra_secreta))
            else: 
                print('Opa, essa letra não está na palavra!')
                chances -= 1
        if '_' in tabuleiro and chances == 0:
            print('Você perdeu, sinto muito! A palavra era {}'.format(palavra_secreta))
    elif dificuldade == 4:
        os.system('cls')
        numero = random.randrange(102, 131)
        palavra_secreta = words[numero].upper()
        tabuleiro = ['_'] * len(palavra_secreta)
        print('='*45)
        print('Perfeito, então vamos lá...')
        print('='*45)
        chances = 6
        listaletras = [letra for letra in palavra_secreta]
        letras_tentadas = []
        while chances > 0:
            if chances == 0:
                print(stages[0])
            elif chances == 1:
                print(stages[1])
            elif chances == 2:
                print(stages[2])
            elif chances == 3:
                print(stages[3])
            elif chances == 4:
                print(stages[4])
            elif chances == 5:
                print(stages[5])
            elif chances == 6:
                print(stages[6])
            print('Palavra:',tabuleiro)
            print('\nLetras tentadas:',letras_tentadas)
            tentativa = input('\nEscolha uma letra: ')
            tentativa = tentativa.upper()
            if tentativa in letras_tentadas:
                print('Opa! Parece que você já tentou essa letra!')
                continue
            letras_tentadas.append(tentativa)
            if tentativa in listaletras:
                print('Você acertou a letra!')
                for indice in range(len(listaletras)):
                    if listaletras[indice] == tentativa:
                        tabuleiro[indice] = tentativa
                if '_' not in tabuleiro:
                    print('\nVocê venceu! A palavra era {}'.format(palavra_secreta))
                    break
            else: 
                print('Opa, essa letra não está na palavra!')
                chances -= 1
        if '_' in tabuleiro and chances == 0:
            print('Você perdeu, sinto muito! A palavra era {}'.format(palavra_secreta))
    else:
        os.system('cls')
        print('ERRO: ESCOLHA UM NUMERO DE 1-4')
        jogar()
#1-41 faceis
#43-82 difíceis
#83-102 Infantil
#102-132 inglês
def regras():
    os.system('cls')
    print('='*90)
    print('Como jogar / regras:')
    print('1 - O Jogo escolherá uma palavra aleatória da dificuldade selecionada.')
    print('2 - Você pode saber quantas letras tem a palavra pela quantidade de tracinhos.')
    print('3 - O jogador escolhe uma letra do alfabeto por vez.')
    print('4 - Caso a palavra possua essa letra ela aparecerá em seu respectivo local.')
    print('5 - Caso a palavra não possua essa letra, o boneco ganhará um novo membro.')
    print('6 - O objetivo é adivinhar a palavra correta antes que o boneco inteiro seja enforcado.')
    print('Boa Sorte Jogador!')
    print('='*90)
def main():
    while True:
        print('Bem vindo ao jogo da forca!')
        menu = int(input('1 - Jogar\n2 - Como Jogar/Regras\n3 - Sair\nO que deseja fazer? '))
        if menu == 1:
            os.system('cls')
            jogar()
            break
        elif menu == 2:
            os.system('cls')
            regras()
        elif menu == 3:
            os.system('cls')
            break
main()
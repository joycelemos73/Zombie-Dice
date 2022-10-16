# Raciocínio Computacional (11100010563_20222_03)
#PUCPR - Análise e Desenvolvimento de Sistemas
# Aluna: Joyce Lemos

# ZOMBIE DICE

import random
import sys
from time import sleep

print('=-' * 10)
print(' ' * 5, 'ZOMBICIDE')
print('=-' * 10)
print('')

nomeJogadores = {}
numJogadores = 0
dadoFace = []
dadoVerde = ['C', 'P', 'C', 'T', 'P', 'C']
dadoAmarelo = ['T', 'P', 'C', 'T', 'P', 'C']
dadoVermelho = ['T', 'P', 'T', 'C', 'P', 'T']
dadoResultados = []


def inicioPartida():
    global numJogadores, nomeJogadores
    while numJogadores < 2:
        numJogadores = int(input('Digite o número de jogadores: [mín.: 2] '))
        if numJogadores < 2:
            print('Opção inválida. Mínimo de jogadores: 2')

    for c in range(numJogadores):
        nomeJogadores.update({str(input(f'Digite o nome do {c + 1}º jogador: ')): {'P': 0, 'C': 0, 'T': 0}})
    print(nomeJogadores)

def novaRolagem():
    sleep(1)
    print('')
    print('=-' * 10)
    print('Escolhendo dados...')
    print('=-' * 10)
    sleep(2)
    print('')
    print('Agora vamos ver quais dados você pegou!')
    sleep(2)
    print('')


def pegarDados():
    dadosJogador = []
    dadosCor = (6 * 'verde ').split() + (4 * 'amarelo ').split() + (3 * 'vermelho ').split()
    print(dadosCor)
    for c in range(0, 3):
        dadosJogador += [random.choice(dadosCor)]
        dadosCor.remove(dadosJogador[-1])
    print(f'Você pegou dados das seguintes cores: ')
    print(dadosJogador)
    print('')
    return dadosJogador


def rolarDados():
    dadosJogador = pegarDados()
    dadoFace = []
    for cor in dadosJogador:
        if cor == 'verde':
            dadoFace += [random.choice(dadoVerde)]
        elif cor == 'amarelo':
            dadoFace += [random.choice(dadoAmarelo)]
        else:
            dadoFace += [random.choice(dadoVermelho)]
    print(f'Essas são as faces dos seus dados: ')
    print(dadoFace)
    print('')
    return dadoFace


def partida():
    inicioPartida()
    while True:
        for jogador in nomeJogadores.keys():
            print(f'Zumbi, {jogador}... Agora é a sua vez!')
            while True:
                novaRolagem()
                dadoResultados = rolarDados()
                for d in dadoResultados:
                    if d == 'P':
                        nomeJogadores[jogador]['P'] += 1
                    elif d == 'C':
                        nomeJogadores[jogador]['C'] += 1
                        if nomeJogadores[jogador]['C'] >= 13:
                            print(f'FIM DE PARTIDA. {jogador} VENCEU!')
                            sys.exit()
                    elif d == 'T':
                        nomeJogadores[jogador]['T'] += 1
                        if nomeJogadores[jogador]['T'] >= 3:
                            nomeJogadores.pop(jogador)
                            print(f'FIM DE PARTIDA. {jogador} PERDEU!')
                            sys.exit()

                print(f'Zumbi {jogador} recebeu {nomeJogadores[jogador]["T"]} tiros, comeu {nomeJogadores[jogador]["C"]} cérebros, e sua vítima fugiu {nomeJogadores[jogador]["P"]} passos.')

                continuarPartida = input('Deseja continuar sua partida? [S/N] ').upper()
                if continuarPartida == 'N':
                    nomeJogadores[jogador]['P'] = 0
                    nomeJogadores[jogador]['T'] = 0
                    break

partida()
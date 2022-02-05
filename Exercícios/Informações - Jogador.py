jogadores = {}
gols = []
time = []

while True:
    jogadores.clear()
    gols.clear()
    jogadores['jogador'] = str(input('Digite o nome do jogador: '))
    jogadores['partidas'] = int(input(f'Quantas partidas o {jogadores["jogador"]} jogou? '))
    for p in range (1, jogadores['partidas']+1):
        gols.append(int(input(f'Quantos gols ele marcou na partida {p}? ')))
    jogadores['gols'] = gols[:]
    jogadores['total'] = sum(gols)
    time.append(jogadores.copy())
    resp = str(input('Deseja adicionar mais algum jogador? [S/N] ')).strip().upper()[0]
    if resp in 'S':
        continue
    else:
        break
print('='*30)
print('cod', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print()
print('='*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*40)
while True:
    busca = int(input('Mostrar os dados de qual jogador? 999 para parar '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro. não existe jogador com o cód da {busca}')
    else:
        print(f' --- levantamento do jogador {time[busca]["jogador"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1}, fez {g} gols')
    print('='*40)
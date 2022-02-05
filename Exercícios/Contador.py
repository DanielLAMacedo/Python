import random
from time import sleep

def contador(i, f, p):
    if p < 0:
       p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p} é igual a: ')


    if i < f:
        cont = i
        while cont <= f:
            print(f' {cont} ', end='', flush=True)

            cont += p
        print('fim!')
    else:
        cont = i
        while cont >= f:
            print(f' {cont} ', end='', flush=True)

            cont -= p
        print('fim')


contador(1,10,1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
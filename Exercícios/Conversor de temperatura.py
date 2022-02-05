while True:
    print()
    valor= input('Digite o valor ser convertido: ').strip()
    if not valor.isnumeric() or not valor.isdecimal():
        print('Por favor, digite um número!')
        continue
    escala= input('O valor informado está em (1)°C, (2)°F ou (3)K: ').strip()
    if escala > '3' or escala <='0':
        print('Digite uma das opções solicitadas!')
        continue

    valor = float(valor)
    escala = int(escala)

    if escala == 1:
        e1= input('Você deseja converter em (1)°F ou (2)K? ')
        if e1 == '1':
            print(f'O valor informado {valor}°C, corresponde a {(valor*9/5+32)}°F')
        else:
            print(f'O valor informado {valor}°C, corresponde a {(valor+273,15)}K')
    elif escala == 2:
        e2= input('Você deseja converter em (1)°C ou (2)K? ')
        if e2 == '1':
            print(f'O valor informado {valor}°F corresponde a {((valor-32)*5/9):.2f}°C')
        else:
            print(f'O valor informado {valor}°F corresponde a {((valor-32)*5/9)+273.15:.2f}K')
    else:
        e3= input('Você deseja converter em (1)°C ou (2)K? ')
        if e3 == '1':
            print(f'O valor informado {valor}K corresponde a {valor-273.15:.2f}°C')
        else:
            print(f'O valor informado {valor}K corresponde a {(((valor-273.15)*9/5)+32):.2f}°F')
    sair = input('Deseja sair? (1)SIM, (2)NÃO ')
    if sair == '1':
        break
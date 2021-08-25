print('bem vindo escolha qual tipo de operação deseja fazer: (1) adição (2) subtração (3) divisão (4) multiplicação')

operacao_escolhida = int(input("digite o número de qual operação você escolheu: "))

if operacao_escolhida == 1:
    print('digite alguns números dos quais deseja somar abaixo:')
    numero_a = int(input("digite aqui o primeiro número: "))
    numero_b = int(input("digite aqui o segundo número: "))
    print(int(numero_a + numero_b))
elif operacao_escolhida == 2:
    print('digite alguns números dos quais deseja subtraír abaixo:')
    numero_a = int(input("digite aqui o primeiro número: "))
    numero_b = int(input("digite aqui o segundo número: "))
    print(int(numero_a - numero_b))
elif operacao_escolhida == 3:
    print('digite alguns números dos quais deseja dividir abaixo:')
    numero_a = int(input("digite aqui o primeiro número: "))
    numero_b = int(input("digite aqui o segundo número: "))
    print(int(numero_a / numero_b))
elif operacao_escolhida == 4:
    print('digite alguns números dos quais deseja multiplicar abaixo:')
    numero_a = int(input("digite aqui o primeiro número: "))
    numero_b = int(input("digite aqui o segundo número: "))
    print(int(numero_a * numero_b))

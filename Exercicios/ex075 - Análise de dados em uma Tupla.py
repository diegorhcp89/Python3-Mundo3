núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o ultimo número: ')))
print(f'Você digitou os valores {núm}')
if 9 in núm:
    print(f'O valor 9 apareceu {núm.count(9)} vezes')
else:
    print('O valor 9 não apareceu nenhuma vez')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi identificado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
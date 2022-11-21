num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')

for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

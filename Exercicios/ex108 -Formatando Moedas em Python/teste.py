import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominado: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')

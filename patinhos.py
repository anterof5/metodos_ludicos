patinhos = 5
contador = patinhos
for n in range(contador):
    if contador is not 1:
        # Usar plural
        print('%i Patinhos foram passear além das montanhas para brincar' % contador)
    else:
        # Usar singular
        print('%i Patinho foi passear além das montanhas para brincar' % contador)
    print('A mamãe gritou quá, quá, quá, quá!')
    contador = contador - 1

    if contador is not 0 and contador is not 1:
        print('Mas só %i patinhos voltaram de lá.' % contador)
    elif contador is 1:
        print('Mas só %i patinho voltou de lá.' % contador)
    else:
        print('Mas nenhum patinho voltou de lá...')

print('''
A mamãe patinha foi procurar
Além das montanhas Na beira do mar
A mamãe gritou: Quá, quá, quá, quá
E os %i patinhos voltaram de lá''' % patinhos)

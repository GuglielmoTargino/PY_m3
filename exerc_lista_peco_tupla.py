
#exercício utilizando tupla
lista=('lapis',1.75,'caderno',20.35,'borracha',2.15)
print(f'{lista}')

for pos in range(0,len(lista)):
    if pos%2==0:
        print(f'{lista[pos]:.<15}',end='')# :.<15 serve para preencher 15 espaços com .
    else:
        print(f' R${lista[pos]}')

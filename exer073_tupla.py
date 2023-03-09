#programa para mostrar os carros em uma tabela
# fiat, ford, vw=volkswagem, gm=chevrolet, rn=renault

lista=('fiat','ford','vw','gm','rn')

print(f'os tres melhores sao{lista[0:3]}')
print(f'os ultimos são {lista[:-2]}') # [lista [:-2] contagem de tras pra frente]
print(f' em ordem alfabetica é {sorted(lista)}')
print(f' a ford está na posição {lista.index("ford")+1}')

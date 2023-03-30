def calcular_media(x):
    soma=0
    for numero in x:
        soma+=numero
    return soma/len(x)

idade=[2,3,4]
print(f"a media é {calcular_media(idade)}")




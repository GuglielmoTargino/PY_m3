# o programa pedirá um numero ao usuario entre 1 e 10
# e o exibirá por extenso esse número.

nr=('0','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')

while True: # linha para garantir digitação correta pelo usuario
    pos=int(input('Digite um número entre 1 e 10_'))
    if 1<=pos<=10:
        break

print('VC digitou ',nr[pos])


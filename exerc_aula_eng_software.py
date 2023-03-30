
#soma1=10+15
#soma2=25+15
#soma3=5+25
#soma4=2+35
#print(f" as quatro somas são {soma1},{soma2},{soma3},{soma4}")

#def soma(numero1, numero2):#cria uma função para se somar dois numeros.
  #return numero1 + numero2 # a variável <soma> returna com o valor de return.

#print(f"A soma do número 5 e 6 é de {soma(5,6)}")# (5,6) o 5=numero1, e o 6=numero2.

def saudacao(nome):
    print(f" Bem vindo {nome}")

saudacao("guga")

#================================================
def calcular_quadrado(numero):
  return numero * numero

def calcular_soma(numero1, numero2):
  soma = numero1 + numero2
  print(f'A soma dos números {numero1} e {numero2} é de {soma}')
  #=============================================================

  # Função principal
def main(): # abre com main e tem que fechar lá embaixo
  # Lê dois número dado pelo usuário
  numero1 = float(input("Digite o primeiro número:\t")) 
  numero2 = float(input("Digite o segundo número:\t"))

  # Calcula o quadrado do primeiro número
  quadrado = calcular_quadrado(numero1)

  # Calcula soma dos dois números informados
  calcular_soma(numero1, numero2)

  # Imprime a soma dos dois números
  print('O quadrado de ', numero1, " é ", quadrado)
main() # fecha o bloco com main.


    




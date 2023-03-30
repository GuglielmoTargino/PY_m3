
  
def calcular_quadrado(q):
  return q*q

def calcular_soma(numero1,numero2):
  return numero2+numero1 


# Função principal
def main(): # abre com main e tem que fechar lá embaixo
  # Lê dois número dado pelo usuário
  numero1 = float(input("Digite o primeiro número:\t")) 
  numero2 = float(input("Digite o segundo número:\t"))

  # Calcula o quadrado do primeiro número
  quadrado = calcular_quadrado(numero1)  

  # Calcula soma dos dois números informados
  soma=calcular_soma(numero1, numero2)
  
   # Imprime a soma dos dois números
  print('O quadrado de ', numero1, " é ", quadrado)
  print(f"a soma de {numero1} com {numero2} é {soma}")

main() # fecha o bloco com main.



    




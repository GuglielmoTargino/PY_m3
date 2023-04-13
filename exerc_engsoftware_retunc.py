# Criando um decorador sem notação
import time # importe da biblioteca time

def criar_potencia(x): #x^y
  def potencia(y):
    return x ** y
  return potencia

# Potência de 5 elevado a 10
resultado = criar_potencia(3)
print(resultado(2))
#imorimindo a data
print(time.localtime()[2])
print(time.localtime()[1])
print(time.localtime()[0])
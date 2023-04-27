#programa com tupla dentro de tupla.
palavra=('carro','livro','pedra')


for g in palavra:
   print(f"a palavra é {g.upper()}")
   for letra in g:
     if letra in 'aeiou':
    
      print(f"as vogais são {letra}")

def cumprimento(nome):
 return f"Olá, {nome}! Seja bem-vinda!"

print(cumprimento("Luana Pinheiro Pinto Silva")) 

import random

def cumprimento(nome):
 return f"Olá, {nome}! Seja bem-vinda!"

def sorteia_media():
numeros = [random.randint(1, 50) for _ in range(3)] 
media = sum(numeros) / len(numeros)
return media

print(cumprimento("Luana Pinheiro Pinto Silva"))
print(f"A média dos números sorteados é: {sorteia_media()}")

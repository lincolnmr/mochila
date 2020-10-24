import random

beneficio = [3, 3, 2, 4, 2, 3, 5, 2]
peso = [5, 4, 7, 8, 4, 4, 6, 8]

def getCromossomo( tamanho ):
  i = 0
  cromossomo = []
  while i < tamanho:
    gene = random.randint(0, 1)
    cromossomo.append(gene)
    i += 1
  return cromossomo

tamanho = 8
cromossomo = getCromossomo( tamanho )

def fitness( cromossomo ):
  i = 0
  vPeso = 0
  vBeneficio = 0
  
  while i < tamanho:
    gene = cromossomo[i]
    if gene == 1:
      vBeneficio += beneficio[i]
      vPeso +=  peso[i]
    i +=1
  if vPeso > 25:
    vBeneficio = -1
  return vBeneficio      

vBeneficio = -1
tamanhoPop = 10

while vBeneficio < 13:
  cromossomo = getCromossomo( tamanho )
  vBeneficio = fitness( cromossomo ) 
  print(cromossomo)  
  print(vBeneficio)

from random import randint

def lista_grande(n):
	lista_r = [randint(1,900) for i in range(n)]
	return lista_r
	
#print(lista_grande(5))
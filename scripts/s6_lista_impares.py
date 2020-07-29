def encontra_impares(lista, lista_impar=[]):
	if len(lista)<1:
		return lista_impar
	else:
		if lista[0]%2:
			lista_impar.append(lista[0])
		lista.remove(lista[0])
		return encontra_impares(lista,lista_impar)
		
#print(encontra_impares([1,2,3,4,5,6,67,7]))
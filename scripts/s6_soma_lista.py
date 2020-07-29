def soma_lista(lista, indice=0, soma =0):
	if indice >= len(lista):
		return soma
	soma += lista[indice]
	indice +=1
	return soma_lista(lista, indice, soma)
	
#print(soma_lista([1,2,3,4]))
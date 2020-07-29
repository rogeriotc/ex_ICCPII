def ordena(lista, passo=0):
	if passo == len(lista)-1:
		return lista
	else:
		min = passo+1
		for i in range(min,len(lista)):
			if lista[i] < lista[min-1]:
				lista[min-1], lista[i] = lista[i], lista[min-1]
		return ordena(lista, passo=min)
    	 
print(ordena([2,5,3,1,7,0,4]))
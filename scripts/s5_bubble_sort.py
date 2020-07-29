def bubble_sort(lista, fim=False):
	if fim:
		return lista
	fim = True
	for i in range(len(lista)-1):
		if lista[i] > lista[i+1]:
			lista[i], lista[i+1] = lista[i+1], lista[i]
			print(lista)
			fim = False
	return bubble_sort(lista, fim)
	
#print(bubble_sort([5,1,4,2]))
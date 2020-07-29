def busca(lista, elemento, min=0,max=0):
	if max < min:
		return False
	else:
		if max == 0:
			max = len(lista)-1
		meio = (min+max)//2
		print(meio)
		if elemento > lista[meio]:
			min = meio+1
			return busca(lista, elemento, min, max)
		elif elemento < lista[meio]:
			max = meio -1
			return busca(lista, elemento, min, max)
		else:
			return meio

#print('esse', busca([1,2,3,5,7,9],4))
def busca(lista, elemento):
	for i in range(len(lista)):
		if elemento == lista[i]:
			return i
	return False
	
#print(busca(['a','e','i'],'o'))
def ordenada(lista):
	lista_clone = lista[:]
	lista.sort()
	if lista_clone == lista:
		return True
	else:
		return False


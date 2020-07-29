def incomodam(n, frase=''):
    if n < 1:
        return frase
    else:
        frase = frase + 'incomodam '
        return incomodam(n-1, frase)


def elefantes(n, nmax=1, frase='Um elefante incomoda muita gente\n'):
    if n < nmax+1:
        return frase
    else:
        if nmax > 1:
            frase = frase + str(nmax) + ' elefantes incomodam muita gente\n'
        nmax += 1
        frase = frase + str(nmax) + ' elefantes ' + incomodam(nmax) + \
            'muito mais\n'
    return elefantes(n, nmax, frase)

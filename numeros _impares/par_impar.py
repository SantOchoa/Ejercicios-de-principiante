numeros =  [1,2,3,4,5,6,7,8,9,10]


def calnumimpar(numeros: list)->list: 
    pares = 0
    for n in numeros:
        if n%2 ==0:
            pares += 1
    return pares

countpar = calnumimpar(numeros)
print(countpar)
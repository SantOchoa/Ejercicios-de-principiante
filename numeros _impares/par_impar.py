def calnumpar(numeros: list)->int: 
    pares = 0
    for n in numeros:
        if n%2 ==0:
            pares += 1
    return pares

def calnumimpar(numeros:list)-> int:
    impares =0 
    for n in numeros:
        if n%2 != 0 :
             impares += 1 
    return impares
    



numeros =  [1,2,3,4,5,6,7,8,9,10,11]
countpar = calnumpar(numeros)
countimpar = calnumimpar(numeros)
print(f"Hay {countpar} numeros pares en la lista")
print(f"Hay {countimpar} numeros inpares en la lista")

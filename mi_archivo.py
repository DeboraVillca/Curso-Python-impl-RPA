#pruebas de las clases 1 y 2 
numeros=[1, 2, 3, 4, 5]

numeros_dobles=[]
for numero in numeros:

    numeros_dobles.append(numero*2)

print(numeros_dobles)

#with open(file) as var:
#procesar el archivo
#reverse, copia la lista y la da vuelta(menos trabajoso que copiar y darla vuelta)
numeros_reverse=numeros[::-1]
print(numeros_reverse)
#no es bueno tener dos listas para muchos elementos
print(numeros[:])#imprime todos los elementos
#tuplas similar a listas , inmutable,metodos count()index()
#todo pude ser anidado ,para el tamaño es print(len(tupla))
#no puede ser compresion list


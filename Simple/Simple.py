import random
import doctest

#Obtiene una lista de 10 Diccionarios con su id y una edad aleatoria de 1 a 100.
def listaDiccionario():
    """
       >>> l=listaDiccionario()
       >>> len(l)==10
       True
       >>> l[0]['id']==0
       True
       >>> 1<=l[0]['edad']<=100
       True
       >>> l[1]['id']==1
       True
       >>> 1<=l[1]['edad']<=100
       True
       >>> l[2]['id']==2
       True
       >>> 1<=l[2]['edad']<=100
       True
       >>> l[3]['id']==3
       True
       >>> 1<=l[3]['edad']<=100
       True
       >>> l[4]['id']==4
       True
       >>> 1<=l[4]['edad']<=100
       True
       >>> l[5]['id']==5
       True
       >>> 1<=l[5]['edad']<=100
       True
       >>> l[6]['id']==6
       True
       >>> 1<=l[6]['edad']<=100
       True
       >>> l[7]['id']==7
       True
       >>> 1<=l[7]['edad']<=100
       True
       >>> l[8]['id']==8
       True
       >>> 1<=l[8]['edad']<=100
       True
       >>> l[9]['id']==9
       True
       >>> 1<=l[9]['edad']<=100
       True
    """
    lista=[]
    i=0
    for i in range(10):
        e=random.randint(1,100)
        diccionario={'id':i,'edad':e}
        lista.append(diccionario)
    return lista

#Ordena la lista de mayor a menor edad
#Imprime el id del más joven y el más viejo
#Devuelve la lista ordenada
def ordenarlista(lista):
    """
       >>> l=listaDiccionario()
       >>> a=ordenarlista(l)
       >>> l!=a
       True
       >>> a[len(a)-1]['id']==a[9]['id']
       True
       >>> a[0]['edad']>=a[1]['edad']>=a[2]['edad']>=a[3]['edad']>=a[4]['edad']>=a[5]['edad']>=a[6]['edad']>=a[7]['edad']>=a[8]['edad']>=a[9]['edad']
       True
    """
    arreglo=lista[:]
    izquierda=0
    derecha=len(arreglo)-1
    quicksort(arreglo,izquierda,derecha)
    print("El id de la persona más joven es: ",arreglo[len(arreglo)-1]['id'])
    print("El id de la persona más vieja es: ",arreglo[0]['id'])
    return arreglo

#Metodo recursivo de quicksort
def quicksort(arreglo, izquierda, derecha):
    if izquierda < derecha:
        indiceParticion = particion(arreglo, izquierda, derecha)
        quicksort(arreglo, izquierda, indiceParticion)
        quicksort(arreglo, indiceParticion + 1, derecha)

#Realiza la partición haciendo los intercambios del quicksort
def particion(arreglo, izquierda, derecha):
    pivote = arreglo[izquierda]['edad']
    while True:
        # Mientras cada elemento desde la izquierda esté en orden (sea mayor que el
        # pivote) continúa avanzando el índice
        while arreglo[izquierda]['edad'] > pivote:
            izquierda += 1

        # Mientras cada elemento desde la derecha esté en orden (sea menor que el
        # pivote) continúa disminuyendo el índice
        while arreglo[derecha]['edad'] < pivote:
            derecha -= 1

        """
            Si la izquierda es mayor o igual que la derecha significa que no
            necesitamos hacer ningún intercambio
            de variables, pues los elementos ya están en orden (al menos en esta
            iteración)
        """
        if izquierda >= derecha:
            # Indicar "en dónde nos quedamos" para poder dividir el arreglo de nuevo
            # y ordenar los demás elementos
            return derecha
        else:
            """
                Si las variables quedaron "lejos" (es decir, la izquierda no superó ni
                alcanzó a la derecha)
                significa que se detuvieron porque encontraron un valor que no estaba
                en orden, así que lo intercambiamos
            """
            arreglo[izquierda], arreglo[derecha] = arreglo[derecha], arreglo[izquierda]
            """
                Ya intercambiamos, pero seguimos avanzando los índices
            """
            izquierda += 1
            derecha -= 1

print = lambda *args, **kwargs: None            
doctest.testmod(verbose=True)

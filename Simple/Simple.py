#Obtiene una lista de 10 Diccionarios con su id y una edad aleatoria de 1 a 100.
import random
import doctest
def listaDiccionario():
    """
       >>> l=listaDiccionario()
       >>> len(l)==10
       True
       >>> l[0]['id']==0
       True
       >>> 0<=l[0]['edad']<=100
       True
       >>> l[1]['id']==1
       True
       >>> 0<=l[1]['edad']<=100
       True
       >>> l[2]['id']==2
       True
       >>> 0<=l[2]['edad']<=100
       True
       >>> l[3]['id']==3
       True
       >>> 0<=l[3]['edad']<=100
       True
       >>> l[4]['id']==4
       True
       >>> 0<=l[4]['edad']<=100
       True
       >>> l[5]['id']==5
       True
       >>> 0<=l[5]['edad']<=100
       True
       >>> l[6]['id']==6
       True
       >>> 0<=l[6]['edad']<=100
       True
       >>> l[7]['id']==7
       True
       >>> 0<=l[7]['edad']<=100
       True
       >>> l[8]['id']==8
       True
       >>> 0<=l[8]['edad']<=100
       True
       >>> l[9]['id']==9
       True
       >>> 0<=l[9]['edad']<=100
       True
    """
    lista=[]
    i=0
    for i in range(10):
        e=random.randint(1,100)
        diccionario={'id':i,'edad':e}
        lista.append(diccionario)
    return lista




doctest.testmod(verbose=True)

import random
import doctest

#Crea una matriz de enteros aleatorios y si encuentra una secuencia de 4
#consecutivos imprime su posición inicial y final.
def matrizConsecutivos():
    m=crearMatriz()
    f=consecutivosFila(m)
    c=consecutivosColumna(m)
    if (len(f)>0 or len(c)>0):
        print("Hay cuatro enteros consecutivos en: ")
        i=0
        while(i<(len(f))):
            print("(",f[i],",",f[i+1],") hasta (",f[i],",",f[i+2],")")
            i=i+3
        i=0
        while(i<(len(c))):
            print("(",c[i],",",c[i+1],") hasta (",c[i+2],",",c[i+1],")")
            i=i+3
    
#Creo la matriz
def crearMatriz():
    """
       >>> m=crearMatriz()
       >>> len(m)==5
       True
       >>> len(m[0])==5
       True
       >>> len(m[1])==5
       True
       >>> len(m[2])==5
       True
       >>> len(m[3])==5
       True
       >>> len(m[4])==5
       True
    """
    m=[]
    for i in range(5):
        m.append([])
        for j in range(5):
            m[i].append(random.randint(-9223372036854775808, 9223372036854775807))
    return m

    
#Veo si hay 4 consecutivos en las filas
def consecutivosFila(m):
    """
       >>> m=[[0,1,2,3,4],[-1,0,1,2,3],[-2,-1,0,1,2],[2,5,7,8,9],[0,-1,-2,-3,-4]]
       >>> f=consecutivosFila(m)
       >>> len(f)==18
       True
       >>> f[0]==0
       True
       >>> f[1]==0
       True
       >>> f[2]==3
       True
       >>> f[3]==0
       True
       >>> f[4]==1
       True
       >>> f[5]==4
       True
       >>> f[6]==1
       True
       >>> f[7]==0
       True
       >>> f[8]==3
       True
       >>> f[9]==1
       True
       >>> f[10]==1
       True
       >>> f[11]==4
       True
       >>> f[12]==2
       True
       >>> f[13]==0
       True
       >>> f[14]==3
       True
       >>> f[15]==2
       True
       >>> f[16]==1
       True
       >>> f[17]==4
       True
    """
    f=[]
    for i in range(5):
        for j in range(2):
            if (m[i][j]==m[i][j+1]-1):
                if (m[i][j+1]==m[i][j+2]-1):
                    if (m[i][j+2]==m[i][j+3]-1):
                        f.append(i)
                        f.append(j)
                        f.append(j+3)
    return f
               
#Veo si hay 4 consecutivos en las columnas
def consecutivosColumna(m):
    """
       >>> m=[[-1,0,1,2,3],[0,1,1,3,3],[1,2,0,4,2],[2,3,7,5,9],[0,-1,-2,6,-4]]
       >>> c=consecutivosColumna(m)
       >>> len(c)==12
       True
       >>> c[0]==0
       True
       >>> c[1]==0
       True
       >>> c[2]==3
       True
       >>> c[3]==0
       True
       >>> c[4]==1
       True
       >>> c[5]==3
       True
       >>> c[6]==0
       True
       >>> c[7]==3
       True
       >>> c[8]==3
       True
       >>> c[9]==1
       True
       >>> c[10]==3
       True
       >>> c[11]==4
       True
    """
    c=[]
    for i in range(2):
        for j in range(5):
            if (m[i][j]==m[i+1][j]-1):
                if (m[i+1][j]==m[i+2][j]-1):
                    if (m[i+2][j]==m[i+3][j]-1):
                        c.append(i)
                        c.append(j)
                        c.append(i+3)
    return c


print = lambda *args, **kwargs: None            
doctest.testmod(verbose=True)

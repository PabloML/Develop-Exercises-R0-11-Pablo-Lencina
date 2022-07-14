import math
import turtle
import doctest

#Excepción que se lanza cuando se instancia un circulo con radio menor o igual que 0
class radioIncorrectoException(Exception):
    def __init__(self):
        super().__init__("Se produjo una excepción porque el radio debe ser mayor que 0.")

#Excepción que se lanza cuando se multiplica a un circulo con un valor menor o igual que 0
class multiplicadorIncorrectoException(Exception):
     def __init__(self):
        super().__init__("Se produjo una excepción porque solo se puede multiplicar un circulo por valores mayores que 0.")

#Clase que representa a los objetos circulo
class circulo:
    #Constructor de la clase con un radio pasado por parametro
    def __init__(self,radio):
        """
           >>> c= circulo(4)
           >>> c.radio()
           4
        """
        if (radio<=0):
            raise radioIncorrectoException()
        self.r=radio

    #Metodo que devuelve el radio del circulo
    def radio(self):
        return self.r

    #Setea el valor del radio del circulo
    def setRadio(self,radio):
        """
           >>> c= circulo(4)
           >>> c.radio()
           4
           >>> c.setRadio(50)
           >>> c.radio()
           50
        """
        if (radio<=0):
            raise radioIncorrectoException()
        self.r=radio 

    #Metrodo que devuelve el perimetro del circulo 
    def perimetro(self):
        """
            >>> c= circulo(4)
            >>> c.perimetro()
            25.132741228718345
        """
        p=2*math.pi*self.r
        return p

    #Metodo que devuelve el area del circulo
    def area(self):
        """
            >>> c= circulo(4)
            >>> c.area()
            50.26548245743669
        """
        a=math.pi*pow(self.r,2)
        return a

    #Metodo que permite multiplicar un circulo para obtener otro con el radio
    #igual al producto entre el radio propio y el valor por el que se multiplica
    def __mul__(self,n):
        """
            >>> c= circulo(4)
            >>> cir=c*5
            >>> cir.radio()
            20
        """
        if (n<=0):
            raise multiplicadorIncorrectoException()
        circle=circulo(self.r*n)
        return circle
    
    #Metodo que permite imprimir el circulo
    def __repr__(self):
        """
            >>> c= circulo(50)
            >>> print(c)
            <BLANKLINE>
        """
        t=turtle.Turtle()
        t.circle(self.r)
        return ""

doctest.testmod(verbose=True)



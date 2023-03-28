class ParImpar:

    numeros = []

    def __init__(self, lista):
        self.numeros = lista

    def add(self, num):
        self.numeros.append(num)

    def sumaPar(self):
        suma=0
        for i in self.numeros:
            if(i%2)==0:
                suma += i
        return suma
    
    def sumaImpares(self):
        suma=0
        for i in self.numeros:
            if(i%2)!=0:
                suma += i
        return suma

    def cuadradoLista(self):
        ArrayCuadrado = []
        for i in self.numeros:
            ArrayCuadrado.append(i*i)
        return ArrayCuadrado

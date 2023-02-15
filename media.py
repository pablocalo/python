class Media:
    arrayNotas=[]
    def notas(self):
        return self.arrayNotas

    def add(self, number):
        if number<0 or number>10:
            raise ValueError
        self.arrayNotas.append(number)

    def media(self):
        suma=0
        for i in self.arrayNotas:
            suma=suma+i
        return suma/len(self.arrayNotas)

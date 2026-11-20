from math import *
class Shape:
    #def __init__(self):
        #raise TypeError("Нельзя напрямую создавать экземпляры класса Shape")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> float|int:
        pass

    def perimeter(self) ->float|int:
        pass

class Circle(Shape):
    def __init__ (self, radius: float):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self.radius=radius
    def __str__(self) -> str:
         return(f"{super().__str__()}\n"
                f"|radius = {self.radius}\n")
    def area(self) -> float:
         return self.radius**2*pi
    def perimeter(self) -> float:
         return self.radius*2*pi

class Rectangle(Shape):
    def __init__(self, wid: float, leng: float):
        if (wid < 0)or(leng < 0):
            raise ValueError("Стороны прямоугольника не могут быть отрицательными")
        self.width = wid
        self.length = leng
    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"|length = {self.length}\n"
                f"|width = {self.width}\n")

    def area(self) -> float:
        return self.length*self.width

    def perimeter(self) -> float:
        return (self.width+self.length)*2


#shape = Rectangle(5, 2)

#print(shape.area(), shape.perimeter())

def create_list (l: list):
    count=input("Введите количество элементов")
    for i in range(int(count)):
        elem=input("Введите элементы (тип формы для каждого)")
        l.append(elem)
    return l

def params (l: list):
    create_list(l)
    par=[]
    for i in range(len(forms)):
        dl=int(input("Введите длину(радиус)"))
        sh=int(input("Введите ширину(если окружность, введите 0)"))
        par.append(dl)
        par.append(sh)
    return par

forms=[]
par=params(forms)

for i in range (len(forms)):
    if forms[i]=="Rectangle":
        shape=Rectangle(par[i+i], par[i+i+1])
        print(shape.area(), shape.perimeter())
    elif forms[i]=="Circle":
        shape = Circle(par[i+i])
        print(shape.area(), shape.perimeter())
    else:
        print("Вашей формы нет в прграмме, проверьте написание на опечатки")




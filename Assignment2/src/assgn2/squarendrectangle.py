#Create a class to print the area of a square and a rectangle. The class has two methods with the same name but
 #different number of parameters. The method for printing area of rectangle has two parameters which are length and breadth 
#respectively while the other method for printing area of square has one parameters which is side of square. 

class shape:
    num=3
    length=6
    width=6
    def square(self):
        print("Square of a number",self.num*self.num)
    def rectangle(self):
        print("Rectangular shape",self.length*self.width)
s=shape()
s1=shape()
s2=shape()
s.square()
s.rectangle()

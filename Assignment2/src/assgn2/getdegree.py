#Create a class ‘Degree’ having a method ‘getDegree’ that prints “I got a degree”. 
#It has two subclasses namely ‘Undergraduate’ and ‘Postgraduate’ each having a method with the same name 
#that prints “I am a Undergraduate” and “I am a Postgraduate” respectively. 
#Call the method by creating an object of each of the three classes.



class Degree:
    def Get_Degree(self):
        print("I got Degree")
class undergraduate:
    def Get_Degree(self):
        print("I am a Undergraduate")
class postgraduate:
    def Get_Degree(self):
        print("I am a postgraduate")
ob=Degree()
ob1=undergraduate()
ob2=postgraduate()
ob.Get_Degree()   
ob1.Get_Degree() 
ob2.Get_Degree()   

            

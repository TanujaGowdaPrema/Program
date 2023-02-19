#Create an abstract class ‘Parent’ with a method ‘message’. 
#It has two subclasses each having a method with the same name ‘message’ that prints. 
#“This is first subclass” and “This is second subclass” respectively.
#Call the methods ‘message’ by creating an object for each subclass.


class parent:
    def message(self):
        pass
class student(parent):
    def message(self):
        print("This is first subclass")
class students(parent):
    def message(self):
        print("This is second subclass")
p=parent()
p.message()
r=student()
r.message()
s=students()
s.message()
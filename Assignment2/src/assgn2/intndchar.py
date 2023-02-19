#1. Create a class to print a integer and a character with two methods having the same name but different sequence of the integer 
#and the character parameters. For example, 
#if the parameter of the first method are of the form (int n, char c),
 #then that of the second method will be of the form (char c, int n).
    
class Name:
    def sameName(self,num,ch):
        #num=int(input("enter the number"))
        #ch=input("enter the character")
        self.num=num
        self.ch=ch
        print("to print the number and character=",self.num,self.ch)
    def sameName(self,ch,num):   
         #ch=input("enter the character")
         #num=int(input("enter the number"))
         self.ch=ch
         self.num=num
         print("to print the number and character=",self.ch,self.num)
n1 = Name()
n1.sameName(10,"god");
n1.sameName("god",11);   
    
    
    
    
    
    
# 8. Create a Bus child class that inherits from the Vehicle class. 
#The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance,
#we need to add an extra 10% on full fare as a maintenance charge.
#So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class vehicle:
    def fare_charge(self):
        seating_capacity=2
        print("seating capacity",'=',seating_capacity*100)    
class bus(vehicle):
    def charge(self): 
        #full_fare=100
        #maintnanca_charge=10
        final_amount=(100+(0.1*100))
        #final_amount=full_fare + maintnanca_charge
        print("final_amount =",final_amount)
    
c=bus()
c.fare_charge()
c.charge()

    
    
    
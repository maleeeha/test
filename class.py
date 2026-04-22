num =20
print(type(num))
 
num =2.0
print(type(num))

num = {'key':20}
print(type(num))

num=[10,20,0,0]
print(type(num))

# inheritence

class Vehicle:
    def Vehicle_info(self):
        print("inside vehicle class")


class Car(Vehicle):
    def Car_info(self):
        print("inside our class")

c1 =Car()
c1.Vehicle_info()
c1.Car_info()
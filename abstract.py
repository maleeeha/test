from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

class defender(Car):
    def mileage(self):
        print('the mileage is 7kmpl')

d =defender()
d.mileage()

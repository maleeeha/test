class Person:
    def __init__(self,name,age):
        self.name = name
        self.age =age

    def greet(self):
        return f"hi,I'm {self.name} and I'm {self.age}years old."
    
    def __repr__(self):
        return f"person(name={self.name!r}, age = {self.age!r})"

p1 =Person("maleeha",19)
p2 =Person("bob",30)

print(p1)
print(p1.greet())
print(p2.name,p2.age)
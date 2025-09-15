class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        def bark(self):
            return f"{self.name}says woof!"
        
        dog = Dog("Bruno",3)
        print(dog.bark()) #output: Bruno says woof!
        

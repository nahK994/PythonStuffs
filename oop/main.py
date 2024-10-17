class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):  # Inherits from Animal
    def speak(self):
        return "Woof!"

class Cat(Animal):  # Inherits from Animal
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

def make_animal_speak(animal: Animal):
    print(animal.speak())

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!


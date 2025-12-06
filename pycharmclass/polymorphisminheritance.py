# oop_inheritance_demo.py
class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

def make_it_speak(animal_obj):
    animal_obj.speak()

def main():
    dog = Dog()
    cat = Cat()
    make_it_speak(dog)
    make_it_speak(cat)

main()
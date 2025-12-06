class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def message(self):
        print("Hello from Child")


obj=Child()
obj.greet()
obj.message()
obj2=Parent()
obj2.greet()



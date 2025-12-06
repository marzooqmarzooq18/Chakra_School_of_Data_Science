class Student:
    def set_details(self,name,marks):
        self.name=name
        self.marks=marks

    def show_details(self):
        print(f"name: {self.name}, Marks: {self.marks}")


s1=Student()
s1.set_details("Asha", 92)
s1.show_details()

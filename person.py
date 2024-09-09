class person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
     print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}")

person1 = person(name="Rita", age=30, gender="female")

person1.introduce()
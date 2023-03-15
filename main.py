class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hello(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")

    def introduce(self):
        print(f"Меня зовут {self.name} и я {self.gender} пола в возрасте {self.age} лет.")

person1 = Human("Rustam", 12, "Mujskoy")
person1.say_hello()

person2 = Human("Yusup", 12, "Mujskoqo")
person2.introduce()


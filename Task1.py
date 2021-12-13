# Task 1
# A Person class
# Make a class called Person. Make the __init__() method take firstname, lastname,
# and age as parameters and add them as attributes.
# Make another method called talk() which makes prints a greeting from the person containing,
# for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

# Завдання 1
# Клас людини
# Створіть клас під назвою Person.
# Зробіть так, щоб метод __init__() брав ім’я,
# прізвище та вік як параметри та додавайте їх як атрибути.
# Зробіть інший метод під назвою talk(), який друкує привітання від особи, яка містить,
# наприклад, такий: «Привіт, мене звати Карл Джонсон і мені 26 років».

class Person:
    def __init__(self, name="", surname="", age=""):
        self.name = name
        self.surname = surname
        self.age = age

    def talk(self):
        print("Привіт, мене звати", self.name, self.surname, "і мені", self.age, "років")


person_1 = Person("Viktor", "Shakhrai", 20)
person_1.talk()

# Task 2
# Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

# Завдання 2
# Собачий вік
# Створіть клас Dog з атрибутом класу `age_factor` рівним 7. Зробіть __init__(),
# який приймає значення для віку собаки.
# Потім створіть метод "human_age", який повертає вік собаки в людському еквіваленті.

class Dog:
    age_factor = 7

    def __init__(self, age_dog):
        self.age_dog = age_dog

    def human_age(self):
        rez = self.age_dog * self.age_factor
        return print(f"The age of your dog:{rez}")


my_dog = Dog(3)
my_dog.human_age()

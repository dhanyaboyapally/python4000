import random

class Animal:
    def __init__(self, animal_type, name):
        self.__animal_type = animal_type
        self.__name = name
        self.__mood = self.__generate_mood()

    def __generate_mood(self):
        mood_number = random.randint(1, 3)
        if mood_number == 1:
            return "happy"
        elif mood_number == 2:
            return "hungry"
        else:
            return "sleepy"

    def get_animal_type(self):
        return self.__animal_type

    def get_name(self):
        return self.__name

    def check_mood(self):
        return self.__mood
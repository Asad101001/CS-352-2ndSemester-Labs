class Animal:

    def speak(self):
        print("... some generic animal noises...")


class Dog(Animal):

    def speak(self):
        print("Woof")


class Cat(Animal):

    def speak(self):
        print("Meow")


class Parrot(Animal):

    def speak(self):
        print("whatever sound a parrot makes !?!")

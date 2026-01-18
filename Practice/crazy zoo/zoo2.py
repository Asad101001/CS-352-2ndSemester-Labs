class Animal:

    def __init__(self):
        print("Animal.__init__() called")
        self.speak()  # tricky line!

    def speak(self):
        print("Generic animal sound")


class Dog(Animal):

    def __init__(self):
        print("Dog.__init__() called")
        super().__init__()  # call parent constructor

    def speak(self):
        print("Woof! (Dog speaking)")


pet = Dog()


#  Dog.__init__() called
#  Animal.__init__() called
#  Woof! (Dog speaking)


#  REASONING:
# ✓ When Dog() is created, first Dog.__init__() runs.
# ✓It calls super().__init__(), which runs Animal.__init__().
# ✓Inside Animal.__init__(), we call self.speak() — and here’s the twist:
# ✓self is actually a Dog object (already allocated),
# ✓so Python dynamically dispatches speak() to Dog.speak(), not Animal.speak().
# ✓Even though the Dog constructor hasn’t finished yet,
# Python binds methods dynamically based on the actual object type, not the constructor’s scope.

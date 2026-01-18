from zoo import *


def random_animal_show(animals):
    print("\nWelcome to the Dynamic Dispatch Zoo!\n")
    for a in animals:
        print(f"Now performing: {a.__class__.__name__}")
        a.speak()  # <-- dynamic dispatch (decided at runtime)
        print("-" * 30)


if __name__ == "__main__":
    animals = [Dog(), Cat(), Parrot(), Animal()]
    random_animal_show(animals)
    
    
# What would happen if  'pet' is typecasted as Animal() , what will be the behaviour?    
  
    # pet: Animal = Dog()
    # pet.speak()

#   Woof!    


# Welcome to the Dynamic Dispatch Zoo!

# Now performing: Dog
# Woof
# ------------------------------
# Now performing: Cat
# Meow
# ------------------------------
# Now performing: Parrot
# whatever sound a parrot makes !?!
# ------------------------------
# Now performing: Animal
# ... some generic animal noises...
# ------------------------------

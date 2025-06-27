# Define a class called dog. Basic attributes of name, age, size.
# Methods of likes_walks and walking_speed
class Dog:
    likes_walks = True
    walking_speed = "Walk"
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size
    
    def go_on_walk(self):
        print(f"Kindly requesting {self.name} to go on a walk...")
        if self.likes_walks == True:
            return f"WOOF! I love walks! Let's walk at this speed: {self.walking_speed}"
        else:
            return f"WOOF! Not a fan of walks myself."
    
    def introduce(self):
        print(f"#### {self.name}'s information ####")
        return f"WOOF! My name is {self.name}. I'm {self.age} years old and my size is {self.size}!"

# Subclasses of Dog are defined below
# Make a poodle subclass, which is low allergen and prances
class Poodle(Dog): 
    walking_speed = "Prance"
    is_low_allergen = True # Use attribute instead of method

    def __init__(self, name, age, size):
        super().__init__(name, age, size)
            
class Labrador(Dog):
    walking_speed = "Run"
    def __init__(self, name, age, size):
        super().__init__(name, age, size)

    def temperament(self):
        if self.age < 2:
            return "Flighty"
        elif self.age <10:
            return "Fun Loving"
        else:
            return "Getting slower"

# Teacher's personal favourite
class CavalierKingCharlesSpaniel(Dog):
    walking_speed = "Bolt" # This dog is really fast and it BOLTS
    def __init__(self, name, age, size):
        super().__init__(name, age, size) # Inherit __init__ from base class

    def temperament(self):
        if self.age < 2:
            return "Flighty"
        elif self.age <10:
            return "Fun Loving"
        else:
            return "Getting slower"

# Teacher's note: Don't use multiple inheritance if you can avoid it!
# Results may be unpredictable and we don't like unpredictable things in software engineering!
class LabraDoodle(Poodle,Labrador):
    # LabraDoodles by default inherit the walking_speed of the Poodle (it's the first argument) - in this case it's a Prance
    def __init__(self, name, age, size):
        super().__init__(name, age, size)

################################################
sam = Dog('Sam', 5, 'enormous')
print(sam.introduce())

jerry = Dog('Jerry', 3, 'wide')
print(jerry.introduce())

bob = Poodle('Bob', 2, 'small')
print(bob.introduce())
print(f"Bob likes walks: {bob.likes_walks}")
print(f"Bob is low allergen: {bob.is_low_allergen}")
print(bob.go_on_walk())

print("Sussy doggo")
swiftie = LabraDoodle('Swiftie', 1, "Medium")
print(swiftie.introduce())
print(swiftie.is_low_allergen)
print(swiftie.temperament())
print(swiftie.go_on_walk())

print("Basic doggo")
basic_doggo = Dog('Henry', 4, 'Large')
print(basic_doggo.name, basic_doggo.age, basic_doggo.size)
print(basic_doggo.go_on_walk())

# Instantiate a CavalierKingCharlesSpaniel object called Zeno
print("Zeno's information:")
zeno = CavalierKingCharlesSpaniel('Zeno', 2, 'medium')
print(zeno.temperament())
print(zeno.go_on_walk())
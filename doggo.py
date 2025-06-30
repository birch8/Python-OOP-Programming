# Define a class called dog. Basic attributes of name, age, size.
# Methods of likes_walks and walking_speed
class Dog:
    likes_walks = True # By default, dogs like walks.
    walking_speed = "Walk" # By default, the dog walks at the walking_speed of "Walk"
    is_low_allergen = False # By default the dog is NOT low allergen
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size
    
    def go_on_walk(self): # Calling this method causes the dog to go on a walk (if it likes walks), and returns its walking speed.
        print(f"Kindly requesting {self.name} to go on a walk...")
        if self.likes_walks == True:
            return f"WOOF! I love walks! Let's walk at this speed: {self.walking_speed}"
        else:
            return f"WOOF! Not a fan of walks myself."
    
    def introduce(self): # Calling this method causes the dog to introduce itself by saying its name, age and size.
        print(f"#### {self.name}'s information ####")
        return f"WOOF! My name is {self.name}. I'm {self.age} years old and my size is {self.size}!"
    
    def allergen_check(self): # Calling this method causes the dog to say whether it is low allergen or not.
        if self.is_low_allergen == True:
            return "WOOF! I'm low allergen!"
        else:
            return "WOOF! I'm NOT low allergen! Am I high allergen??"
        
    def temperament(self): # Calling this method returns the dog's temperament.
        print(f"{self.name}'s temperament is:")
        if self.age < 2:
            return "Jumpy"
        elif self.age <10:
            return "Fun Loving"
        else:
            return "Getting slower"

# Subclasses of Dog are defined below
# Make a poodle subclass, which is low allergen and prances
class Poodle(Dog): 
    walking_speed = "Prance" # Override the default walking_speed and replace it with Prance
    is_low_allergen = True # Change low allergen to True for poodles

    def __init__(self, name, age, size):
        super().__init__(name, age, size) # Inherit __init__ from base class
            
class Labrador(Dog):
    walking_speed = "Run" # Override the default walking_speed and replace it with Run
    def __init__(self, name, age, size):
        super().__init__(name, age, size) # Inherit __init__ from base class

    def temperament(self):
        print(f"{self.name}'s temperament is:")
        if self.age < 2: # Labrador inherits the temperament method but overrides the values returned.
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

    def temperament(self): # CavalierKingCharlesSpaniel inherits the temperament method but overrides the values returned.
        print(f"{self.name}'s temperament is:")
        if self.age < 2:
            return "Energetic"
        elif self.age <10:
            return "Powerful"
        else:
            return "Wise"

# Teacher's note: Don't use multiple inheritance if you can avoid it!
# Results may be unpredictable and we don't like unpredictable things in software engineering!
class LabraDoodle(Poodle,Labrador):
    # LabraDoodles by default inherit the walking_speed of the Poodle (it's the first argument) - in this case it's a Prance
    def __init__(self, name, age, size):
        super().__init__(name, age, size)
    
    # Currently the LabraDoodle also has inherited the Flighty part of the temperament method from Labrador, which isn't found in Poodle.

#################### Creating objects and calling methods ##############################
sam = Dog('Sam', 5, 'enormous') # First example doggo
print(sam.introduce()) # Make Sam introduce itself

jerry = Dog('Jerry', 3, 'wide') # Second example doggo
print(jerry.introduce())
print(jerry.allergen_check()) # Check if Jerry is low allergen

bob = Poodle('Bob', 2, 'small') # Third example doggo (poodle)
print(bob.introduce())
print(f"Bob likes walks: {bob.likes_walks}") # Check if Bob likes walks
print(bob.allergen_check()) 
print(bob.go_on_walk()) # Let Bob go on a walk

swiftie = LabraDoodle('Swiftie', 1, "Medium") # Fourth example doggo (LabraDoodle)
print(swiftie.introduce())
print(swiftie.allergen_check())
print(swiftie.temperament()) # Check Swiftie's temperament
print(swiftie.go_on_walk())

# basic_doggo = Dog('Henry', 4, 'Large')
# print(basic_doggo.introduce())
# print(basic_doggo.go_on_walk())

# Instantiate a CavalierKingCharlesSpaniel object called Zeno
zeno = CavalierKingCharlesSpaniel('Zeno', 2, 'medium') # Fifth example doggo (CavalierKingCharlesSpaniel)
print(zeno.introduce())
print(zeno.temperament())
print(zeno.go_on_walk())
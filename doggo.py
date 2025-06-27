# Define a class called dog. Basic attributes of name, age, size.
# Methods of likes_walks and walking_speed
class Dog:
    likes_walks = True
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size
    
    def walking_speed(self):
        return "Walk"
    
    def introduce(self):
        return f"WOOF! My name is {self.name}. I'm {self.age} years old and my size is {self.size}!"

# Subclasses of Dog are defined below
# Make a poodle subclass, which is "low alergen" and prances
class Poodle(Dog): 
    is_low_allergen = True # Use attribute instead of method
    def __init__(self, name, age, size):
        super().__init__(name, age, size)

    def walking_speed(self): # Inherit the method but override the return
        return "Prance"
            
class Labrador(Dog):
    def __init__(self, name, age, size):
        super().__init__(name, age, size)

    def temperament(self):
        if self.age < 2:
            return "Flighty"
        elif self.age <10:
            return "Fun Loving"
        else:
            return "Getting slower"
        
    def walking_speed(self):
        return "Run"

# Teacher's personal favourite
class CavalierKingCharlesSpaniel(Dog):
    def __init__(self, name, age, size):
        super().__init__(name, age, size) # Inherit __init__ from base class

    def temperament(self):
        if self.age < 2:
            return "Flighty"
        elif self.age <10:
            return "Fun Loving"
        else:
            return "Getting slower"
        
    def walking_speed(self):
        return "Bolt" # This dog is super fast and it BOLTS

# Teacher's note: Don't use multiple inheritance if you can avoid it!
# Results may be unpredictable and we don't like unpredictable things in software engineering!
class LabraDoodle(Poodle,Labrador):
    def __init__(self, name, age, size):
        super().__init__(name, age, size)

    def walking_speed(self):
        return super().walking_speed() # This returns "Prance", as it inherits Poodle from super() *before* Labrador
        # return Labrador.walking_speed(self) # This returns the Labrador (explicityly stated)
################################################
sam = Dog('Sam', 5, 'enormous')
print("#### Sam's information ####")
print(sam.introduce())

jerry = Dog('Jerry', 3, 'wide')
print("#### Jerry's information ####")
print(jerry.introduce())

bob = Poodle('Bob', 2, 'small')
print(bob.name, bob.age, bob.size)
print(bob.likes_walks)
print(bob.walking_speed())
print(bob.is_low_allergen)

print("Sussy doggo")
swiftie = LabraDoodle('Swiftie', 1, "Medium")
print(swiftie.name, swiftie.age, swiftie.size)
print(swiftie.is_low_allergen)
print(swiftie.temperament())
print(swiftie.walking_speed())

print("Basic doggo")
basic_doggo = Dog('Henry', 4, 'Large')
print(basic_doggo.name, basic_doggo.age, basic_doggo.size)
print(basic_doggo.walking_speed())

# Instantiate a CavalierKingCharlesSpaniel object called Zeno
print("Zeno's information:")
zeno = CavalierKingCharlesSpaniel('Zeno', 2, 'medium')
print(zeno.temperament())
print(zeno.walking_speed())
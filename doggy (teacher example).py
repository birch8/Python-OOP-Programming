'''We define a class called dog. The basic attributes are:
name, age, size.
The methods are likes_walks and walking_speed'''

class Dog:
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size

    def likes_walks(self):
        return True
    
    def walking_speed(self):
        return "Walk"

'''Subclasses are defined below'''    
class Poodle(Dog):
    def __init__(self, name, age, size):
        super().__init__(name, age, size)

    def low_alergen(self):
        return "Yes"

    def walking_speed(self):
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

class CavalierKingCharlesSpaniel(Dog):
    def __init__(self, name, age, size):
        super().__init__(name, age, size)

    def walking_speed(self):
        return "Bolt"
    
    def temperament(self):
        if self.age < 2:
            return "Flighty"
        elif self.age <10:
            return "Fun Loving"
        else:
            return "Getting slower"
        
### DON'T USE MULITPLE INHERITANCE IF YOU CAN AVOID IT!
# RESULTS MAY BE UNPREDICATBLE!       
class LabraDoodle(Poodle,Labrador):
    def __init__(self, name, age, size):
        super().__init__(name, age, size)

    def walking_speed(Labrador):
        return "Run"
    
###########################################################################
 
bob = Poodle('Bob', 2, 'small')
print("Bob's information:-")
print(bob.name, bob.age, bob.size)
print(bob.likes_walks())
print(bob.walking_speed())

'''swiftie = LabraDoodle('Alice', 1, "Medium")
print(swiftie.name, swiftie.age, swiftie.size)
print(swiftie.low_alergen())
print(swiftie.temperament())
print(swiftie.walking_speed())'''

print("a basic dog:-")
basic_doggo = Dog('Henry', 4, 'Large')
print(basic_doggo.name, basic_doggo.age, basic_doggo.size)
print(basic_doggo.walking_speed())

print("Zneo's information:-")
zeno = CavalierKingCharlesSpaniel('Zeno', 2, 'medoium')
print(zeno.temperament())
print(zeno.walking_speed())


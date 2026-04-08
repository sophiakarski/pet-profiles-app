# Pet name,
# Pet age, 
# Pet species (cat/dog), 
# Pet gender (male/female), 
# Pet Documents (in form of URLs).

class Pet:
    # constructor method
    def __init__(self, name: str, age: int, species: str, gender: str):
        self.name = name
        self.age = age
        self.species = species
        self.gender = gender
    
    def describe(self):
        # Leila is a 6 year old cat
        print(f"{self.name} is a {self.age} year old {self.species}.")


class Animal():
    
    #Animal instance constructor with paramets as name, pet, sound for properties
    def __init__(self, name, pet, sound="Unavailable animal sound"):
        self.name = name
        self.pet = pet
        self.sound = sound
    
    def pet_info(self):
        print(f"The pet's name is: {self.name}")
        print(f"{self.name} is a {self.pet}")
        print(f"{self.name} usally {self.sound}")
        

dog_object = Animal("Veda", "dog", "woofs")
cat_object = Animal("Tarun", "cat", "meows")     

dog_object.pet_info()
print()
cat_object.pet_info()
    

    
    
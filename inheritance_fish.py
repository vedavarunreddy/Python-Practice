'''
Inheritance practice for objects and classes
'''

class Animal():
    def __init__(self, name, pet, sound=None, owner_name=None):
        self.name = name
        self.pet = pet
        self.sound = sound
        self.owner_name = owner_name
        
    def animal_details(self):
        print(f"{self.name} is a {self.pet} and it often makes the sound, {self.sound}")
        
    def ownership_to_customer(self, owner_name):
        self.owner_name = owner_name
        print(f"\n{self.name} ownership changed to: {self.owner_name}")

# dog_object = Animal("Tommy", "dog")
# dog_object.animal_details()
# dog_object.ownership_to_customer("Veda")

# print(dog_object.pet)
# print(dog_object.owner)
# print(dog_object.sound)
# print(dog_object.name)


class Fish(Animal):
    def __init__(self, name, pet, home, sound=None, owner_name=None, ocean_name=None):
        super().__init__(name,pet,sound,owner_name)
        self.home = home
        self.ocean_name = ocean_name
        
    def swim(self):
        if self.sound == None:
            print("I might be a fish ...")
        else:
            print("Are you sure you are a fish?")
    
    def ocean(self, ocean_name):
        self.ocean = ocean_name
        print(f"{self.name} is in {self.ocean} ocean now.")
        

fish1 = Fish("nemo", "fish", "water", "bubbles", "Veda", "Pacific")
fish1.swim()
fish1.animal_details()
fish1.ocean("Atlantic")
import time

class Agent():
    def __init__(self, name, health, car):
        self.name = name
        self.health = health
        self.car = car
    
    def agent_info(self):
        print(f"Welcome Agent: {self.name}")
        if self.health >= 90:
            print(f"You appear ... healthy. You are at {self.health}% now ")
        else:
            print(f"Your health can improve! You are at {self.health}% now")
        #anticipation = time.sleep(1)
        print(f"How about a car for you ehh Agent? Lets say, mmm ... {self.car}")

# bond = Agent("James Bond", 100, "Aston Martin")
# bond.agent_info()
# print()
# silva = Agent("Raoul Silva", 100, "Dodge")
# silva.agent_info()


class Spy(Agent):
    def __init__(self, name, health, car, agency, location, killed=False):
        super().__init__(name, health, car)
        self.agency = agency
        self.location = location
        self.killed = killed
        
    def assassinate(self, to_assassinate):
        if to_assassinate.health > 0:
            to_assassinate.health = to_assassinate.health - 20
            print(f"{to_assassinate.name} has lost health ... new health is {to_assassinate.health}%")
            if to_assassinate.health == 0:
                to_assassinate.killed = True
                print(f"{to_assassinate.name} has fallen. Killed = {to_assassinate.killed}")

bond = Spy("James Bond", 100, "Aston Martin", "MI5", "London")
bond.agent_info()
time.sleep(5)
print()
silva = Spy("Raoul Silva", 100, "Dodge", "KGB", "Moskova")
silva.agent_info()

while True:
    if silva.health <= 0 or bond.health <= 0:
        print(f'Looks like we have a winner amongst the agents!')
        break
    bond.assassinate(silva)
    silva.assassinate(bond)
    time.sleep(2)

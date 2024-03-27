class Player():
    def __init__(self, player_name, score, team="no team currently"):
        self.player_name = player_name
        self.score = score
        self.team = team
    
    def show_stats(self):
        print(f"{self.player_name} plays for: {self.team} and he scored {self.score}")
    
    def select_team(self):
        team = input("Enter a team for this player to join!: ")
        self.team = team
        
    def update_team(self):
        pass

player_1 = Player("Veda", 10)
player_1.show_stats()
player_1.select_team()
player_1.show_stats()
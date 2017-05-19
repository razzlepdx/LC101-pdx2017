class Player():
    
    '''Player takes several parameters: name (a string), number (an int), hitting_arm (a string), games_played (a number), lifetime_hits (a number), and lifetime_rbis (a number)'''
    
    def __init__(self, name, number, hitting_arm, games_played=0, lifetime_hits=0, lifetime_rbi=0):
        self.name = name
        self.number = number
        self.hitting_arm = hitting_arm
        self.games_played = games_played
        self.lifetime_hits = lifetime_hits
        self.lifetime_rbi = lifetime_rbi

    def __str__(self):
    	return "Player name: {}\nPlayer number: {}\nPlayer arm: {}".format(self.name, self.number, self.hitting_arm)
    
    def game_finished(self, hits, rbis):
        
    	'''needs to display the hits and RBIs from the current game, and update total variables'''
        
    	self.games_played += 1
    	self.lifetime_hits += hits
    	self.lifetime_rbi += rbis
    	return "{} just finished a game with a total of {} hits and {} RBIs".format(self.name, hits, rbis)

    def lifetime_total(self):
        
    	'''displays all hits and RBIs over player history''' 
        
    	return "{} Stats\n Total hits: {} \n Total RBIs: {}".format(self.name, self.lifetime_hits, self.lifetime_rbi)

    
    def num_of_games(self):
    	'''displays the number of games played'''
    	return "Total games played: {}".format(self.games_played)

        
    
    

my_player = Player("Terry Wilson", 9, "right", 16, 35, 23)
print(my_player)
print(my_player.game_finished(3,1))
print(my_player.lifetime_total())
print(my_player.num_of_games())
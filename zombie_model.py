"""Module of a zombie apocalypse adapted from StandardModel.py"""

import numpy as np
import matplotlib.pyplot as plt
import random

class human:
    
    x = None
    y = None

    def __init__(self,base_chance_of_survival):
        
        self.chance_of_survival = base_chance_of_survival 
    
    def place_at(self, coord):
        """Place entity at coordinates (x,y).

        Parameters
        ----------
        coord: tuple
            (x,y) coordinates where to place the human.
        """
        self.x = coord[0]
        self.y = coord[1]

    def move(self):
        """Move the human by randomly pushing it in both directions."""
        self.x += np.random.randint(low=-1, high=2)
        self.y += np.random.randint(low=-1, high=2)
    
    def gets_weapon(self,weapon):
        """Give the human a weapon to improve chances of survival.
        
        Parameters
        ----------
        weapon: string
            Choose one of the following to provide human with an 
            increased chance of survival:
            
            "pistol": Increase chance of survival by 30 percent.
            "rifle": Increase chance of survival by 40 percent.
            "grenade": Increase chance of survival by 50 percent.
            "rocket launcher": Increase chance of survival by 80 percent.
        
        """
        self.weapon=weapon
        if self.weapon == "pistol":
            self.chance_of_survival=self.chance_of_survival* 1.3
        
        elif self.weapon == "rifle":
            self.chance_of_survival=self.chance_of_survival* 1.4 
            
        elif self.weapon == "grenade":
            self.chance_of_survival=self.chance_of_survival* 1.5  
       
        elif self.weapon == "rocket launcher":
            self.chance_of_survival=self.chance_of_survival* 1.8  
            
        elif self.weapon == "None":
            self.chance_of_survival=self.chance_of_survival* 1

            

class zombie:
    
    x = None
    y = None

    def __init__(self, smell_radius):
        
        self.smell_radius = smell_radius
        
        self.smallest_dist = np.inf
        self.smell_human = False
        self.human_loc = [0,0]
        
    def place_at(self, coord):
        """Place entity at coordinates (x,y).

        Parameters
        ----------
        coord: tuple
            (x,y) coordinates where to place the zombie.
        """
        self.x = coord[0]
        self.y = coord[1]

    def move(self):
        """Move the zombie by randomly pushing it in both directions."""
        
        if self.smell_human == True:

            self.x += np.sign(self.human_loc[0]-self.x)*np.random.randint(low=0, high=2)

            self.y += np.sign(self.human_loc[1]-self.y)*np.random.randint(low=0, high=2)
            
            self.smell_human = False
            
        else:
            self.x += np.random.randint(low=-1, high=2)
            self.y += np.random.randint(low=-1, high=2)

class alpacalypse:
    """alpacalypse class. Let chaos ensue."""
    _all_entities = None

    def __init__(self, width, height):

        self.width = width
        self.height = height

        # Create empty lists for the human and zombie objects.
        self.zombies = []
        self.humans = []
        
        # Create empty lists for the total number of humans and zombies at 
        # the end of each iteration
        self.human_count = []
        self.zombie_count = []
        
    def evolve(self):
        
        self.move_entities()
        
        self.boundary_conditions()    
        
        self.check_interaction()
        
        self.human_count.append(len(self.humans))
        
        self.zombie_count.append(len(self.zombies))

    def move_entities(self):
        """Runs the move method in each of the entity objects in 
        the list of self.all_entities list
        """
        for ip in self._all_entities:
            ip.move()

    def boundary_conditions(self):
        """Makes sure all the entities are within the bounds of the map
        
        If it is found that they are outside the map after moving, they
        are sent back to being within the map boundaries
        """
        for ip in self._all_entities:
            if ip.x > self.width:
                ip.x -= self.width

            if ip.y > self.height:
                ip.y -= self.height

            if ip.x < 0:
                ip.x += self.width

            if ip.y < 0:
                ip.y += self.height

    def draw(self):
        """Plots the humans and zombies in the list onto the plot of the apocalypse.
        zombies are plotted as green circles and humans are plotted
        as purple plus signs.
        """
        
        # adds 'zombie' label to legend
        plt.scatter(self.zombies[0].x, self.zombies[0].y, marker="o", c = "g", label = "zombie")
        
        # adds 'human' label to legend
        plt.scatter(self.humans[0].x, self.humans[0].y, marker="P", c = "purple",label = "human")
        
        for ip in self.zombies:
            plt.scatter(ip.x, ip.y, marker="o", c = "g")

        for ip in self.humans:
            plt.scatter(ip.x, ip.y, marker="P", c = "purple")
            
        plt.legend()
        
    def check_interaction(self):
        """Features several different behaviors in the humans and zombies:
        
        Ability to fight back - Checks if a human and zombie are on the same
        location, then adds a random chance of the human either surviving and
        becoming stronger, or dying and becoming a zombie. This is based off of 
        the set chance of survival and a random value between 0 and 1
        
        Zombie Scent - Zombies check to see if there are any humans within
        a set radius of them, if there are, then the zombie records the human's
        location and prepared to move in the human's direction
        """
        
        for ip1 in range(len(self.humans)-1, -1, -1):
            p1 = self.humans[ip1]
            for ip2 in range(len(self.zombies)-1, -1, -1):
                p2 = self.zombies[ip2]
                if p1.x == p2.x and p1.y == p2.y:
                    # Base ability with some randomness can kill zombie
                    if (p1.chance_of_survival * random.uniform(0,1) > 0.5):
                        # human killed zombie
                        self.zombies.pop(ip2)
                        # Base ability increased
                        p1.chance_of_survival *= 1.01
                        continue
                    # zombie infected human
                    else :
                        self.humans.pop(ip1)
                        self.zombies.append(zombie(p2.smell_radius))
                        self.zombies[-1].place_at(coord=(p1.x, p1.y))
                        continue
                
                
                dist = np.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)  # tracks distance to all humans on the map
                if dist <= p2.smell_radius: # if the human is within the scent radius then proceed
                    if dist < p2.smallest_dist:
                        p2.smallest_dist = dist
                        p2.human_loc[0] = p1.x
                        p2.human_loc[1] = p1.y
                        p2.smell_human = True
                        continue
                        
                    continue

        # update the list
        self._all_entities = [*self.humans, *self.zombies]

"""Module of a zombie apocalypse."""

import numpy as np
import matplotlib.pyplot as plt
import random

class human:
    
    x = None
    y = None

    def __init__(self,base_chance_of_survival):
        
        # add any special attributes here
        
        self.name = None # only here so code doesn't return an error
        
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
        Weapon list:
        Pistol: Increase chance of survival by 30 percent.
        Rifle: Increase chance of survival by 40 percent.
        Grenade: Increase chance of survival by 50 percent.
        Rocket_launcher: Increase chance of survival by 80 percent.
        * Capped at 90 percent.           
        """
        self.weapon=weapon
        if self.Weapon == "Pistol":
            self.survival_chance=self.survival_chance* 1.3
        
        elif self.Weapon == "Rifle":
            self.chance_of_survival=self.chance_of_survival* 1.4 
            
        elif self.Weapon == "Grenade":
            self.chance_of_survival=self.chance_of_survival* 1.5  
       
        elif self.Weapon == "Rocket_launcher":
            self.chance_of_survival=self.chance_of_survival* 1.8  
            
            

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
    """alpacalipse class. There is nothing otherwise."""
    _all_entities = None

    def __init__(self, width, height):

        self.width = width
        self.height = height

        # Create empty lists for the humans and zombies.
        self.zombies = []
        self.humans = []

    def evolve(self):
        
        self.move_entities()
        
        self.boundary_conditions()    
        
        self.check_interaction()
        
        

    def move_entities(self):
        """Runs the move method in each of the entity objects in 
        the list of self.all_entities list
        """
        for ip in self._all_entities:
            ip.move()

    def boundary_conditions(self):
        """Makes sure that all of the entity objects are within
        the boundaries of the universe. If a particle is found to 
        be outside of the universe, it is re-indexed to a position
        inside the universe
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
        as blue stars.
        """
        for ip in self.zombies:
            plt.scatter(ip.x, ip.y, marker="o", c = "g")

        for ip in self.humans:
            plt.scatter(ip.x, ip.y, marker="*", c = "b")

    def check_interaction(self):
        """Checks to see if there are any human-zombie interactions on the map.
        If there are, converts the human into a zombie (we can add more complexity
        to this later)
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
                        
                dist = np.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)     
                if dist <= p2.smell_radius:
                    if dist < p2.smallest_dist:
                        p2.smallest_dist = dist
                        p2.human_loc[0] = p1.x
                        p2.human_loc[1] = p1.y
                        p2.smell_human = True
                        continue
                        
                    continue

        # update the list
        self._all_entities = [*self.humans, *self.zombies]

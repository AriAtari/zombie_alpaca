"""Module of a zombie apocalypse."""

import numpy as np
import matplotlib.pyplot as plt

class human:
    
    x = None
    y = None

    def __init__(self):
        
        # add attributes here
        self.name = None # only here so code doesn't return an error
        
    def place_at(self, coord):
        """Place entity at coordinates (x,y).

        Parameters
        ----------
        coord: tuple
            (x,y) coordinates where to place the particle.
        """
        self.x = coord[0]
        self.y = coord[1]

    def move(self):
        """Move the particle by randomly pushing it in both directions."""
        self.x += np.random.randint(low=-1, high=2)
        self.y += np.random.randint(low=-1, high=2)

class zombie:
    
    x = None
    y = None

    def __init__(self):
        
        # add attributes here
        self.name = None # only here so code doesn't return an error
        
    def place_at(self, coord):
        """Place entity at coordinates (x,y).

        Parameters
        ----------
        coord: tuple
            (x,y) coordinates where to place the particle.
        """
        self.x = coord[0]
        self.y = coord[1]

    def move(self):
        """Move the particle by randomly pushing it in both directions."""
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
        """Runs the move method in each of the particle objects in 
        the list of self.all_entities list
        """
        for ip in self._all_entities:
            ip.move()

    def boundary_conditions(self):
        """Makes sure that all of the particle objects are within
        the boundaries of the universe. If a particle is found to 
        be outside of the universe, it is re-indexed to a position
        inside the universe
        """
        for ip in self._entities:
            if ip.x > self.width:
                ip.x -= self.width

            if ip.y > self.height:
                ip.y -= self.height

            if ip.x < 0:
                ip.x += self.width

            if ip.y < 0:
                ip.y += self.height

    def draw(self):
        """Plots the fermions (in the self.fermions list) as well as
        the bosons (from self.bosons) onto the plot of the universe.
        fermions are plotted as blue circles and bosons are plotted
        as red stars.
        """
        for ip in self.zombies:
            plt.scatter(ip.x, ip.y, marker="o", c = "b")

        for ip in self.humans:
            plt.scatter(ip.x, ip.y, marker="*", c = "r")

    def check_interaction(self):
        """Checks to see if there are any particle-antiparticle
        collisions of fermions on the map. If there is a collision,
        it creates a boson in the location of the collision
        """

        for ip1, p1 in enumerate(self.humans):
            for ip2, p2 in enumerate(self.zombies[ip1:]):
                if p1.x == p2.x and p1.y == p2.y:

                    self.humans.pop(ip1)

                    self.zombies.append(zombie(name = "",charge=0.0, mass=0.0,spin=1.0) )
                    self.zombies[-1].place_at(coord=(p1.x, p1.y))

                    continue

            continue

        # update the list
        self._all_entities = [*self.humans, *self.zombies]

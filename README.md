# Zombie Alpacalypse

## The story so far.
One day everyone lived in peace and harmony thanks to the abunace of precious alpacas to pet. The alpacas helped people destress and have an uplift in mood. But one day a toxic waste spill from the nuclear energy corporation "Nuke'Em" fell into the river that the adorable alpacas drink from. This caused the alpacas to become neon green but they were still pasifists, however, they now have an abilty to make people into zombies through touch. Humans knew this but they are just so cute people couldnt stop petting them and turning into zombies. Its an ALPACALYPSE!!!

## Introduction
In this project, we simulate the fallout of a zombie alpacalypse in which we see a horde of zombie alpacas attacking a crowd of unsuspecting humans. Based heavily on the standard_model.py code from HMK 2, we start by simulating crowd of randomly moving humans and zombies that wander around an area of a set size. If the human and zombie end up wandering onto the same space as one another, the human is bitten by the zombie and becomes a zombie themselves.

After creating this basic simulation, we then went on to add a number of different behaviors exhibited by both the humans and zombies to increase the complexity of our model. Some of these behaviors include: Giving the zombie alpacas the ability to 'smell' humans that are within a certain distance of them, the ability for humans to fight back against the zombies and grow stronger from each zombie they succesfuly kill, and the ability for humans to pick up weapons to further increase their likely hood of sucessfully killing a zombie.

## Basic Simulation - Elias Taira
To run the basic simulation, with no special behaviors of any kind, we must first import all of the appropriate libraries necessary to run our code. Additionally, we must also import the classes we will be using from our 'zombie_model.py' file 
```
# Importing necessary libraries to run simulation
import numpy as np
import matplotlib.pyplot as plt
import time
from IPython.display import display, clear_output

# Importing necessary classes to run simulation
from zombie_model import human, zombie, alpacalypse 
```
Next, we initialize our 'alpacalypse()' class which will act as our map for which we will be placing our humans and zombies. This class takes in two arguments, width and height, which determine the size of the map in units of the number of elements in an array

We also initialize lists of 'human()' and 'zombie()' objects via two separate 'for' loops. This will then create a list of human and zombie objects that are all the same as one another. There are also some special behaviors that we created that are inside of these objcts. However, for the sake of running the basic simulation before we add any more complex behaviors, we will set them all to 0 to keep the model as simple as possible. We then finish initializing our model by adding the human and zombie lists to tone single list within the 'alpacalypse' object.
```
np.random.seed(123456789) # setting a seed so that analysis is repreatable

my_alpaca_base = alpacalypse(width = 200 , height = 200) # initializing alpacalypse class

# Initializing a bunch of humans and zombies
for p in range(200):
    my_alpaca_base.humans.append(
        human(base_chance_of_survival = 0) # setting to 0 to remove complex behaviors
    )
    
    my_alpaca_base.zombies.append(
        zombie(smell_radius = 0) # setting to 0 to remove complex behaviors
    )

# Group both sets of entities in one list
my_alpaca_base._all_entities = [*my_alpaca_base.humans, *my_alpaca_base.zombies]
```
Now, we prepare to run our simulation by first placing our humans and zombies that we created in the prior step onto our board. To do this, we use the '.place()' method that is within the 'human()' and 'zombie()' objects. Again, we use a 'for' loop to iterate through each object in the list to place them.
```
for hum in my_alpaca_base.humans:
    hum.place_at([np.random.randint(low = 0, high = my_alpaca_base.width),np.random.randint(low = 0, high = my_alpaca_base.height)])
    
for zom in my_alpaca_base.zombies:
    zom.place_at([np.random.randint(low = 0, high = my_alpaca_base.width),np.random.randint(low = 0, high = my_alpaca_base.height)])
```
Now, we run the ABM. The only method we actually need to run for this is the '.evolve()' method, which basically moves the iteration forward by 1 timestep. To iterate over multiple timesteps, we run the '.evolve()' method a specified number of times via a 'for' loop. Should we want to make an animation of the state of the ABM after each timestep, we add in some code to plot out the map of humans and zombies contained within our 'alpacalypse' object after each timestep, which involves the use of the '.draw()' method to plot out the current position of each human and zombie on the map.
```
# Initializes an image for which the animation will take place on
# Comment out next line to allow model to run faster
fig, ax = plt.subplots(figsize = (10,10))

start = time.time() # Records the start time of the simulation
times = [] # Initializes an empty time array

# Using a for loop to run the model for 100 iterations
for i in range(100):
    
    # Running the ABM
    my_alpaca_base.evolve()
    my_alpaca_base.draw()
    
    # Code used to create an animation for each iteration of the model
    # If you want the model to run faster, comment out the next 4 lines of code
    plt.title(f"Time = {i}")
    clear_output(wait=True) 
    display(fig)            
    fig.clear()             
        
    end = time.time() # Records how long it has been since the start of the model's runtime
    times.append(end-start) # Defines how much time has passed and appends it to the time list
    
print("Total time =", end-start)  # Prints out how long the entire model took to run
```
If the animation code has not been commented out, the image should look something like this:

<img src="https://github.com/AriAtari/zombie_alpaca/blob/main/Images/basic_sim_pic.jpg" width="300" height="300">

To see the full animation, go to 'Zombie_alpaca.ipynb' to view it

## Adding Behaviors

### Zombie's ability to smell - Caroline VanDenBrouck

### Human's ability to fight back and become stronger - Xiaoyanbin Cai


### Providing the humans with weaponry - Arian Andalib

Every zombie alpacalypse needs weapons and so let there be weapons! 
To give a human a weapon you only need to say 
```
human.gets_weapon(weapon)   
```
Where 'weapon' can be Pistol, Rifle, Grenade, and Rocket launcher!! The input should be as a string.
```
- Pistol: Increase chance of survival by 30 percent.
- Rifle: Increase chance of survival by 40 percent.
- Grenade: Increase chance of survival by 50 percent.
- Rocket launcher: Increase chance of survival by 80 percent.

```
### Plotting

In addition to being able to plot the current positions of each of the humans an zombies, the 'alpacalypse()' class also has two other attribues, 'human_count' and 'zombie_count' that record the number of humans and zombies at the end of each iteration respectively. These attributes can be very helpful for performing various kinds of analysis on the model to be able to better understand the different behaviors of the humans and zombies as we iterate through the ABM.

We will now show an example of one of the ways in which we create plots using the  'human_count' and 'zombie_count' attributes. The full list different visualizations we performed can be found on 'zombie_model_plot.ipynb'

In the following cell, we analyze the base model (no smell radius, no ability to fight back against zombies) at various different proprtions to evaluate the number of humans being bit for each starting population
```
# Preping and running the alpacalypse.iterate() function much like the very first example

import numpy as np
import matplotlib.pyplot as plt
import time
from IPython.display import display, clear_output

# Importing necessary classes to run simulation
from zombie_model import human, zombie, alpacalypse 

np.random.seed(123456789)

hpops = [350,300,250,200,150,100,50]

plt.figure(figsize = (15,10))

for num in range(7): # running the simulation 7 different times to accound for the different 
    
    my_alpaca = alpacalypse(width = 200 , height = 200)
    
    for p in range(hpops[num]):
        my_alpaca.humans.append(
            human(base_chance_of_survival = 0)
        )
    for p in range(400-hpops[num]):
        my_alpaca.zombies.append(
            zombie(smell_radius = 0)
        )

    my_alpaca._all_entities = [*my_alpaca.humans, *my_alpaca.zombies]

    for hum in my_alpaca.humans:
        hum.place_at([np.random.randint(low = 0, high = my_alpaca.width),np.random.randint(low = 0, high = my_alpaca.height)])

    for zom in my_alpaca.zombies:
        zom.place_at([np.random.randint(low = 0, high = my_alpaca.width),np.random.randint(low = 0, high = my_alpaca.height)])
    
    for i in range(100):
        my_alpaca.evolve()
    
   
    humans_eaten = hpops[num] - np.array(my_alpaca.human_count) # calculating the total number of humans bitten after each iteration
    
    plt.plot(range(100),humans_eaten,label = "Human Pop = {}".format(hpops[num]))
    plt.xlabel('Time')
    plt.ylabel("Humans Eaten")
    plt.legend()
```
The output should look something like this:
![image](https://user-images.githubusercontent.com/86431659/164883117-c3783e75-744f-4b64-8a1d-cbaa3b9a11a2.png)



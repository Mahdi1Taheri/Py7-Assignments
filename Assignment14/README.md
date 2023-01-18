# Stars Wars Game
## About Game Play:
This game is my first Python game.
As you can see from the image below, this is a space war game where you have a spaceship that must protect your planet from enemies.
Enemies attack you from above and you have to destroy them by shooting them, and also your ship should not collide with enemies because you will be game over.
Currently, the ship only moves left and right.
In the lower left corner, the number of your lives and your score will be displayed.
Every enemy that comes out from below (passes your planet) will reduce your life. And destroying each enemy will add one point to your score.
[img]

## About Code:
### The libraries I used:

* For random location of enemies
`import random`

* For each enemy to enter after three seconds
`import time`
* For making the game(GUI &...)
`import arcade`
### This game is based on object oriented programming
In this code we have a main class called **Game** To implement all objects on the game.\n
a **Spaceship** class for our ship.\n
[img]
a **Bullet** class for bullets that shoots with the ship.\n
a  **Enemy** class for enemies for the enemies who attack us.\n
a **Heart** class for lives.

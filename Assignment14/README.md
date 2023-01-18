# Stars Wars Game
## About Game Play
This game is my first Python game.<br /> 
As you can see from the image below, this is a space war game where you have a spaceship that must protect your planet from enemies.<br /> 
Enemies attack you from above and you have to destroy them by shooting them, and also your ship should not collide with enemies because you will be game over.<br /> 

<br /> Currently, the ship only moves left and right.<br /> 
In the lower left corner, the number of your lives and your score will be displayed.<br /> 
Every enemy that comes out from below (passes your planet) will reduce your life. And destroying each enemy will add one point to your score.


## About Code
### The libraries I used

* For random location of enemies
`import random`

* For each enemy to enter after three seconds
`import time`
* For making the game(GUI &...)
`import arcade`
### This game is based on object oriented programming
In this code we have a main class called **Game** To implement all objects on the game.<br /> 
a **Spaceship** class for our ship.<br /> 
a **Bullet** class for bullets that shoots with the ship.<br /> 
a  **Enemy** class for enemies for the enemies who attack us.<br /> 
a **Heart** class for lives.
### Game Screenshots
![Game](https://i.postimg.cc/WbK19wMc/Star-Wars-Game1.png)<br /> 
Game Over:
![GameOver](https://i.postimg.cc/jd7SnqZT/gameOver.png)

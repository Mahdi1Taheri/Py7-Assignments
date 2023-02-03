import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.YELLOW
        self.radius = 15
        self.change_x = random.choice([-1,1])
        self.change_y = random.choice([-1,1])
        self.speed = 5
        self.width = self.radius * 2
        self.height = self.radius * 2
    
    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
    
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y, self.radius, self.color)

class Rocket(arcade.Sprite):
    def __init__(self, x, y, c, n):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = c
        self.name = n
        self.change_x = 0
        self.change_y = 0
        self.width = 10
        self.height = 60
        self.speed = 50
        self.score = 0

    def move(self,game, ball):
        if ball.center_x > game.width // 2:
            
            if self.center_y > ball.center_y:
                self.change_y = -1

            if self.center_y < ball.center_y:
                self.change_y = 1
            
            self.center_y += self.change_y * self.speed

            if self.center_y < 60:
                self.center_y = 60
            
            if self.center_y > game.height - 60:
                self.center_y = game.height - 60
    
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y,
        self.width, self.height, self.color)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800,height=500,title= "Pong")
        arcade.set_background_color(arcade.color.DARK_RED)
        self.player_1 = Rocket(40, self.height//2, arcade.color.WHITE,"Mahdi")
        self.player_2 = Rocket(self.width-40, self.height//2, arcade.color.BLACK, "Asghar")
        self.ball = Ball(self)


    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_outline(self.width // 2, self.height // 2, self.width - 30,
         self.height - 20,
         arcade.color.WHITE, border_width=10)

        arcade.draw_line(self.width // 2 ,15,self.width//2, self.height-30,
        color=arcade.color.WHITE,line_width= 10)

        self.player_1.draw()
        self.player_2.draw()
        self.ball.draw()
        arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.player_1.height < y < self.height - self.player_1.height:
            self.player_1.center_y = y

    def on_update(self, delta_time: float):
        self.ball.move()
        self.player_2.move(self,self.ball)
        if self.player_2.height < self.player_2.center_y - self.player_2.speed and \
                self.player_2.center_y - self.player_2.speed < self.height - self.player_2.height:
            self.player_2.move(self,self.ball)

        if self.ball.center_y < 30 or self.ball.center_y > self.height - 30:
            self.ball.change_y *= -1
        
        if arcade.check_for_collision(self.player_1, self.ball) or \
            arcade.check_for_collision(self.player_2,self.ball):
            self.ball.change_x *= -1

        if self.ball.center_x < 0:
            print("Goal!!")
            self.player_2.score += 1
            del self.ball
            self.ball = Ball(self)

        if self.ball.center_x > self.width:
            print("goall")
            self.player_1.score += 1
            del self.ball
            self.ball = Ball(self)


window = Game()
arcade.run()
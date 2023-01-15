import random
import arcade

class Apple(arcade.Sprite):
    def __init__(self, game):
        super().__init__("apple.png")
        self.width = 48
        self.height = 48
        self.center_x = random.randint(10,game.width - 10)
        self.center_y = random.randint(10,game.height - 10)
        self.change_x = 0
        self.change_y = 0

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.GREEN
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 0
        self.body = []


    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
        for part in self.body:
            arcade.draw_rectangle_filled(part['x'],part['y'],self.width,self.height,self.color)


    def eat(self, food):
        self.score += 1
        print("Score:", self.score)
        del food
        

    def move(self):
        self.body.append({'x': self.center_x ,'y': self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width= 500, height=500, title="Snake Game🐍")
        arcade.set_background_color(arcade.color.KHAKI)
        self.snake = Snake(self)
        self.food = Apple(self)

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.food.draw()
        arcade.finish_render()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
    
   

    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake,self.food):
            self.snake.eat(self.food)
            self.food = Apple(self)

    
if __name__ == "__main__":
    game = Game()
    arcade.run()
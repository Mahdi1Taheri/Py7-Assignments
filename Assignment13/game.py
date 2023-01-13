import random
import arcade



class Spaceship(arcade.Sprite):
    def __init__(self,game,name):
        super().__init__("Assignment13\pngwing.com (2).png")
        self.center_x = game.width // 2
        self.center_y = 100
        self.width = 140
        self.height = 140
        self.name = name
        self.speed = 8

    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x -= self.speed

        elif self.change_x == 1:
            if self.center_x < self.game_width:
                self.center_x += self.speed

    def fire(self):
        new_bullet = Bullet()
        self.bullet_list.append(new_bullet)


class Bullet(arcade.Sprite):
    def __init__(self,host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 3
        self.change_x = 0
        self.change_y = 1

class Enemy(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__("Assignment13/pngwing.com (1).png")
        self.center_x = random.randint(0,w)
        self.center_y = h + 24
        self.width = 120
        self.height = 120
        self.angle = 0
        self.speed = 2

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height=600,title="Star Wars")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture("Assignment13/107763.jpg")
        self.me = Spaceship(self,"Mahdi")
        self.enemies = Enemy(self.width,self.height)
    
    # showing
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,1000,600,self.background)
        self.me.draw()

        for enemy in self.enemies:
            enemy.draw()
        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        print("a key has been pressed!")
        
        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.me.move("L")
        elif symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.me.move("R")
        elif symbol == arcade.key.SPACE:
            ...
    
    # تابعي كه تند تند به صورت اتومات اجرا ميشه
    def on_update(self, delta_time: float):
        for enemy in self.enemies:
            if arcade.check_for_collision(self.me,enemy):
                print("Game Over☠")
                exit(0)

        for enemy in self.enemies:
            for bullet in self.me.bullet_list:
                self.enemies.remove(enemy)
                self.me.bullet_list.remove(bullet)

        self.me.move()

        for enemy in self.enemies:
            enemy.move()

        for bullet in self.me.bullet_list:
            bullet.move()

        for enemy in self.enemies:
            if enemy.center_y < 0:
                self.enemies.remove(enemy)

        if random.randint(1,100) == 5:
            self.new_enemy = Enemy(self.width,self.height)
            self.enemy.append(self.new_enemy)


window = Game()
arcade.run()
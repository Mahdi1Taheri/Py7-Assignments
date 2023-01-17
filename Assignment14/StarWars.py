import random
import time
import arcade

class Spaceship(arcade.Sprite):
    def __init__(self,w,name):
        super().__init__("images/pngwing.com (2).png")
        self.center_x = w // 2
        self.center_y = 100
        self.change_x = 0
        self.change_y = 0
        self.width = 140
        self.height = 140
        self.name = name
        self.speed = 10
        self.game_width = w
        self.bullet_list = []

    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x -= self.speed

        elif self.change_x == 1:
            if self.center_x < self.game_width:
                self.center_x += self.speed

    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet) 

class Bullet(arcade.Sprite):
    def __init__(self,host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 5
        self.change_x = 0
        self.change_y = 1
    
    def move(self):
        self.center_y += self.speed

class Enemy(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__("images/pngwing.com (1).png")
        self.center_x = random.randint(10,w)
        self.center_y = h + 24
        self.width = 120
        self.height = 120
        self.angle = 0
        self.speed = 2
        

    def move(self):
        self.center_y -= self.speed

class Heart(arcade.Sprite):
    def __init__(self,x):
        super().__init__("images/icons8-heart-94.png")
        self.center_x = 50 * x
        self.center_y = 30
        self.width = 50
        self.height = 50

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height=600,title="Star Wars")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture("images/107763.jpg")
        self.me = Spaceship(self.width,"Mahdi")
        self.score = 0
        self.hearts = []
        self.laser_sound = arcade.load_sound("sounds/arcade_resources_sounds_fall3.wav")
        self.hurt_sound = arcade.load_sound("sounds/arcade_resources_sounds_error2.wav")
        self.gameover_sound = arcade.load_sound("sounds/D2ZZHGM-game-over.mp3")

        for x in range(1,4):
            self.heart = Heart(x)
            self.hearts.append(self.heart)

        self.time = time.time()
        self.enemies = []
        self.enemy_lst = []
        self.n = 0

    
    # showing
    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_lrwh_rectangle_textured(0,0,1000,600,self.background)
        self.me.draw()
        arcade.draw_text(f"Score: {self.score}", 30,60,arcade.color.WHITE,20,font_name = "Courier New")
        
        for heart in self.hearts:
            heart.draw()

        for enemy in self.enemies:
            enemy.draw()
            
        if len(self.hearts) <= 0:
            arcade.draw_lrtb_rectangle_filled(0,1000,600,0,arcade.color.BLACK)
            arcade.draw_text("GAME OVER", 380,300,arcade.color.WHITE,33, font_name= "Cambria")
            arcade.draw_text(f"Score: {self.score}", 440,250,arcade.color.WHITE,20,font_name = "Courier New")
            self.me.center_x = -1
            self.me.center_y = -1
            
            

        for bullet in self.me.bullet_list:
            bullet.draw()
        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        
        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.me.change_x = -1
        elif symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.me.change_x = 1
        elif symbol == arcade.key.DOWN:
            self.me.change_x = 0
        elif symbol == arcade.key.SPACE:
            self.laser_sound.play()
            self.me.fire()
    
    # تابعي كه تند تند به صورت اتومات اجرا ميشه
    def on_update(self, delta_time: float):
        for enemy in self.enemies:
            if arcade.check_for_collision(self.me,enemy):
                print("Game Over☠")
                exit(0)

        

        for enemy in self.enemies:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy,bullet):
                    self.hurt_sound.play()
                    self.enemies.remove(enemy)
                    self.score += 1
                    self.me.bullet_list.remove(bullet)
                    
                elif bullet.center_y > 1000:
                    self.me.bullet_list.remove(bullet)
                    
        self.me.move()

        for enemy in self.enemies:
            enemy.move()

        for bullet in self.me.bullet_list:
            bullet.move()

        for enemy in self.enemies:
                if enemy.center_y < 0:
                    self.enemies.remove(enemy)
                    if len(self.hearts) > 0:
                        self.hearts.pop(-1)
            
        if self.time + 3 < time.time():
            self.new_enemy = Enemy(self.width,self.height)
            self.enemies.append(self.new_enemy)
            self.enemy_lst.append(self.new_enemy)
            for i in range(len(self.enemy_lst)):
                self.new_enemy.speed += 0.20
            self.time = time.time()
            
    
window = Game()
arcade.run()

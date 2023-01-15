import arcade

class Pattern(arcade.Window):
    def __init__(self):
        super().__init__(600,600,title="🔶Arcade Pattern🔷")
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

window = Pattern()
arcade.run()
    
        
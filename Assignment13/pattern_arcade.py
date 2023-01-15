# Library imports
import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110

arcade.open_window(400, 400, "Aracde Pattern")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

# Loop for each row
for row in range(10):
    # Loop for each column
    # Change the number of columns depending on the row we are in
    for column in range(10):
        # Calculate our location
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        if row % 2 == 0:
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x,y,10,10,arcade.color.RED,45)
            elif column % 2 != 0:
                arcade.draw_rectangle_filled(x,y,10,10,arcade.color.BLUE,45)
        
        elif row % 2 != 0:
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x,y,10,10,arcade.color.BLUE,45)
            elif column % 2 != 0:
                arcade.draw_rectangle_filled(x,y,10,10,arcade.color.RED,45)

# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
    
        
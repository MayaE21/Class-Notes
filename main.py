import arcade


def main():
    arcade.open_window(1000, 900, "This is the Comp151 House")
    arcade.set_background_color(arcade.color.BABY_BLUE)
    # build house base
    block = arcade.create_rectangle(475, 250, 450, 450, arcade.color.WINE)
    door = arcade.create_rectangle(475, 125, 100, 200, arcade.color.WHITE)
    roof = arcade.create_polygon([(475, 700),(250, 475),(700,475)],
                                 arcade.color.TEA_ROSE)
    window1 = arcade.create_ellipse(400, 275, 50, 50, arcade.color.BANANA_MANIA)
    window2 = arcade.create_ellipse(600, 275, 50, 50, arcade.color.BANANA_MANIA)
    arcade.start_render()

    block.draw()
    door.draw()
    roof.draw()
    window1.draw()
    window2.draw()
    arcade.finish_render()
    arcade.run()

main()















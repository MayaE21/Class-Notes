import arcade



def main():
    arcade.open_window(1000, 700, "This is a Cartoon computer")
    arcade.set_background_color(arcade.color.BABY_BLUE)

 # I created an image of a computer I started off making different size of rectangles. This allow the sceen of the image
    #to appear.
    block1 = arcade.create_rectangle(500, 500, 600, 350, arcade.color.LION)
    block2 = arcade.create_rectangle(495, 495, 450, 310, arcade.color.WHITE)
    block3 = arcade.create_rectangle(480, 275, 50, 100, arcade.color.GRAY)
#I was trying to draw a mouse for the computer and a line attached to the computer
    block4 = arcade.draw_circle_filled(140, 120, 40, arcade.color.BABY_BLUE)
    block5 = arcade.draw_line(y1=10, x1=20, y2=10, x2=20, arcade.color.PINK)

##I was trying to see if I could draw in image inside of the computer since, the text wouldn't go in
    arcade.draw_circle_filled(50, 500, 600, arcade.color.SUNSET)
    arcade.draw_text("Welcome, Please login", 150, 120, arcade.color.BLACK, 20, 220)
    arcade.draw_triangle_filled(y1=450, x1=500, y2=120, x2=390, arcade.color.RED)




    block1.draw()
    block2.draw()
    block3.draw()
    block4.draw()
    block5.draw()





    arcade.run()






main()
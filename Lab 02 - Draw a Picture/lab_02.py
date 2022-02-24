import arcade
arcade.open_window(1000, 1000, "Dibujo")  # abro ventana del dibujo

arcade.set_background_color(arcade.color.DEEP_SKY_BLUE)  # selecciono color del fondo

arcade.start_render()  # empiezo a dibujar
# dibujo el sol
arcade.draw_circle_filled(975, 975, 100, arcade.csscolor.YELLOW)

# dibujo los rayos de sol
arcade.draw_line(975, 975, 880, 880, arcade.color.YELLOW, 5)
arcade.draw_line(975, 975, 850, 975, arcade.color.YELLOW, 5)
arcade.draw_line(975, 975, 975, 850, arcade.color.YELLOW, 5)
arcade.draw_line(975, 975, 860, 925, arcade.color.YELLOW, 5)
arcade.draw_line(975, 975, 925, 860, arcade.color.YELLOW, 5)

# dibujo las montañas
arcade.draw_polygon_filled(((150, 450), (250, 550), (400, 625), (490, 500), (600, 700), (750, 850), (900, 450)),
                           arcade.color.BROWN)

# dibujo la nieve
arcade.draw_triangle_filled(250, 550, 400, 625, 454, 550, arcade.color.WHITE)
arcade.draw_triangle_filled(600, 700, 750, 850, 806.5, 700, arcade.color.WHITE)

# dibujo la nube
arcade.draw_ellipse_filled(250, 850, 330, 175, arcade.color.WHITE)
arcade.draw_ellipse_filled(250, 850, 155, 230, arcade.color.WHITE)
arcade.draw_ellipse_filled(335, 850, 110, 190, arcade.color.WHITE)
arcade.draw_ellipse_filled(165, 850, 110, 190, arcade.color.WHITE)

# dibujo el cesped
arcade.draw_lrtb_rectangle_filled(0, 1000, 450, 0, arcade.color.GREEN)

# dibujo la carretera
arcade.draw_lrtb_rectangle_filled(0, 1000, 400, 300, arcade.color.COOL_GREY)
arcade.draw_lrtb_rectangle_filled(0, 1000, 355, 345, arcade.color.WHITE)

# dibujo un coche
# dibujo las ruedas
arcade.draw_circle_filled(50, 322, 20, arcade.color.WARM_BLACK)
arcade.draw_circle_filled(150, 322, 20, arcade.color.WARM_BLACK)
# dibujo la carroceria
arcade.draw_polygon_filled(((20, 335), (20, 350), (40, 400), (150, 400), (170, 370), (205, 370), (205, 335)),
                           arcade.color.RED)

# termino de dibujar y ejecuto
arcade.finish_render()
arcade.run()

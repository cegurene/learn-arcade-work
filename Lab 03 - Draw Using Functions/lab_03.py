import arcade


def dibuja_sol():
    """Dibujo el sol"""
    # dibujo el sol
    arcade.draw_circle_filled(975, 975, 100, arcade.csscolor.YELLOW)

    # dibujo los rayos de sol
    arcade.draw_line(975, 975, 880, 880, arcade.color.YELLOW, 5)
    arcade.draw_line(975, 975, 850, 975, arcade.color.YELLOW, 5)
    arcade.draw_line(975, 975, 975, 850, arcade.color.YELLOW, 5)
    arcade.draw_line(975, 975, 860, 925, arcade.color.YELLOW, 5)
    arcade.draw_line(975, 975, 925, 860, arcade.color.YELLOW, 5)


def dibuja_montannas():
    """Dibujo las montañas y la nieve"""
    # dibujo las montañas
    arcade.draw_polygon_filled(((150, 450), (250, 550), (400, 625), (490, 500), (600, 700), (750, 850), (900, 450)),
                               arcade.color.BROWN)

    # dibujo la nieve
    arcade.draw_triangle_filled(250, 550, 400, 625, 454, 550, arcade.color.WHITE)
    arcade.draw_triangle_filled(600, 700, 750, 850, 806.5, 700, arcade.color.WHITE)


def dibuja_nube():
    """Dibujo la nube"""
    # dibujo la nube
    arcade.draw_ellipse_filled(180, 850, 240, 125, arcade.color.WHITE)
    arcade.draw_ellipse_filled(180, 850, 105, 170, arcade.color.WHITE)
    arcade.draw_ellipse_filled(240, 850, 100, 140, arcade.color.WHITE)
    arcade.draw_ellipse_filled(120, 850, 100, 140, arcade.color.WHITE)


def dibuja_cesped():
    """Dibujo el cesped"""
    # dibujo el cesped
    arcade.draw_lrtb_rectangle_filled(0, 1000, 450, 0, arcade.color.GREEN)


def dibuja_carretera():
    """Dibujo la carretera"""
    # dibujo la carretera
    arcade.draw_lrtb_rectangle_filled(0, 1000, 400, 300, arcade.color.COOL_GREY)
    arcade.draw_lrtb_rectangle_filled(0, 1000, 355, 345, arcade.color.WHITE)


def dibuja_coche(x, y):
    """Dibujo el coche"""
    # asigno punto de referencia
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # dibujo un coche
    # dibujo las ruedas
    arcade.draw_circle_filled(50 + x, 322 + y, 20, arcade.color.WARM_BLACK)
    arcade.draw_circle_filled(150 + x, 322 + y, 20, arcade.color.WARM_BLACK)
    # dibujo la carroceria
    arcade.draw_polygon_filled(((20 + x, 335 + y), (20 + x, 350 + y), (40 + x, 395 + y), (150 + x, 395 + y),
                                (170 + x, 370 + y), (205 + x, 370 + y), (205 + x, 335 + y)), arcade.color.RED)


def dibujar_todo(delta_time):
    """Dibujo"""
    arcade.start_render()  # empiezo a dibujar
    dibuja_sol()
    dibuja_montannas()
    dibuja_nube()
    dibuja_cesped()
    dibuja_carretera()
    dibuja_coche(dibujar_todo.mov_coche_x, 0)
    dibujar_todo.mov_coche_x += 2
    arcade.finish_render()


dibujar_todo.mov_coche_x = 0


def main():
    arcade.open_window(1000, 1000, "Dibujo")  # abro ventana del dibujo
    arcade.set_background_color(arcade.color.DEEP_SKY_BLUE)  # selecciono color del fondo

    # dibujo 60 veces por segundo
    arcade.schedule(dibujar_todo, 1/60)

    # termino de dibujar y ejecuto
    arcade.run()


# llamar para ejecutar
main()

import pyray as pr

from random import randint, choice

pr.init_window(800, 600, "Camera")
pr.set_target_fps(60)
# player
pos = pr.Vector2()
radius = 50
direction = pr.Vector2()
speed = 400

# circles, es una lista por comprension de circulos que empaqueta circulos de radio aleatorios dentro de la instancia de la ventana en ejecucion
circles = [
    (
        pr.Vector2(randint(-2000,2000),randint(-1000,1000)), # pos
        randint(50,200), # radius
        choice([pr.RED, pr.GREEN, pr.BLUE, pr.YELLOW, pr.ORANGE]) # color
        # del modulo random choice hace algo parecido solo que le damos una lista de 4 elementos y eligue entre esos 4
    ) 
    for i in range(100)
]

#definamos el sistema de camara que se compone de dos partes
# PARTE 1:
# definimos antes del bucle la camara de juego
camera = pr.Camera2D()
camera.zoom = 1
# ahora defino el objetivo de la camara para que siga al jugador
camera.target = pos
# para que tenga sentido el movimiento debo de añadirle el desplazamiento es decir un OFFSET
camera.offset = pr.Vector2(400,300)
# ahora añado una rotacion para que se mueva con respecto al jugador
camera.rotation = 0
while not pr.window_should_close():
    # input
    direction.x = int(pr.is_key_down(pr.KEY_RIGHT)) - int(pr.is_key_down(pr.KEY_LEFT))
    direction.y = int(pr.is_key_down(pr.KEY_DOWN)) - int(pr.is_key_down(pr.KEY_UP))
    direction = pr.vector2_normalize(direction)

    # movement
    dt = pr.get_frame_time()
    pos.x += direction.x * speed * dt
    pos.y += direction.y * speed * dt
    # la camara que sigue al jugador
    camera.target = pos
    # actualizo el zoom de la camara
    # detecto el movimiento de la rueda del raton
    #digamos que el mejor metodo seria este de momento
    rueda = pr.get_mouse_wheel_move()
    if rueda != 0:
        # mientras la rueda no se mueva es 0, cuando se mueve se mueve en justamente flotantes aunque no pareciera
        zoom_speed = 0.1
        camera.zoom += rueda * zoom_speed
        camera.zoom = max(0.1,camera.zoom)
    #camera update, es decir actualiza el valor de la camara
    rotacion_de_camara = int(pr.is_key_down(pr.KEY_D)) - int(pr.is_key_down(pr.KEY_A))
    camera.rotation += dt * rotacion_de_camara * 50
    # drawing
    pr.begin_drawing()
    # de la parte 1 llamamos a la camara
    pr.begin_mode_2d(camera)
    pr.clear_background(pr.WHITE)
    for circle in circles:
        pr.draw_circle_v(*circle) #hacemos lo mismo solo que desempaqueto la lista de tuplas generada mas arriba
    pr.draw_circle_v(pos, radius, pr.BLACK)
    pr.end_mode_2d() # hay que finalizar el modo antes de terminar el dibujado
    pr.end_drawing()

pr.close_window()
import pyray as pr


pr.init_window(1200, 600, "Input")
# determino una tecla para salir rapido
pr.set_exit_key(pr.KEY_ESCAPE)
pr.set_target_fps(60) ## OBLIGATORIO PORQUE SIEMPRE FALLA EN TASAS DE REFRESCO DEMASIADO ALTAS
ship_texture = pr.load_texture('basics/assets/spaceship.png')
ship_pos = pr.Vector2(0,0)
ship_direction = pr.Vector2(0,0)
ship_speed = 800

while not pr.window_should_close():
    # input
    # mouse input
    #ship_pos = pr.get_mouse_position()
    #print(pr.is_mouse_button_down(0)) # 0 es derecha 1 es izquierda y 2 es el del medio o la rueda del mouse. es decir nos devuelve el estado del boton del mouse 
    #if pr.is_key_pressed(pr.KEY_A):
    #    print('a')
    #ship input
    # una mejor solucion no llamada elegante es convertir al flotante que produce el movimiento en un entero por medio de reconvertir el valor por medio de int() que tomara el valor flotante haciendo
    # que este se trunque a su entero mas cercano de modo tal que no se pelee al momento de usar los vectores en el espacio
    ship_direction.x = int(pr.is_key_down(pr.KEY_RIGHT)) - int(pr.is_key_down(pr.KEY_LEFT))
    ship_direction.y = int(pr.is_key_down(pr.KEY_DOWN)) - int(pr.is_key_down(pr.KEY_UP))
    ship_direction = pr.vector2_normalize(ship_direction)
    #actualizo el fotograma siguiente
    dt = pr.get_frame_time()
    # para hacer que la nave se pueda mover debo de sumar el valor de la direccion a la posicion 
    # estaba asignando al principio
    ship_pos.x += ship_direction.x * ship_speed * dt
    ship_pos.y += ship_direction.y * ship_speed * dt
    # drawing
    pr.draw_fps(0,0)
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    pr.draw_texture_v(ship_texture, ship_pos, pr.WHITE)
    pr.end_drawing() 

pr.close_window()


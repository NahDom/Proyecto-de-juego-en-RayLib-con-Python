import pyray as pr
#from raylib import * 

# set window
pr.init_window(1200, 400, "Move")
#pr.set_target_fps(100)

ship = pr.load_texture('basics/assets/spaceship.png')
ship_position = pr.Vector2(0,0)
ship_direction = pr.Vector2(1,1)
ship_speed = 600

while not pr.window_should_close():
    # updates
    if ship_position.y >= 400 - 50:
        ship_direction.y = -1
    if ship_position.x >= 1200 - 60:
        ship_direction.x = -1
    if ship_position.y <= 0:
        ship_direction.y = 1
    if ship_position.x <= 0:
        ship_direction.x = 1
        
        
    # delta time para fps
    dt = pr.get_frame_time()
    ship_position.x += ship_direction.x * ship_speed * dt
    ship_position.y += ship_direction.y * ship_speed * dt
    # drawing
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    # le envio el vector de posicion en pantalla
    pr.draw_texture_v(ship, ship_position, pr.WHITE)
    pr.draw_fps(0,0)
    pr.end_drawing()
pr.close_window()
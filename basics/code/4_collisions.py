import pyray as pr


pr.init_window(800, 600, "Collisions")
player_pos = pr.Vector2(0,0)
obstacle_pos = pr.Vector2(500,400) 
player_radius = 50
obstacle_radius = 30

# los rectangulos ya vienen como una clase especifica en raylib por lo que no genera mucho problema su definicion
r1 = pr.Rectangle(40,40,200,200)
r2 = pr.Rectangle(0,0,100,100)
while not pr.window_should_close():
    
    # input 
    player_pos = pr.get_mouse_position()
    # obtengo la posicion del rectangulo con respecto a la del jugador
    r2.x = pr.get_mouse_x()
    r2.y = pr.get_mouse_y()

    # colisiones --> lo que se estudia aqui
    #print(pr.check_collision_circles(player_pos, player_radius, obstacle_pos, obstacle_radius))
    #print(pr.check_collision_circle_rec(player_pos,player_radius,r1))
    # realmente aqui verifico que exista colision nada mas solo eso, luego devuelto la lista del vector de colision
    #if pr.check_collision_recs(r1,r2):
        # verifico si hubo colision entre los cubos para generar el overlapping
    collider = pr.get_collision_rec(r1,r2)
        #imprimo en donde ocurre me da un struct de los valores
        #print(f"collision width: {collider.width}")
        #print(f"collision height: {collider.height}")
    # drawing
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    #pr.draw_circle_v(player_pos, player_radius, pr.WHITE)
    pr.draw_circle_v(obstacle_pos, obstacle_radius, pr.RED)    
    pr.draw_rectangle_rec(r1,(255,145,150,20))
    pr.draw_rectangle_rec(r2,pr.RED)
    # realmente lo que ocurre en esta parte es bastante intuitivo, lo que hago es ver si el collider toca al otro, y
    # al momento de imprimir por pantalla despues de los demas dibujos actualizo la instancia del rectangulo de modo tal
    # que raylib siempre dibuje por pantalla la colision entre los objetos es decir el overlapping
    if collider:
        pr.draw_rectangle_rec(collider,pr.BLUE)
    pr.end_drawing()

pr.close_window()
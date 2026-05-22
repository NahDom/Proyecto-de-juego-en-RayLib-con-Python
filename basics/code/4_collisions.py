import pyray as pr


pr.init_window(800, 600, "Collisions")
player_pos = pr.Vector2(0,0)
obstacle_pos = pr.Vector2(500,400) 
player_radius = 50
obstacle_radius = 30

while not pr.window_should_close():
    
    # input 
    player_pos = pr.get_mouse_position()
    
    # drawing
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    pr.draw_circle_v(player_pos, player_radius, pr.WHITE)
    pr.draw_circle_v(obstacle_pos, obstacle_radius, pr.RED)    
    pr.end_drawing()

pr.close_window()
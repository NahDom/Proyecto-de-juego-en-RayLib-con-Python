import pyray as pr
#from raylib import *
# creamos una ventana

pr.init_window(1100,640, 'test')

#importar imagenes/texturas

spaceship_texture = pr.load_texture('basics/assets/spaceship.png') # un metodo para que la ruta directa de la textura pueda ser encontrada de forma mas dinamica
spaceship_image = pr.load_image('basics/assets/spaceship.png')
pr.image_color_grayscale(spaceship_image)
new_texture = pr.load_texture_from_image(spaceship_image)
cowboy_image = pr.load_image('basics/assets/animation/0.png')
cowboy_texture = pr.load_texture_from_image(cowboy_image)

# importar fuentes

font = pr.load_font('basics/assets/animation/Zero Hour.otf')

# bucle de juego

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    
    pr.draw_line_ex(pr.Vector2(0,0),pr.Vector2(500,200),10.0,(255,0,0,255))
    #pr.draw_pixel(100,200,pr.RED)
    #pr.draw_pixel_v(pr.Vector2(150,200),pr.BLUE)
    #pr.draw_circle_v(pr.Vector2(150,200), 50, pr.YELLOW)
    #pr.draw_circle(150,200,40,(255,0,255,255))
    
    # mostrar imagenes
    pr.draw_texture(spaceship_texture, 0,0, pr.WHITE)
    pr.draw_texture_v(new_texture, pr.Vector2(900,260), pr.GRAY)
    pr.draw_texture(cowboy_texture, 400,300, pr.WHITE)
    
    pr.draw_text('Primer linea de texto en RayLib con Python',0,200, 30, pr.WHITE)
    pr.draw_text_ex(font,'TEXTO DE PRUEBA', pr.Vector2(0,600), 50, 2, pr.YELLOW)
    
    pr.end_drawing()
    # por como funciona el linker tengo que llamar a pr. a cada maldita funcion, por esto soy de c/c++
pr.close_window()
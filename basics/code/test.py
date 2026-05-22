import pyray as rl

def main():
    # Inicializar la ventana
    rl.InitWindow(800, 600, "Zoom 2D en Raylib con Python")
    rl.SetTargetFPS(60)

    # Configurar la cámara 2D
    camera = rl.Camera2D()
    camera.zoom = 1.0

    while not rl.WindowShouldClose():
        # --- LÓGICA DEL ZOOM ---
        # Detectar el movimiento de la rueda del ratón
        rueda = rl.GetMouseWheelMove()
        if rueda != 0:
            # Obtener la posición actual del ratón antes del zoom
            mouse_world_pos = rl.GetScreenToWorld2D(rl.GetMousePosition(), camera)
            
            # Cambiar el nivel de zoom
            factor_zoom = 0.125
            camera.zoom += rueda * factor_zoom
            
            # Limitar el zoom para que no se invierta o se aleje demasiado
            if camera.zoom < 0.1:
                camera.zoom = 0.1
            if camera.zoom > 3.0:
                camera.zoom = 3.0

            # Ajustar el offset para que el zoom enfoque hacia donde apunta el ratón
            camera.offset = rl.GetMousePosition()
            camera.target = mouse_world_pos

        # --- DIBUJO ---
        rl.BeginDrawing()
        rl.ClearBackground(rl.RAYWHITE)

        # Activar el entorno de la cámara
        rl.BeginMode2D(camera)

        # Dibujar un grid o elementos para notar el zoom
        rl.DrawRectangle(-500, -500, 2000, 2000, rl.LIGHTGRAY)
        rl.DrawCircle(400, 300, 50, rl.RED)
        rl.DrawText("¡Acerca o aleja con la rueda del ratón!", -100, -100, 20, rl.DARKBLUE)

        rl.EndMode2D()

        rl.DrawText("Usa la rueda del ratón para hacer Zoom", 10, 10, 20, rl.BLACK)
        rl.EndDrawing()

    rl.CloseWindow()

if __name__ == "__main__":
    main()

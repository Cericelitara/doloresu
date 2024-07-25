elif event.type == pygame.JOYAXISMOTION:
    axis = event.axis
    value = event.value
    print(f"Joystick axis {axis} moved to {value:.2f}.")

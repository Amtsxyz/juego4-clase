"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

# importa herramientas para generar números aleatorios y controlar la ventana del juego
from random import randrange
from turtle import *

# importa la función para manejar posiciones y movimientos
from freegames import vector

# establece la posición inicial de la pelota, su velocidad y la lista de objetivos
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    # revisa si la pelota está fuera de la pantalla para permitir un nuevo lanzamiento
    if not inside(ball):
        # coloca la pelota en su posición inicial
        ball.x = -199
        ball.y = -199

        # calcula la velocidad de la pelota dependiendo de dónde se haga clic
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    # revisa si una posición se encuentra dentro de los límites de la pantalla
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    # limpia la pantalla para dibujar los elementos actualizados
    clear()

    # recorre los objetivos y dibuja cada uno en color azul
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    # dibuja la pelota en color rojo si sigue dentro de la pantalla
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    # actualiza la pantalla para mostrar los cambios
    update()


def move():
    """Move ball and targets."""
    # genera un nuevo objetivo de manera aleatoria
    if randrange(40) == 0:
        # establece su posición inicial y lo agrega a la lista
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # mueve todos los objetivos lentamente hacia la izquierda
    for target in targets:
        target.x -= 0.5

    # revisa si la pelota está dentro de la pantalla
    if inside(ball):
        # aplica la gravedad y actualiza la posición de la pelota
        speed.y -= 0.35
        ball.move(speed)

        # revisa si la pelota salió de la ventana
        if not inside(ball):
            # regresa la pelota a su posición inicial y detiene su velocidad
            ball.x = -200
            ball.y = -200
            speed.x = 0
            speed.y = 0

    # crea una copia de los objetivos y limpia la lista original
    dupe = targets.copy()
    targets.clear()

    # revisa qué objetivos siguen a una distancia mayor a 13 de la pelota
    for target in dupe:
        if abs(target - ball) > 13:
            # conserva los objetivos que todavía no han sido golpeados
            targets.append(target)

    # dibuja nuevamente la pelota y los objetivos
    draw()

    # revisa si algún objetivo salió de los límites de la pantalla
    for target in targets:
        if not inside(target):
            return

    # vuelve a ejecutar el movimiento después de 50 milisegundos
    ontimer(move, 50)


# configura el tamaño y la posición de la ventana del juego
setup(420, 420, 370, 0)

# oculta la tortuga y prepara el movimiento sin dibujar sus desplazamientos
hideturtle()
up()
tracer(False)

# permite lanzar la pelota haciendo clic en cualquier parte de la pantalla
onscreenclick(tap)

# inicia el movimiento del juego y mantiene abierta la ventana
move()
done()
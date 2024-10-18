import pyglet
from pyglet.gl import *

# Configuração da janela
window = pyglet.window.Window(800, 600, "VR Simulation")
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (800/600), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)

# Configuração do cubo
cube_vertices = [
    -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1,  # Face de trás
    -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1,      # Face da frente
    -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1,   # Face inferior
    1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1,      # Face superior
    -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1,   # Face esquerda
    -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1      # Face direita
]


def draw_cube():
    glBegin(GL_QUADS)
    for i in range(0, len(cube_vertices), 3):
        glVertex3f(cube_vertices[i], cube_vertices[i+1], cube_vertices[i+2])
    glEnd()


@window.event
def on_draw():
    window.clear()
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)
    glRotatef(1, 3, 1, 1)
    draw_cube()


@window.event
def update(dt):
    glRotatef(1, 3, 1, 1)


# Configuração do relógio
pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()

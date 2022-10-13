import math
import glfw

from OpenGL.GL import *
from OpenGL.GLU import *

def frange(x, y, jump):
    import decimal
    while x < y:
        yield float(x)
        x += decimal.Decimal(jump)

def draw_circle(x, y, radius, triangleAmount, color):
    twicePi: GLfloat = 2.0 * math.pi

    glColor(color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(triangleAmount):
        glVertex2f(
            x + (radius * math.cos(i * twicePi / triangleAmount)),
            y + (radius * math.sin(i * twicePi / triangleAmount) * 1.1),
        )
    glEnd()
    glFlush()

def draw_rectangle(x1, y1, x2, y2, color):
    glColor(color)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y2)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x2, y1)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def outer_coords(x, y, k, radius):
    xRes = x + radius * math.cos((2 * math.pi * k) / 5 + (math.pi / 2))
    yRes = y + radius * math.sin((2 * math.pi * k) / 5 + (math.pi / 2)) * 1.1
    return (xRes, yRes)

def inner_coords(x, y, k, radius):
    xRes = x + radius * math.cos((2 * math.pi * k) / 5 + (math.pi / 2) + (2 * math.pi / 10))
    yRes = y + radius * math.sin((2 * math.pi * k) / 5 + (math.pi / 2) + (2 * math.pi / 10)) * 1.1
    return (xRes, yRes)

def draw_star(x_center, y_center, radius, color):

    glPointSize(4)
    glBegin(GL_TRIANGLES)
    glColor((0.95, 0.18, 0.12))
    glVertex2f(outer_coords(x_center, y_center, 0, radius)[0], outer_coords(x_center, y_center, 0, radius)[1])
    glVertex2f(outer_coords(x_center, y_center, 2, radius)[0], outer_coords(x_center, y_center, 2, radius)[1])
    glVertex2f(inner_coords(x_center, y_center, 2, radius / 2)[0], inner_coords(x_center, y_center, 2, radius / 2)[1] + 0.01)

    glVertex2f(outer_coords(x_center, y_center, 0, radius)[0], outer_coords(x_center, y_center, 0, radius)[1])
    glVertex2f(outer_coords(x_center, y_center, 3, radius)[0], outer_coords(x_center, y_center, 3, radius)[1])
    glVertex2f(inner_coords(x_center, y_center, 2, radius / 2)[0], inner_coords(x_center, y_center, 2, radius / 2)[1] + 0.01)

    glVertex2f(outer_coords(x_center, y_center, 1, radius)[0], outer_coords(x_center, y_center, 1, radius)[1])
    glVertex2f(outer_coords(x_center, y_center, 4, radius)[0], outer_coords(x_center, y_center, 4, radius)[1])
    glVertex2f(inner_coords(x_center, y_center, 2, radius / 2)[0], inner_coords(x_center, y_center, 2, radius / 2)[1] + 0.01)


    glEnd()

def display():
    glfw.init()
    window = glfw.create_window(900, 700, "DPRK", None, None)
    glfw.set_window_pos(window, 500, 300)
    glfw.make_context_current(window)

    glClearColor(0.7, 0.8, 0.9, 0.0)


    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        draw_rectangle(-0.8, -0.55, 0.8, 0.55, (0.23, 0.36, 0.89))
        draw_rectangle(-0.8, -0.40, 0.8, 0.40, (1.0, 1.0, 1.0))
        draw_rectangle(-0.8, -0.35, 0.8, 0.35, (0.95, 0.18, 0.12))
        draw_circle(-0.42, 0.0, 0.2, 1000, (1.0, 1.0, 1.0))
        draw_star(-0.42, 0.0, 0.15, (0.95, 0.18, 0.12))
        glfw.swap_buffers(window)
    glfw.terminate()

display()

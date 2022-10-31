import math
import glfw
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def lab1():
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
        glVertex2f(inner_coords(x_center, y_center, 2, radius / 2)[0],
                   inner_coords(x_center, y_center, 2, radius / 2)[1] + 0.01)

        glVertex2f(outer_coords(x_center, y_center, 0, radius)[0], outer_coords(x_center, y_center, 0, radius)[1])
        glVertex2f(outer_coords(x_center, y_center, 3, radius)[0], outer_coords(x_center, y_center, 3, radius)[1])
        glVertex2f(inner_coords(x_center, y_center, 2, radius / 2)[0],
                   inner_coords(x_center, y_center, 2, radius / 2)[1] + 0.01)

        glVertex2f(outer_coords(x_center, y_center, 1, radius)[0], outer_coords(x_center, y_center, 1, radius)[1])
        glVertex2f(outer_coords(x_center, y_center, 4, radius)[0], outer_coords(x_center, y_center, 4, radius)[1])
        glVertex2f(inner_coords(x_center, y_center, 2, radius / 2)[0],
                   inner_coords(x_center, y_center, 2, radius / 2)[1] + 0.01)

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


def lab2():
    edges = ((0, 1), (0, 5), (0, 3),
             (0, 1), (0, 7), (0, 3),

             (0, 2), (0, 5), (0, 4),
             (0, 2), (0, 8), (0, 4),

             (0, 3), (0, 8), (0, 2),
             (0, 3), (0, 6), (0, 2),

             (0, 4), (0, 6), (0, 1),
             (0, 4), (0, 7), (0, 1),
    )

    lines = (
        (0, 1), (1, 7), (1, 6), (0, 6),
        (0, 5), (0, 3), (3, 5), (0, 7),
        (0, 2), (0, 8), (2, 8), (2, 6),
        (0, 4), (4, 5), (4, 8), (7, 3),
    )

    def PyramidLines(height, width, edges, color):
        vertices = ((0.0, 2.5 + height, 0.0),
                    # outer
                    (1.0 + width, 1.0 + height, -1.0 - width),
                    (-1.0 - width, 1.0 + height, -1.0 - width),
                    (1.0 + width, 1.0 + height, 1.0 + width),
                    (-1.0 - width, 1.0 + height, 1.0 + width),
                    # inner
                    (0.0, 1.0 + height, 0.5),
                    (0.0, 1.0 + height, -0.5),
                    (0.5, 1.0 + height, 0.0),
                    (-0.5, 1.0 + height, 0.0))

        glBegin(GL_LINES)
        glColor4f(*color)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

    def Pyramid(height, width, edges, color):
        vertices = (
            (0.0, 2.5 + height, 0.0),
            # outer
            (1.0 + width, 1.0 + height, -1.0 - width),
            (-1.0 - width, 1.0 + height, -1.0 - width),
            (1.0 + width, 1.0 + height, 1.0 + width),
            (-1.0 - width, 1.0 + height, 1.0 + width),
            # inner
            (0.0, 1.0 + height, 0.5),
            (0.0, 1.0 + height, -0.5),
            (0.5, 1.0 + height, 0.0),
            (-0.5, 1.0 + height, 0.0)
        )

        glBegin(GL_TRIANGLES)
        glColor4f(*color)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

    def Trunk(color):
        glBegin(GL_TRIANGLES)
        glColor4f(*color)

        ACDB = (
            (0.2, -0.2),    # 10
            (0.27, 0),
            (0.2, 0.2),     # 11
            (0, 0.27),
            (-0.2, 0.2),    # 01
            (-0.27, 0),
            (-0.2, -0.2),   # 00
            (0, -0.27),
            (0.2, -0.2),    # 10
        )
        for i in range(len(ACDB) - 1):
            glVertex3fv((ACDB[i][0], 0, ACDB[i][1]))
            glVertex3fv((ACDB[i + 1][0], 0, ACDB[i + 1][1]))
            glVertex3fv((ACDB[i + 1][0], -1, ACDB[i + 1][1]))

            glVertex3fv((ACDB[i][0], 0, ACDB[i][1]))
            glVertex3fv((ACDB[i][0], -1, ACDB[i][1]))
            glVertex3fv((ACDB[i + 1][0], -1, ACDB[i + 1][1]))
        glEnd()

    def Top(top, color):
        glBegin(GL_TRIANGLES)
        glColor4f(*color)
        # base
        glVertex3fv((0.14, top, 0.14))
        glVertex3fv((-0.14, top, 0.14))
        glVertex3fv((0.14, top, -0.14))

        glVertex3fv((-0.14, top, -0.14))
        glVertex3fv((-0.14, top, 0.14))
        glVertex3fv((0.14, top, -0.14))

        edges = (
            (0.14, 0.14),
            (-0.14, 0.14),
            (-0.14, -0.14),
            (0.14, -0.14),
            (0.14, 0.14),
        )
        for i in range(len(edges) - 1):
            glVertex3fv((edges[i][0], top, edges[i][1]))
            glVertex3fv((edges[i + 1][0], top, edges[i + 1][1]))
            glVertex3fv((0, 0.5 + top, 0))
        glEnd()

    def TreeCubeToy(coords, color):
        glBegin(GL_TRIANGLES)
        glColor4f(*color)
        # base
        glVertex3fv((0.1 + coords[0],  coords[1], 0.1 + coords[2]))
        glVertex3fv((-0.1 + coords[0], coords[1], 0.1 + coords[2]))
        glVertex3fv((0.1 + coords[0], coords[1], -0.1 + coords[2]))

        glVertex3fv((-0.1 + coords[0], coords[1], -0.1 + coords[2]))
        glVertex3fv((-0.1 + coords[0], coords[1], 0.1 + coords[2]))
        glVertex3fv((0.1 + coords[0], coords[1], -0.1 + coords[2]))

        glVertex3fv((0.1 + coords[0], 0.15 + coords[1], 0.1 + coords[2]))
        glVertex3fv((-0.1 + coords[0], 0.15 + coords[1], 0.1 + coords[2]))
        glVertex3fv((0.1 + coords[0], 0.15 + coords[1], -0.1 + coords[2]))

        glVertex3fv((-0.1 + coords[0], 0.15 + coords[1], -0.1 + coords[2]))
        glVertex3fv((-0.1 + coords[0], 0.15 + coords[1], 0.1 + coords[2]))
        glVertex3fv((0.1 + coords[0], 0.15 + coords[1], -0.1 + coords[2]))

        edges = ((0.1, 0.1),
                 (-0.1, 0.1),
                 (-0.1, -0.1),
                 (0.1, -0.1),
                 (0.1, 0.1),
        )
        for i in range(len(edges) - 1):
            glVertex3fv((edges[i][0] + coords[0], coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], coords[1], edges[i + 1][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], 0.2 + coords[1], edges[i + 1][1] + coords[2]))

            glVertex3fv((edges[i][0] + coords[0], coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i][0] + coords[0], 0.2 + coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], 0.2 + coords[1], edges[i + 1][1] + coords[2]))

        glEnd()


    def display():
        pg.init()
        display = (800, 600)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)

        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_LIGHT0)
        gluPerspective(50, (display[0] / display[1]), 0.1, 50.0)

        glTranslatef(0.0, -1.0, -10)
        glRotatef(30, 10, 0, 0)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            glRotatef(1, 0, 1, 0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            Pyramid(1, -0.2, edges, (0.5, 0.7, 0.25, 1.0))
            PyramidLines(1, -0.2, lines, (0.5, 0.75, 0.3, 1.0))
            Pyramid(0, 0.0, edges, (0.5, 0.8, 0.25, 1.0))
            PyramidLines(0, 0.0, lines, (0.5, 0.75, 0.3, 1.0))
            Pyramid(-1, 0.2, edges, (0.5, 0.9, 0.25, 1.0))
            PyramidLines(-1, 0.2, lines, (0.5, 0.75, 0.3, 1.0))
            Trunk((0.43, 0.26, 0.15, 1.0))
            Top(3.3, (1.0, 0.9, 0.0, 1.0))
            Top(3.6, (1.0, 0.98, 0.16, 1.0))

            TreeCubeToy((-1.1, -0.15, -1.1), (1.0, 0.16, 0.16, 1.0))
            TreeCubeToy((-1.1, -0.15, 1.1), (1.0, 0.98, 0.16, 1.0))
            TreeCubeToy((1.1, -0.15, -1.1), (1.0, 0.98, 0.16, 1.0))
            TreeCubeToy((1.1, -0.15, 1.1), (1.0, 0.16, 0.16, 1.0))

            TreeCubeToy((-1.0, 0.85, -1.0), (0.16, 0.16, 1.0, 1.0))
            TreeCubeToy((-1.0, 0.85, 1.0), (1.0, 0.16, 0.16, 1.0))
            TreeCubeToy((1.0, 0.85, -1.0), (1.0, 0.16, 0.16, 1.0))
            TreeCubeToy((1.0, 0.85, 1.0), (0.16, 0.16, 1.0, 1.0))

            TreeCubeToy((-0.8, 1.85, -0.8), (0.16, 0.8, 0.5, 1.0))
            TreeCubeToy((-0.8, 1.85, 0.8), (0.16, 0.16, 1.0, 1.0))
            TreeCubeToy((0.8, 1.85, -0.8), (0.16, 0.16, 1.0, 1.0))
            TreeCubeToy((0.8, 1.85, 0.8), (0.16, 0.8, 0.5, 1.0))

            pg.display.flip()
            pg.time.wait(10)

    display()

lab2()
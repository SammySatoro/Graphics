import math
import glfw
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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



def lab3():

    def draw_sphere(x, y, z, radius, color):
        sphere = gluNewQuadric()
        glTranslatef(x, y, z)  # coords
        glColor3f(*color)  # color
        gluSphere(sphere, radius, 20, 20)  # draw sphere


    def draw_pyramid(x, y, z, size=1.0, color=(1.0, 1.0, 1.0, 1.0)):
        glBegin(GL_TRIANGLES)
        glColor4f(*color)

        glVertex3fv((0.0 + x, 0.0 + y, 0.0 + z))
        glVertex3fv(((0.5*size) + x, (0.2 * size) + y, 0.0 + z))
        glVertex3fv(((0.75 * size) + x, 0.0 + y, (0.5 * size) + z))

        glVertex3fv((0.0 + x, 0.0 + y, 0.0 + z))
        glVertex3fv(((0.5 * size) + x, -(0.2 * size) + y, 0.0 + z))
        glVertex3fv(((0.75 * size) + x, 0.0 + y, (0.5 * size) + z))

        glEnd()


    def display():
        pg.init()
        display = (1200, 900)
        scree = pg.display.set_mode(display, DOUBLEBUF | OPENGL)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])


        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

        glMatrixMode(GL_MODELVIEW)
        gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        glLoadIdentity()
        displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
        mouseMove = [0, 0]
        pg.mouse.set_pos(displayCenter)

        pg.mouse.set_visible(False)
        up_down_angle = 0.0
        paused = False
        run = True


        z = 0

        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE or event.key == pg.K_RETURN:
                        run = False
                    if event.key == pg.K_PAUSE or event.key == pg.K_p:
                        paused = not paused
                        pg.mouse.set_pos(displayCenter)
                if not paused:
                    if event.type == pg.MOUSEMOTION:
                        mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
                    pg.mouse.set_pos(displayCenter)

            if not paused:
                # get keys
                keypress = pg.key.get_pressed()
                # mouseMove = pygame.mouse.get_rel()

                # init model view matrix
                glLoadIdentity()

                # apply the look up and down
                up_down_angle += mouseMove[1] * 0.1
                glRotatef(up_down_angle, 1.0, 0.0, 0.0)

                # init the view matrix
                glPushMatrix()
                glLoadIdentity()
                ms = 0.06
                # apply the movment
                if keypress[pg.K_w]:
                    glTranslatef(0, 0, ms)
                if keypress[pg.K_s]:
                    glTranslatef(0, 0, -ms)
                if keypress[pg.K_d]:
                    glTranslatef(-ms, 0, 0)
                if keypress[pg.K_a]:
                    glTranslatef(ms, 0, 0)

                # apply the left and right rotation
                glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

            # multiply the current matrix by the get the new view matrix and store the final view matrix
            glMultMatrixf(viewMatrix)
            viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

            # apply view matrix
            glPopMatrix()
            glMultMatrixf(viewMatrix)
            lightpos = (2.0 * math.cos(z), -2.0 * math.cos(z), 2.0)
            z += 0.1

            glPushMatrix()

            glLightfv(GL_LIGHT0, GL_POSITION, lightpos)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen

            # glPushMatrix()

            draw_sphere(0.0, 0.0, 0.0, 0.5, (0.8, 0.7, 0.6))        # head

            draw_sphere(0.42, 0.2, 0.0, 0.1, (0.8, 0.7, 1.0))       # eye
            draw_sphere(0.0, -0.4, 0.0, 0.1, (0.8, 0.7, 1.0))       # eye
            draw_sphere(0.065, 0.0, 0.0, 0.05, (0.0, 0.0, 0.0))     # pupil
            draw_sphere(0.0, 0.4, 0.0, 0.05, (0.0, 0.0, 0.0))       # pupil

            draw_sphere(-0.03, -0.2, -0.15, 0.07, (1.0, 0.5, 0.5))  # nose
            draw_sphere(-0.1, 0.08, -0.035, 0.15, (0.8, 0.8, 0.7))  #
            draw_sphere(0.0, -0.16, 0.0, 0.15, (0.8, 0.8, 0.7))     #

            draw_pyramid(-0.5, 0.3, 0.39, 0.8, (0.85, 0.75, 0.65, 1.0))     # ear
            draw_pyramid(-0.5, 0.3, 0.38, 0.8, (1.0, 0.5, 0.5, 1.0))        #

            draw_pyramid(-0.5, -0.1, 0.39, 0.8, (0.85, 0.75, 0.65, 1.0))    # ear
            draw_pyramid(-0.5, -0.1, 0.38, 0.8, (1.0, 0.5, 0.5, 1.0))       #

            draw_sphere(-0.7, 0.08, -0.1, 0.3, (0.8, 0.7, 0.6))     # neck

            draw_sphere(-0.3, 0.0, -0.18, 0.45, (0.8, 0.7, 0.6))    # body
            for i in range(8):                                      #
                draw_sphere(-0.1, 0.0, 0.0, 0.45, (0.8, 0.7, 0.6))  #

            # left front paw
            draw_sphere(0.9, 0.25, -0.2, 0.2, (0.8, 0.7, 0.6))
            for i in range(6):
                draw_sphere(-0.01, 0.01, -0.07, 0.2 - (i / 100), (0.8, 0.7, 0.6))
            for i in range(6):
                draw_sphere(0.03, 0.01, -0.07, 0.17 - (i / 100), (0.8, 0.7, 0.6))
            draw_sphere(0.0, 0.0, 0.0, 0.13, (0.8, 0.8, 0.7))

            draw_sphere(0.1, -0.12, -0.05, 0.08, (0.8, 0.8, 0.7))
            draw_sphere(0.0, 0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
            draw_sphere(0.0, 0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
            draw_sphere(0.0, 0.08, 0.0, 0.08, (0.8, 0.8, 0.7))

            # right front paw
            draw_sphere(-0.24, -0.75, 0.9, 0.2, (0.8, 0.7, 0.6))
            for i in range(6):
                draw_sphere(-0.01, -0.01, -0.07, 0.2 - (i / 100), (0.8, 0.7, 0.6))
            for i in range(6):
                draw_sphere(0.03, -0.01, -0.07, 0.17 - (i / 100), (0.8, 0.7, 0.6))
            draw_sphere(0.0, 0.0, 0.0, 0.13, (0.8, 0.8, 0.7))
            draw_sphere(0.1, 0.12, -0.05, 0.08, (0.8, 0.8, 0.7))
            draw_sphere(0.0, -0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
            draw_sphere(0.0, -0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
            draw_sphere(0.0, -0.08, 0.0, 0.08, (0.8, 0.8, 0.7))

            # right back paw
            draw_sphere(-1.2, 0.25, 0.9, 0.25, (0.8, 0.7, 0.6))
            for i in range(4):
                draw_sphere(0.02, 0.0, -0.07, 0.25 - (i / 100), (0.8, 0.7, 0.6))
            for i in range(5):
                draw_sphere(-0.02, 0.0, -0.07, 0.2 - (i / 100), (0.8, 0.7, 0.6))
            for i in range(3):
                draw_sphere(0.03, 0.0, -0.07, 0.15 - (i / 100), (0.8, 0.7, 0.6))

            draw_sphere(0.0, 0.0, 0.0, 0.14, (0.8, 0.8, 0.7))
            draw_sphere(0.1, 0.12, -0.05, 0.08, (0.8, 0.8, 0.7))
            draw_sphere(0.0, -0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
            draw_sphere(0.0, -0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
            draw_sphere(0.0, -0.08, 0.0, 0.08, (0.8, 0.8, 0.7))

            # left back paw
            draw_sphere(-0.15, 0.65, 0.9, 0.25, (0.8, 0.7, 0.6))
            for i in range(4):
                draw_sphere(0.02, 0.0, -0.07, 0.25 - (i / 100), (0.8, 0.7, 0.6))
            for i in range(5):
                draw_sphere(-0.02, 0.0, -0.07, 0.2 - (i / 100), (0.8, 0.7, 0.6))
            for i in range(3):
                draw_sphere(0.03, 0.0, -0.07, 0.15 - (i / 100), (0.8, 0.7, 0.6))

            draw_sphere(0.0, 0.0, 0.0, 0.14, (0.8, 0.8, 0.7))
            draw_sphere(0.1, -0.12, -0.05, 0.08, (0.8, 0.8, 0.7))
            draw_sphere(0.0, 0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
            draw_sphere(0.0, 0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
            draw_sphere(0.0, 0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
            # glPopMatrix()


            # tail
            draw_sphere(-0.3, -0.38, 1.2, 0.25, (0.8, 0.7, 0.6))
            draw_sphere(-0.2, 0.0, 0.1, 0.1, (0.8, 0.7, 0.6))
            for i in range(5):
                draw_sphere(-0.02, 0.0, 0.05, 0.1, (0.8, 0.7, 0.6))
            for i in range(2):
                draw_sphere(0.0, 0.0, 0.05, 0.1, (0.8, 0.7, 0.6))
            for i in range(3):
                draw_sphere(0.02, 0.0, 0.05, 0.1, (0.8, 0.7, 0.6))
            for i in range(2):
                draw_sphere(0.02, 0.0, 0.03, 0.1, (0.8, 0.7, 0.6))
            for i in range(4):
                draw_sphere(0.02, 0.0, 0.04, 0.1, (0.8, 0.7, 0.6))
            for i in range(5):
                draw_sphere(0.02, 0.0, 0.04, 0.1 - (i / 100), (0.8, 0.8, 0.7))
            for i in range(5):
                draw_sphere(0.02, 0.0, 0.04 - (i / 100), 0.05 - (i / 100), (0.8, 0.8, 0.7))

            pg.display.flip()  # Update the screen
            pg.time.wait(10)

        pg.quit()

    display()


def lab4():
    import math


    def draw_sphere(x, y, z, radius, color):
        sphere = gluNewQuadric()
        glTranslatef(x, y, z)  # coords
        glColor3f(*color)  # color
        gluSphere(sphere, radius, 20, 20)  # draw sphere


    def draw_pyramid(x, y, z, size=1.0, color=(1.0, 1.0, 1.0, 1.0)):
        glBegin(GL_TRIANGLES)
        glColor4f(*color)

        glVertex3fv((0.0 + x, 0.0 + y, 0.0 + z))
        glVertex3fv(((0.5*size) + x, (0.2 * size) + y, 0.0 + z))
        glVertex3fv(((0.75 * size) + x, 0.0 + y, (0.5 * size) + z))

        glVertex3fv((0.0 + x, 0.0 + y, 0.0 + z))
        glVertex3fv(((0.5 * size) + x, -(0.2 * size) + y, 0.0 + z))
        glVertex3fv(((0.75 * size) + x, 0.0 + y, (0.5 * size) + z))

        glEnd()

    pg.init()
    display = (1200, 900)
    scree = pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

    sphere = gluNewQuadric()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()
    displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
    mouseMove = [0, 0]
    pg.mouse.set_pos(displayCenter)

    pg.mouse.set_visible(False)
    up_down_angle = 0.0
    paused = False
    run = True

    ambient = (0, 0, 0, 1)
    lightpos = (2, 2, 2)
    coef = 0

    # Lighting
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE or event.key == pg.K_RETURN:
                    run = False
                if event.key == pg.K_PAUSE or event.key == pg.K_p:
                    paused = not paused
                    pg.mouse.set_pos(displayCenter)
            if not paused:
                if event.type == pg.MOUSEMOTION:
                    mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
                pg.mouse.set_pos(displayCenter)

        if not paused:
            # get keys
            keypress = pg.key.get_pressed()
            # mouseMove = pygame.mouse.get_rel()

            # init model view matrix
            glLoadIdentity()

            # apply the look up and down
            up_down_angle += mouseMove[1] * 0.1
            glRotatef(up_down_angle, 1.0, 0.0, 0.0)

            # init the view matrix
            glPushMatrix()
            glLoadIdentity()
            ms = 0.06
            # apply the movment
            if keypress[pg.K_w]:
                glTranslatef(0, 0, ms)
            if keypress[pg.K_s]:
                glTranslatef(0, 0, -ms)
            if keypress[pg.K_d]:
                glTranslatef(-ms, 0, 0)
            if keypress[pg.K_a]:
                glTranslatef(ms, 0, 0)

            # apply the left and right rotation
            glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

        # multiply the current matrix by the get the new view matrix and store the final vie matrix
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen
        lightpos = (-2.0 * math.sin(coef), 2.0, -2.0 * math.sin(coef))
        coef += 0.1

        glPushMatrix()

        glLightfv(GL_LIGHT0, GL_POSITION, lightpos)


        draw_sphere(0.0, 0.0, 0.0, 0.5, (0.8, 0.7, 0.6))  # head

        draw_sphere(0.42, 0.2, 0.0, 0.1, (0.8, 0.7, 1.0))  # eye
        draw_sphere(0.0, -0.4, 0.0, 0.1, (0.8, 0.7, 1.0))  # eye
        draw_sphere(0.065, 0.0, 0.0, 0.05, (0.0, 0.0, 0.0))  # pupil
        draw_sphere(0.0, 0.4, 0.0, 0.05, (0.0, 0.0, 0.0))  # pupil

        draw_sphere(-0.03, -0.2, -0.15, 0.07, (1.0, 0.5, 0.5))  # nose
        draw_sphere(-0.1, 0.08, -0.035, 0.15, (0.8, 0.8, 0.7))  #
        draw_sphere(0.0, -0.16, 0.0, 0.15, (0.8, 0.8, 0.7))  #

        draw_pyramid(-0.5, 0.3, 0.39, 0.8, (0.85, 0.75, 0.65, 1.0))  # ear
        draw_pyramid(-0.5, 0.3, 0.38, 0.8, (1.0, 0.5, 0.5, 1.0))  #

        draw_pyramid(-0.5, -0.1, 0.39, 0.8, (0.85, 0.75, 0.65, 1.0))  # ear
        draw_pyramid(-0.5, -0.1, 0.38, 0.8, (1.0, 0.5, 0.5, 1.0))  #

        draw_sphere(-0.7, 0.08, -0.1, 0.3, (0.8, 0.7, 0.6))  # neck

        draw_sphere(-0.3, 0.0, -0.18, 0.45, (0.8, 0.7, 0.6))  # body
        for i in range(8):  #
            draw_sphere(-0.1, 0.0, 0.0, 0.45, (0.8, 0.7, 0.6))  #

        # left front paw
        draw_sphere(0.9, 0.25, -0.2, 0.2, (0.8, 0.7, 0.6))
        for i in range(6):
            draw_sphere(-0.01, 0.01, -0.07, 0.2 - (i / 100), (0.8, 0.7, 0.6))
        for i in range(6):
            draw_sphere(0.03, 0.01, -0.07, 0.17 - (i / 100), (0.8, 0.7, 0.6))
        draw_sphere(0.0, 0.0, 0.0, 0.13, (0.8, 0.8, 0.7))

        draw_sphere(0.1, -0.12, -0.05, 0.08, (0.8, 0.8, 0.7))
        draw_sphere(0.0, 0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
        draw_sphere(0.0, 0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
        draw_sphere(0.0, 0.08, 0.0, 0.08, (0.8, 0.8, 0.7))

        # right front paw
        draw_sphere(-0.24, -0.75, 0.9, 0.2, (0.8, 0.7, 0.6))
        for i in range(6):
            draw_sphere(-0.01, -0.01, -0.07, 0.2 - (i / 100), (0.8, 0.7, 0.6))
        for i in range(6):
            draw_sphere(0.03, -0.01, -0.07, 0.17 - (i / 100), (0.8, 0.7, 0.6))
        draw_sphere(0.0, 0.0, 0.0, 0.13, (0.8, 0.8, 0.7))
        draw_sphere(0.1, 0.12, -0.05, 0.08, (0.8, 0.8, 0.7))
        draw_sphere(0.0, -0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
        draw_sphere(0.0, -0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
        draw_sphere(0.0, -0.08, 0.0, 0.08, (0.8, 0.8, 0.7))

        # right back paw
        draw_sphere(-1.2, 0.25, 0.9, 0.25, (0.8, 0.7, 0.6))
        for i in range(4):
            draw_sphere(0.02, 0.0, -0.07, 0.25 - (i / 100), (0.8, 0.7, 0.6))
        for i in range(5):
            draw_sphere(-0.02, 0.0, -0.07, 0.2 - (i / 100), (0.8, 0.7, 0.6))
        for i in range(3):
            draw_sphere(0.03, 0.0, -0.07, 0.15 - (i / 100), (0.8, 0.7, 0.6))

        draw_sphere(0.0, 0.0, 0.0, 0.14, (0.8, 0.8, 0.7))
        draw_sphere(0.1, 0.12, -0.05, 0.08, (0.8, 0.8, 0.7))
        draw_sphere(0.0, -0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
        draw_sphere(0.0, -0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
        draw_sphere(0.0, -0.08, 0.0, 0.08, (0.8, 0.8, 0.7))

        # left back paw
        draw_sphere(-0.15, 0.65, 0.9, 0.25, (0.8, 0.7, 0.6))
        for i in range(4):
            draw_sphere(0.02, 0.0, -0.07, 0.25 - (i / 100), (0.8, 0.7, 0.6))
        for i in range(5):
            draw_sphere(-0.02, 0.0, -0.07, 0.2 - (i / 100), (0.8, 0.7, 0.6))
        for i in range(3):
            draw_sphere(0.03, 0.0, -0.07, 0.15 - (i / 100), (0.8, 0.7, 0.6))

        draw_sphere(0.0, 0.0, 0.0, 0.14, (0.8, 0.8, 0.7))
        draw_sphere(0.1, -0.12, -0.05, 0.08, (0.8, 0.8, 0.7))
        draw_sphere(0.0, 0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
        draw_sphere(0.0, 0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
        draw_sphere(0.0, 0.08, 0.0, 0.08, (0.8, 0.8, 0.7))
        # glPopMatrix()

        # tail
        draw_sphere(-0.3, -0.38, 1.2, 0.25, (0.8, 0.7, 0.6))
        draw_sphere(-0.2, 0.0, 0.1, 0.1, (0.8, 0.7, 0.6))
        for i in range(5):
            draw_sphere(-0.02, 0.0, 0.05, 0.1, (0.8, 0.7, 0.6))
        for i in range(2):
            draw_sphere(0.0, 0.0, 0.05, 0.1, (0.8, 0.7, 0.6))
        for i in range(3):
            draw_sphere(0.02, 0.0, 0.05, 0.1, (0.8, 0.7, 0.6))
        for i in range(2):
            draw_sphere(0.02, 0.0, 0.03, 0.1, (0.8, 0.7, 0.6))
        for i in range(4):
            draw_sphere(0.02, 0.0, 0.04, 0.1, (0.8, 0.7, 0.6))
        for i in range(5):
            draw_sphere(0.02, 0.0, 0.04, 0.1 - (i / 100), (0.8, 0.8, 0.7))
        for i in range(5):
            draw_sphere(0.02, 0.0, 0.04 - (i / 100), 0.05 - (i / 100), (0.8, 0.8, 0.7))

        glPopMatrix()

        pg.display.flip()  # Update the screen
        pg.time.wait(10)

    pg.quit()


def lab5():
    import sys

    global x_rotation
    global y_rotation
    global ambient
    global torcolor
    global lightpos
    global x_light_rotation
    global y_light_rotation
    global z_light_rotation

    def init():
        global x_rotation
        global y_rotation
        global ambient
        global torcolor
        global lightpos
        global x_light_rotation
        global y_light_rotation
        global z_light_rotation
        x_rotation = 0.0
        y_rotation = 0.0
        ambient = (0.0, 1.0, 0.0, 1.0)
        # ambient = (1.0, 1.0, 1.0, 1.0)
        torcolor = (0.9, 0.6, 0.3, 1.0)
        x_light_rotation = 1.0
        y_light_rotation = 1.0
        z_light_rotation = 1.0
        lightpos = (x_light_rotation, y_light_rotation, z_light_rotation)

        glClearColor(0.75, 0.75, 0.75, 1.0)
        gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
        glRotatef(0, 1.0, 0.0, 0.0)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, lightpos)


    def speckeys(key, x, y):
        global x_rotation
        global y_rotation
        global x_light_rotation
        global y_light_rotation
        global z_light_rotation

        if key == GLUT_KEY_UP:
            x_rotation -= 0.5
        if key == GLUT_KEY_DOWN:
            x_rotation += 0.5
        if key == GLUT_KEY_LEFT:
            y_rotation -= 0.5
        if key == GLUT_KEY_RIGHT:
            y_rotation += 0.5

        if key == GLUT_KEY_F1:
            x_light_rotation -= 0.5
        if key == GLUT_KEY_F2:
            x_light_rotation += 0.5
        if key == GLUT_KEY_F3:
            y_light_rotation -= 0.5
        if key == GLUT_KEY_F4:
            y_light_rotation += 0.5
        if key == GLUT_KEY_F5:
            z_light_rotation -= 0.5
        if key == GLUT_KEY_F6:
            z_light_rotation += 0.5

        glutPostRedisplay()



    def draw():
        global x_rotation
        global y_rotation
        global x_light_rotation
        global y_light_rotation
        global z_light_rotation
        global lightpos
        global greencolor
        global torcolor
        global lightpos

        lightpos = (x_light_rotation, y_light_rotation, z_light_rotation)
        glClear(GL_COLOR_BUFFER_BIT)
        glPushMatrix()  # Сохраняем текущее положение "камеры"
        glRotatef(x_rotation, 1.0, 0.0, 0.0)
        glRotatef(y_rotation, 0.0, 1.0, 0.0)
        glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

        # Устанавливаем материал: рисовать с 2 сторон, освещение зеркальных бликов, зеленый цвет
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, torcolor)
        glTranslatef(0.0, 0.0, 0.2)  # Сдвинемся по оси Z на 0.2

        glutSolidTorus(0.2, 0.5, 48, 48)

        glPopMatrix()
        glutSwapBuffers()

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    glutInitWindowSize(600, 600)
    glutInitWindowPosition(660, 240)

    glutInit(sys.argv)
    glutCreateWindow("God Of Lightning")

    glutDisplayFunc(draw)
    glutSpecialFunc(speckeys)

    init()
    glutMainLoop()



def lab55():
    import math


    def render_torus(x, y, pol, radius, rot_speed):
        twicePi: GLfloat = 2.0 * math.pi
        torus = gluNewQuadric()
        glTranslatef(0, 0, -0.6)
        for i in range(rot_speed, pol + rot_speed):
            if i >= rot_speed and i < pol / 2 + rot_speed: glColor3f(1.0,1.0,1.0)
            elif i < rot_speed or i > pol / 2 + rot_speed: glColor3f(1.0,1.0,1.0)

            glTranslatef(x + (radius * math.cos(i * twicePi / 360) / 10),
                         y - (radius * math.sin(i * twicePi / 360) / 10),
                         0)
            gluSphere(torus, radius, 15, 15)

    pg.init()
    display = (1200, 900)
    scree = pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()
    displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
    mouseMove = [0, 0]
    pg.mouse.set_pos(displayCenter)

    pg.mouse.set_visible(False)
    up_down_angle = 0.0
    paused = False
    run = True

    ambient = (0, 1, 0, 0.1)
    lightpos = (0, 0, 2)
    speed = 0

    # Lighting
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE or event.key == pg.K_RETURN:
                    run = False
                if event.key == pg.K_PAUSE or event.key == pg.K_p:
                    paused = not paused
                    pg.mouse.set_pos(displayCenter)
            if not paused:
                if event.type == pg.MOUSEMOTION:
                    mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
                pg.mouse.set_pos(displayCenter)

        if not paused:
            # get keys
            keypress = pg.key.get_pressed()
            # mouseMove = pygame.mouse.get_rel()

            # init model view matrix
            glLoadIdentity()

            # apply the look up and down
            up_down_angle += mouseMove[1] * 0.1
            glRotatef(up_down_angle, 1.0, 0.0, 0.0)

            # init the view matrix
            glPushMatrix()
            glLoadIdentity()
            ms = 0.06
            # apply the movment
            if keypress[pg.K_w]:
                glTranslatef(0, 0, ms)
            if keypress[pg.K_s]:
                glTranslatef(0, 0, -ms)
            if keypress[pg.K_d]:
                glTranslatef(-ms, 0, 0)
            if keypress[pg.K_a]:
                glTranslatef(ms, 0, 0)

            # apply the left and right rotation
            glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

        # multiply the current matrix by the get the new view matrix and store the final vie matrix
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen
        lightpos = (0.0, 0.0, 1.0)

        glPushMatrix()

        glLightfv(GL_LIGHT0, GL_POSITION, lightpos)


        render_torus(0, 0, 360, 0.2, speed)
        speed += 1

        glPopMatrix()

        pg.display.flip()  # Update the screen
        pg.time.wait(10)

    pg.quit()

if __name__ == '__main__':

    lab55()

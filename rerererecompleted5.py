from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

import pygame as pg
from pygame.locals import *

def lab5():
    pg.init()
    display = (1200, 900)
    scree = pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)

    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT)

    # GL_EMISSION - цвет собственного излучения материала (светящийся)
    # just in case - GL_AMBIENT_AND_DIFFUSE
    # Из-за фонового (glLightfv(GL_LIGHT0, GL_AMBIENT, [0.0, 1.0, 0.0, 1.0]) 121 строка) света
    # и свечения материала верхняя часть тора светится белым, хотя источник света зеленый
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, [0.1, 0.7, 0.1, 0.6])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 5)


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


    ambient = (.1, .1, .1, 1)

    lightpos = (0, 2, 0)

    # Lighting
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

    rotation = 0

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

            keypress = pg.key.get_pressed()


            glLoadIdentity()

            up_down_angle += mouseMove[1] * 0.1
            glRotatef(up_down_angle, 1.0, 0.0, 0.0)

            glPushMatrix()
            glLoadIdentity()
            ms = 0.06

            if keypress[pg.K_w]:
                glTranslatef(0, 0, ms)
            if keypress[pg.K_s]:
                glTranslatef(0, 0, -ms)
            if keypress[pg.K_d]:
                glTranslatef(-ms, 0, 0)
            if keypress[pg.K_a]:
                glTranslatef(ms, 0, 0)

            glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)


        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

        lightpos = (0, -1.0, 3)


        glPushMatrix()

        glClearColor(0.0, 0.0, 0.0, 1.0)

        glutInit(sys.argv)


        # Фоновый зеленый свет - GL_AMBIENT
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.0, 1.0, 0.0, 1.0])  # light color

        # rotate the object
        glRotatef(rotation, 1, 0, 0)
        glColor3f(0.5, 0.5, 0.5)
        glutSolidTorus(0.2, 0.5, 48, 48)


        rotation += 1
        if rotation > 360:
            rotation = 0

        glPopMatrix()

        pg.display.flip()  # Update the screen
        pg.time.wait(10)

    pg.quit()

lab5()

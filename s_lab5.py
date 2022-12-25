from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

import glfw
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

    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # Устанавливаем материал GL_SPECULAR - зеркальный
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1.0, 0.2, 0.2, 0.6])
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


    ambient = (0.4, 0.4, 0.4, 1)
    # Позиция источника света над шаром
    lightpos = (0, 2, 0)

    # Lighting
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

    def RenderWall(x, y, z, color):
        glTranslatef(x, y, z)
        glColor4f(*color)
        for i in range(12):
            for j in range(4):
                glutSolidCube(0.5)
                glTranslatef(0.0, 0.0, 0.5)
            glTranslatef(0.0, 0.5, -2.0)
        glTranslatef(-x, -y, -z)

    rotation = 0
    direction = 1
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

        # Устанавливаем начальное положение объектов
        glTranslatef(0, 20.0, -1.0)
        glClearColor(0.0, 0.0, 0.0, 1.0)

        glutInit(sys.argv)

        # Рендерим стенки
        RenderWall(-1, 3, 0, (0.8, 0.1, 1.0, 1))
        RenderWall(11, -3, 0, (0.8, 0.1, 1.0, 1))

        # Рассеянный красный свет - GL_DIFFUSE
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 0.0, 0.0, 1])  # light color

        # Перемещение шара
        glTranslatef(rotation, -6, 0.5)
        # Серый цвет
        glColor3f(0.65, 0.65, 0.65)
        # Сфера
        glutSolidSphere(1, 30, 30)

        # Сторона перемещения меняется с помощью изменения знака переменной direction {-1, 1},
        # которая домножается на rotation
        rotation += 0.1 * direction
        if rotation > 10 or rotation < 0:
            direction *= -1

        glPopMatrix()

        pg.display.flip()  # Update the screen
        pg.time.wait(10)

    pg.quit()

lab5()
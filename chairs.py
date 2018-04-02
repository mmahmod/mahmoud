from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
global x
global y
global z

def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,0.5,1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(15,10,15,0,0,0,0,1,0)

def cube(x,y,z,r,g,b):
    glPushMatrix()
    glColor(0.2,0.4,0.5,0.8)
    glScale(x,y,z)
    glutWireCube(2)
    glPopMatrix()



def draw():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
 #1   
    glTranslate(5,0,0)
    cube(2.5,1,3,0,1,0)
    glTranslate(0,4,-2)
    cube(2.5,3,1,0,1,1)
    glLoadIdentity()

    glTranslate(7.25,-3,2.5)
    cube(0.25,2,0.5,1,0,0)
    glLoadIdentity()

    glTranslate(7.25, -3, -2.5)
    cube(0.25, 2, 0.5,1,0,0,)
    glLoadIdentity()

    glTranslate(-2.25, -5, -6.5)
    cube(0.25, 2, 0.5,1,0,0)
    glLoadIdentity()
    glTranslate(2.25, -2, 2.5)
    cube(0.25, 2, 0.5,1,0,0)




#2
    glTranslate(-3,5.5,2)
    cube(2.5,1,3,1,1,0)

    glTranslate(0,4,-2)
    cube(2.5,3,1,0,1,1)
    glLoadIdentity()

    glTranslate(-2.25,0.25,0.5)
    cube(0.25,2,0.5,1,1,1)
    glLoadIdentity()


    glTranslate(-2.25, 0.25, 0.5)
    cube(0.25, 2, 0.5, 0, 0, 0)
    glLoadIdentity()


    glTranslate(-8.25, 0.25, 0.5)
    cube(0.25, 2, 0.5, 0, 0, 0)
    glLoadIdentity()


    glTranslate(-2.25, 0.25, 3.5)
    cube(0.25, 2, 0.5, 0, 0, 0)
    glLoadIdentity()


    glTranslate(-8.25, 0.25, 3.5)
    cube(0.25, 2, 0.5, 0, 0, 0)
    glLoadIdentity()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,500)
glutCreateWindow(b"korsyen")
myinit()
glutDisplayFunc(draw)
#glutIdleFunc(draw)
glutMainLoop()

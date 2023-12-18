from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def point(x,y,size):
    glColor3ub(100,0,0)
    glRectf(x-size,y-size,x+size,y+size)

def theScreenContent():
    point(200,200,3)
    glFlush()

glutInit()

glutCreateWindow("point")
gluOrtho2D(0,400,0,400)

glutDisplayFunc(theScreenContent)
glutIdleFunc(theScreenContent)
glutMainLoop()

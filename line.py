from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def line(x1,y1,x2,y2):
    glColor3ub(100,0,0)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()

def theScreenContent():
    line(100,100,400,400)
    glFlush()

glutInit()

glutCreateWindow("point")
gluOrtho2D(0,400,0,400)

glutDisplayFunc(theScreenContent)
glutIdleFunc(theScreenContent)
glutMainLoop()

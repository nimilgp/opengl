from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def square():
    glColor3ub(100,0,0)
    glRectf(0,0,100,100)

def bg():
    glColor3ub(255,255,255)
    glRectf(0,0,500,500)

def myInit():
    #glClearColor(0,0,1,1) or just draw window sized rectangle in fg
    gluOrtho2D(0, 500, 0, 500)

def theScreenContent():
    #glClear(GL_COLOR_BUFFER_BIT) #for clearing current color buffer
    #glLoadIdentity()
    bg()
    square()
    #glutSwapBuffers()  or use glFlush()
    glFlush()

glutInit()
#glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
#glutInitWindowSize(400,400)
#glutInitWindowPosition(0,0)

glutCreateWindow("basic")
gluOrtho2D(0, 500, 0, 500)

glutDisplayFunc(theScreenContent)
#glutIdleFunc(theScreenContent)
glutMainLoop()

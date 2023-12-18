from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def ddaLine(x1,y1,x2,y2):
    deltax = x2 - x1
    deltay = y2 - y1
    steps = 0
    
    if abs(deltax) > abs(deltay):
        steps = abs(deltax)
    else:
        steps = abs(deltay)
    
    xinc = deltax/steps
    yinc = deltay/steps

    glColor3ub(100,0,0)
    glBegin(GL_POINTS)
    #dda code
    for step in range(steps):
        glVertex2f(round(x1),round(y1))
        x1 = x1 + xinc
        y1 = y1 + yinc
    glEnd()

def theScreenContent():
    ddaLine(100,100,400,400)
    glFlush()

glutInit()

glutCreateWindow("point")
gluOrtho2D(0,400,0,400)

glutDisplayFunc(theScreenContent)
glutIdleFunc(theScreenContent)
glutMainLoop()

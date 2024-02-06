from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import math

LENGTH = 50
X_POS = 100
Y_POS = 200
X_VEL = 15
Y_VEL = 10
GRAV_ACC = -0.5
UNIT_TIME = 0

def parabolicPath():
    X_REF = X_VEL*UNIT_TIME
    Y_REF = Y_VEL*UNIT_TIME + GRAV_ACC*UNIT_TIME**2/2 
    theta = math.atan((Y_VEL+GRAV_ACC*UNIT_TIME)/X_VEL)
    return X_REF,Y_REF,theta

def sky():
    glColor3ub(116,195,227)
    glRectf(0,0,1000,500)

def ground():
    glColor3ub(94,255,116)
    glRectf(0,0,1000,100)

def javelin(x,y,theta):
    x += X_POS
    y += Y_POS
    x1 = x + LENGTH*math.cos(theta)
    x2 = x - LENGTH*math.cos(theta)
    y1 = y + LENGTH*math.sin(theta)
    y2 = y - LENGTH*math.sin(theta)
    glLineWidth(5)
    glColor3ub(255,255,255)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()

def theScreenContent():
    global UNIT_TIME
    UNIT_TIME += 0.1
    time.sleep(0.01)
    sky()
    ground()
    x,y,theta=parabolicPath()
    javelin(x,y,theta)
    glFlush()

glutInit()
glutInitWindowSize(1000,500)
glutCreateWindow("javelin in projectile motion")
gluOrtho2D(0, 1000, 0, 500)
glutDisplayFunc(theScreenContent)
glutIdleFunc(theScreenContent)
glutMainLoop()

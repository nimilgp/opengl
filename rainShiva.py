from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import random
import math

RAINDROPLETS = []
TERM_VERTICAL_VEL = -10
HORIZONTAL_VEL = -3
BGCOLOR = [0.4,0.92,1]
RAINCOLOR = [0.02,0.44,0.6]
RAINSIZE = 5
RAINLENGTH = 10
DEGREE = 30
THETA = DEGREE*math.pi/180
RAINSTRENGTH = 10

def drawDroplet(xh,yh):
    xl = xh - RAINLENGTH*math.sin(THETA)
    yl = yh - RAINLENGTH*math.cos(THETA)
    glLineWidth(RAINSIZE)
    glColor3f(*RAINCOLOR)
    glBegin(GL_LINES)
    glVertex(xl,yl)
    glVertex(xh,yh)
    glEnd()

def drawRain():
    for drop in RAINDROPLETS:
        drawDroplet(*drop)
    glFlush()

def gravity():
    global RAINDROPLETS
    for drop in RAINDROPLETS:
        drop[0] += HORIZONTAL_VEL 
        drop[1] += TERM_VERTICAL_VEL

def spawnDroplets():
    global RAINDROPLETS
    for i in range(RAINSTRENGTH):    
        x = random.randint(-1000,1000)
        y = 600
        RAINDROPLETS.append([x,y])

def Bg():
    glColor3f(*BGCOLOR)
    glRectf(0,0,500,500)

def theScreenContent():
    time.sleep(0.02)
    Bg()
    spawnDroplets()
    gravity()
    drawRain()
    drawRain()
    drawRain()
    drawRain()
    drawRain()
    glFlush()

glutInit()
glutInitWindowSize(500,500)
glutCreateWindow("flood fill")
gluOrtho2D(0, 500, 0, 500)
glutDisplayFunc(theScreenContent)
glutIdleFunc(theScreenContent)
glutMainLoop()

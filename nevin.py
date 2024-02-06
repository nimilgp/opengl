from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time

sys.setrecursionlimit(10000)

WINDOWHEIGHT = 500
BGCOLOR = [0.36,0.81,1]
OLDCOLOR = [1,1,1]
NEWCOLOR = [1,0,0]
SZ = 2

def Bg():
    glColor3f(*BGCOLOR)
    glRectf(0,0,500,500)

def squareToFill():
    glColor3f(*OLDCOLOR)
    glRectf(100,100,300,200)

def putPixel(x,y):
    glPointSize(SZ)
    glBegin(GL_POINTS)
    glVertex(x,y)
    glEnd()
    glFlush()

def floodFill(x,y):
     readColor = glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT)[0][0]
     if all(readColor == OLDCOLOR):
         glColor3f(*NEWCOLOR)
         putPixel(x,y)
         floodFill(x+SZ,y)
         floodFill(x,y+SZ)
         floodFill(x-SZ,y)
         floodFill(x,y-SZ)

def mouseClick(button,state,x,y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = WINDOWHEIGHT - y
        floodFill(x,y)
        
def theScreenContent():
    Bg()
    squareToFill()
    glFlush()

glutInit()
glutInitWindowSize(500,500)
glutCreateWindow("flood fill")
gluOrtho2D(0, 500, 0, 500)
glutDisplayFunc(theScreenContent)
glutMouseFunc(mouseClick)
glutMainLoop()

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

allThePaintedSpots = [[200,200],[200,300]]

def paint_spot(blx,bly):
    glColor3ub(188, 153, 115)
    spot_width = 50
    spot_height = 10
    glRectf(blx, bly, blx+spot_width, bly+spot_height)

def painted_spots_loop():
    global allThePaintedSpots
    for spot in allThePaintedSpots:
        paint_spot(spot[0],spot[1])

def uncolored_house_struct():
    glColor3ub(170, 136, 100)   
    glRectf(200,200,600,400)

def door():
    glColor3ub(89, 50, 7)   
    glRectf(350,200,450,350)
    
def chimmeny():
    glColor3ub(127, 96, 63)
    glRectf(550,400,600,600)

def roof():
    glBegin(GL_TRIANGLES)
    glColor3ub(153, 29, 10)
    glVertex2f(400.0,600.0)
    glVertex2f(100.0,400.0)
    glVertex2f(700.0,400.0)
    glEnd()

def uncolored_house():
    uncolored_house_struct()
    door()
    chimmeny()
    roof()
    painted_spots_loop()

def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    uncolored_house()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("House")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

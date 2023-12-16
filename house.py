from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

spotsToPaint = []
allThePaintedSpots = []
spot_height = 1

def generate_spots(x,ystart,ystop):
    global spotsToPaint 
    for y in range(ystart,ystop):
        spotsToPaint.append([x,y])
generate_spots(200,200,400)
generate_spots(250,200,400)
generate_spots(300,200,400)
generate_spots(350,350,400)
generate_spots(400,350,400)
generate_spots(450,200,400)
generate_spots(500,200,400)
generate_spots(550,200,400)

def sky():
    glColor3ub(103, 163, 252)   
    glRectf(0,0,800,800)

def ground():
    glColor3ub(54, 160, 81)   
    glRectf(0,0,800,200)

def paint_spot(blx,bly):
    global spot_height
    glColor3ub(188, 153, 115)
    spot_width = 50
    glRectf(blx, bly, blx+spot_width, bly+spot_height)

def painted_spots_loop():
    global allThePaintedSpots
    if len(allThePaintedSpots) == 0:
        return
    for spot in allThePaintedSpots:
        paint_spot(spot[0],spot[1])

def uncolored_house_struct():
    glColor3ub(170, 136, 100)   
    glRectf(200,200,600,400)

def door_handle():
    #glColor3ub(141, 140, 140)   
    glColor3ub(35, 35, 35)   
    glRectf(425,250,435,275)

def door_border():
    glColor3ub(73, 41, 7)   
    glRectf(350,200,450,350)

def inner_door():
    dw = 10 #design width for the door
    glColor3ub(89, 50, 7)   
    glRectf(350+dw,200+dw,450-dw,350-dw)

def door():
    door_border()
    inner_door()
    door_handle()

def chimmeny():
    glColor3ub(127, 96, 63)
    glRectf(550,400,600,600)

def roof():
    glBegin(GL_QUADS)
    glColor3ub(153, 29, 10)
    glVertex2f(100.0,400.0)
    glVertex2f(300,500)
    glVertex2f(500,500)
    glVertex2f(700.0,400.0)
    glEnd()

def draw_screen():
    time.sleep(0.01)
    sky()
    ground()
    uncolored_house_struct()
    door()
    chimmeny()
    roof()
    painted_spots_loop()
    global allThePaintedSpots
    global spotsToPaint
    if(len(spotsToPaint)>0):
        tempSpot = spotsToPaint.pop(0)
        allThePaintedSpots.append(tempSpot)

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
    draw_screen()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Man Painting His House")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

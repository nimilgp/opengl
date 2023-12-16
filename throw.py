from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

time = 0
animation_speed = 0.05
line_length=0.1
javelin_translate_y=0
javelin_translate_x=0

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1, 1, -1, 1) 

def draw_circle(center_x, center_y, radius, segments):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(center_x, center_y)
    for i in range(segments + 1):
        theta = i * (2.0 * math.pi / segments)
        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    
def ground():
    glBegin(GL_LINES)
    glVertex2f(-1, -0.2)
    glVertex2f(1,- 0.2)
    glEnd()

def draw_line_below_circle(center_x, center_y, radius, line_length):
    glBegin(GL_LINES)
    glVertex2f(center_x, center_y - radius)
    glVertex2f(center_x, center_y - radius - line_length)
    glEnd()

def draw_hands(center_x, center_y, arm_length):
    glBegin(GL_LINES)
    # Right hand
    glVertex2f(center_x, center_y - 0.6 * arm_length)
    glVertex2f(center_x + arm_length, center_y - arm_length)
    # Left hand
    glVertex2f(center_x, center_y - 0.6 * arm_length)
    glVertex2f(center_x - arm_length, center_y - arm_length)
    glEnd()

def draw_javelin(center_x, center_y, radius, line_length,arm_length):
    global javelin_translate_y
    global javelin_translate_x 
    javelin_translate_y+=0.008
    javelin_translate_x+=0.004
    glBegin(GL_LINES)  

    glVertex2f(center_x-javelin_translate_x, center_y + radius + line_length+ javelin_translate_y)
    glVertex2f(center_x + arm_length-javelin_translate_x, center_y - radius - line_length * 0.5+ javelin_translate_y)  

    glEnd()

def draw_legs(center_x, center_y, leg_length, radius):
    global leg_animation
    global time
    leg_animation = leg_length * math.sin(time)
    leg_offset = 0.1 * math.sin(leg_animation)
    
    glBegin(GL_LINES)
    # Right leg
    glVertex2f(center_x, center_y - radius - leg_length)
    glVertex2f(center_x + 0.05- leg_animation, center_y - leg_length * 2.0 - leg_offset)
    # Left leg
    glVertex2f(center_x, center_y - radius - leg_length)
    glVertex2f(center_x - 0.05+ leg_animation, center_y - leg_length * 2.0 + leg_offset)
    time += animation_speed * 2
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_circle(0.0, 0.0, 0.1, 100)
    draw_line_below_circle(0.0, 0.0, 0.1, 0.2)
    draw_hands(0.0, 0.0, 0.15)
    draw_legs(0.0, 0.0, 0.2, 0.1)
    draw_javelin(0.0, 0.0, 0.1, 0.1,0.15) 
    ground()
    glutSwapBuffers()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutCreateWindow("Stickman Example")
    glutInitWindowSize(800, 1000)
    glutDisplayFunc(display)
    glutTimerFunc(16, update, 0) 
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()

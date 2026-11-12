from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = tx = ty = 0
scale = 1
mode = 0

faces = [
    ((1,0,0), [(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]),
    ((0,1,0), [(-1,-1,-1),(-1,1,-1),(1,1,-1),(1,-1,-1)]),
    ((0,0,1), [(-1,1,-1),(-1,1,1),(1,1,1),(1,1,-1)]),
    ((1,1,0), [(-1,-1,-1),(1,-1,-1),(1,-1,1),(-1,-1,1)]),
    ((1,0,1), [(1,-1,-1),(1,1,-1),(1,1,1),(1,-1,1)]),
    ((0,1,1), [(-1,-1,-1),(-1,-1,1),(-1,1,1),(-1,1,-1)])
]

def draw_cube():
    glBegin(GL_QUADS)
    for color, verts in faces:
        glColor3fv(color)
        for v in verts:
            glVertex3fv(v)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 6, 0, 0, 0, 0, 1, 0)

    glTranslatef(tx, ty, 0)
    glScalef(scale, scale, scale)
    glRotatef(angle, 1, 1, 1)

    draw_cube()
    glutSwapBuffers()

def idle():
    global angle, tx, scale
    if mode == 1:
        angle += 0.5
    elif mode == 2:
        tx = tx + 0.005 if tx < 2 else -2
    elif mode == 3:
        scale = scale + 0.005 if scale < 2 else 0.5
    glutPostRedisplay()

def menu(opt):
    global mode
    if opt == 4:
        exit()
    mode = opt

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w / h, 1, 20)
    glMatrixMode(GL_MODELVIEW)

def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"3D Polygon Animation")

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)

    glutCreateMenu(menu)
    for i, text in enumerate(["Rotate", "Translate", "Scale", "Exit"], 1):
        glutAddMenuEntry(text, i)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

    glutMainLoop()

main()

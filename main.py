import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OGL

RES = [800,600]

def main():
    pygame.display.init()
    screen = pygame.display.set_mode(RES, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Juego de prueba")
    gluPerspective(45, (RES[0]/RES[1]), 0.1, 200.0)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    clock = pygame.time.Clock()
    ogl = OGL.Graphics()
    while True:
        ogl.refresh()
        glClearColor(1,1,1,1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        pygame.display.flip()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
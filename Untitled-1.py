
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

pygame.display.set_caption("Marte Gacute")

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0,0,-5)

while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
         pygame.quit()
         quit()
glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
pygame.display.flip()
pygame.time.wait(15)

glBegin(GL_POINTS)
glVertex3f(-0.5, 0.5, 0.5)
glVertex3f(-0.5, -0.5, 0.5)
glVertex3f(0.5, -0.5, 0.5)
glVertex3f(0.5, 0.5, 0.5)
glEnd()
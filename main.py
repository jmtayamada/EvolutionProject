import pygame
from Classes.Basic import *
from Classes.Grass import *
from pygame.locals import *
from GlobalVar import *

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))

running = True

screen.fill("white")

organisms.append(Grass(5, 5, [0, 1], screen))


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  for obj in organisms:
    obj.Turn()
  pygame.display.update()
pygame.quit()

from Classes.Grass import *
from Classes.Herbivore import *
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

for obj in range(20):
  organisms.append(Grass(RandomPosition(), RandomPosition(), [], screen))

for obj in range(10):
  organisms.append(Herbivore(RandomPosition(), RandomPosition(), [], screen))

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  for obj in organisms:
    if obj.type == "grass":
      obj.Turn()
  for obj in organisms:
    if obj.type == "herbivore":
      obj.Turn()
  pygame.display.update()
  clock.tick(10)
pygame.quit()

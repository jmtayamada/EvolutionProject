import pygame
from Classes.Basic import *
import random
from GlobalVar import *


class Grass(Basic):
  def __init__(self, posx, posy, genes, screen):
    super().__init__(posx, posy, genes, "grass", screen)

  def Turn(self):
    self.Draw()
    self.Spread()
    self.KillStacked()
    self.age += 1
    self.OldAgeKill()


  def OldAgeKill(self):
    if random.randint(self.age, 10) == 10:
      self.Kill()

  def Draw(self):
    pygame.draw.rect(self.screen, "green", (self.x * 20, self.y * 20, 20, 20))

  def Spread(self):
    if random.randint(1,5) == 5:
      n = random.choice([-1, 1])
      n2 = random.choice([-1,1])
      organisms.append(Grass(self.x + n, self.y + n2, self.genes, self.screen))


  def KillStacked(self):
    for obj in organisms:
      if self.type == "grass" and self.x == obj.x and self.y == obj.y and self != obj:
        obj.Kill()

import pygame
from Classes.Basic import *
import random
from GlobalVar import *


class Grass(Basic):
  def __init__(self, posx, posy, genes, screen):
    super().__init__(posx, posy, genes, "grass", screen)
    self.energy = 0

  def Turn(self):
    self.Draw()
    self.Spread()
    self.KillStacked()
    self.energy += random.randint(1, 5)

  def Draw(self):
    pygame.draw.rect(self.screen, "green", (self.x * 20, self.y * 20, 20, 20))

  def Spread(self):
    if random.randint(1,5) == 5:
      n = random.randint(-1, 1)
      n2 = random.randint(-1, 1)
      organisms.append(Grass(self.x + n, self.y + n2, self.genes, self.screen))

  def KillStacked(self):
    for obj in organisms:
      if self.type == "grass" and self.x == obj.x and self.y == obj.y and self != obj:
        obj.Kill()

  def BorderKill(self):
    if self.x > 19 or self.x < 0 or self.y > 19 or self.y < 0:
      self.Kill()
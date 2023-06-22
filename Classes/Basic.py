from GlobalVar import *
import pygame


class Basic:
  AgeInitial = 0

  def __init__(self, posx, posy, genes, objType, surface):
    self.x = posx
    self.y = posy
    self.genes = genes
    self.age = Basic.AgeInitial
    self.type = objType
    self.screen = surface

  def Kill(self):
    pygame.draw.rect(self.screen, "white", (self.x * 20, self.y * 20, 20, 20))
    organisms.remove(self)

from Classes.Basic import *
import random
from GlobalVar import *
import copy


class Herbivore(Basic):
  def __init__(self, posx, posy, genes, screen):
    super().__init__(posx, posy, genes, "herbivore", screen)
    self.energy = 500
    self.collisions = []
    self.hasReproduced = False
    if len(self.genes) != 10:
      self.RandomGenes()

  def RandomGenes(self):
    self.genes.clear()
    for x in range(10):
      self.genes.append(random.randint(0, 3))

  def Turn(self):
    self.Move()
    self.GetCollisions()
    self.Eat()
    self.Draw()
    self.Reproduce()
    self.energy -= 1
    self.age += 1
    self.KillChecks()

  def KillChecks(self):
    if self.energy == 0:
      self.Kill()
      return
    if random.randint(self.age, 100) == 100:
      self.Kill()
      return

  def Draw(self):
    pygame.draw.rect(self.screen, "brown", (self.x * 20, self.y * 20, 20, 20))

  def Move(self):
    pygame.draw.rect(self.screen, "white", (self.x * 20, self.y * 20, 20, 20))
    if self.genes[random.randint(0, 9)] == 0:
      self.x += 1
    elif self.genes[random.randint(0, 9)] == 1:
      self.x -= 1
    elif self.genes[random.randint(0, 9)] == 2:
      self.y += 1
    else:
      self.y -= 1
    if self.x > 19:
      self.x = 0
    if self.x < 0:
      self.x = 19
    if self.y > 19:
      self.y = 0
    if self.y < 0:
      self.y = 19

  def GetCollisions(self):
    self.collisions.clear()
    for obj in organisms:
      if obj.x == self.x and obj.y == self.y:
        self.collisions.append(obj)

  def Eat(self):
    for obj in self.collisions:
      if obj.type == "grass":
        self.energy += obj.energy
        obj.Kill()

  def Reproduce(self):
    mate = None
    childgenes = []
    if self.energy > 10 and self.age > 10:
      for obj in self.collisions:
        if obj.type == "herbivore" and not obj.hasReproduced and obj.energy > 10 and self.age > 10:
          mate = obj
          break
      if mate is not None:
        sample1 = random.sample(self.genes, 5)
        sample2 = random.sample(mate.genes, 5)
        for x in range(len(sample1)):
          childgenes.append(sample1.pop())
        for x in range(len(sample2)):
          childgenes.append(sample2.pop())
        if random.randint(1, 100) == 100:
          childgenes.pop(random.randint(0, 9))
          childgenes.append(random.randint(0, 3))
        organisms.append(Herbivore(copy.copy(self.x), copy.copy(self.y), copy.copy(childgenes), self.screen))
        self.hasReproduced = True
        mate.hasReproduced = True
        childgenes.clear()
        sample1.clear()
        sample2.clear()

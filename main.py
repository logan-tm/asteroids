import pygame
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
  pygame.init()

  # initialize loop items
  clock = pygame.time.Clock()
  dt = 0 # seconds
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  # initialize groups
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = updatable, drawable
  Asteroid.containers = asteroids, updatable, drawable
  AsteroidField.containers = updatable
  Shot.containers = shots, updatable, drawable

  # initialize game objects
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()

  # game loop =====================================
  while True:

    # check for quit
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    # update & check collisions
    for u in updatable:
      u.update(dt)
    
    for a in asteroids:
      if a.is_colliding_with(player):
        print("Game over!")
        return
      for s in shots:
        if s.is_colliding_with(a):
          s.kill()
          a.kill()

    # draw
    screen.fill("black")
    for d in drawable:
      d.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000 # save delta time as seconds from ms
  # game loop =====================================

if __name__ == "__main__":
  main()
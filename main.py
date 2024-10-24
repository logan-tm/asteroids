import pygame
from constants import *
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
  Player.containers = updatable, drawable
  Asteroid.containers = asteroids, updatable, drawable
  AsteroidField.containers = updatable

  # initialize game objects
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()

  # game loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("black")
    for u in updatable:
      u.update(dt)
    for d in drawable:
      d.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000 # save delta time as seconds from ms

if __name__ == "__main__":
  main()
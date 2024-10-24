import pygame
from constants import *
from player import Player

def main():
  # print("Starting asteroids!")
  # print(f"Screen width: {SCREEN_WIDTH}")
  # print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init()
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = updatable, drawable
  clock = pygame.time.Clock()
  dt = 0 # seconds
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  # updatable.add(player)
  # drawable.add(player)

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
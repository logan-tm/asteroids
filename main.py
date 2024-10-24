import pygame
from constants import *

def main():
  # print("Starting asteroids!")
  # print(f"Screen width: {SCREEN_WIDTH}")
  # print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0 # seconds
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill((0,0,0))
    pygame.display.flip()
    dt = clock.tick(60) / 1000 # save delta time as seconds from ms

if __name__ == "__main__":
  main()
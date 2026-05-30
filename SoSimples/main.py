import pygame
from constants import *
from logger import log_state
from player import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0.0
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	print("Starting Asteroids")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		log_state()
		for event in pygame.event.get():
			pass
		#this method I use to set a screen on black
		screen.fill("black")
		player.update(dt)
		player.draw(screen)
		#I used this method for refresh the window
		dt = clock.tick(60) / 1000
	display.flip()

if __name__ == "__main__":
    main()

import pygame
import os
import time
import random
pygame.font.init()

width, height = 450, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("pixel game")

# assets eller alla bilder/png för spelare, fiender och skott/laser
# Fiender
red_space_ship = pygame.image.load(os.path.join("PNG", "assets", "pixel_ship_red_small.png"))
green_space_ship = pygame.image.load(os.path.join("PNG", "assets", "pixel_ship_green_small.png"))
blue_space_ship = pygame.image.load(os.path.join("PNG", "assets", "pixel_ship_blue_small.png"))

# Spelare
yellow_space_ship = pygame.image.load(os.path.join("PNG", "assets", "pixel_ship_yellow.png"))

# Skott/laser
red_laser = pygame.image.load(os.path.join("PNG", "assets", "pixel_laser_red.png"))
green_laser = pygame.image.load(os.path.join("PNG", "assets", "pixel_laser_green.png"))
blue_laser = pygame.image.load(os.path.join("PNG", "assets", "pixel_laser_blue.png"))
yellow_laser = pygame.image.load(os.path.join("PNG", "assets", "pixel_laser_yellow.png"))

# Bakgrund
background = pygame.transform.scale(pygame.image.load(os.path.join("PNG", "assets", "background-black.png")), (width, height))


class Ship:
    def __init__(self, x, y, health=100):
        self.x =x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50), 2)

def main_loop():
    run = True
    fps = 60
    lvl = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 25)

    player_speed = 4

    ship = Ship(225, 300)

    clock = pygame.time.Clock()

    def redraw_window():
        window.blit(background, (0, 0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        lvl_label = main_font.render(f"lvl: {lvl}", 1, (255, 255, 255))

        window.blit(lives_label, (10, 10))
        window.blit(lvl_label, (width - lvl_label.get_width() - 10, 10))

        ship.draw(window)

        pygame.display.update()


    while run:
        clock.tick(fps)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship.x - player_speed > 0:
            ship.x -= player_speed
        if keys[pygame.K_RIGHT] and ship.x + player_speed +50 < width:
            ship.x += player_speed
        if keys[pygame.K_UP] and ship.y - player_speed > 0:
            ship.y -= player_speed
        if keys[pygame.K_DOWN] and ship.y + player_speed + 50 < height:
            ship.y += player_speed

main_loop()

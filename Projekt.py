
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

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, speed):
        self.y += speed

    def not_on_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def hit(self, object):
        return collide(object, self)

class Ship:
    COOLDOWN = 30
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.player_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def lasers_move(self, speed, object1):
        self.cooldown()
        for laser in self.lasers:
            laser.move(speed)
            if laser.not_on_screen(height):
                self.lasers.remove(laser)
            elif laser.hit(object1):
                object1.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down >= self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1

    def shoot(self):
        if self.cool_down == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down = 1

    def Player_width(self):
        return self.ship_img.get_width()

    def Player_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = yellow_space_ship
        self.laser_img = yellow_laser
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

        def lasers_move(self, speed, objects):
            self.cool_down()
            for laser in self.lasers:
                laser.move(speed)
                if laser.not_on_screen(height):
                    self.lasers.remove(laser)
                else:
                    for object in objects:
                        if laser.collide():
                            objects.remove(object)
                            self.lasers.remove(laser)

class Enemy(Ship):
    color_set = {
            "red": (red_space_ship, red_laser),
            "green": (green_space_ship, green_laser),
            "blue": (blue_space_ship, blue_laser)
        }
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.color_set[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move_ship(self, vel):
        self.y += vel


def collide(object1, object2):
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) != None

def main_loop():
    run = True
    fps = 60
    lvl = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 25)
    L_font = pygame.font.SysFont("comicsans", 45)

    enemies = []
    lvl_length = 5
    enemy_speed = 1

    player_speed = 4.5
    laser_speed = 3

    player = Player(175, 500)

    clock = pygame.time.Clock()

    L = False
    L_count = 0
    def redraw_window():
        window.blit(background, (0, 0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        lvl_label = main_font.render(f"lvl: {lvl}", 1, (255, 255, 255))

        window.blit(lives_label, (10, 10))
        window.blit(lvl_label, (width - lvl_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(window)

        player.draw(window)

        if L:
            L_label = L_font.render("You took an L!", 1, (255, 255, 255))
            window.blit(L_label, (width/2 - L_label.get_width()/2, 150))



        pygame.display.update()


    while run:
        clock.tick(fps)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            L = True
            L_count += 1

        if L:
            if L_count > fps * 3.5:
                run = False
            else:
                continue

        if len(enemies) == 0:
            lvl += 1
            lvl_length += 5
            for i in range(lvl_length):
                enemy = Enemy(random.randrange(50, width-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_speed > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x + player_speed + player.Player_width() < width:
            player.x += player_speed
        if keys[pygame.K_UP] and player.y - player_speed > 0:
            player.y -= player_speed
        if keys[pygame.K_DOWN] and player.y + player_speed + player.Player_height() < height:
            player.y += player_speed
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move_ship(enemy_speed)
            enemy.lasers_move(laser_speed, player)
            if enemy.y + enemy.Player_height() > height:
                lives -= 1
                enemies.remove(enemy)

        player.lasers_move(laser_speed, enemies)



main_loop()


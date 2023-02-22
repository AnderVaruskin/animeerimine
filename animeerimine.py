import pygame
import random


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("bg_rally.jpg")

red_car = pygame.image.load("f1_red.png")
red_car_rect = red_car.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.1))

blue_car = pygame.image.load("f1_blue.png")

blue_car_speed = 1

score = 0
font = pygame.font.Font(None, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    screen.blit(red_car, red_car_rect)

    if random.random() < 0.01:
        x = random.randint(0, SCREEN_WIDTH-30)
        y = random.randint(-500, -50)
        blue_cars.append(pygame.Rect(x, y, 30, 50))

    for car in blue_cars:
        car.move_ip(0, blue_car_speed)

        if car.bottom > SCREEN_HEIGHT:
            blue_cars.remove(car)
            score += 1

    for car in blue_cars:
        pygame.draw.rect(screen, (0, 0, 255), car)

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
import pygame
import random

pygame.init()

# Oyna sozlamalari
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
BLOCK = 20

# Ranglar
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)


def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(win, GREEN, (*block, BLOCK, BLOCK))


def game():
    snake = [(100, 100)]
    dx, dy = BLOCK, 0

    food = (
        random.randrange(0, WIDTH, BLOCK),
        random.randrange(0, HEIGHT, BLOCK)
    )

    run = True
    while run:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and dy == 0:
            dx, dy = 0, -BLOCK
        if keys[pygame.K_DOWN] and dy == 0:
            dx, dy = 0, BLOCK
        if keys[pygame.K_LEFT] and dx == 0:
            dx, dy = -BLOCK, 0
        if keys[pygame.K_RIGHT] and dx == 0:
            dx, dy = BLOCK, 0

        head = (snake[0][0] + dx, snake[0][1] + dy)
        snake.insert(0, head)

        if head == food:
            food = (
                random.randrange(0, WIDTH, BLOCK),
                random.randrange(0, HEIGHT, BLOCK)
            )
        else:
            snake.pop()

        if (
                head[0] < 0 or head[0] >= WIDTH or
                head[1] < 0 or head[1] >= HEIGHT or
                head in snake[1:]
        ):
            run = False

        win.fill(BLACK)
        draw_snake(snake)
        pygame.draw.rect(win, RED, (*food, BLOCK, BLOCK))
        pygame.display.update()

    pygame.quit()


game()

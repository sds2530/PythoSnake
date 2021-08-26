import pygame
import random

# Create the Screen
pygame.init()
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))

# Set Display Caption
pygame.display.set_caption("PythoSnake")

white = (255, 255, 255)
yellow = (255, 255, 102)
green = (0, 255, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

snake_speed = 15
snake_block = 10

font_style = pygame.font.SysFont("Arial", 25, bold=True, italic=True)
score_font = pygame.font.SysFont("Arial", 20, bold=True, italic=True)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    msgs = font_style.render(msg, True, color)
    dis.blit(msgs, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close:
            dis.fill(black)
            message("You Lost! Press Q-Quit or P-Play Again", white)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        # Create the Snake
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        snake(snake_block, snake_list)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            print("Yummy!!")

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()

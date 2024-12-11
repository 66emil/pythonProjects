import pygame
import random
pygame.init()

WIDTH, HEIGHT = 400, 400  
cell_size = 20            

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Разноцветная змейка")

snake = [(100, 100), (80, 100), (60, 100)]  
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]  # Красный, зеленый, синий, желтый, оранжевый
direction = "RIGHT"

def generate_apple():
    x = random.randint(0, (WIDTH - cell_size) // cell_size) * cell_size
    y = random.randint(0, (HEIGHT - cell_size) // cell_size) * cell_size
    return (x, y)

apple = generate_apple()
apple_color = (255, 0, 0)  # Красный цвет яблока

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    head_x, head_y = snake[0]
    if direction == "UP":
        new_head = (head_x, head_y - cell_size)
    elif direction == "DOWN":
        new_head = (head_x, head_y + cell_size)
    elif direction == "LEFT":
        new_head = (head_x - cell_size, head_y)
    elif direction == "RIGHT":
        new_head = (head_x + cell_size, head_y)

    # Проверяем, не вышла ли голова змейки за пределы поля
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        print("Змейка врезалась в стену! Игра окончена.")
        running = False
        continue

    # Проверяем, не врезалась ли змейка сама в себя
    if new_head in snake:
        print("Змейка врезалась сама в себя! Игра окончена.")
        running = False
        continue

    # Добавляем новую голову
    snake.insert(0, new_head)

    # Проверяем, съела ли змейка яблоко
    if new_head == apple:
        apple = generate_apple()
    else:
        snake.pop()

    screen.fill((255, 255, 255))  

    # Рисуем сетку
    for x in range(0, WIDTH, cell_size):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))  
    for y in range(0, HEIGHT, cell_size):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))   

    # Рисуем разноцветную змейку
    for i, segment in enumerate(snake):
        segment_color = colors[i % len(colors)]  # Используем цвета по очереди
        pygame.draw.rect(screen, segment_color, (segment[0], segment[1], cell_size, cell_size))

    # Рисуем яблоко
    pygame.draw.rect(screen, apple_color, (apple[0], apple[1], cell_size, cell_size))

    pygame.display.flip()

    pygame.time.delay(100)

pygame.quit()

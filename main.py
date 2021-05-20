import pygame, sys, random



def end():
    pygame.quit()
    sys.exit()

def main():
    pygame.init()

    sw = 800
    sh = 600
    font = pygame.font.SysFont('comicsans',40)
    scr = pygame.display.set_mode((sw, sh))

    snk_x = sw//4
    snk_y = sh//10

    snake = [
        [snk_x, snk_y],
        [snk_x-10, snk_y],
        [snk_x-20, snk_y],
    ]
    head = [snk_x, snk_y]

    food = [sw//2, sh//2]

    direction = 'right'
    speed = 25
    score = 0
    clock = pygame.time.Clock()

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end()
                if event.key == pygame.K_UP:
                    direction = 'up'
                if event.key == pygame.K_DOWN:
                    direction = 'down'
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                if event.key == pygame.K_RIGHT:
                    direction = 'right'
            elif event.type == pygame.QUIT:
                end()
        scr.fill((0,0,0))

        if head[0]+10 in [0, sw] or head[1] in [0, sh] or snake[0] in snake[1:]:
            end()
        for part in snake:
            pygame.draw.rect(scr, (255,255,0), (part[0], part[1],10, 10))

        if direction == 'up':
            head[1] -= 10 
        if direction == 'down':
            head[1] += 10 
        if direction == 'left':
            head[0] -= 10 
        if direction == 'right':
            head[0] += 10 

        snake.append(list(head))

        pygame.draw.rect(scr, (255,0,0), (food[0], food[1], 10, 10))

        score_font = font.render(f'{score}' , True , (255,255,255))
        font_pos = score_font.get_rect(center=(sw//2-40 , 30))
        scr.blit(score_font , font_pos)

        if pygame.Rect(head[0], head[1], 10, 10).colliderect(pygame.Rect(food[0], food[1], 10, 10)):
            food = [random.randrange(40, sw-40), random.randrange(40, sh-40)]
            score += 1
        else:
            snake.pop(0)

        pygame.display.update()
        clock.tick(speed)

if __name__ == '__main__':
    main()

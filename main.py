import pygame
import random
pygame.font.init()

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("number genorator")

Health_font = pygame.font.SysFont('comicsans', 40)
number_Font = pygame.font.SysFont('comicsans', 40)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30
DELAY = 900



def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()
    for repeat_count in range(1):
        draw_number()

def draw_number():
    for repeat_count in range(1):
        randomlist = random.sample(range(1, 100), 10)
        draw_text = number_Font.render(str(randomlist), 1, BLACK)
        WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(900)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Up-Down Game (Pygame)")

user_input = ""
font = pygame.font.Font(None, 74)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("입력 완료:", user_input)
                user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    text = font.render(user_input, True, (255, 255, 255))
    screen.blit(text, (200, 150))
    
    pygame.display.update()
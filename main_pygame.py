import pygame
import sys

pygame.init() # 초기화
screen = pygame.display.set_mode((600,400)) # 화면 크기 설정
pygame.display.set_caption("Up-Down Game (Pygame)") # 창 이름 설정

user_input = "" # 유저 입력을 받는 변수
font = pygame.font.Font(None, 74) # 글자 크기 설정

while True: # 메인 루프
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("입력 완료:", user_input)
                user_input = "" # 유저 입력 초기화
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    text = font.render(user_input, True, (255, 255, 255)) # 화면에 텍스트 렌더링
    screen.blit(text, (200, 150))
    
    pygame.display.update()
import pygame
import sys
import random

pygame.init() # 초기화
screen = pygame.display.set_mode((600,400)) # 화면 크기 설정
pygame.display.set_caption("Up-Down Game (Pygame)") # 창 이름 설정

answer = random.randrange(1, 101) # 난수로 답을 저장

user_input = "" # 유저 입력을 받는 변수
message = "" # 메시지 초기화
font = pygame.font.SysFont("malgungothic", 74) # 글자 크기 설정

while True: # 화면에 표시하는 메인 루프
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # 업다운 게임 메인 루프
                try:
                    guess = int(user_input)
                    if guess < answer:
                        message = "업"
                    elif guess > answer:
                        message = "다운"
                    elif guess == answer:
                        message = "정답!"
                except:
                    message = "숫자를 입력해 주세요."
                    
                print("입력 완료 :",user_input)
                user_input = "" # 유저 입력 초기화
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode


    text = font.render(user_input, True, (255, 255, 255)) # 화면에 입력값 렌더링
    screen.blit(text, (200, 150))

    message_text = font.render(message, True, (255, 255 ,0)) # 업다운 판별값 렌더링
    screen.blit(message_text, (200, 250))

    pygame.display.update()
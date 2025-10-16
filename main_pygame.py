import pygame
import sys
import random

pygame.init() # 초기화
screen = pygame.display.set_mode((600,400)) # 화면 크기 설정
pygame.display.set_caption("Up-Down Game (Pygame)") # 창 이름 설정

font = pygame.font.SysFont("malgungothic", 74) # 글자 크기 설정

def init_game(): # 게임 변수 초기화 함수 
    answer = random.randrange(1, 101) # 정답 난수
    count = 0 # 시도 횟수 초기화
    user_input = "" # 입력 초기화
    message = "" # 메시지 초기화
    return answer, count, user_input, message # 변경된 상태를 다시 반환

def handle_input(event, user_input, answer, count, message): # 입력 처리 함수
    if event.key == pygame.K_RETURN: # 엔터 키를 눌렀을 때 실행
        try:
            guess = int(user_input) # 정수로 변환
            count += 1 # 시도 횟수 증가
            if guess < answer:
                message = "업"
            elif guess > answer:
                message = "다운"
            elif guess == answer:
                message = "정답!"
        except ValueError:
            message = "숫자를 입력해 주세요."
            
        print("입력 완료 :",user_input)
        user_input = "" # 입력값 초기화
    elif event.key == pygame.K_BACKSPACE: # 백스페이스 키를 누르면 user_input의 마지막 글자 지움
        user_input = user_input[:-1] # 문자열의 마지막 문자 제외
    elif event.unicode.isdigit(): # 숫자만 입력받기
        user_input += event.unicode # user_input에 추가

    return user_input, count, message # 입력 처리 후 최신 상태를 반환


answer, count, user_input, message = init_game()

while True: # 화면에 표시하는 메인 루프
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            user_input, count, message = handle_input(event, user_input, answer, count, message)

    text = font.render(user_input, True, (255, 255, 255)) # 화면에 입력값 출력
    screen.blit(text, (200, 150))

    message_text = font.render(message, True, (255, 255 ,0)) # 업다운 판별값 출력
    screen.blit(message_text, (200, 250))
    count_text = font.render(f"시도 횟수 : {count}", True, (200,200,200)) # 시도 횟수 화면에 출력
    screen.blit(count_text, (100, 50))

    pygame.display.update()
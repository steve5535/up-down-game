import random

def up_down_game():
    count = 0
    dap= random.randrange(1,101) #1~100까지의 난수중 한가지를 dap에 저장
    print('1~100사이에 수를 입력해주세요.')
    
    while True : #본게임 반복문
        ip=int(input('답을 입력 하세요 :'))
        count+=1 #순서 카운트
        
        if not (0<ip<101):
            print('1~100사이에 수를 입력해주세요.')
            continue
        else:
            if ip>dap:
                print('다운')
            elif ip<dap:
                print('업')
            elif ip == dap:
                print('%d만에 정답!!!' %count)
                break

if __name__ == "__main__":
    up_down_game()